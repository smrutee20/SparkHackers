from torch import nn
from torchvision import models

# Feature Extractor using ResNet18
class FeatureExtractor(nn.Module):
    def __init__(self):
        """
        Initializes FeatureExtractor using pretrained ResNet18 model.
        """
        super(FeatureExtractor, self).__init__()
        self.model = models.resnet18(pretrained=True)
        self.model = nn.Sequential(*list(self.model.children())[:-2])  # Remove the last fully connected layer

    def forward(self, x):
        return self.model(x)