# 📊 Beer Recipe Data Imputation - FACENS Data Science Postgraduate Project

## 📝 Resumo da Estratégia de Imputação de Dados (PT-BR)

Para realizar uma imputação eficiente e coerente com as características do dataset, apliquei diferentes técnicas de preenchimento de valores ausentes, considerando o tipo da variável, a distribuição dos dados e a quantidade de valores faltantes.

### 🔍 Ausência de dados antes da imputação

| Coluna            | Valores Ausentes | Percentual (%) |
|-------------------|------------------|----------------|
| Name              | 1                | 0.00%          |
| Style             | 467              | 0.88%          |
| BoilGravity       | 2985             | 5.63%          |
| MashThickness     | 22367            | 42.21%         |
| PitchRate         | 27907            | 52.65%         |
| PrimaryTemp       | 16260            | 30.69%         |
| PrimingMethod     | 47745            | 90.12%         |
| PrimingAmount     | 49221            | 92.88%         |
| UserId            | 35012            | 66.08%         |

📌 As demais colunas não apresentavam valores nulos.

### 📈 Resultado após a imputação:

```text
Column            Missing Values (After)
-----------------------------------------
Name              0
Style             0
BoilGravity       0
MashThickness     0
PitchRate         0
PrimaryTemp       0
PrimingMethod     0
PrimingAmount     0
UserId            0
```

Todas as colunas com dados ausentes foram tratadas com sucesso.

### 📷 Visualização (Antes e Depois)

<p float="left">
  <img src="images/before_imputation.png" width="48%" alt="Antes da Imputação">
  <img src="images/after_imputation.png" width="48%" alt="Depois da Imputação">
</p>

### ✅ Imputações Realizadas

- **BoilGravity → Interpolação Linear**  
Usada por ser uma variável numérica contínua, com tendência progressiva. A interpolação linear preserva a lógica entre os valores anteriores e posteriores, sem distorcer a média.

- **MashThickness → Média Móvel + Mediana**  
A média móvel suaviza a série de dados, mas pode não preencher os extremos (início ou fim do dataset). Por isso, usei a mediana como fallback, garantindo o preenchimento completo.

- **PrimaryTemp e PitchRate → KNN Imputer**  
Optei pelo algoritmo K-Nearest Neighbors (KNN) por se tratar de variáveis dependentes de outras características do processo (como OG, ABV e IBU). O KNN considera essas relações e faz imputações mais realistas.

- **Style → Forward Fill**  
Preenchimento para frente funciona bem para colunas categóricas quando os dados seguem um padrão sequencial de entrada, como é comum em cadastros de receitas.

- **PrimingMethod e PrimingAmount → Backward Fill + Valor padrão**  
Como possuem muitos nulos e não há garantias de padrão de sequência, apliquei backward fill e, se ainda houvesse valores ausentes, completei com 'Desconhecido' e '0.0'.

- **Name → Forward Fill**  
Apenas um valor ausente, então optei por repetir o valor anterior para manter consistência com os dados próximos.

- **UserId → Backward Fill + Moda**  
Usei backward fill para manter alguma coerência local, e a moda (valor mais comum) para cobrir eventuais lacunas finais.

📌 Todos os dados ausentes foram completamente eliminados após essas etapas.

O código completo foi implementado utilizando Python, Pandas, Scikit-learn, Matplotlib e Missingno para validação visual.

## 📁 Estrutura do Projeto

```
beer-recipe-imputation-facens/
├── data/
│   └── recipeData.csv               # Dataset original
├── images/
│   ├── before_imputation.png       # Visual antes da imputação
│   ├── after_imputation.png        # Visual depois da imputação
│   └── missing_before_barh.png     # Barras horizontais com nulos
├── analytics/
│   └── initial_explorer.py         # Análise exploratória opcional
├── src/
│   └── imputation.py               # Funções de imputação
├── main.py                         # Script principal
├── requirements.txt                # Dependências
└── README.md                       # Documentação
```

---

## ▶️ Execução

```bash
python main.py
```

- Gera o dataset limpo: `data/recipeData_imputed.csv`
- Salva os gráficos em `images/`

---

## 👨‍💻 Autor

**Felipe Fernandes**  
Pós-graduando em Data Science pela FACENS.  
Código estruturado com foco em boas práticas de tratamento de dados.

Contribuições são bem-vindas! 🍻

---

## 📝 Data Imputation Strategy Summary (English)

To achieve an efficient and context-aware imputation strategy, I applied multiple techniques depending on each variable's type, distribution, and null rate.

Below is a summary of each method and rationale:

| Column             | Method Used                                  | Rationale |
|--------------------|-----------------------------------------------|-----------|
| `BoilGravity`      | Linear Interpolation                         | Continuity between numerical values |
| `MashThickness`    | Moving Average + Median fallback             | Smooth data and ensure full coverage |
| `PrimaryTemp` & `PitchRate` | KNN Imputer with correlated features | Multivariate and realistic filling |
| `Style`            | Forward Fill                                 | Sequential category in recipes |
| `PrimingMethod`    | Backward Fill + Fallback 'Unknown'           | Categorical with high missing rate |
| `PrimingAmount`    | Backward Fill + Fallback '0.0'               | Complements method field |
| `Name`             | Forward Fill                                 | Only 1 missing value |
| `UserId`           | Backward Fill + Mode                         | Local coherence + common value fallback |

📌 After these steps, **all missing values were successfully imputed**.

Libraries used: `pandas`, `scikit-learn`, `matplotlib`, `missingno`

---

📁 This repository follows a clean Python structure, with modular scripts and a clear `main.py` pipeline. See the `src/`, `analytics/`, and `images/` folders for more details.

👨‍💻 Author: Felipe Fernandes  
📍 Project developed during the Data Science and Data Engineering Postgraduate Program at FACENS.