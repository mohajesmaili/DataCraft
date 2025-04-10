from datasets import load_dataset
from langdetect import detect, LangDetectException

# Load the dataset
dataset = load_dataset("MohamedRashad/arabic-img2md")  # Actual dataset name

def is_arabic(text):
    try:
        return detect(text) != 'en'  # Keep only non-English texts
    except LangDetectException:
        return False

# Extract non-English texts from the 'markdown' column
arabic_texts = [
    sample["markdown"] for sample in dataset["train"] 
    if is_arabic(sample["markdown"])
]

# Save to a txt file
output_file = "arabic_texts.txt"
with open(output_file, "w", encoding="utf-8") as f:
    for index, text in enumerate(arabic_texts):
        f.write(text + "\n")
        print(f"Number: {index}")

print(f"Total Number of Texts: {len(dataset['train'])}")
print(f"Total Number of Arabic Texts: {len(arabic_texts)}")