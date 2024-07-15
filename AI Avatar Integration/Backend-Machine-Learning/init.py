from TryON.TryOnDataset import TryOnDataset
from TryON.TryOnNet import TryOnNet
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import transforms
from torch.utils.data import DataLoader

# Transformations for the dataset
transform = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
])

# Create Dataset and DataLoader
trainDataset = TryOnDataset(personDir='data/train/person', clothingDir='data/train/clothing', targetDir='data/train/target', transform=transform)
trainDataLoader = DataLoader(trainDataset, batchSize=4, shuffle=True)

# Training Loop
model = TryOnNet()
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

for epoch in range(10):
    model.train()
    runningLoss = 0.0
    for i, (person, clothing, target) in enumerate(trainDataLoader):
        optimizer.zero_grad()
        output = model(person, clothing)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()
        runningLoss += loss.item()

    print(f'Epoch {epoch+1}, Loss: {runningLoss / len(trainDataLoader)}')

    # Optionally save the model checkpoint
    torch.save(model.state_dict(), f'modelEpoch_{epoch+1}.pth')

# Evaluation
model.eval()
with torch.no_grad():
    for person, clothing in testDataLoader:
        output = model(person, clothing)
        # Save or display the output image
        # Example: torchvision.utils.save_image(output, 'output.png')
