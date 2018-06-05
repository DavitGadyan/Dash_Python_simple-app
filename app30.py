import dash
import dash_core_components as dcc
import dash_html_components as html
from plotly.offline import iplot,plot
import pandas as pd
import numpy as np
from graphs6 import f1,f2,f3

import plotly.graph_objs as go
header=dict(values=['Type of object','Syntax'],
            align = ['left','center'],
            font = dict(color = 'black', size = 12),
            fill = dict(color='#119DFF')
            )
cells=dict(values=[['List','Dictionary','Tuple'],
                   ['[1,0,-9,11]','{"Name":"Status")','(5,8,string)']],
           align = ['left','center'],
           fill = dict(color=["yellow","white"]),
           font= dict(color='black',size=10)
           )
trace = go.Table(header=header, cells=cells)
data = [trace]
layout = dict(width=1000, height=400)
f4 = dict(data=data, layout=layout)


app=dash.Dash()
server=app.server
app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})
app.layout = html.Div([

html.Div([dcc.Markdown('''

# Basics of Python
''')
],className='row',style={'text-align':'center'}),

html.Div([dcc.Markdown('''
### Starting from simple: What is Python?
'''),
dcc.Markdown('''
##### *Python is a general purpose programming language.*
'''),
dcc.Markdown('''
### What can we do with Python?
'''),
dcc.Markdown('''
#####
- Data Analsysis
- Machine Learning
- Web Development (using DASH)
- Data Visualization
- and many more for those who want to learn)))

[Here is link to video explaining wide-range usefulness of Python programm.](https://www.youtube.com/watch?v=hxGB7LU4i1I)

'''),
dcc.Markdown('''
### Let's practice right away...Say Hello to World!!!
'''),
dcc.Markdown('''
 *For doing that we need to type and run the following code:*
'''),
dcc.Markdown('''

Inline code snippet: True

Type the following:
```
print("Hello World!")

```
'''),

html.Div(dcc.Input(id='input-box', type='text')),
    html.Button('Submit', id='button'),
    html.Div(id='output-container-button',
             children='Enter a value and press submit',style={'color':'green'})
],className='row'),
html.H1("Variable Types"),
html.P("There are four types of variables in Python:"),
html.Div([html.Div([
dcc.Markdown('''
* Integers
* Floats
* Strings
* Booleans
''')],className="four columns"),
html.Div([
dcc.Graph(id='table',figure=f4)
    ],className='eight columns',style={'background':'lightblue'})
],className="row"),
html.Div([
dcc.Markdown('''
Let's conduct a small quiz

'''),
dcc.Markdown('''
**Which one of the following options is object type in Python?**
    '''),
dcc.RadioItems(id='input_radio',
    options=[
        {'label': 'Booleans', 'value': 'BL'},
        {'label': 'List', 'value': 'lt'},
        {'label': 'anaconda', 'value': 'a'}
    ],
    value='Booleans'
),
html.Div(
    id="output-radioitem-button",
     children='Choose option!!',style={'color':'green'}
    )

    ],className='row'),
html.Div([]),

dcc.Markdown('''
To understand the type of the variable we use type function:
```
type(variable)
```
    '''),
dcc.Markdown('''
Which option has the following order of variable types: integer,string,boolean,float.
    '''),
dcc.RadioItems(id='input_radio2',
    options=[
        {'label': 'Man,True,10,10.0', 'value': '1'},
        {'label': 'False,Garden,11,1.0', 'value': '2'},
        {'label': '1,number,False,111.0', 'value': '3'}
    ],
    value='Choose option'
),
html.Div(id = 'output-radioitem-button2',style={'color':'green'}),
dcc.Markdown('''
Let's have a look on popularity of Python as programming language compared to other program languages!!!
For this purpose we will use some real dataset:Stack Overflow Developer Survey, 2017!!!!!!

Dataset is taken from [kaggle.com](https://www.kaggle.com/stackoverflow/so-survey-2017/data)

Let's analyze popularity of programming languages immediately from those who actively use it.

Here are pie charts representing their preferences. Note that practically **all programmers** use not only single language but rather suitable for their needs portfolio of languages...

    '''),
dcc.Graph(id='graph1',figure=f1),
html.H4("Python is not as much popular as Java or JavaScript but we may say it has already reached C,C#. However, if we look on the second pie chart which shows the languages that programmers want to learn, we may observe that Python is on the second position.This is proof that current trend of programming moves towards Python!!! So that is one reason why it is useful to learn Python!!!!"
    ),
dcc.Graph(id='graph2',figure=f2),
dcc.Graph(id='graph3',figure=f3),
html.H2("So what is the conclusion?...It is simple: Learn,learn and learn!!!!")

],className='row',style={'background':"lightblue"})
@app.callback(
    dash.dependencies.Output('output-container-button', 'children'),
    [dash.dependencies.Input('button', 'n_clicks')],
    [dash.dependencies.State('input-box', 'value')]
)
def update_output(n_clicks,value):
    if value=='print'+'('+'"Hello World!"'+')':
        return 'Hello World!'
    elif value=="":
        return "Type!!!!!"
    else:
        return "Try again!!"


@app.callback(
    dash.dependencies.Output('output-radioitem-button', 'children'),
    [dash.dependencies.Input('input_radio', 'value')]
)
def update_output(value):
    if value=='lt':
        return 'You are right!'
    else:
        return "Try again!!"

@app.callback(
    dash.dependencies.Output('output-radioitem-button2', 'children'),
    [dash.dependencies.Input('input_radio2', 'value')]
)
def update_output(value):
    if value=='3':
        return 'You are right!'
    else:
        return "Try again!!"
if __name__ == '__main__':
    app.run_server(debug=True)