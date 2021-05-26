
from pathlib import Path
import multiprocessing as mp
from time import time
import shutil
import zipfile
import os
from ds4h.data.download import download_ftp

DEFAULT_YEARS = range(2010, 2019 + 1)
SINASC_2020_URL = "http://svs.aids.gov.br/dantps/centrais-de-conteudos/dados-abertos/sinasc/DNBR20DA.zip"

N_JOBS = 4

def download_dbc(save_path, years=DEFAULT_YEARS, n_jobs=N_JOBS):
    save_path = Path(save_path)

    save_path.mkdir(exist_ok=True)

    SINASC_URLS = [
        f"ftp://ftp.datasus.gov.br/dissemin/publicos/SINASC/1996_/Dados/DNRES/DNSP{year}.dbc"
        for year in years
    ]  

    args = [
        (url, save_path / url.split("/")[-1])
        for url in SINASC_URLS
    ]

    print("Downloading data from {} years using {} threads".format(len(SINASC_URLS), N_JOBS), end="")
    start = time()
    with mp.Pool(n_jobs) as pool:
        pool.starmap(download_ftp, args)
    print(
        "Download completed in {:.1f}s".format(time() - start)
    )

def download_dbf_2020(save_folder):
    save_folder = Path(save_folder)
    save_folder.mkdir(exist_ok=True, parents=True)

    zip_filename = SINASC_2020_URL.split("/")[-1]
    
    zip_save_filepath = save_folder / zip_filename

    download_ftp(SINASC_2020_URL, zip_save_filepath)
    with zipfile.ZipFile(zip_save_filepath, 'r') as zip_ref:
        zip_ref.extractall(save_folder)
    
    os.remove(zip_save_filepath)


