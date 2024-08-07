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

### Instalação
Para instalar as dependências, execute o seguinte comando em seu terminal:

`Bash`
`pip install pandas pgmpy`

### Estrutura do Arquivo CSV (dadosAVC.csv)
O arquivo CSV utilizado possui as seguintes colunas:
- Idade: [inteiros]
- Sexo: ['M' 'F']
- Pressao_Arterial: ['Alta' 'Baixa' 'Normal']
- Diabetes: ['Sim' 'Não']
- Historico_Familiar_AVC: ['Não' 'Sim']
- Ausencia_Exercicios: ['Sim' 'Não']
- Ma_Alimentacao: ['Sim' 'Não']
- Tabagismo: ['Sim' 'Não']
- Consumo_Alcool: ['Diario' 'Ocasional' 'Semanal' 'Nunca' 'Social' 'Diário']
- Horas_Sono: [6 7 5 8 4 9]
- Estresse: ['Alto' 'Baixo' 'Médio']
- AVC: ['Não' 'Sim']
