import numpy as np
x = np.arange(1,26)

y =x.reshape(5,5)
z=np.array([]).astype(int)

print(y)
for i in x:
    if i%2!=0:
        z = np.append(z,i)

print ("\n\n",z)