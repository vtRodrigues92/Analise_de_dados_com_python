# %%
#importando bibliotecas

# Link do dataset = https://www.kaggle.com/tanuprabhu/population-by-country-2020/version/4

from os import name
from numpy.core.fromnumeric import size
import pandas as pd
import numpy as np
import plotly.offline as py
import plotly.graph_objs as go
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt


# %%
#Lendo dataset

dataset = pd.read_csv('Dataset2_population.csv', sep=";")
dataset.head()

# %%
# 1 - Treemap marcando a população por País

g1 = px.treemap(dataset,
                path=[px.Constant("all"),'Pais'],
                values='Populacao',
                tile = )

g1.update_traces(root_color="lightgrey")
g1.update_layout(margin = dict(t=50, l=25, r=25, b=25))
g1.show()



# %%
# 2 - Grafico de rosca mostrando porcentagem da populção sobre a população Mundial

g2 = px.pie(dataset,
            names = 'Pais',
            values = 'Populacao mundial (%)',
            title= 'População Mundial (%)(2020)',
            labels={'lifeExp':'life expectancy'}, color_discrete_sequence=px.colors.qualitative.Bold);


g2.update_traces(textposition='inside', textinfo='percent+label')
g2.update_traces(hole=.6, hoverinfo="label+percent+name")


# %%
# 3 - Grafifo de barras por média de idade

g3 = px.bar(dataset,
            x = 'Media idade',
            y = 'Pais',
            title = 'Média de idade por pais(2020)',
            color_discrete_sequence=px.colors.qualitative.Bold)

g3.show()


# %%
# 4 - Grafico de colunas empilhadas por zona de habitação

g4_1 = go.Bar(x = dataset['Pais'],
              y = dataset['Pop urbana'],
              name = 'Pop urbana',
              marker = {'color': '#636EFA'})

g4_2 = go.Bar(x = dataset['Pais'],
              y = dataset['Pop Rural'],
              name = 'Pop Rural',
              marker = {'color': '#FF97FF'})

grafico = [g4_1, g4_2]

layout = go.Layout(title = 'Zona de habitação(2020)',
         barmode='stack')


fig = go.Figure(data = grafico, layout=layout)

py.iplot(fig)
# %%
# 5 - Grafico de linha de pessoas migrantes por país

g5 = px.line(dataset,
             x = 'Pais',
             y = 'Migrantes(liq)',
             title = 'Quantidade de pessoas migrantes(2020)',
             line_shape = 'spline')

g5.update_xaxes(title = None)

g5.show()

# %%
# 6 - Bubble Charts marcando a área do terreno por País

g6 = px.scatter_geo(dataset,
                    locations="ISO_alpha",
                    size="Area do terreno(KM)",
                    color = 'Pais',
                    projection="natural earth",
                    title='Área do terreno por País(2020)',
                    size_max=35)
g6.show()


# %%
# 7 - Grafico de colunas por taxa de fertilidade

g7 = px.bar(dataset,
            x = 'Pais',
            y = 'Fert. Rate',
            title = 'Taxa de fertilidade por País(2020)',
            color_discrete_sequence=["magenta"])


g7.show()


# %%
# 8 - Grafico de Funil com area

g8 = px.funnel_area(dataset,
               values='Mudanca anual',
               names= 'Pais',
               title = 'Variação da população referente ao ano anterior(2019)')
g8.show()

# %%
# 9 - Heatmap com a correlação do dataset original

dataset_original = pd.read_csv('population_by_country_2020_Original.csv', sep=';')
dataset_original[['Fert. Rate', 'Med. Age','Urban Pop %','World Share']] = dataset_original[['Fert. Rate', 'Med. Age','Urban Pop %','World Share']].apply(pd.to_numeric)

dataset_new = dataset_original.corr()

fig_dims = (13, 5)
fig, ax = plt.subplots(figsize=fig_dims)
g9 = sns.heatmap(dataset_new, linewidths=.5, ax=ax, annot=True, cmap = "Blues")

g9.set_title("Heatmap com a correlação do dataset original", fontsize = 25);


#%%

# 10 - scatterplot mostrando a disperção da média de idade x taxa de fertilidade

sns.set()
fig_dims = (13, 5)
fig, ax = plt.subplots(figsize=fig_dims)
g10 = sns.scatterplot(data = dataset_original,
                x = 'Med. Age',
                y = 'Fert. Rate')

g10.set_title("Disperção da média de idade x taxa de fertilidade", fontsize = 25 );

#%%