import plotly 
plotly.tools.set_credentials_file(username='carlos3lb',api_key='b1egRO4gQMKXtmjkbmgb')
import plotly.plotly as py
import plotly.graph_objs as go

def months():
    return ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def genarate_yearly_comparative(total, comun, personal, year):
    trace1 = go.Scatter(
        x = months(),
        y = total,
        name = 'Total',
        line = dict(color = ('rgb(22, 96, 167)'), width = 2 )
    )
    trace2 = go.Scatter(
        x = months(),
        y = comun,
        name = 'Comun',
        line = dict(color = ('rgb(133, 86, 83)'), width = 2, dash = 'dot' )
    )
    trace3 = go.Scatter(
        x = months(),
        y = personal,
        name = 'Fide',
        line = dict(color = ('rgb(219, 219, 57)'), width = 2, dash = 'dot' )
    )
    data = [trace1, trace2, trace3]
    layout = dict(title = 'Compartiva gastos año ' + str(year),
                xaxis = dict(title = 'Mes'),
                yaxis = dict(title = 'Euros'))

    fig = dict(data=data, layout=layout)
    py.image.save_as(fig, filename='yearly_comparative.png')

    #py.image.save_as(fig, filename='a-simple-plot.png')
    #layout = go.Layout(title='A Simple Plot', width=800, height=640)
    #fig = dict(data=[data], layout=layout)
    #py.image.save_as(fig, filename='yearly_comparativea.png')