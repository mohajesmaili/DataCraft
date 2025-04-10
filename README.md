# DataCraft

Welcome to **DataCraft**, a project designed to create, process, and manage datasets with a focus on text-to-image generation and multilingual text processing. This repository is divided into four main components, each serving a specific purpose in the workflow.

## Project Structure

### 1. Image_Creator
- **Purpose**: Generates images from text using specific fonts.
- **Description**: This section takes text input (e.g., from a wordlist) and creates images with customizable fonts. It uses Python’s PIL (Pillow) library to render text onto images with predefined settings like font size, background color, and text color.
- **Key Features**:
  - Supports multiple font files (`.ttf` or `.otf`).
  - Outputs images in JPG format.
  - Centers text dynamically based on image size.
- **Directory**: `Image_Creator/`
- **Example Usage**: Run the script to convert a list of words into images with various fonts.

### 2. Load_Dataset
- **Purpose**: Loads datasets to extract text content.
- **Description**: This part is responsible for fetching datasets (e.g., from Hugging Face) and extracting textual data, specifically targeting non-English content like Arabic or Persian markdown files. It uses the `datasets` library and language detection to filter texts.
- **Key Features**:
  - Filters out English text using `langdetect`.
  - Saves extracted text into a `.txt` file for further processing.
- **Directory**: Contains the script for dataset loading (e.g., `load_dataset.py`).

### 3. Raw_Data
- **Purpose**: Stores raw text files.
- **Description**: This section acts as a storage hub for unprocessed text data extracted from datasets or provided manually. It serves as the input source for other components like `Image_Creator` or `Vocab`.
- **Key Features**:
  - Simple text files (`.txt`) containing raw data.
  - No processing applied at this stage.
- **Directory**: `Raw_Data/`

### 4. Vocab
- **Purpose**: Processes and normalizes Persian and Arabic words.
- **Description**: This component focuses on cleaning, normalizing, and preparing Persian and Arabic text for further use (e.g., removing diacritics, standardizing characters, or creating a vocabulary list). It’s useful for downstream tasks like dataset creation or NLP.
- **Key Features**:
  - Handles multilingual text preprocessing.
  - Outputs normalized word lists or vocabularies.
- **Directory**: `Vocab/`
- **Example Usage**: Normalize a raw text file to prepare it for image generation or analysis.
