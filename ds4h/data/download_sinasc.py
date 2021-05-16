
from pathlib import Path
from ds4h.data.download import download_ftp

DEFAULT_YEARS = range(2010, 2019 + 1)

def download_dbc(save_path, years=DEFAULT_YEARS):
    dbc_save_folder = Path(save_path)

    dbc_save_folder.mkdir(exist_ok=True)

    SINASC_URLS = [
        f"ftp://ftp.datasus.gov.br/dissemin/publicos/SINASC/1996_/Dados/DNRES/DNSP{year}.dbc"
        for year in years
    ]  

    for url in SINASC_URLS:
        print("Downloading", url.split("/")[-1])
        save_path = dbc_save_folder / url.split("/")[-1]
        download_ftp(url, save_path)
    