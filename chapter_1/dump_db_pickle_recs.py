'''
dumps the entire database by using the standard library’s glob
module to do filename expansion and thus collect all the files in this directory with
a .pkl extension. To load a single record, we open its file and deserialize with pickle;
we must load only one record file, though, not the entire database, to fetch one record.
'''
import glob, pickle
for filename in glob.glob('*.pkl'):                                         # for 'bob', 'sue', 'tom'
    recfile = open(filename, 'rb')
    record = pickle.load(recfile)
    print(filename, '=>\n ', record)


suefile = open('sue.pkl', 'rb')
print(pickle.load(suefile)['name'])                                          # fetch sue's name 
