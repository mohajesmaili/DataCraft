import os
from glob import glob
import arabic_reshaper
from bidi.algorithm import get_display
from trdg.generators import GeneratorFromStrings

# Font and path settings
FONTS_DIR = "Image_Creator/Fonts/"         # Fonts folder
OUTPUT_DIR = "Image_Creator/Output"     
INPUT_FILE = "Vocab/Result/Normilized_fas.txt" 
MAX_LINES_TO_PROCESS = 1000

# Create output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load all .ttf fonts from the fonts directory
font_files = glob(os.path.join(FONTS_DIR, '*.ttf'))
if not font_files:
    raise ValueError("No fonts found in the specified directory!")

print(f"Number of fonts found: {len(font_files)}")

# Function to prepare Persian text for rendering
def prepare_farsi_text(text):
    reshaper = arabic_reshaper.ArabicReshaper(
        {'delete_harakat': False}  # Preserves diacritics
    )
    reshaped_text = reshaper.reshape(text)
    return get_display(reshaped_text)  # Handles right-to-left (RTL) direction

with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f if line.strip()] 


selected_lines = lines[:MAX_LINES_TO_PROCESS]
texts = [prepare_farsi_text(line) for line in selected_lines]

# Generator settings
generator = GeneratorFromStrings(
    texts,
    fonts=font_files,  # Use all detected fonts
    language='fa',     # Persian/Arabic language mode
    size=70,           # Font size
    background_type=2, # Random background
    text_color='#000000',  # Black text
    margins=(10, 10, 10, 10)   # Margins (top, right, bottom, left)
)

# Generate and save images
for i, (img, lbl) in enumerate(generator):
    output_path = os.path.join(OUTPUT_DIR, f'output_{i}.png')
    img.save(output_path)
    print(f'Image saved: {output_path} (Font used: {generator.fonts[i % len(generator.fonts)]})')