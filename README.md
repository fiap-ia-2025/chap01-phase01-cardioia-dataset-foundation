# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
  <a href="https://www.fiap.com.br/">
    <img src="assets/img/logo-fiap.jpg" alt="FIAP - Faculdade de Informática e Administração Paulista" border="0" width="40%" height="40%">
  </a>
</p>

## 👥 Grupo [Número]

## 👨‍🎓 Integrantes

- Amanda Vieira Pires (RM566330)
- Ana Gabriela Soares Santos (RM565235)
- Bianca Nascimento de Santa Cruz Oliveira (RM561390)
- Milena Pereira dos Santos Silva (RM565464)
- Nayana Mehta Miazaki (RM565045)

## 👩‍🏫 Professores

### Tutor(a)

- Lucas Gomes Moreira

### Coordenador(a)

- André Godoi

---

# ❤️ CardioIA – Fase 1: Batimentos de Dados

## 🎯 Visão geral

O **CardioIA** é um projeto acadêmico que simula o ecossistema de uma cardiologia moderna, integrando dados clínicos, Machine Learning, Visão Computacional, IoT e agentes inteligentes para triagem, diagnósticos, monitoramento e previsões médicas.

Nesta **Fase 1 – Batimentos de Dados**, assumimos o papel de cientistas de dados hospitalares: o desafio é levantar, organizar e entender dados cardiológicos que, nas fases seguintes, alimentarão os módulos inteligentes do CardioIA. A entrega contempla três tipos de dados — numéricos, textuais e visuais — com atenção à **governança de dados** e ao **viés**.

## 📋 Objetivos e entregas

- **Parte 1 – Dados numéricos (IoT):** dataset com variáveis clínicas cardíacas (mín. 100 linhas), organizado e documentado.
- **Parte 2 – Dados textuais (NLP):** mínimo dois textos (.txt) sobre doenças cardíacas/saúde cardiovascular, para exploração com NLP.
- **Parte 3 – Dados visuais (VC):** mínimo 100 imagens de exame cardiológico (ex.: ECG, raio-X torácico ou angiograma), para análise com Visão Computacional.

Os conjuntos completos estão disponíveis via **links públicos** (Google Drive, OneDrive ou similar), indicados nas seções abaixo.

---

## 📊 Parte 1 – Dados numéricos (IoT)

**Objetivo:** Dataset para prever **risco de doença cardíaca** (input: idade, pressão, colesterol, sintomas etc. → output: presença/ausência de doença).

### Origem dos dados

