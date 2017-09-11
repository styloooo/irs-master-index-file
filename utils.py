import shutil
import os
import zipfile

from urllib.request import urlopen

DB_URL = os.environ['DB_URL']

DOWNLOAD_FILE_DIR = os.path.join(os.getcwd(), 'data')
EXTRACTED_FILE_DIR = os.path.join(DOWNLOAD_FILE_DIR, 'unzipped')
CSV_FILE_DIR = os.path.join(DOWNLOAD_FILE_DIR, 'csv')


def unzip_file(path):
    zippedFile = zipfile.ZipFile(path, 'r')
    zippedFile.extractall(EXTRACTED_FILE_DIR)
    zippedFile.close()
    # how to get one file name to return path


def download_file(url):
    fileName = url.split('/')[-1]
    extension = fileName.split('.')[-1]

    zipped = True if extension == 'zip' else False

    if zipped:
        outFilePath = os.path.join(DOWNLOAD_FILE_DIR, fileName)
    else:
        outFilePath = os.path.join(EXTRACTED_FILE_DIR, fileName)

    with urlopen(url) as response, open(outFilePath, 'wb') as outFile:
        shutil.copyfileobj(response, outFile)

    if zipped:
        unzip_file(outFilePath)
