"""
Script de limpeza do dataset Heart Disease (Cleveland).
Alinhado às decisões da EDA (notebooks/eda_heart_cleveland.ipynb, seção 8).

- Substitui "?" em ca e thal por NaN, preenche com a moda e converte para numérico.
- Cria coluna target_binario (0 = sem doença, 1 = risco).
- Mantém o valor 564 de colesterol (documentar no README).
- Salva resultado em data/heart_real_cleaned.csv.
"""

import os
import pandas as pd
import numpy as np

# -----------------------------------------------------------------------------
# 1. Caminhos 
# -----------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PATH_RAW = os.path.join(BASE_DIR, "..", "data", "heart_disease_cleveland_raw.csv")
PATH_CLEANED = os.path.join(BASE_DIR, "..", "data", "heart_real_cleaned.csv")

COLUMNS = [
    "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
    "thalach", "exang", "oldpeak", "slope", "ca", "thal", "target",
]

# -----------------------------------------------------------------------------
# 2. Carregar dados brutos
# -----------------------------------------------------------------------------
df = pd.read_csv(PATH_RAW, header=None, names=COLUMNS)
print(f"Linhas carregadas: {len(df)}")

# -----------------------------------------------------------------------------
# 3. Tratar "?" em ca e thal (preencher com moda, converter para numérico)
# -----------------------------------------------------------------------------
for col in ["ca", "thal"]:
    # Substituir "?" por NaN (garante que reconhecemos como faltante)
    df[col] = df[col].replace("?", np.nan)
    # Converter para numérico (valores não numéricos viram NaN)
    df[col] = pd.to_numeric(df[col], errors="coerce")
    # Preencher NaN com a moda da coluna
    mode_val = df[col].mode()
    fill_val = mode_val.iloc[0] if len(mode_val) > 0 else 0
    df[col] = df[col].fillna(fill_val)
    # Garantir tipo inteiro (ca e thal são categorias 0-3, 3/6/7)
    df[col] = df[col].astype(int)
    print(f"  {col}: preenchidos com moda = {fill_val}")

# -----------------------------------------------------------------------------
# 4. Criar target_binario (0 = sem doença, 1 = risco)
# -----------------------------------------------------------------------------
df["target_binario"] = (df["target"] >= 1).astype(int)
print(f"target_binario: 0 = { (df['target_binario'] == 0).sum() }, 1 = { (df['target_binario'] == 1).sum() }")

# -----------------------------------------------------------------------------
# 5. Salvar dataset limpo
# -----------------------------------------------------------------------------
df.to_csv(PATH_CLEANED, index=False)
print(f"\nDataset limpo salvo em: {PATH_CLEANED}")
print(f"Shape final: {df.shape}")
