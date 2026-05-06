import os
import shutil

# Folder path to organize (change this)
SOURCE_FOLDER = r"D:\Downloads"

# File type mapping
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
}

def organize_files():
    for file in os.listdir(SOURCE_FOLDER):
        file_path = os.path.join(SOURCE_FOLDER, file)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        moved = False
        for folder, extensions in FILE_TYPES.items():
            if file.lower().endswith(tuple(extensions)):
                folder_path = os.path.join(SOURCE_FOLDER, folder)
                os.makedirs(folder_path, exist_ok=True)
                shutil.move(file_path, folder_path)
                moved = True
                break

        # Move unknown files to "Others"
        if not moved:
            others_path = os.path.join(SOURCE_FOLDER, "Others")
            os.makedirs(others_path, exist_ok=True)
            shutil.move(file_path, others_path)

    print("✅ File organization completed!")

organize_files()
