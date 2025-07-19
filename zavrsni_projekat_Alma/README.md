# 🍷 Wine Quality Prediction Project
Dataset: winequality-red.csv
Domena: Zdravlje / prehrambena industrija
Opis: Sadrži hemijska mjerenja vina (npr. pH, alkohol, šećeri) i ocjenu kvaliteta od strane sommeliera (0–10).
Cilj: Predikcija kvaliteta vina na osnovu njegovih karakteristika.

Ovaj projekat koristi dataset **`winequality-red.csv`** za analizu i predikciju kvaliteta crvenog vina.

## 📁 Struktura projekta

```
zavrsni_projekat/
├── data/                          # Ulazni CSV fajlovi
├── etl/                           # ETL moduli (Extract, Transform, Load)
│   ├── extract/
│   │   └── extractor.py
│   ├── transform/
│   │   └── transformer.py
│   └── load/
│       └── loader.py
├── analysis/                      # Analiza podataka
│   ├── eda.ipynb                  # Exploratory Data Analysis u Jupyteru
|   |── eda_executed.ipynb         # Rezultati Data Analysis
|   |── upiti.py                   # SQL upiti u Pythonu
├── ml/                            # Machine Learning modul
│   ├── model.py                   # Trening i evaluacija modela
│   └── train_model.ipynb          # ML Notebook
├── requirements.txt               # Lista biblioteka
├── main.py                        # Glavna ETL skripta
└── README.md                      # Dokumentacija projekta
```

## 📌 Opis projekta

Cilj projekta je analizirati karakteristike crvenih vina i na osnovu tih karakteristika predvidjeti kvalitet vina korištenjem regresionih i klasifikacionih algoritama.

## ✅ Ključne faze projekta

1. **ETL obrada podataka**
   - Učitavanje iz CSV fajla
   - Čišćenje podataka i transformacija
   - Ubacivanje u SQLite bazu

 2. **SQL analiza**
   - 5 SQL upita nad bazom
   - Integracija upita u Python koristeći `sqlite3` i `pandas`

 3. **EDA - Exploratory Data Analysis**
   - Korelacija, boxplot, histogrami, scatter plot
   - Vizualizacije sa `matplotlib` i `seaborn`

4. **Mašinsko učenje**
    - split_data() za pripremu podataka
    - train_model() sa Pipeline + GridSearchCV
    - evaluate_model() za izvještaj tačnosti
    - explain_model_shap() za SHAP analizu (samo RandomForest)
    - plot_feature_importance() za feature importance (samo RandomForest) 

5. **Objektno-orijentisani kod**
   - Trening modela sa GridSearchCV pipeline-om
   - Evaluacija modela na test skupu
   - SHAP analiza (samo za RandomForest)
   - Feature importance

## ▶️ Pokretanje projekta

1. Kloniraj repozitorij:
```bash
git clone https://github.com/AlmaSnagic/ZavrsniAlma/tree/main/zavrsni_projekat_Alma
cd zavrsni_projekat_Alma
```

2. Instaliraj zavisnosti:
```bash
pip install -r requirements.txt
```

3. Pokreni Jupyter notebook:
```bash
   python .\zavrsni_projekat_Alma\main.py
```

## 🔧 Requirements

 - pandas
 - sqlalchemy
 - pyodbc
 - matplotlib
 - seaborn
 - scikit-learn
 - notebook
 - nbconvert
 - nbformat
 - scipy
 - os

---