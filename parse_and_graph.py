import pandas as pd
import graphviz as gv

INPUTDIR = 'example/'
OUTPUTDIR = 'example/'
SUBPATH = 'redacted_team_raw.csv'

raw_df = pd.DataFrame.from_csv(INPUTDIR + SUBPATH, header=1)
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
graph.render(OUTPUTDIR + SUBPATH + '.gv', view=True)

# calculate probability
"""

p = number of people
s = distinct strengths
t = distinct possible strengths
d = depth (number of top strengths per person)


pvalue_for_s_strengths = ways_with_s_strengths / ways_with_t_strengths

---

ways_with_t_strengths = ncr(t, d) ** p

---

ways_with_s_strengths

Underestimate
# undercounts distinct ways to pick set S out of T

    ways_with_s_strengths >= ncr(s, d) ** p

Overestimate
# overcounts situations where p people don't use all s strengths

    ways_with_s_strengths <= ncr(s, d) ** p * ncr(t, s)

It would be good to incorporate actual distributions:
https://drive.google.com/file/d/0B9GCEaVaZ_FLZDM0bk9Dckc2Sms/view

"""

p = melted_df.index.nunique()
s = melted_df.variable.nunique()

import ncr

def underestimate(t=34, d=5, p=p, s=s):
    return ncr.Fraction(ncr.ncr(s,d),ncr.ncr(t, d)) ** p

def overestimate(t=34, d=5, p=p, s=s):
    return underestimate(t, d, p, s) * ncr.ncr(t,s)

under = underestimate()
print("\nUnderestimate:")
print(under)
print(float(under))

over = overestimate()
print("\nOverestimate:")
print(over)
print(float(over))
