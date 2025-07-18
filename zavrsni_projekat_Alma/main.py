from src.extract.extractor import load_dataset
from src.transform.transformer import clean_dataset
from src.load.loader import load_to_mssql

dataset_path = "zavrsni_projekat_Alma\data\winequality-red.csv"
table_name = "winequality-red"
connection_string = "mssql+pyodbc://DESKTOP-36F1SCR\SQLEXPRESS/Wine?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"

df = load_dataset(dataset_path)
df_clean = clean_dataset(df)
load_to_mssql(df_clean, table_name, connection_string)


from analysis import upiti

if __name__ == "__main__":
    upiti.pokreni_upite()

from sqlalchemy import create_engine
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import os

def run_notebook(notebook_path):
    with open(notebook_path) as f:
        nb = nbformat.read(f, as_version=4)
    
    ep = ExecutePreprocessor(timeout=600, kernel_name='venv')
    ep.preprocess(nb, {'metadata': {'path': os.path.dirname(notebook_path)}})

    # Sačuvan izvršeni notebook da vidimo rezultate
    executed_path = notebook_path.replace('.ipynb', '_executed.ipynb')
    with open(executed_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

    print(f"Notebook izvršen i sačuvan kao: {executed_path}")

if __name__ == "__main__":
    run_notebook("C:/Users/Alma/Desktop/zavrsniAlma/zavrsni_projekat_Alma/analysis/eda.ipynb")

from ml.train_model import run_training

if __name__ == "__main__":
    connection_string = "mssql+pyodbc://DESKTOP-36F1SCR\\SQLEXPRESS/wine?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"
    table_name = "winequality_red"
    run_training(connection_string, table_name)



