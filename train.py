import os
import torch
import torch.optim as optim
import torch.nn as nn
from torch.utils.data import DataLoader
from dataset import SuperResolutionDataset
from model import DeconvNet
from torchvision import transforms

# Training loop
def train_model(sr_model, data_loader, loss_function, optim, epochs, dev):
    sr_model.train()
    for epoch in range(epochs):
        running_loss = 0.0
        for low_res, high_res in data_loader:
            low_res = low_res.to(dev)
            high_res = high_res.to(dev)

            optim.zero_grad()

            outputs = sr_model(low_res)
            loss = loss_function(outputs, high_res)
            loss.backward()
            optim.step()

            running_loss += loss.item()

        print(f"Epoch {epoch+1}/{epochs}, Loss: {running_loss / len(data_loader):.4f}")

if __name__ == "__main__":
    # Dataset and DataLoader
    low_res_dir = "dataset/low_res"
    high_res_dir = "dataset/high_res"
    transform = transforms.Compose([
        transforms.ToTensor()
    ])
    dataset = SuperResolutionDataset(low_res_dir, high_res_dir, transform=transform)
    data_loader = DataLoader(dataset, batch_size=8, shuffle=True)

    # Initialize model, loss, and optimizer
    dev = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    sr_model = DeconvNet().to(dev)
    loss_function = nn.MSELoss()
    optim = optim.Adam(sr_model.parameters(), lr=0.001)

    # Train the model
    epochs = 20
    train_model(sr_model, data_loader, loss_function, optim, epochs, dev)

    # Save the model
    os.makedirs("saved_models", exist_ok=True)
    torch.save(sr_model.state_dict(), "saved_models/deconv_super_res_model.pth")
    print("Model saved to saved_models/deconv_super_res_model.pth")
