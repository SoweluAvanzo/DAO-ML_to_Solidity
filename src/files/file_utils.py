import os

def check_and_make_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def get_base_folder(folder_base):
    if folder_base != None:
        return folder_base
    try:
        return os.path.abspath(__file__)
    except:
        return os.getcwd()

def concat_folder_filename(*parts):
    return os.path.join(*parts)
