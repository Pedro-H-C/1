import plotly.express as px
import pandas as pd
dados = pd.read_csv("marketing_investimento.csv")

parametros = ["idade", "saldo", "tempo_ult_contato", "numero_contatos"]
for parametro in parametros:
    px.box(dados, x=parametro, color="aderencia_investimento").show()