# this requires ipy to do shell command, but not used in this version anyway
# csvs = ! ls *.csv

import pandas as pd
import graphviz as gv
# csvs
# files = {k: with open(k, 'rb') as fp:  fp.read() for k in csvs}
# files = {k: open(k, 'rb').read() for k in csvs}
# files
# files[csvs[0]]
# files[csvs[0]].split('\r')
# files[csvs[0]].string.split('\r')
# files[csvs[0]].decode().split('\r')
# line_split = files[csvs[0]].decode().split('\r')
# column_split = [line.split(',') for line in line_split]
# column_split
# import numpy as np
# import pandas as pd
# [len(line) for line in column_split]
# import csv
# help(csv.excel.mro)
# csv.excel.mro
# help(csv)
# csv_files = {k: csv.reader(open(k, 'rb')).read() for k in csvs}
# help(csv)
# csv_files = {k: [row for row in csv.reader(open(k, 'rb'))] for k in csvs}
# csv_files = {k: [row for row in csv.reader(open(k, 'r'))] for k in csvs}
# csv_files
# [len(row) for row in csv_files[csvs[0]]]
# csv_files[csvs[0]]
# trim_files = {k: v.filter(lambda x: set(x) != set('')) for k, v in csv_files.items()}
# trim_files = {k: filter(lambda x: set(x) != set(''), v) for k, v in csv_files.items()}
# trim_files
# ttrim_files = {k: [x for x in v[:-1] if set(x) != set('')] for k, v in csv_files.items()}
# trim_files = {k: [x for x in v[:-1] if set(x) != set('')] for k, v in csv_files.items()}
# trim_files[csvs[0]]
# trim_files[csvs[0]][-1]
# set(trim_files[csvs[0]][-1])
# set(trim_files[csvs[0]][-1]) != set('')
# set(trim_files[csvs[0]][-1]) == set('')
# set(trim_files[csvs[0]][-1]) == {''}
# set(trim_files[csvs[0]][-1]) != {''}
# a
# set(trim_files[csvs[0]][-1]) == set([''])
# trim_files = {k: [x for x in v[:-1] if set(x) != {''}] for k, v in csv_files.items()}
# trim_files[csvs[0]][-1]
# history
# help(csv.DictReader)
# csv_dicts = {k: [row for row in csv.DictReader(open(k, 'r'))] for k in csvs}
# csv_dicts
# help(csv.DictReader)
# help(csv.reader)
# help(csv)
# ! pip install pandas
# import pandas as pd
# pd.DataFrame.fromcsv('executive_team_raw.csv', header=1)
# pd.DataFrame.from_csv('executive_team_raw.csv', header=1)
exec_df = pd.DataFrame.from_csv('executive_team_raw.csv', header=1)
# exec_df.dropna(thresh=6, axis=0)
# exec_df
# exec_df.dropna(thresh=5, axis=0)
trim_exec_df = exec_df.dropna(thresh=5, axis=0)
# trim_exec_df
# pd.melt(trim_exec_df)
# pd.melt(trim_exec_df, id_vars=1)
# pd.melt(trim_exec_df, id_vars=0)
# pd.melt(trim_exec_df, id_vars=[0])
# pd.melt(trim_exec_df, id_vars=['Unnamed'])
# pd.melt(trim_exec_df, id_vars=[''])
# trim_exec_df.cols
# trim_exec_df.columns
# pd.melt(trim_exec_df, id_vars=[35])
# pd.melt(trim_exec_df, id_vars=['Unnamed: 35'])
# melted_exec_df = pd.melt(trim_exec_df, id_vars=['Unnamed: 35'])
# melted_exec_df = pd.melt(trim_exec_df, id_vars=['Unnamed: 35']).dropna()
# melted_exec_df
# trim_exec_df.columns
# trim_exec_df.index
# melted_exec_df = pd.melt(trim_exec_df)
# melted_exec_df
# melted_exec_df = pd.melt(trim_exec_df), id_vars=['index'])
# trim_exec_df.reset_index(columns={'index':'name'})
# trim_exec_df.reset_index()
# trim_exec_df.reset_index(col_fill = 'Names')
# trim_exec_df.reset_index(col_fill = 'Names').rename(columns={'index':'Name})
# trim_exec_df.reset_index(col_fill = 'Names').rename(columns={'index':'Name'})
# pandas.melt(trim_exec_df.reset_index(col_fill = 'Names').rename(columns={'index':'Name'}), id_vars=['Name'])
# pd.melt(trim_exec_df.reset_index(col_fill = 'Names').rename(columns={'index':'Name'}), id_vars=['Name'])
# trim_row_exec_df = exec_df.dropna(thresh=5, axis=0)
# pd.melt(trim_exec_df.reset_index(col_fill = 'Names').rename(columns={'index':'Name'}), id_vars=['Name']).dropna()
# pd.melt(trim_exec_df.reset_index(), id_vars=['index']) #.rename(columns={'index':'Name'}).dropna()
# pd.melt(trim_exec_df.reset_index(), id_vars=['index']).rename(columns={'index':'name', 'variable':'strength', 'value':'rank'}).dropna()
# ! pip install pygraphviz
# import pygraphviz as gv
# from pygraphviz import graphviz as gv
# help(gv)
# ! pip install graphviz
# import graphviz as gv
graph = gv.Graph()
# melted = pd.melt(trim_exec_df.reset_index(), id_vars=['index']).rename(columns={'index':'name', 'variable':'strength', 'value':'rank'}).dropna()
# melted.to_dict()
# help(melted.to_dict)
# melted.to_dict('records')
# melted
# length_df = melted['rank'] / 6
# length_df
# length_df = melted + (melted['rank'] / 6)
# melted['length'] = melted['rank'] / 6
# melted
# help(graph.edges)
# help(graph.edge)
# records = melted.to_dict('records')
# records[0]
# help(graph.edge)
# renamed = melted.rename(columns={'name':'tail_name','strength':'head_name','rank':'label'})
# renamed
# for edge in renamed.to_dict('records'):
#     graph.edge(**edge)
# import pdb; pdb.pm()
# help(graph.edge)
# renamed.columns
# melted
melted = pd.melt(trim_exec_df.reset_index(), id_vars=['index']).rename(columns={'index':'name', 'variable':'strength', 'value':'rank'}).dropna()
# melted
# renamed = melted.rename(columns={'name':'tail_name','strength':'head_name','rank':'label'})
# for edge in renamed.to_dict('records'):
#     graph.edge(**edge)
# import pdb; pdb.pm()
# melted.columns
# strings_df = melted[['name', 'strength']]
# strings_df['rank'] = string(melted['rank'])
# strings_df['rank'] = str(melted['rank'])
# strings_df
strings_df['rank'] = melted['rank'].apply(str)
# strings_df
# for edge in strings_df.to_dict('records'):
#     graph.edge(**edge)
# for edge in strings_df.rename(columns={'name':'tail_name','strength','head_name','rank':'label'}).to_dict('records'):
#     graph.edge(**edge)
for edge in strings_df.rename(columns={'name':'tail_name','strength':'head_name','rank':'label'}).to_dict('records'):
    graph.edge(**edge)
# graph
# graph.render(view=true)
# graph.render(view=True)
# graph.engine
graph.engine = 'neato'
# graph.render(view=True)
# graph.graph_attr['overlap'] = False
# graph.render(view=True)
graph.graph_attr['overlap'] = 'false'
graph.render(view=True)
# history
