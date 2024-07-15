from torch import nn 
# Parallel Diffusion Module
class ParallelDiffusion(nn.Module):
    def __init__(self):
        """
        Initializes Parallel Diffusion module.
        """
        super(ParallelDiffusion, self).__init__()
        self.conv1 = nn.Conv2d(512, 512, kernelSize=3, padding=1)
        self.conv2 = nn.Conv2d(512, 512, kernelSize=3, padding=1)
        self.relu = nn.ReLU(inplace=True)

    def forward(self, personFeatures, clothingFeatures):
        combinedFeatures = torch.cat([personFeatures, clothingFeatures], dim=1)
        x = self.relu(self.conv1(combinedFeatures))
        x = self.relu(self.conv2(x))
        return x