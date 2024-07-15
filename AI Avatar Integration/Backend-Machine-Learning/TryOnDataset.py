# Custom Dataset Class for Try-On Project
from PIL import Image
from torchvision import datasets

import os


class TryOnDataset(datasets):
    def __init__(self, personDir, clothingDir, targetDir, transform=None):
        """
        Args:
            personDir (str): Directory with person images.
            clothingDir (str): Directory with clothing images.
            targetDir (str): Directory with target images.
            transform (callable, optional): Optional transform to be applied on a sample.
        """
        self.personDir = personDir
        self.clothingDir = clothingDir
        self.targetDir = targetDir
        self.personImages = os.listdir(personDir)
        self.transform = transform

    def __len__(self):
        return len(self.personImages)

    def __getitem__(self, idx):
        personPath = os.path.join(self.personDir, self.personImages[idx])
        clothingPath = os.path.join(self.clothingDir, self.personImages[idx])
        targetPath = os.path.join(self.targetDir, self.personImages[idx])

        personImage = Image.open(personPath).convert("RGB")
        clothingImage = Image.open(clothingPath).convert("RGB")
        targetImage = Image.open(targetPath).convert("RGB")

        if self.transform:
            personImage = self.transform(personImage)
            clothingImage = self.transform(clothingImage)
            targetImage = self.transform(targetImage)

        return personImage, clothingImage, targetImage