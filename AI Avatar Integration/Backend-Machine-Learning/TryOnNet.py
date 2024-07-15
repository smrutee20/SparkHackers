# Try-On Network combining all components
from TryON.FeatureExtractor import FeatureExtractor
from TryON.ParallelDiffusion import ParallelDiffusion
from TryON.STN import STN
from TryON.UNet import UNet


class TryOnNet(nn.Module):
    def __init__(self):
        """
        Initializes TryOnNet model combining FeatureExtractor, STN, ParallelDiffusion, and UNet.
        """
        super(TryOnNet, self).__init__()
        self.featureExtractor = FeatureExtractor()
        self.stn = STN()
        self.diffusion = ParallelDiffusion()
        self.unet = UNet(nChannels=512, nClasses=3)

    def forward(self, person, clothing):
        personFeatures = self.featureExtractor(person)
        clothingFeatures = self.featureExtractor(clothing)
        alignedClothing = self.stn(clothingFeatures)
        diffusedFeatures = self.diffusion(personFeatures, alignedClothing)
        output = self.unet(diffusedFeatures)
        return output