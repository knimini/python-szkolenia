# generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.
d=dict()
for i in range(1,21):
    d[i]=i**2
for (k,v) in d.items():
    print (v)
# 
d = {k:k**2 for k in range(1,21)}
print(d)
