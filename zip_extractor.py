import zipfile


def extract_archive(file_path, dest_dir):
    with zipfile.ZipFile(file_path, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == '__main__':
    extract_archive(file_path=r'D:\Python\PythonProject\todo_app\compressed\compressed.zip',
                    dest_dir=r'D:\Python\PythonProject\todo_app\files')
