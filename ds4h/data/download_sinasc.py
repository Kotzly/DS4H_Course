
DEFAULT_YEARS = range(2010, 2019 + 1)

def download_dbc(save_path, years=DEFAULT_YEARS):
    root = Path(save_path)

    #Paulo criou a pasta aqui? 
    dbc_save_folder = root / "SINASC_DBC"
    dbf_save_folder = root / "SINASC_DBF"
    csv_save_folder = root / "SINASC_CSV"

    dbc_save_folder.mkdir(exist_ok=True)
    dbf_save_folder.mkdir(exist_ok=True)
    csv_save_folder.mkdir(exist_ok=True)

    SINASC_URLS = [
        f"ftp://ftp.datasus.gov.br/dissemin/publicos/SINASC/1996_/Dados/DNRES/DNSP{year}.dbc"
        for year in range(2010, 2019 + 1)
    ]  

    for url in SINASC_URLS:
        print("Downloading", url.split("/")[-1])
        save_path = dbc_save_folder / url.split("/")[-1]
        download_ftp(url, save_path)
    