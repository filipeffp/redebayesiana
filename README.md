# Redes Bayesianas
Repositório para seminário referente a Redes bayesianas

## README: Predição de AVC com Redes Bayesianas

### Descrição
Este script Python utiliza a biblioteca pgmpy para construir e treinar uma rede bayesiana com o objetivo de prever a ocorrência de um Acidente Vascular Cerebral (AVC). A rede é treinada utilizando dados de um arquivo CSV (dadosAVC.csv) e os parâmetros são estimados utilizando o método de máxima verossimilhança.

### Requisitos
- Python: Versão 3.x
#### Bibliotecas:
- pandas: Manipulação de dados
- pgmpy: Modelagem e inferência em redes bayesianas

### Estrutura do Arquivo CSV (dadosAVC.csv)
O arquivo CSV utilizado possui as seguintes características
| Campo | Valores |
| ----------- | ----------- |
| Idade | [inteiros] |
| Sexo: | ['M' 'F'] |
| Pressao_Arterial: | ['Alta' 'Baixa' 'Normal'] |
| Diabetes: | ['Sim' 'Não'] |
| Historico_Familiar_AVC: | ['Não' 'Sim'] |
| Ausencia_Exercicios: | ['Sim' 'Não'] |
| Ma_Alimentacao: | ['Sim' 'Não'] |
| Tabagismo: | ['Sim' 'Não'] |
| Consumo_Alcool: | ['Diario' 'Ocasional' 'Semanal' 'Nunca' 'Social' 'Diário'] |
| Horas_Sono: | [inteiros] |
| Estresse: | ['Alto' 'Baixo' 'Médio'] |
| AVC: | ['Não' 'Sim'] |

### Passo 1: Instalar as Bibliotecas Necessárias
Primeiro, você precisa instalar as bibliotecas necessárias. Você pode fazer isso usando o comando pip:

`pip install pandas pgmpy matplotlib`

### Passo 2: Importar as bibliotecas necessárias
Depois carregue as bibliotecas a serem utilizadas:

`import pandas as pd`

`from pgmpy.models import BayesianNetwork`

`from pgmpy.estimators import MaximumLikelihoodEstimator`

`from pgmpy.inference import VariableElimination`

### Passo 3: Carregar os Dados
Carregar os dados do arquivo CSV

`data = pd.read_csv('dadosAVC.csv')`

### Passo 4: Definir a Estrutura da Rede Bayesiana
Defina a estrutura da rede bayesiana especificando as relações entre as variáveis:

`model = BayesianNetwork([
    ('Pressao_Arterial', 'AVC'),
    ('Diabetes', 'AVC'),
    ('Historico_Familiar_AVC', 'AVC'),
    ('Ausencia_Exercicios', 'AVC'),
    ('Ma_Alimentacao', 'AVC'),
    ('Tabagismo', 'AVC'),
    ('Consumo_Alcool', 'AVC'),
    ('Horas_Sono', 'AVC'),
    ('Estresse', 'AVC')
])`

### Passo 5: Ajustar os Parâmetros da Rede
Ajuste os parâmetros da rede usando o estimador de máxima verossimilhança:

`model.fit(data, estimator=MaximumLikelihoodEstimator)`

### Passo 6: Realizar Inferências na Rede
Use a eliminação de variáveis para realizar inferências na rede bayesiana:

`inference = VariableElimination(model)`

#### Exemplo de consulta: Probabilidade de AVC dado que a pressão arterial é alta
`query_result = inference.query(variables=['AVC'], evidence={'Pressao_Arterial': 'Alta'})
print(query_result)`

##### Exemplo de consulta: Probabilidade de AVC dado que a pessoa tem diabetes e histórico familiar de AVC
`query_result = inference.query(variables=['AVC'], evidence={'Diabetes': 'Sim', 'Historico_Familiar_AVC': 'Sim'})
print(query_result)`
