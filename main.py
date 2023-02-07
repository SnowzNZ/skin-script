import os
import subprocess

from PIL import Image

folder_path = r"C:\Users\jackson\AppData\Local\osu!\Skins\Rohulk 4.0"


# delete all SD images (non @2x)
for filename in os.listdir(folder_path):
    if filename.endswith(".png") and not filename.endswith("@2x.png"):
        file_path = os.path.join(folder_path, filename)
        os.remove(file_path)

# convert all .wav files to .ogg losslessly with ffmpeg
for filename in os.listdir(folder_path):
    if filename.endswith(".wav"):
        wav_path = os.path.join(folder_path, filename)
        ogg_path = os.path.splitext(wav_path)[0] + ".ogg"
        subprocess.run(
            ["ffmpeg", "-i", wav_path, "-c:a", "libvorbis", "-q:a", "5", ogg_path]
        )

# delete all .wav files that arent needed anymore
for filename in os.listdir(folder_path):
    if filename.endswith(".wav"):
        wav_path = os.path.join(folder_path, filename)
        ogg_path = os.path.splitext(wav_path)[0] + ".ogg"
        if os.path.exists(ogg_path):
            os.remove(wav_path)

# blank images to small low size ones
blank_img = Image.new("RGBA", (1, 1), (0, 0, 0, 0))
for filename in os.listdir(folder_path):
    if filename.endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
        file_path = os.path.join(folder_path, filename)
        img = Image.open(file_path)
        img_data = img.getdata()
        fully_transparent = all(val[3] == 0 for val in img_data)
        fully_black = all(val == (0, 0, 0, 255) for val in img_data)
        fully_white = all(val == (255, 255, 255, 255) for val in img_data)
        if fully_transparent or fully_black or fully_white:
            blank_img.save(file_path)

# compress all images
for filename in os.listdir(folder_path):
    if filename.endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
        file_path = os.path.join(folder_path, filename)
        img = Image.open(file_path)
        img.save(file_path, optimize=True, quality=90)