- **Abordagem:** híbrida (base real limpa; dados simulados poderão ser agregados em etapa posterior para ampliar o conjunto).
- **Dados reais:** [UCI Machine Learning Repository – Heart Disease Dataset (Cleveland)](https://archive.ics.uci.edu/dataset/45/heart+disease), arquivo processado (14 atributos). Licença de uso acadêmico e pesquisa. Dados anonimizados.
- **Tratamento:** Os dados brutos foram explorados no notebook `notebooks/eda_heart_cleveland.ipynb` e limpos pelo script `scripts/clean_heart_data.py`: substituição de `"?"` em **ca** e **thal** pela moda, criação da coluna **target_binario** (0 = sem doença, 1 = risco). O valor extremo de **colesterol (564 mg/dL)** foi mantido como caso real e documentado (decisão consciente após EDA).
- **Arquivo entregue:** `data/heart_real_cleaned.csv` (303 linhas × 15 colunas, incluindo `target_binario`).

### 🔗 Link para o dataset completo

- [Inserir link público – Google Drive / OneDrive] *(subir o arquivo `heart_real_cleaned.csv` e colar o link aqui)*

**Como reproduzir a limpeza (Parte 1):** na raiz do repositório, com o ambiente ativado (`pip install -r requirements.txt`), executar `python scripts/clean_heart_data.py`. O script lê `data/heart_disease_cleveland_raw.csv` e gera `data/heart_real_cleaned.csv`.

### Variáveis e relevância clínica

| Variável   | Descrição | Relevância para IA em saúde |
|------------|-----------|-----------------------------|
| age        | Idade (anos) | Fator de risco em scores (ex.: Framingham); entrada em modelos de triagem e predição. |
| sex        | Sexo (1=homem, 0=mulher) | Diferenças de risco entre sexos; variável de controle em modelos. |
| cp         | Tipo de dor no peito (1–4) | Sintoma clínico relevante para classificação e triagem. |
| trestbps   | Pressão arterial em repouso (mmHg) | Hipertensão é fator de risco; uso em scores e modelos preditivos. |
| chol       | Colesterol sérico (mg/dL) | Fator de risco cardiovascular; entrada em modelos de risco. |
| fbs        | Glicemia em jejum > 120 (0/1) | Indicador de diabetes; comorbidade em modelos. |
| restecg    | ECG em repouso (0,1,2) | Achado objetivo; suporte a triagem e diagnóstico. |
| thalach    | Frequência cardíaca máxima no teste (bpm) | Capacidade funcional; fortemente associado ao target na EDA. |
| exang      | Angina induzida por exercício (0/1) | Sintoma de isquemia; relevante para classificação. |
| oldpeak    | Depressão do segmento ST | Marcador de isquemia no teste de esforço. |
| slope      | Inclinação do segmento ST (1–3) | Achado de ECG no esforço. |
| ca         | Nº de vasos principais (0–3) | Severidade angiográfica; preditor forte. |
| thal       | Talassemia (3/6/7) | Resultado do teste de esforço. |
| target     | Diagnóstico original (0–4) | 0 = sem doença; 1–4 = graus de doença. |
| target_binario | Risco binário (0/1) | Variável alvo para modelo: 0 = sem risco, 1 = risco. |

**Variáveis mais relevantes para o modelo de risco:** **thalach** (FC máxima), **idade** e **trestbps** (pressão) mostraram tendência clara com o target na EDA; **ca** e **thal** são preditores clínicos fortes. O colesterol isolado teve distribuição similar entre as classes; útil em combinação com as demais.

**Tamanho do dataset:** 303 linhas, 15 variáveis (14 originais + `target_binario`).

---

## 📄 Parte 2 – Dados textuais (NLP)

Mínimo dois textos (.txt) sobre doenças cardíacas ou saúde cardiovascular (fontes: SciELO, BVS, SUS, Projeto Gutenberg). Os arquivos ficam em `docs/`. No README, descrever fonte de cada texto e como podem ser usados em NLP (extração de sintomas, classificação de tópicos, sumarização) e por que isso é relevante para o CardioIA.

- **Link (se aplicável):** [pasta no Drive ou indicar: "Arquivos em `docs/`"]
- *(Seção a ser preenchida pela equipe responsável.)*

---

## 🖼️ Parte 3 – Dados visuais (Visão computacional)

Mínimo 100 imagens (.jpg ou .png) de um tipo de exame cardiológico (ECG, raio-X de tórax ou angiograma). Incluir link público (Google Drive/OneDrive) e explicar brevemente como as imagens podem ser usadas em VC (detecção de padrões, bordas, anomalias) e a importância para o CardioIA.

- **Link para as imagens:** [Inserir link público]
- *(Seção a ser preenchida pela equipe responsável.)*

---

## 📁 Estrutura do repositório

```
chap01-phase01-cardioia-dataset-foundation/
├── README.md                    # Visão geral, links e descrição das 3 partes
├── data/                        # Parte 1 – dados numéricos
│   ├── heart_disease_cleveland_raw.csv   # Dados brutos (Cleveland)
│   └── heart_real_cleaned.csv            # Dados limpos (entregável)
├── docs/                        # Parte 2 – textos .txt para NLP
├── notebooks/                   # EDA e análise da Parte 1
│   └── eda_heart_cleveland.ipynb
└── scripts/                     # Parte 1 – carregamento e limpeza
    ├── load_dataset.py          # Carrega e inspeciona o CSV bruto
    └── clean_heart_data.py      # Aplica limpeza e gera heart_real_cleaned.csv
```

---

## ⚖️ Governança de dados e viés

- **Rastreabilidade:** Parte 1: origem UCI/Cleveland citada; limpeza documentada no notebook de EDA e no script `clean_heart_data.py`. Partes 2 e 3: fontes e links descritos nas seções correspondentes.
- **Viés:** O dataset Cleveland refere-se a um único centro e uma população específica (EUA, período do estudo); resultados de modelos treinados nessa base podem não generalizar diretamente para outros contextos. O valor 564 (colesterol) foi mantido por decisão explícita após análise (caso extremo real).
- **Uso ético:** Dados anonimizados; licença e citação da fonte (UCI) respeitadas.

---

## 🛠 Tecnologias utilizadas (Fase 1)

- **Versionamento:** Git / GitHub
- **Parte 1 – Dados numéricos:** Python 3, Pandas, Jupyter (EDA em notebook; scripts `load_dataset.py` e `clean_heart_data.py`)
- **Armazenamento dos conjuntos completos:** Links públicos (Google Drive / OneDrive) nas seções correspondentes

---

