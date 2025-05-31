import zipfile
import pathlib


def make_archive(files_path, dest_dir):
    dest_path = pathlib.Path(dest_dir, 'compressed.zip')
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for file_path in files_path:
            file_path = pathlib.Path(file_path) # make specific path object
            archive.write(file_path, arcname=file_path.name)


if __name__ == '__main__':
    make_archive(files_path=['files/a.txt', 'files/b.txt', 'files/c.txt'], dest_dir='compressed')
