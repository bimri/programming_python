import cgi, sys
form = cgi.FieldStorage() # print all inputs to stderr; stodout=reply page
for name in form.keys():
    print('[%s:%s]' % (name, form[name].value), end=' ', file=sys.stderr)


'''
The moral of this story is that unless you can be sure that the names of all but the
leftmost URL query parameters embedded in HTML are not the same as the name of
any HTML character escape code like amp, you should generally either use a semicolon
as a separator, if supported by your tools, or run the entire URL through cgi.escape
after escaping its parameter names and values with urllib.parse.quote_plus:
'''
