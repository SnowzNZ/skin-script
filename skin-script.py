from tkinter import filedialog
from pick import pick
import os
from PIL import Image
from rich.progress import track


def remove_foreign_files(skin):
    ...


def downscale_2x_to_sd(skin_folder):
    print("Downscaling all @2x assets to SD...")
    # Iterate over all files in the skin folder
    for asset in track(os.listdir(skin_folder)):
        # Get the file name and extension from the file path
        file_name, file_ext = os.path.splitext(asset)
        # Check if the file name ends in @2x
        if file_name.endswith("@2x"):
            # Open the image
            image = Image.open(asset)
            # Downscale it by 0.5
            image.resize(
                (image.width // 2, image.height // 2), Image.Resampling.LANCZOS
            )
            # Save it as a new file without @2x
            image.save(file_name[:-3] + file_ext)


def convert_audio_to_ogg(skin):
    ...


if __name__ == "__main__":
    skin_folder = filedialog.askdirectory()
    if skin_folder:
        option, index = pick(
            [
                "Remove all foreign files",
                "Downscale all @2x assets to SD",
                "Convert all audio files to ogg",
            ],
            "skin-script v1",
        )
        if index == 0:
            remove_foreign_files(skin_folder)
        if index == 1:
            downscale_2x_to_sd(skin_folder)
        if index == 2:
            convert_audio_to_ogg(skin_folder)
