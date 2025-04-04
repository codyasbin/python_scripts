import os
import hashlib

def get_file_checksum(file_path):
    """
    Generate MD5 checksum of a file.
    """
    hasher = hashlib.md5()
    try:
        with open(file_path, 'rb') as file:
            for chunk in iter(lambda: file.read(4096), b""):
                hasher.update(chunk)
    except UnicodeDecodeError:
        pass  # Ignore files that cannot be decoded
    return hasher.hexdigest()

def find_duplicates(directory):
    """
    Find duplicate files in a directory and its subdirectories.
    """
    duplicates = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            checksum = get_file_checksum(file_path)
            if checksum in duplicates:
                duplicates[checksum].append(file_path)
            else:
                duplicates[checksum] = [file_path]
    return {checksum: file_paths for checksum, file_paths in duplicates.items() if len(file_paths) > 1}

def delete_duplicates(duplicates):
    """
    Delete duplicate files, keeping only the original ones.
    """
    for checksum, file_paths in duplicates.items():
        original_file = file_paths[0]
        duplicate_files = file_paths[1:]
        print(f"Keeping original file: {original_file}")
        for duplicate_file in duplicate_files:
            print(f"Deleting duplicate file: {duplicate_file}")
            os.remove(duplicate_file)

def main():
    directory = input("Enter the directory path to search for duplicate files: ")
    if not os.path.isdir(directory):
        print("Invalid directory path.")
        return

    duplicates = find_duplicates(directory)
    if not duplicates:
        print("No duplicate files found.")
        return

    delete_duplicates(duplicates)
    print("Duplicate files deleted successfully.")

if __name__ == "__main__":
    main()
