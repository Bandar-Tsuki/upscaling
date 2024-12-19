import os
from torch.utils.data import Dataset
from PIL import Image

class SuperResolutionDataset(Dataset):
    def __init__(self, low_res_dir, high_res_dir, transform=None):
        self.low_res_dir = low_res_dir
        self.high_res_dir = high_res_dir
        self.low_res_files = sorted(os.listdir(low_res_dir))
        self.high_res_files = sorted(os.listdir(high_res_dir))
        self.transform = transform

    def __len__(self):
        return len(self.low_res_files)

    def __getitem__(self, idx):
        low_res_path = os.path.join(self.low_res_dir, self.low_res_files[idx])
        high_res_path = os.path.join(self.high_res_dir, self.high_res_files[idx])

        low_res_image = Image.open(low_res_path).convert("RGB")
        high_res_image = Image.open(high_res_path).convert("RGB")

        if self.transform:
            low_res_image = self.transform(low_res_image)
            high_res_image = self.transform(high_res_image)

        return low_res_image, high_res_image
