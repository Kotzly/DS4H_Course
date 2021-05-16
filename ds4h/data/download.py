import shutil
import urllib.request as request
from contextlib import closing
from pathlib import Path
import zipfile38 as zipfile
from ds4h.data.download_utils import download_from_url, get_sinasc_url, get_sim_url, get_srag_url

DEPTH = "../.."

FILEPATH = "ftp://ftp.datasus.gov.br/tabwin/tabwin/TAB415.zip"
THIRD_PARTY_FOLDER = Path(__file__).absolute().parent / DEPTH / "third_party"
OUTPUT_FILEPATH =  THIRD_PARTY_FOLDER / "TAB415.zip"

def download_ftp(url, savepath):
    with closing(request.urlopen(url)) as r:
        with open(savepath, 'wb') as f:
            shutil.copyfileobj(r, f)

if __name__ == "__main__":
    
    if not OUTPUT_FILEPATH.exists():
        print("Downloading ZIP file.")
        download_from_url(FILEPATH, OUTPUT_FILEPATH)
    else:
        print("ZIP file already downloaded.")

    if not (THIRD_PARTY_FOLDER / "dbf2dbc.exe").exists():
        print("Extracting to", THIRD_PARTY_FOLDER)
        with zipfile.ZipFile(OUTPUT_FILEPATH, 'r') as zip_ref:
            zip_ref.extractall(THIRD_PARTY_FOLDER)

    RAW_SINASC_FOLDER = Path(".") / DEPTH / "data" / "raw" / "SINASC_dbf" 
    RAW_SIM_FOLDER = Path(".") / DEPTH / "data" / "raw" / "SIM_dbf" 
    RAW_SRAG_FOLDER = Path(".") / DEPTH / "data" / "raw" / "SRAG_csv" 

    RAW_SINASC_FOLDER.mkdir(exist_ok=True, parents=True)
    RAW_SIM_FOLDER.mkdir(exist_ok=True, parents=True)
    RAW_SRAG_FOLDER.mkdir(exist_ok=True, parents=True)

    for year in range(2010, 2021 + 1):
        sinasc_url_path = get_sinasc_url("SP", year)
        sim_fet_url_path = get_sim_url("SP", year, "DOFET")
        sim_mat_url_path = get_sim_url("SP", year, "DOMAT")

        name = lambda x: x.split("/")[-1]

        download_from_url(
            sinasc_url_path,
            RAW_SINASC_FOLDER / name(sinasc_url_path)
        )
        download_from_url(
            sim_fet_url_path,
            RAW_SIM_FOLDER / name(sim_fet_url_path)
        )
        download_from_url(
            sim_mat_url_path,
            RAW_SIM_FOLDER / name(sim_mat_url_path)
        )
    
        srag_url = get_srag_url(year)

        if srag_url is not None:
            download_from_url(
                srag_url,
                RAW_SRAG_FOLDER / name(srag_url),
            )