# statelist python
```py
from oy3opy.statelist import StateList

# init
sl = StateList([1,2,3,4,5]) # List[Any]
print(sl)

# append
sl.append(6)
sl[7] = {'mark': True}
print(sl)

# remove
sl.remove(2)
del sl[5]
print(sl)

# update
sl.update(1,{'active':True})
sl[3] = {'mark': False}
print(sl)

# get
print('get(3): ', sl.get(3))
print('[1]: ', sl[1])

# iter
print(sl)
for (item, state) in sl:
    print(item, state)

# save/loads
s = sl.dumps() # equals json.dumps(sl)
sl = StateList(s)
print(sl)
```
