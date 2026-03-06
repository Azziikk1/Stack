import os
from PIL import Image

icon_path = 'icon_512_final.png'
base_path = 'android/app/src/main/res'

print(f"Icon exists: {os.path.exists(icon_path)}")
print(f"Base path exists: {os.path.exists(base_path)}")

img = Image.open(icon_path).convert('RGBA')

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
    print(f"Done: {folder} ({size}x{size})")

# adaptive icon klasörü varsa xml'leri sil (varsayılan ikonu devre dışı bırak)
anydpi = os.path.join(base_path, 'mipmap-anydpi-v26')
if os.path.exists(anydpi):
    for f in os.listdir(anydpi):
        os.remove(os.path.join(anydpi, f))
        print(f"Removed adaptive icon: {f}")

print('All icons created!')
