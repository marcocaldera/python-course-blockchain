simple_list = [1, 2, 3, 4]
simple_list.extend([5, 6, 7])
print(simple_list)
# del(simple_list[0])
del simple_list[0]
print(simple_list)

d = {'name': 'Max'}
print(d.items())
for k, v in d.items():
    print(k, v)
del(d['name'])
print(d)

# TUPLE
t = (1, 2, 3)
print(t.index(1))
# del(t[0]) # doesn'work tuple are immutable
print(t)

# SET
s = {'Max', 'Anna', 'Max'}
# del(s['Max']) # non si può, serve usare il metodo s.discard(...)
print(s)
