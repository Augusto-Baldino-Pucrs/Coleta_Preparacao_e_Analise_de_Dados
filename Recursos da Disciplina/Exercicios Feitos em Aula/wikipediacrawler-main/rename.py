import os
import re

def rename_files():
    directory = 'pages'
    invalid_chars = r'[\\/:*?"<>|]'

    for filename in os.listdir(directory):
        new_filename = re.sub(invalid_chars, '', filename)
        if new_filename != filename:
            print(f'Renaming: {filename} -> {new_filename}')
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

if __name__ == "__main__":
    rename_files()