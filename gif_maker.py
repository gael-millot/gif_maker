from PIL import Image, ImageOps
import glob, os




# Parameters that need to be set by the user
image_folder = r"/mnt/c/Users/gmillot/Documents/Git_projects/gif_maker/dataset" # example for Linux execution: "/mnt/c/Users/gmillot/Documents/Git_projects/gif_maker/gif_maker.py". Example for Windows PowerShell execution: "C:\Users\gmillot\Documents\Git_projects\gif_maker\gif_maker.py"
target_size = (800, 600)  # (width, height) of the output gif (in points)
delay=1000 # millisecondes
# End Parameters that need to be set by the user

# Output folder (on your Desktop, next to the script)
output_folder = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(output_folder, exist_ok=True)

# Gather all images in the folder with common extensions
image_files = []
for ext in ("*.jpg", "*.jpeg", "*.png", "*.bmp", "*.gif"):
    image_files.extend(glob.glob(os.path.join(image_folder, ext)))

if not image_files:
    print(f"No images found in {image_folder}")
    exit()

# Resize and pad each image
for file in image_files:
    img = Image.open(file)
    img.thumbnail(target_size, Image.Resampling.LANCZOS)
    result = ImageOps.pad(img, target_size, color='white')
    result.save(os.path.join(output_folder, f"resized_{os.path.basename(file)}"))

# Create the GIF from resized images
resized_files = sorted(glob.glob(os.path.join(output_folder, "resized_*")))
frames = [Image.open(img) for img in resized_files]

frames[0].save(
    os.path.join(output_folder, 'slideshow.gif'),
    format='GIF',
    save_all=True,
    append_images=frames[1:],
    duration=delay, # millisecondes
    loop=0
)

print(f"✅ GIF created successfully at: {output_folder}")