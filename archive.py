# -*- coding: utf-8 -*-
import os
import zipfile
import sys

def zip_folder(folder_path, zip_file_path):
    """
    Compresses the contents of the specified folder into a ZIP file.
    
    Args:
        folder_path (str): The path of the folder to be compressed.
        zip_file_path (str): The path where the ZIP file will be saved.
    """
    with zipfile.ZipFile(zip_file_path + '.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, folder_path))

def create_archive_dir(root_dir):
    """
    Creates the archive directory where compressed folders will be saved.
    
    Args:
        root_dir (str): The root directory that is being processed.
    
    Returns:
        str: The path of the archive directory.
    """
    archive_dir = root_dir + "_archive"
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)
    return archive_dir

def count_folders_with_files(root_dir):
    """
    Counts the number of folders that contain files within the root directory.
    
    Args:
        root_dir (str): The root directory to be counted.
    
    Returns:
        int: The total number of folders containing files.
    """
    count = 0
    for dirpath, _, filenames in os.walk(root_dir):
        if filenames:
            count += 1
    return count

def process_directory(root_dir, archive_dir, total_folders):
    """
    Processes the root directory and compresses folders containing files.
    Prints the progress of compression.

    Args:
        root_dir (str): The root directory to be processed.
        archive_dir (str): The directory where compressed folders will be saved.
        total_folders (int): The total number of folders containing files.
    """
    current_count = 0
    for dirpath, dirnames, filenames in os.walk(root_dir):
        relative_path = os.path.relpath(dirpath, root_dir)
        archive_subdir = os.path.join(archive_dir, relative_path)

        if filenames:  # If the folder contains any files
            current_count += 1
            print(f"Compressing folder {current_count} of {total_folders}: {dirpath}")
            if not os.path.exists(os.path.dirname(archive_subdir)):
                os.makedirs(os.path.dirname(archive_subdir))
            zip_file_path = archive_subdir  # Add .zip when creating the zip file
            zip_folder(dirpath, zip_file_path)
            
            # Clear dirnames to prevent descending into subdirectories
            dirnames.clear()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for root_dir in sys.argv[1:]:
            root_dir = root_dir.strip().strip('"')  # Remove leading and trailing whitespace and quotes
            if os.path.isdir(root_dir):
                print(f"Processing directory: {root_dir}")
                archive_dir = create_archive_dir(root_dir)  # Create the archive directory
                total_folders = count_folders_with_files(root_dir)  # Count the total number of folders with files
                process_directory(root_dir, archive_dir, total_folders)  # Process and compress the folders
                print(f"Archiving completed for {root_dir}. Archived folders are saved in: {archive_dir}")
            else:
                print(f"Skipping non-directory path: {root_dir}")
    else:
        print("Please provide the root directory paths by dragging and dropping them onto the script.")

