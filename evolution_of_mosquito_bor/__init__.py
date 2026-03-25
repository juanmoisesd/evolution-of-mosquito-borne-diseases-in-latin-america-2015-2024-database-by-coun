"""Dataset on the evolution of mosquito-borne diseases in Latin America and the Car
DOI:https://juanmoisesd.github.io/evolution-of-mosquito-borne-diseases-in-latin-america-2015-2024-database-by-coun/"""
__version__="1.0.0"
import pandas as pd,io,requests
def load_data(f=None):
  rid="https://juanmoisesd.github.io/evolution-of-mosquito-borne-diseases-in-latin-america-2015-2024-database-by-coun/".split(".")[-1];m=requests.get("https://zenodo.org/api/records/"+rid,timeout=30).json();csvs=[x for x in m.get("files",[]) if x["key"].endswith(".csv")]
  if not csvs:raise ValueError("No CSV")
  tgt=next((x for x in csvs if f and x["key"]==f),csvs[0]);return pd.read_csv(io.StringIO(requests.get(tgt["links"]["self"],timeout=60).text))
def cite():return "de la Serna, Juan Moisés (2025). Dataset on the evolution of mosquito-borne diseases in Latin"
def info():print("DOI: https://juanmoisesd.github.io/evolution-of-mosquito-borne-diseases-in-latin-america-2015-2024-database-by-coun/\nGitHub: https://github.com/juanmoisesd/evolution-of-mosquito-borne-diseases-in-latin-america-2015-2024-database-by-coun")
