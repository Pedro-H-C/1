import plotly.express as px
import pandas as pd
dados = pd.read_csv("marketing_investimento.csv")

dados.info()

graficos = []
px.histogram(dados, x = 'aderencia_investimento', text_auto = True).show()
parametros = ["estado_civil", "escolaridade", "inadimplencia", "fez_emprestimo"]
for parametro in parametros:
    px.histogram(dados, x=parametro, text_auto=True, color='aderencia_investimento', barmode="group").show()