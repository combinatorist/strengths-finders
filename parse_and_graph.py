import pandas as pd
import graphviz as gv

FILEPATH = 'example/redacted_team_raw.csv'

raw_df = pd.DataFrame.from_csv(FILEPATH, header=1)
melted_df = pd.melt(raw_df.reset_index(), id_vars=['index']).dropna()
strings_df = melted_df.applymap(str)

graph = gv.Graph()
graph_renaming = {'index':'tail_name','variable':'head_name','value':'rank'}
for edge in strings_df.rename(columns=graph_renaming).to_dict('records'):
    graph.node(edge['tail_name'], fillcolor='lightblue', style='filled')
    graph.edge(**edge)
graph.engine = 'circo'
graph.format = 'png'
graph.graph_attr['overlap'] = 'false'
graph.render(FILEPATH + '.gv', view=True)
