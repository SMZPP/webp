from PIL import Image
import os

def convert_webp_to_jpg(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for file_name in os.listdir(input_folder):
        if file_name.endswith('.webp'):
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, f"{os.path.splitext(file_name)[0]}.jpg")

            with Image.open(input_path) as img:
                img = img.convert('RGB')
                img.save(output_path, 'JPEG')
            print(f"Converted: {file_name} -> {output_path}")

input_folder = './input'
output_folder = './output'
convert_webp_to_jpg(input_folder, output_folder)
