n = int(input("Enter the number of elements: "))
l = list()
print("Enter the elements to list: ")
l = [input() for i in range(n)]
print(f'Original list {l}')
nl = list()
for e in l:
    if e not in nl:
        nl.append(e)
print(f'New list {nl}')
