from config import UPLOAD_PATH
from os import path, listdir, remove

# define methods
def recover_image(id):
    files = listdir(UPLOAD_PATH)
    if files:
        for file in files:
            if f'img_{id}_' in file:
                return file
    else:
        pass

def delete_file(id):
    file = recover_image(id)
    if file:
        remove(path.join(UPLOAD_PATH, file))
    else:
        pass