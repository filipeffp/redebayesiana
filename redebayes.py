import pandas as pd
from pgmpy.models import BayesianNetwork
from pgmpy.estimators import BayesianEstimator
from pgmpy.inference import VariableElimination

# Carregar os dados do arquivo CSV
data = pd.read_csv('dadosAVC.csv')

print(data.head(10))

# Exibir os valores únicos de cada coluna
for column in data.columns:
    unique_values = data[column].unique()
    print(f"Valores possíveis para {column}: {unique_values}")

# Definir a estrutura da rede bayesiana
model = BayesianNetwork([
    ('Pressao_Arterial', 'AVC'),
    ('Diabetes', 'AVC'),
    ('Historico_Familiar_AVC', 'AVC'),
    ('Ausencia_Exercicios', 'AVC'),
    ('Ma_Alimentacao', 'AVC'),
    ('Tabagismo', 'AVC'),
    ('Consumo_Alcool', 'AVC'),
    ('Horas_Sono', 'AVC'),
    ('Estresse', 'AVC')
])

# Ajustar os parâmetros da rede usando BayesianEstimator
model.fit(data, estimator=BayesianEstimator)

# Inferência na rede bayesiana
inference = VariableElimination(model)

# Exemplo de consulta: Probabilidade de 'AVC' dado que a 'pressão arterial é alta'
print("\nExemplo de consulta: Probabilidade de 'AVC' dado que a 'pressão arterial é alta'")
query_result = inference.query(variables=['AVC'], evidence={'Pressao_Arterial': 'Alta'})
print(query_result)

# Exemplo de consulta: Probabilidade de AVC dado que a pessoa tem diabetes e histórico familiar de AVC
print("\nExemplo de consulta: Probabilidade de 'AVC' dado que a pessoa tem diabetes e histórico familiar de AVC")
query_result = inference.query(variables=['AVC'], evidence={'Diabetes': 'Sim', 'Historico_Familiar_AVC': 'Sim'})
print(query_result)
