from torch import nn

# Spatial Transformer Network (STN)
class STN(nn.Module):
    def __init__(self):
        """
        Initializes Spatial Transformer Network.
        """
        super(STN, self).__init__()
        self.localization = nn.Sequential(
            nn.Conv2d(3, 8, kernelSize=7),
            nn.MaxPool2d(2, stride=2),
            nn.ReLU(True),
            nn.Conv2d(8, 10, kernelSize=5),
            nn.MaxPool2d(2, stride=2),
            nn.ReLU(True)
        )

        self.fcLoc = nn.Sequential(
            nn.Linear(10 * 53 * 53, 32),
            nn.ReLU(True),
            nn.Linear(32, 3 * 2)
        )

        self.fcLoc[2].weight.data.zero_()
        self.fcLoc[2].bias.data.copy_(torch.tensor([1, 0, 0, 0, 1, 0], dtype=torch.float))

    def forward(self, x):
        xs = self.localization(x)
        xs = xs.view(-1, 10 * 53 * 53)
        theta = self.fcLoc(xs)
        theta = theta.view(-1, 2, 3)
        grid = F.affine_grid(theta, x.size())
        x = F.grid_sample(x, grid)
        return x