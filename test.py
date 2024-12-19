import torch
from PIL import Image
from torchvision import transforms
from model import DeconvNet
import os

def enhance_image(input_path, output_path, model, device):
    model.eval()
    with torch.no_grad():
        image = Image.open(input_path).convert("RGB")

        # Cek ukuran gambar dan sesuaikan jika lebih besar dari 500x500
        max_size = 500
        width, height = image.size
        if width > max_size or height > max_size:
            ratio = min(max_size / width, max_size / height)
            new_width = int(width * ratio)
            new_height = int(height * ratio)
            image = image.resize((new_width, new_height))

        transform = transforms.Compose([
            transforms.ToTensor()
        ])
        tensor_image = transform(image).unsqueeze(0).to(device)
        enhanced_image = model(tensor_image).squeeze(0).cpu()
        output_image = transforms.ToPILImage()(enhanced_image)
        output_image.save(output_path)
        return output_image


if __name__ == "__main__":
    # Prompt user for input image
    input_path = input("Please enter the path to the input image: ")
    if not os.path.exists(input_path):
        print(f"Error: File {input_path} does not exist.")
        exit()

    output_path = "enhanced_output.png"

    # Load the model
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = DeconvNet().to(device)

    # Memuat state_dict dengan weights_only=True untuk menghindari peringatan
    state_dict = torch.load("saved_models/deconv_super_res_model.pth", 
                            map_location=device, weights_only=True)
    model.load_state_dict(state_dict)

    # Enhance the image
    enhanced_image = enhance_image(input_path, output_path, model, device)

    # Display the images side by side
    original_image = Image.open(input_path)
    original_image.show(title="Original Image")
    enhanced_image.show(title="Enhanced Image")
    print(f"Enhanced image saved to {output_path}")
