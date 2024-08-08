import pandas as pd
from pgmpy.models import BayesianNetwork
from pgmpy.estimators import BayesianEstimator
from pgmpy.inference import VariableElimination
import networkx as nx
import matplotlib.pyplot as plt

# Carregar os dados do arquivo CSV
data = pd.read_csv('dadosAVC.csv')

print(data.head(10))

# Exibir os valores únicos de cada coluna
for column in data.columns:
    unique_values = data[column].unique()
    print(f"Valores possíveis para {column}: {unique_values}")

# Definir a estrutura da rede bayesiana
model = BayesianNetwork([
    ('Horas_Sono', 'Estresse'),
    ('Pressao_Arterial', 'AVC'),
    ('Diabetes', 'AVC'),
    ('Historico_Familiar_AVC', 'AVC'),
    ('Ausencia_Exercicios', 'AVC'),
    ('Ma_Alimentacao', 'AVC'),
    ('Tabagismo', 'Pressao_Arterial'),
    ('Consumo_Alcool', 'AVC'),
    ('Estresse', 'Pressao_Arterial')
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

# Visualizar a rede bayesiana
def plot_network(model):
    G = nx.DiGraph()
    G.add_edges_from(model.edges())
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=3500, node_color="skyblue", font_size=8, font_weight="bold", arrows=True)
    plt.title("Rede Bayesian")
    plt.show()

plot_network(model)
