import os
import pandas as pd

# caminho do dataset 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "..", "data", "heart_disease_cleveland_raw.csv")

# nomes das colunas (Cleveland processed - 14 atributos; último = "num" na UCI, "target" em ML)
columns = [
    "age",       # idade (anos)
    "sex",       # sexo (1=homem, 0=mulher)
    "cp",        # tipo dor no peito (1-4)
    "trestbps",  # pressão arterial em repouso (mmHg)
    "chol",      # colesterol (mg/dl)
    "fbs",       # glicemia em jejum > 120 (1=sim, 0=não)
    "restecg",   # ECG em repouso (0,1,2)
    "thalach",   # freq. cardíaca máx. no teste (bpm)
    "exang",     # angina induzida por exercício (1=sim, 0=não)
    "oldpeak",   # depressão ST no exercício
    "slope",     # inclinação segmento ST (1,2,3)
    "ca",        # nº vasos principais (0-3)
    "thal",      # talassemia (3=normal, 6=defeito fixo, 7=reversível)
    "target"     # diagnóstico (0=sem doença, 1-4=doença; muitas vezes binarizado 0 vs 1+)
]

# carregar dataset
df = pd.read_csv(file_path, header=None, names=columns)

# mostrar primeiras linhas
print("--- Primeiras linhas ---")
print(df.head())

# informações gerais
print("\n--- Info ---")
print(df.info())