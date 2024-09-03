import pip
from pip._internal import main as pipmain

def install_whl(path):
    pip.main(['install', path])

install_whl(r"LOL")
