import matplotlib.pyplot as plt

x_values = list(range(1,5001))
y_values = [pow(x,3) for x in x_values]

plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolors='none',s=20)

plt.axis([0,5050,0,pow(5050,3)])
plt.title("Cubic Numbers")
plt.xlabel("Value")
plt.ylabel("Cubic of Value")

plt.savefig('sample_cubic_scatter.png',bbox_inches='tight')