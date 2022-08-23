import sys
from bot import aria2, LOGGER, DOWNLOAD_DIR
import shutil
import os
import pathlib
import magic
import tarfile
from .exceptions import NotSupportedExtractionArchive


def clean_download(path: str):
    if os.path.exists(path):
        LOGGER.info(f"Cleaning download: {path}")
        shutil.rmtree(path)


def start_cleanup():
    try:
        shutil.rmtree(DOWNLOAD_DIR)
    except FileNotFoundError:
        pass


def clean_all():
    aria2.remove_all(True)
    try:
        shutil.rmtree(DOWNLOAD_DIR)
    except FileNotFoundError:
        pass


def exit_clean_up(signal, frame):
    try:
        LOGGER.info("Please wait, while we clean up the downloads and stop running downloads")
        clean_all()
        sys.exit(0)
    except KeyboardInterrupt:
        LOGGER.warning("Force Exiting before the cleanup finishes!")
        sys.exit(1)


def get_mime_type(file_path):
    mime = magic.Magic(mime=True)
    mime_type = mime.from_file(file_path)
    mime_type = mime_type if mime_type else "text/plain"
    return mime_type
