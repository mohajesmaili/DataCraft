from PIL import Image, ImageDraw, ImageFont
import os

# Initial settings
FONT_DIR = "Image_Creator/Fonts/"         # Fonts folder
OUTPUT_DIR = "Image_Creator/Output"       # Output images folder
IMAGE_SIZE = (1100, 110)    # Image size
FONT_SIZE = 35              # Font size
BG_COLOR = (255, 255, 255)  # Background color
TEXT_COLOR = (0, 0, 0)      # Text color

wordlist_file = "Image_Creator/Segment_Text.txt"

# Reading the file contents
with open(wordlist_file, "r", encoding="utf-8") as file:
    wordlist = file.readlines()

# Removing spaces and empty lines from the end of each word
wordlist = [word.strip() for word in wordlist]

# Creating the output folder (if it doesn't exist)
os.makedirs(OUTPUT_DIR, exist_ok=True)

for filename in os.listdir(FONT_DIR):
    if filename.lower().endswith(".ttf") or filename.lower().endswith(".otf"):
        font_path = os.path.join(FONT_DIR, filename)
        font_name = os.path.splitext(filename)[0]

        try:
            for index, i in enumerate(wordlist):
                img = Image.new("RGB", IMAGE_SIZE, BG_COLOR)
                draw = ImageDraw.Draw(img)

                font = ImageFont.truetype(font_path, FONT_SIZE)
                text_width, text_height = draw.textsize(i, font=font)
                position = ((IMAGE_SIZE[0] - text_width) // 2, (IMAGE_SIZE[1] - text_height) // 2)

                # Writing text on the image
                draw.text(position, i, font=font, fill=TEXT_COLOR)

                # Saving the image
                output_path = os.path.join(OUTPUT_DIR, f"{index}_{font_name}.jpeg")
                img.save(output_path)
                print(f" Segment {index}_{font_name} Created")

        except Exception as e:
            print(f" Error: {filename}: {e}")