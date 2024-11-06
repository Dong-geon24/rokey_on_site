import os

def delete_txt_files(directory):
    """
    Deletes all .txt files in the specified directory.

    Parameters:
    - directory: The directory where .txt files will be deleted.
    """
    # List all files in the directory
    files_in_directory = os.listdir(directory)

    # Loop through the files and delete the ones with .txt extension
    for file in files_in_directory:
        if file.endswith('.txt'):
            file_path = os.path.join(directory, file)
            try:
                os.remove(file_path)
                print(f"Deleted: {file}")
            except Exception as e:
                print(f"Error deleting {file}: {e}")

def main():
    # Specify the directory where .txt files should be deleted
    directory = '/home/rokey/Downloads/sung_c'  # 디렉토리 경로를 입력하세요.

    delete_txt_files(directory)

if __name__ == "__main__":
    main()
