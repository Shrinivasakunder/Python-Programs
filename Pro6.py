s = input("Enter the string: ").lower().split()
d = dict()
for w in s:
    d[w] = d.get(w, 0)+1
for k,v in d.items():
    print(f'{k.capitalize()} - {v}')
