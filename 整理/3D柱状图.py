#3D柱状图
#特征点在图片中的坐标位置
m = 448
n = 392

import numpy as np
import matplotlib.pyplot as plt

# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
from colors import (colors,font1,font2)
fig = plt.figure(figsize=(6*1.5, 5*1.5))  # 画布宽长比例
ax = fig.add_subplot( projection='3d')
#ax1.tick_params(labelsize=15)
ax.tick_params(labelsize=15)
x=[4,3,2,1,0,4,3,2,1,0,4,3,2,1,0]
y=[0,0,0,0,0,8,0,7,7,3,0,8,8,0,7]
y=[i*1.5+2 for i in y]

z=[3,5,2,7,2,4,7,4,1,8,9,3,8,6,0]
z=[i*1.5 for i in z]
dx=[0.2*5/4.5 for _ in range(len(x))]
dy=[8,8,5,9,7,2,3,2,2,5,2,2,1,2,2]
dz=[5,5,7,4,5,3,3,6,7,2,1,3,2,2,8]
color=[i%5 for i in range(len(x))]
for i in range(len(x)):
    ax.bar3d(x[i], y[i], z[i], dx[i], dy[i], dz[i], shade=True,color=colors["red"])

ax.set_xlabel('Frame',font=font2,labelpad=8.5)
ax.set_ylabel('Width',font=font2,labelpad=8.5)
ax.set_zlabel('Height',font=font2,labelpad=8.5)
ax.set_xticks(np.arange(0, 4.0000000001, 1))
ax.set_yticks(np.arange(0, 20.000000001, 20))
ax.set_zticks(np.arange(0, 20.000000001, 20))
plt.grid(axis = 'x')
plt.tight_layout()
plt.savefig("../figures/3D柱状图.png",format="png", bbox_inches='tight')
plt.show()