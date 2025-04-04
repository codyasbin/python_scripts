import os
import shutil

def organize_files_by_type(directory):
    # Dictionary to map file extensions to their corresponding folder names
    file_type_folders = {
        '.txt': 'Text',
        '.jpg': 'Images',
        '.jpeg': 'Images',
        '.png': 'Images',
        '.gif': 'Images',
        '.pdf': 'Documents',
        '.docx': 'Documents',
        '.xlsx': 'Spreadsheets',
        '.csv': 'Spreadsheets',
        '.ppt': 'Presentations',
        '.pptx': 'Presentations',
        # Add more file extensions and their corresponding folder names here
    }

    # Change working directory to the target directory
    os.chdir(directory)

    # Iterate over all the files in the directory
    for filename in os.listdir(directory):
        # Skip directories
        if os.path.isdir(filename):
            continue

        # Get file extension
        _, file_extension = os.path.splitext(filename)

        # Determine the folder name based on file extension
        folder_name = file_type_folders.get(file_extension.lower())

        # If the file type is known
        if folder_name:
            # Create the folder if it doesn't exist
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)

            # Move the file to the corresponding folder
            shutil.move(filename, os.path.join(folder_name, filename))

if __name__ == "__main__":
    target_directory = input("Enter the path of the directory to organize: ")
    organize_files_by_type(target_directory)
    print(f"Files in '{target_directory}' have been organized by type.")
