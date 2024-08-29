import numpy as np
import matplotlib.pyplot as plt

#a
a = np.array([67.1,1,-0.3,5.2,-6])
b = np.array([1,3,2.2,5.1,1])

#b
print(np.dot(a,b))

#c
print(a*b)

#d
A = np.array([[2,-1,-3],[4,-1.5,-2.5],[7.3,-0.9,-0.2]])

#e
print(np.transpose(A))

#f
Matriz = np.ones((3,3))
redondear = np.round(a) #redondea al mas cercano
ceil = np.ceil(a) #redondea arriba
floor = np.floor(a) #redondea abajo

#g,h,i
print(A[0,2])
print(A[1,:])
print(A.shape)

#j,k,l,m,n
x = np.arange(0,81)
y1 = np.sin(np.pi*0.18*x)
y2 = np.cos(2*np.pi*0.03*x)
y3 = y1+y2
y4 = y1*y2
fig, (ax1, ax2) = plt.subplots(2, 1)

ax1.plot(x,y1,label= 'seno', color = 'black')
ax1.plot(x,y2, label = 'coseno', color = 'blue')

ax1.set_title('grafica 1')
ax1.set_xlabel('Eje x')
ax1.set_ylabel('Eje y')
ax1.legend()

ax2.plot(x,y3, label='suma', color = 'red')
ax2.plot(x,y4, label = 'producto', color = 'green')


ax2.set_xlabel('Eje x')
ax2.set_ylabel('Eje y')
ax2.legend()

plt.plot()

plt.show()