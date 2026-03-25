"""Dataset on the evolution of mosquito-borne diseases in Latin America and the Caribbean 2015-2024. In
DOI: https://github.com/juanmoisesd/evolution-of-mosquito-borne-diseases-in-latin-america-2015-2024-database-by-coun | GitHub: https://github.com/juanmoisesd/evolution-of-mosquito-borne-diseases-in-latin-america-2015-2024-database-by-coun"""
__version__="1.0.0"
__author__="de la Serna, Juan Moisés"
import pandas as pd, io
try:
    import requests
except ImportError:
    raise ImportError("pip install requests")

def load_data(filename=None):
    """Load dataset from Zenodo. Returns pandas DataFrame."""
    rid="https://github.com/juanmoisesd/evolution-of-mosquito-borne-diseases-in-latin-america-2015-2024-database-by-coun".split(".")[-1]
    meta=requests.get(f"https://zenodo.org/api/records/{rid}",timeout=30).json()
    csvs=[f for f in meta.get("files",[]) if f["key"].endswith(".csv")]
    if not csvs: raise ValueError("No CSV files found")
    f=next((x for x in csvs if filename and x["key"]==filename),csvs[0])
    return pd.read_csv(io.StringIO(requests.get(f["links"]["self"],timeout=60).text))

def cite(): return f'de la Serna, Juan Moisés (2025). Dataset on the evolution of mosquito-borne diseases in Latin America and the Car. Zenodo. https://github.com/juanmoisesd/evolution-of-mosquito-borne-diseases-in-latin-america-2015-2024-database-by-coun'
def info(): print(f"Dataset: Dataset on the evolution of mosquito-borne diseases in Latin America and the Car\nDOI: https://github.com/juanmoisesd/evolution-of-mosquito-borne-diseases-in-latin-america-2015-2024-database-by-coun\nGitHub: https://github.com/juanmoisesd/evolution-of-mosquito-borne-diseases-in-latin-america-2015-2024-database-by-coun")