import shutil
import urllib.request as request
from contextlib import closing

STATES = "AC AL AP AM BA CE DF ES GO MA MT MS MG PA PB PR PE PI RJ RN RS RO RR SC SP SE TO".split()

def get_sinasc_url(state, year):
    if not state in STATES:
        print(f"No state {state}.")
        return None
    url = f"ftp://ftp.datasus.gov.br/dissemin/publicos/SINASC/1996_/Dados/DNRES/DN{state}{year}.dbc"
    return url

    
def get_srag_url(year):
    urls = {
        2020: "https://s3-sa-east-1.amazonaws.com/ckan.saude.gov.br/SRAG/2020/INFLUD-12-04-2021.csv",
        2021: "https://s3-sa-east-1.amazonaws.com/ckan.saude.gov.br/SRAG/2021/INFLUD21-12-04-2021.csv"
    }
    if not year in urls:
        print("Please select one of the years:", list(urls.keys()))
        return None
    return urls[year]

def get_sim_url(state, year, domain="DOMAT"):
    if not state in STATES:
        print(f"No state {state}.")
        return None
    domains = ["DOMAT", "DO", "DOFET"]
    if domain == "DOMAT":
        url = f"ftp://ftp.datasus.gov.br/dissemin/publicos/SIM/CID10/DOFET/DOMAT{year % 100}.dbc"
    elif domain == "DO":
        url = f"ftp://ftp.datasus.gov.br/dissemin/publicos/SIM/CID10/DORES/DO{state}{year}.dbc"
    elif domain == "DOFET":
        url = f"ftp://ftp.datasus.gov.br/dissemin/publicos/SIM/CID10/DOFET/DOFET{year % 100}.dbc"
    return url


def get_preprocessed_url_id(what):
    return {
        "csv": "1MG2aEjc2YXK2pPr_LgNnYCp_V0RCLXmw",
        "dbf": "1ECVCGkma71aGabmf-wXVF4_UOttUQQCV"
    }[what]

def download_from_url(urlpath, savepath):
    try:
        with closing(request.urlopen(urlpath)) as r:
            with open(savepath, 'wb') as f:
                shutil.copyfileobj(r, f)
    except:
        print(urlpath, "does not exist.")