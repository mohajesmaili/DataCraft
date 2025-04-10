# Read the input text file
input_file = 'Raw_Data/input.txt'  # Replace with your file path
output_file = 'Image_Creator/Segment_Text.txt'

Split_Word=9

with open(input_file, 'r', encoding='utf-8') as f:
    text = f.read()

# Split the text into words
words = text.split()

# Create sentences with exactly 8 words each
split_text = []
for i in range(0, len(words), Split_Word):
    chunk = words[i:i + Split_Word]  # Take up to 8 words at a time
    split_text.append(' '.join(chunk))

# Write to output file (each part on a new line)
with open(output_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(split_text))

print(f"Success! The text has been split into sentences of {Split_Word} words and saved to {output_file}")