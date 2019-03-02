import dash    
import dash_auth
import requests
import dash_core_components as dcc
from dash.dependencies import Input,Output
import dash_html_components as html

app = dash.Dash('curie')

VALID_USERNAME_PASSWORD_PAIRS = [
    ['curie', 'labs']
]
curie = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(children=[html.H3('Enter The Zip Code'),dcc.Input(id='input',value=' ',type='integer'),
                                html.Div(id='output')
                                ])
@app.callback(
    Output(component_id='output',component_property='children'),
    [Input(component_id='input',component_property='value')])

def update_value(input_data):
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+input_data+',in&appid=6e1ce28c313d0a06df997b912c3e991e') #Calling the API#
    json_object = r.json() #Making the JSON_OBJECT to reach the data of any ZIP code.#
    temp_k = float(json_object['main']['temp'])
    temp_h = float(json_object['main']['humidity'])
    temp_d = str(json_object['weather'][0]['description'])
    temp_l = str(json_object['name'])
    temp_f = (temp_k - 273.15) * 1.8 + 32
    temp_c = (temp_f - 32) * 5/9
    return dcc.Graph(id='Internship',figure={'data':[{'x':[temp_c],'y':[temp_c],'type':'bar','name':'Temperature/C','text':temp_l},
                                                     {'x':[temp_c],'y':[temp_c],'type':'line','name':'Temperature/C','text':temp_l},
                                                    {'x':[temp_h],'y':[temp_h],'type':'bar','name':'Humidity','text':temp_d},
                                                     {'x':[temp_h],'y':[temp_h],'type':'line','name':'Humidity','text':temp_d},
                                                     
                                                     ],'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }}})  
if __name__=='__main__':
    app.run_server(debug=True)
