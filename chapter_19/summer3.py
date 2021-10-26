"Summing with dictionaries"

sums = {}
for line in open('table4.txt'):
    cols = [float(col) for col in line.split()]
    for pos, val in enumerate(cols):
       sums[pos] = sums.get(pos, 0.0) + val

for key in sorted(sums):
    print(key, '=', sums[key])


"""
Splitting on whitespace extracts the columns, and float converts to numbers,
but a fixed-size list won’t easily accommodate a set of sums (at least, not without extra
code to manage its size). Dictionaries are more convenient here because we can use
column positions as keys instead of using absolute offsets.
"""
