import operator
d = {'a': 25, 'b': 61, 'c': 38, 'd': 54, 'e': 2, 'f': 10, 'g': 84}
l = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
print(f'The highest 3 values in a dictionary are: {dict(l[0:3])}')
