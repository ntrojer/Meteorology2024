import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from dataset import PVDataLSTM  # Dataset-Klasse aus separater Datei
from model import PVLSTM       # LSTM-Modell aus separater Datei

def train(model, dataloader, criterion, optimizer, num_epochs=20):
    """
    Trainiere das Modell mit stündlichen Daten.
    """
    for epoch in range(num_epochs):
        model.train()
        total_loss = 0
        
        for input_seq, target in dataloader:
            optimizer.zero_grad()
            
            # Vorhersage
            predictions = model(input_seq)
            
            # Verlust berechnen
            loss = criterion(predictions, target)
            
            # Backpropagation und Optimierung
            loss.backward()
            optimizer.step()
            
            total_loss += loss.item()
        
        avg_loss = total_loss / len(dataloader)
        print(f"Epoch {epoch+1}/{num_epochs}, Loss: {avg_loss:.4f}")

def evaluate(model, dataloader, criterion):
    """
    Evaluierung des Modells mit täglichen Mittelwerten.
    """
    model.eval()
    total_loss = 0
    
    with torch.no_grad():
        for input_seq, target in dataloader:
            # Vorhersage
            predictions = model(input_seq)
            
            # Verlust berechnen
            loss = criterion(predictions, target)
            total_loss += loss.item()
    
    avg_loss = total_loss / len(dataloader)
    print(f"Evaluation Loss (Daily Data): {avg_loss:.4f}")
    return avg_loss

if __name__ == "__main__":
    # Hyperparameter
    seq_length = 5  # Anzahl der Tage in der Sequenz
    batch_size = 32
    num_epochs = 20
    learning_rate = 0.001
    
    # Daten laden
    hourly_dataset = PVDataLSTM(csv_file="ml_data_hourly.csv", seq_length=seq_length, mode="hourly")
    daily_dataset = PVDataLSTM(csv_file="ml_data_daily.csv", seq_length=seq_length, mode="daily")
    
    hourly_dataloader = DataLoader(hourly_dataset, batch_size=batch_size, shuffle=True)
    daily_dataloader = DataLoader(daily_dataset, batch_size=batch_size, shuffle=False)
    
    # Modell, Verlustfunktion und Optimizer initialisieren
    model = PVLSTM(input_size=3, hidden_size=64, num_layers=2, output_size=24)
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    
    # Training mit stündlichen Daten
    print("Starting training with hourly data...")
    train(model, hourly_dataloader, criterion, optimizer, num_epochs=num_epochs)
    
    # Evaluierung mit täglichen Mittelwerten
    print("\nStarting evaluation with daily data...")
    evaluate(model, daily_dataloader, criterion)
