import torch.nn as nn

class PVLSTM(nn.Module):
    def __init__(self, input_size=3, hidden_size=64, num_layers=2, output_size=24):
        """
        Args:
            input_size: Number of input features (e.g., temperature, radiation, wspd).
            hidden_size: Number of LSTM units.
            num_layers: Number of LSTM layers.
            output_size: Number of hourly predictions (24 for hourly PVpot).
        """
        super(PVLSTM, self).__init__()
        
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        # LSTM Forward Pass
        _, (hidden, _) = self.lstm(x)
        
        # Verwende den letzten Hidden State für die Vorhersage
        output = self.fc(hidden[-1])  # [Batch, Hidden] -> [Batch, Output]
        return output
