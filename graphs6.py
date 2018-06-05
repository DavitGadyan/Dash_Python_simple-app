import pandas as pd
database=pd.read_csv('survey_results_public.csv')

used_langs=database['HaveWorkedLanguage']
l_used_langs=used_langs.value_counts()
l_used_langs=l_used_langs.to_frame(name=None)
used_langs_cl=l_used_langs.reset_index().head(15)

want_langs=database['WantWorkLanguage']
l_want_langs=want_langs.value_counts()
l_want_langs=l_want_langs.to_frame(name=None)
l_want_langs.reset_index()
want_langs_cl=l_want_langs.reset_index().head(15)



from plotly.offline import plot, iplot
import plotly.graph_objs as go


labels = [used_langs_cl['index'][0],used_langs_cl['index'][1],used_langs_cl['index'][2],used_langs_cl['index'][3],used_langs_cl['index'][4],used_langs_cl['index'][5],used_langs_cl['index'][6],used_langs_cl['index'][7],used_langs_cl['index'][8],used_langs_cl['index'][9],used_langs_cl['index'][10],used_langs_cl['index'][11],used_langs_cl['index'][12],used_langs_cl['index'][13],used_langs_cl['index'][14]]
values = [used_langs_cl['HaveWorkedLanguage'][0],used_langs_cl['HaveWorkedLanguage'][1],used_langs_cl['HaveWorkedLanguage'][2],used_langs_cl['HaveWorkedLanguage'][3],used_langs_cl['HaveWorkedLanguage'][4],used_langs_cl['HaveWorkedLanguage'][5],used_langs_cl['HaveWorkedLanguage'][6],used_langs_cl['HaveWorkedLanguage'][7],used_langs_cl['HaveWorkedLanguage'][8],used_langs_cl['HaveWorkedLanguage'][9],used_langs_cl['HaveWorkedLanguage'][10],used_langs_cl['HaveWorkedLanguage'][11],used_langs_cl['HaveWorkedLanguage'][12],used_langs_cl['HaveWorkedLanguage'][13],used_langs_cl['HaveWorkedLanguage'][14]]

trace = go.Pie(labels=labels, values=values)

data = [trace]
layout=dict(title="Languages used by programmers in 2017 year")
f1 = dict(data=data,layout=layout) # figure showing languages portfolio proportion used during work by programmers


from plotly.offline import plot, iplot
import plotly.graph_objs as go


labels = [want_langs_cl['index'][0],want_langs_cl['index'][1],want_langs_cl['index'][2],want_langs_cl['index'][3],want_langs_cl['index'][4],want_langs_cl['index'][5],want_langs_cl['index'][6],want_langs_cl['index'][7],want_langs_cl['index'][8],want_langs_cl['index'][9],want_langs_cl['index'][10],want_langs_cl['index'][11],want_langs_cl['index'][12],want_langs_cl['index'][13],want_langs_cl['index'][14]]
values = [want_langs_cl['WantWorkLanguage'][0],want_langs_cl['WantWorkLanguage'][1],want_langs_cl['WantWorkLanguage'][2],want_langs_cl['WantWorkLanguage'][3],want_langs_cl['WantWorkLanguage'][4],want_langs_cl['WantWorkLanguage'][5],want_langs_cl['WantWorkLanguage'][6],want_langs_cl['WantWorkLanguage'][7],want_langs_cl['WantWorkLanguage'][8],want_langs_cl['WantWorkLanguage'][9],want_langs_cl['WantWorkLanguage'][10],want_langs_cl['WantWorkLanguage'][11],want_langs_cl['WantWorkLanguage'][12],want_langs_cl['WantWorkLanguage'][13],want_langs_cl['WantWorkLanguage'][14]]

trace = go.Pie(labels=labels, values=values)

data = [trace]
layout=dict(title="Languages wanted to be learned by programmers in 2017 year")
f2 = dict(data=data,layout=layout) # figure showing languages portfolio proportion which programmers want to learn

ed_type=database["EducationTypes"]
l_ed_type=ed_type.value_counts()
l_ed_type=l_ed_type.to_frame(name=None)
ed_type_cl=l_ed_type.reset_index().head(10)

from plotly.offline import plot, iplot
import plotly.graph_objs as go

x_values = [ed_type_cl['index'][0],ed_type_cl['index'][1],ed_type_cl['index'][2],ed_type_cl['index'][3],ed_type_cl['index'][4],ed_type_cl['index'][5],ed_type_cl['index'][6],ed_type_cl['index'][7],ed_type_cl['index'][8],ed_type_cl['index'][9]]
y_values = [ed_type_cl['EducationTypes'][0],ed_type_cl['EducationTypes'][1],ed_type_cl['EducationTypes'][2],ed_type_cl['EducationTypes'][3],ed_type_cl['EducationTypes'][4],ed_type_cl['EducationTypes'][5],ed_type_cl['EducationTypes'][6],ed_type_cl['EducationTypes'][7],ed_type_cl['EducationTypes'][8],ed_type_cl['EducationTypes'][9]]


trace = go.Bar(x=x_values, y=y_values ,marker=dict(
        color=['rgba(34,139,34,1)', 'rgba(24,116,205,1)',
               'rgba(255,215,0,1)', 'rgba(0,255,255,1)',
               'rgba(238,154,73,1)','rgba(255,62,150,1)','rgba(205,201,201,1)','rgba(205,201,201,1)','rgba(205,201,201,1)','rgba(205,201,201,1)']),)

data = [trace]
layout=dict(title="10 most popular ways to learn Programming!!")
f3 = dict(data=data,layout=layout)