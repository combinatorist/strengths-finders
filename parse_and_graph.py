import pandas as pd
import graphviz as gv

FILEPATH = 'example/redacted_team_raw.csv'

raw_df = pd.DataFrame.from_csv(FILEPATH, header=1)
melted_df = pd.melt(raw_df.reset_index(), id_vars=['index']).dropna()

joined_df = pd.merge(left=melted_df, right=melted_df, how='left', on='variable')
# drop self- and double-joins
filtered_df = joined_df[joined_df.index_x < joined_df.index_y]
# single, weighted edge
grouped_df = filtered_df.groupby(['index_x', 'index_y']).count().reset_index()
# coalesced_df = joined_df + joined_df['']

strings_df = grouped_df.applymap(str)

graph = gv.Graph()
graph_renaming = {'index_x':'tail_name','index_y':'head_name','variable':'weight'}
for edge in strings_df.rename(columns=graph_renaming).to_dict('records'):
    graph.node(edge['tail_name'], fillcolor='lightblue', style='filled')
    graph.node(edge['head_name'], fillcolor='lightblue', style='filled')
    graph.edge(**edge)
graph.engine = 'circo'
graph.graph_attr['overlap'] = 'false'
graph.render(view=True)
