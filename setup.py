from setuptools import setup

APP = ['image_downloader_gui.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': False,
    'packages': ['PyQt5', 'requests', 'selenium', 'chromedriver_autoinstaller', 'chardet', 'charset_normalizer'],
    'iconfile': 'icon.icns',
}

setup(
    name='ImageDownloader',
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)