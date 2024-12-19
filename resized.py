from PIL import Image, ImageOps
import os


def resize_images(input_folder, output_folder, target_size):
    """
    Resize all images in the input folder to the target size and save them in the output folder.

    :param input_folder: Path to the folder containing input images
    :param output_folder: Path to the folder to save resized images
    :param target_size: Tuple (width, height) specifying the target resolution
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        input_path = os.path.join(input_folder, file_name)

        # Check if the file is an image
        if os.path.isfile(input_path) and file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            try:
                with Image.open(input_path) as img:
                    img_resized = img.resize(target_size, Image.Resampling.LANCZOS)
                    output_path = os.path.join(output_folder, file_name)
                    img_resized.save(output_path)
                    print(f"Resized and saved: {output_path}")
            except Exception as e:
                print(f"Error processing {file_name}: {e}")


if __name__ == "__main__":
    # Folder paths
    input_folder = "data/high_res"  # Replace with your input folder
    output_folder = "data/low_res"  # Replace with your output folder

    # Target resolution
    target_size = (32, 32)  # Replace with desired resolution (width, height)

    # Run the resizing function
    resize_images(input_folder, output_folder, target_size)
