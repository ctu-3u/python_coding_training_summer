import matplotlib.pyplot as plt 

from random_walk import RandomWalk


rw = RandomWalk(50000)
rw.fill_walk()

# plt.title("Random Walk", fontsize=14)
# plt.xlabel("x position",fontsize=12)
# plt.ylabel("y position",fontsize=12)
# plt.tick_params(axis='both',labelsize=10)
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
plt.scatter(rw.x_values,rw.y_values,s=1,c=list(range(rw.num_points)),cmap=plt.cm.Blues,edgecolors='none')
# plt.plot(rw.x_values,rw.y_values,linewidth=1)
plt.scatter(0,0,s=50,edgecolors='none',c='red')
plt.show()

