import pip
from pip._internal import main as pipmain

def install_whl(path):
    pip.main(['install', path])

install_whl(r"C:\\Users\\LarsErikHaukås.LT-PF1VY9A4\\OneDrive - Krokeide Videregående Skole\\VG1\\curses-2.2.1+utf8-cp310-cp310-win_amd64.whl")