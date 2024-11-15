from PIL import Image
import os

def convert_and_resize_webp_to_png(input_folder, output_folder, size=(32, 32)):
    os.makedirs(output_folder, exist_ok=True)

    for file_name in os.listdir(input_folder):
        if file_name.endswith('.webp'):
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, f"{os.path.splitext(file_name)[0]}.png")

            with Image.open(input_path) as img:
                img = img.convert('RGBA')
                img = img.resize(size, Image.ANTIALIAS)
                img.save(output_path, 'PNG')
            print(f"Converted and resized: {file_name} -> {output_path}")

input_folder = './input'
output_folder = './output'
convert_and_resize_webp_to_png(input_folder, output_folder)
