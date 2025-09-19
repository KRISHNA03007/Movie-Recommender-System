import os

# List of folders to create (lowercase)
folders = [
    "data",
    "notebooks",
    "src",
    "config",
    "logs",
    "outputs",
    "tests"
]

# Base path (current directory)
base_path = os.getcwd()  # or set a specific path like "C:/Users/krish/Desktop/NEW"

# Create folders
for folder in folders:
    folder_path = os.path.join(base_path, folder)
    try:
        os.makedirs(folder_path, exist_ok=True)  # exist_ok=True avoids error if folder exists
        print(f"Created folder: {folder_path}")
    except Exception as e:
        print(f"Error creating folder {folder_path}: {e}")
