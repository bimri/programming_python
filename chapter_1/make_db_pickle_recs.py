"Using Per-Record Pickle Files"
'''
As mentioned earlier, one potential disadvantage of this section’s examples so far is
that they may become slow for very large databases: because the entire database must
be loaded and rewritten to update a single record, this approach can waste time. We
could improve on this by storing each record in the database in a separate flat file.
'''

from initdata import bob, sue, tom
import pickle
for (key, record) in [('bob', bob), ('tom', tom), ('sue', sue)]:
    recfile = open(key + '.pkl', 'wb')
    pickle.dump(record, recfile)
    recfile.close()
