# UNet Model for image synthesis
class UNet(nn.Module):
    def __init__(self, nChannels, nClasses):
        """
        Initializes UNet model.
        Args:
            nChannels (int): Number of input channels.
            nClasses (int): Number of output classes.
        """
        super(UNet, self).__init__()
        self.encoder = nn.Sequential(
            nn.Conv2d(nChannels, 64, kernelSize=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(64, 64, kernelSize=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernelSize=2)
        )
        self.decoder = nn.Sequential(
            nn.Conv2d(64, 64, kernelSize=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(64, nClasses, kernelSize=3, padding=1),
            nn.Sigmoid()
        )

    def forward(self, x):
        x = self.encoder(x)
        x = self.decoder(x)
        return x