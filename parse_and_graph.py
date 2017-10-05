import pandas as pd
import graphviz as gv

exec_df = pd.DataFrame.from_csv('executive_team_raw.csv', header=1)
trim_exec_df = exec_df.dropna(thresh=5, axis=0)
graph = gv.Graph()
melted = pd.melt(trim_exec_df.reset_index(), id_vars=['index']).rename(columns={'index':'name', 'variable':'strength', 'value':'rank'}).dropna()
strings_df = melted[['name', 'strength']]
strings_df['rank'] = melted['rank'].apply(str)
for edge in strings_df.rename(columns={'name':'tail_name','strength':'head_name','rank':'label'}).to_dict('records'):
    graph.edge(**edge)
graph.engine = 'neato'
graph.graph_attr['overlap'] = 'false'
graph.render(view=True)
