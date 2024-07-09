import os
import sys

def rename_folder(folder_path, new_name):
    # Get the directory of the current folder
    folder_directory = os.path.dirname(folder_path)
    
    # New folder path with the new name
    new_folder_path = os.path.join(folder_directory, new_name)
    
    try:
        # Rename the folder
        os.rename(folder_path, new_folder_path)
        print(f'Successfully renamed folder to "{new_name}".')
    except Exception as e:
        print(f'Error occurred while renaming the folder: {e}')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please drag and drop one or more folders onto the script.")
        sys.exit(1)

    # Process each folder path provided
    for folder_path in sys.argv[1:]:
        new_folder_name = folder_path + '_archive'
        rename_folder(folder_path, new_folder_name)

