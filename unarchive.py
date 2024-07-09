# -*- coding: utf-8 -*-
import os
import zipfile
import sys

def unzip_folder(zip_file_path, extract_to_path):
    """
    Extracts the contents of the specified ZIP file into a directory.
    
    Args:
        zip_file_path (str): The path of the ZIP file to be extracted.
        extract_to_path (str): The path where the contents will be extracted.
    """
    with zipfile.ZipFile(zip_file_path, 'r') as zipf:
        zipf.extractall(extract_to_path)

def process_zip_files(archive_dir, root_dir):
    """
    Processes the archive directory to find and unzip ZIP files.
    Prints the progress of extraction.

    Args:
        archive_dir (str): The archive directory to be processed.
        root_dir (str): The directory where unzipped folders will be saved.
    """
    zip_files = [os.path.join(root, file) 
                 for root, _, files in os.walk(archive_dir) 
                 for file in files if file.endswith('.zip')]

    total_zip_files = len(zip_files)
    for count, zip_file_path in enumerate(zip_files, start=1):
        relative_path = os.path.relpath(zip_file_path, archive_dir)
        extract_to_path = os.path.join(root_dir, os.path.dirname(relative_path))

        print(f"Extracting file {count} of {total_zip_files}: {zip_file_path}")
        if not os.path.exists(extract_to_path):
            os.makedirs(extract_to_path)
        unzip_folder(zip_file_path, extract_to_path)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for archive_dir in sys.argv[1:]:
            archive_dir = archive_dir.strip().strip('"')  # Remove leading and trailing whitespace and quotes
            if archive_dir.endswith('_archive') and os.path.isdir(archive_dir):
                root_dir = archive_dir[:-8]  # Remove '_archive' from the end
                if not os.path.exists(root_dir):
                    os.makedirs(root_dir)
                print(f"Processing archive directory: {archive_dir}")
                process_zip_files(archive_dir, root_dir)  # Process and unzip the ZIP files
                print(f"Unzipping completed for {archive_dir}. Unzipped folders are saved in: {root_dir}")
            else:
                print(f"Skipping non-archive directory: {archive_dir}")
    else:
        print("Please provide the archive directory paths by dragging and dropping them onto the script.")
