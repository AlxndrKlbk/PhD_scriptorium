g0 = graph(type="well",default_value=0)
g1 = graph(type="well",default_value=0)
g2 = graph(type="well",default_value=0)
for w in get_all_wells():
  for c in w.get_connections_from_branch (branch_id = 0):
    g0[w]+=copr[c]
  for c in w.get_connections_from_branch (branch_id = 1):
    g1[w]+=copr[c]
  for c in w.get_connections_from_branch (branch_id = 2):
    g2[w]+=copr[c]
export (g0, name = 'orat_branch0')
export (g1, name = 'orat_branch1')
export (g2, name = 'orat_branch2')
