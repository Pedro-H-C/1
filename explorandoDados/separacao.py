import plotly.express as px
import pandas as pd
dados = pd.read_csv("marketing_investimento.csv")

from sklearn.compose import make_column_transformer as mct
from sklearn.preprocessing import OneHotEncoder

x = dados.drop('aderencia_investimento', axis = 1)
y = dados['aderencia_investimento']


colunas = x.columns
one_hot = mct((
    OneHotEncoder(drop = "if_binary"),
    ["estado_civil", "escolaridade", "inadimplencia", "fez_emprestimo"]
),
    remainder = "passthrough",
    sparse_threshold = 0)

x = one_hot.fit_transform(x)

one_hot.get_feature_names_out(colunas) 

pd.Dataframe(x, columns = one_hot.get_feature_names_out(colunas))