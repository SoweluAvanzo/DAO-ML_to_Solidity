import os

PATH_SEPARATOR_CHAR = os.path.sep
INVALID_FILE_CHARS = ":; \t\n\r()[]{}|!\"£$%&=?^\'^*@#§°€<>"


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


def concat_folder_filename(*parts) -> str:
    return os.path.join(*parts)


def file_exists(path: str):
    return os.path.isfile(path)


def list_files_in(folder_path: str):
    return os.listdir(folder_path)


def delete_file(file_path: str):
    return os.remove(file_path)


def extract_folder_from_full_path(full_path: str):
    index_start_filename = full_path.rfind(os.sep)
    if index_start_filename <= 0:
        return full_path
    return full_path[:index_start_filename]


def sanitize_filename(s: str) -> str:
    for c in INVALID_FILE_CHARS:
        s = s.replace(c, '_')
    return s
