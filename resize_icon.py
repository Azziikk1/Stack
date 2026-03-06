import os, shutil
from PIL import Image

icon_path = 'icon_512_final.png'
base_path = 'android/app/src/main/res'

img = Image.open(icon_path).convert('RGB')

sizes = {
    'mipmap-mdpi':    48,
    'mipmap-hdpi':    72,
    'mipmap-xhdpi':   96,
    'mipmap-xxhdpi':  144,
    'mipmap-xxxhdpi': 192,
}

for folder, size in sizes.items():
    path = os.path.join(base_path, folder)
    os.makedirs(path, exist_ok=True)
    resized = img.resize((size, size), Image.LANCZOS)
    resized.save(os.path.join(path, 'ic_launcher.png'))
    resized.save(os.path.join(path, 'ic_launcher_round.png'))
    fg = os.path.join(path, 'ic_launcher_foreground.png')
    if os.path.exists(fg):
        resized.save(fg)
    print(f"Done: {folder} ({size}x{size})")

# anydpi-v26 tamamen sil
anydpi = os.path.join(base_path, 'mipmap-anydpi-v26')
if os.path.exists(anydpi):
    shutil.rmtree(anydpi)
    print(f"Deleted adaptive icons: {anydpi}")

print('All done!')
