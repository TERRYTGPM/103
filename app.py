import pandas
import plotly.express as px

dataframe = pandas.read_csv("Copy+of+data+-+data.csv")

fig = px.scatter(dataframe, x="date", y="cases", color="country")

fig.show()