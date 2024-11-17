from PIL import Image
import os

def convert_and_resize_images(input_folder, output_folder, output_format="PNG", size=(32, 32)):
    """
    指定フォルダ内のWebP画像を指定の形式に変換し、指定サイズにリサイズする。

    :param input_folder: 変換対象のWebP画像があるフォルダ
    :param output_folder: 変換後の画像を保存するフォルダ
    :param output_format: 出力画像形式 (例: "PNG", "JPEG")
    :param size: リサイズ後の画像サイズ（幅, 高さ）
    """
    # 出力フォルダが存在しない場合、作成
    os.makedirs(output_folder, exist_ok=True)

    for file_name in os.listdir(input_folder):
        if file_name.endswith('.webp'):
            input_path = os.path.join(input_folder, file_name)
            output_filename = f"{os.path.splitext(file_name)[0]}.{output_format.lower()}"
            output_path = os.path.join(output_folder, output_filename)

            with Image.open(input_path) as img:
                img = img.convert('RGBA') if output_format == "PNG" else img.convert('RGB')
                img = img.resize(size, Image.Resampling.LANCZOS)
                img.save(output_path, output_format.upper())
            print(f"Converted and resized: {file_name} -> {output_path}")

print("=== WebP画像を変換＆リサイズツール ===")
input_folder = "./input"
output_folder = "./output"
output_format = input("出力画像形式を指定してください (例: PNG, JPEG): ").upper()
width = int(input("リサイズ後の幅を入力してください: "))
height = int(input("リサイズ後の高さを入力してください: "))
size = (width, height)

convert_and_resize_images(input_folder, output_folder, output_format, size)
print("処理が完了しました！")
