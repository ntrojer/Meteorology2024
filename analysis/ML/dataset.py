import pandas as pd
import torch
from torch.utils.data import Dataset

class PVDataLSTM(Dataset):
    def __init__(self, csv_file, seq_length=5, mode="hourly"):
        """
        Args:
            csv_file (string): Path to the CSV file with data.
            seq_length (int): Number of days in the input sequence.
            mode (string): 'hourly' for hourly data or 'daily' for daily data.
        """
        self.data = pd.read_csv(csv_file)
        self.seq_length = seq_length
        self.mode = mode
        
        if mode == "hourly":
            # Direkte stündliche Daten verwenden
            self.features = self.data[["t2m", "ssrd", "wspd", "valid_time", "longitude", "latitude"]].values
            self.labels = self.data["pvpot"].values
        elif mode == "daily":
            # Tagesmittelwerte berechnen
            self.data["day"] = pd.to_datetime(self.data["valid_time"]).dt.date
            daily_data = self.data.groupby("day").mean().reset_index()
            
            self.features = daily_data[["t2m", "ssrd", "wspd", "valid_time", "longitude", "latitude"]].values
            self.labels = daily_data["pvpot"].values

    def __len__(self):
        return len(self.features) - self.seq_length

    def __getitem__(self, idx):
        # Eingabesequenz: Vergangene seq_length Tage
        input_seq = self.features[idx:idx + self.seq_length]
        target = self.labels[idx + self.seq_length]
        
        # Umwandlung in Tensoren
        input_seq = torch.tensor(input_seq, dtype=torch.float32)
        target = torch.tensor(target, dtype=torch.float32)
        
        return input_seq, target
