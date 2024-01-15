# import matplotlib.pyplot as plt
# import numpy as np
#
# import matplotlib.pyplot as plt
# import matplotlib as mpl
# import numpy as np
#
# mpl.rcParams["font.sans-serif"] = ["SimHei"]
# mpl.rcParams["axes.unicode_minus"] = False
# #
# # 44 1 10 0.4885
# # 35 4 13 0.482
# # 37 4 10 0.4615
# # 35 37 44
# # 110 410 413
# # 35 -0.021 -0.02 0.482
# # 37 -0.04245 0.4615 0.449
# # 39 0.4705 0.469 0.0.4495
# x = np.arange(4)
# # # # a=[0.4705,-0.04245+0.1,-0.021+0.1]
# # # # b=[0.46,0.4615,-0.02+0.05]
# # # # c=[0.44,0.4,0.482]
# acc=[1.0,0.95,0.92,0.88]
# bar_width = 0.5
# tick_label = ['Ours', 'w/o\n'+'transfer', 'w/o\n reuse','w/o\n SR']
# fig,ax=plt.subplots(figsize=(5, 4.5))
# # plt.figure(figsize=(5, 5))
# from colors import colors
# ax.bar(x+bar_width, acc, bar_width, align="center", color=colors["green"],edgecolor='black', label="Action1")
# #ax.bar(x + bar_width, b, bar_width, color="#EA5455", align="center", label="Action2")
# #ax.bar(x + 2 * bar_width, c, bar_width, color="#FFD460", align="center", label="Action3")
# font1 = {'family' : 'Arial',
# 'weight' : 'normal',
# 'size'   : 25,
#          }
# font2 = {'family' : 'Arial',
# 'weight' : 'normal',
# 'size'   : 25,
#          }
# fls=25
# fs=20
# # plt.grid(axis='y')  # 网格线
# # plt.xlabel("Reward")
# ax.set_ylabel("F1-score",size=20)
# my_y_ticks = np.arange(0.80, 1.05, 0.05)
# plt.yticks(my_y_ticks)
# ax.set_ylim(0.8, 1.01)
#
# ax.annotate("",
#                 xy=(1.5, 0.948),
#                 xytext=(1.5, 1),
#                 # xycoords="figure points",
#                 arrowprops=dict(arrowstyle="->", color="r",lw=2))
# ax.annotate("",
#                 xy=(2.5, 0.918),
#                 xytext=(2.5, 1),
#                 # xycoords="figure points",
#                 arrowprops=dict(arrowstyle="->", color="r",lw=2))
# ax.annotate("",
#                 xy=(3.5, 0.878),
#                 xytext=(3.5, 1),
#                 # xycoords="figure points",
#                 arrowprops=dict(arrowstyle="->", color="r",lw=2))
# ax.set_xticks(x + bar_width , tick_label,size=fls,rotation = 360)
# ax.plot([0.26, 3.72], [1, 1], c='black', linestyle='--')
# plt.text(0.95, 0.952, '0.05',size=fs)
# plt.text(1.95, 0.922, '0.08',size=fs)
# plt.text(2.950, 0.882, '0.12',size=fs)
# plt.yticks( size=fs)#设置大小及加粗
# #plt.legend( ncol=3, bbox_to_anchor=(1.05, 1.25),prop=font1)
# plt.tight_layout()
# plt.savefig('break.svg',format='svg')
# plt.savefig('break.pdf')
# plt.show()
#
#
#



import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False
#
# 44 1 10 0.4885
# 35 4 13 0.482
# 37 4 10 0.4615
# 35 37 44
# 110 410 413
# 35 -0.021 -0.02 0.482
# 37 -0.04245 0.4615 0.449
# 39 0.4705 0.469 0.0.4495

# # # a=[0.4705,-0.04245+0.1,-0.021+0.1]
# # # b=[0.46,0.4615,-0.02+0.05]
# # # c=[0.44,0.4,0.482]
acc=[1.0,0.95,0.92,0.88]
# ours=0.84
# acc=[0.84  ,0.774858199,   0.8 ]
# acc=[i/0.84 for i in acc]
# print(acc)
# [1.0, 0.9224502369047619, 0.9523809523809524]
acc=[1.0, 0.92, 0.95]
acc=[0.87,0.73, 0.8]
#
# x = np.arange(len(acc))
x=np.array([0,1.5,3])   #柱子的中间
bar_width = 0.5
tick_label = ['Ours', 'w/o\nHybrid \ncodec', 'w/o\n Bandwidth\n controller']
fig,ax=plt.subplots(figsize=(5, 4))
# plt.figure(figsize=(5, 5))
from colors import colors
ax.bar(x, acc, bar_width, align="center", color=colors["green"],edgecolor='black', label="Action1")
#ax.bar(x + bar_width, b, bar_width, color="#EA5455", align="center", label="Action2")
#ax.bar(x + 2 * bar_width, c, bar_width, color="#FFD460", align="center", label="Action3")
font1 = {'family' : 'Arial',
'weight' : 'normal',
'size'   : 21,
         }
font2 = {'family' : 'Arial',
'weight' : 'normal',
'size'   : 21,
         }
fls=21
fs=16
# plt.grid(axis='y')  # 网格线
# plt.xlabel("Reward")
ax.set_ylabel("F1-score",size=20)
# my_y_ticks = np.arange(0.80, 1.05, 0.05)
# plt.yticks(my_y_ticks)
plt.yticks(np.arange(0,1.1,0.05))
# ax.set_ylim(0.85, 1.01)

ax.set_ylim(0.7, 0.9)
# acc=[1.0, 0.92, 0.95]
# 0.87.73 0.8
'''
    xy=(横坐标，纵坐标)  箭头尖端
    xytext=(横坐标，纵坐标) 文字的坐标，指的是最左边的坐标
    arrowprops= {
        facecolor= '颜色',
        shrink = '数字' <1  收缩箭头
    }

'''
ax.annotate("",
                xy=(1.5, 0.73),
                xytext=(1.5, 0.87),
                # xycoords="figure points",
                arrowprops=dict(arrowstyle="->", color="r",lw=2))
ax.annotate("",
                xy=(3, 0.8),
                xytext=(3., 0.87),
                # xycoords="figure points",
                arrowprops=dict(arrowstyle="->", color="r",lw=2))


# ax.annotate("",
#                 xy=(2, 0.92),
#                 xytext=(2, 1),
#                 # xycoords="figure points",
#                 arrowprops=dict(arrowstyle="->", color="r",lw=2))
# ax.annotate("",
#                 xy=(3.5, 0.95),
#                 xytext=(3.5, 1),
#                 # xycoords="figure points",
#                 arrowprops=dict(arrowstyle="->", color="r",lw=2))
# ax.annotate("",
#                 xy=(3.5, 0.878),
#                 xytext=(3.5, 1),
#                 # xycoords="figure points",
#                 arrowprops=dict(arrowstyle="->", color="r",lw=2))
ax.set_xticks(x, tick_label,size=fls,rotation = 360)
ax.plot([0.26, 3.72], [0.87, 0.87], c='black', linestyle='--')
# plt.text(0.95, 0.952, '0.08',size=16)
# plt.text(1.95, 0.922, '0.05',size=16)
# [0,1.5,3]
# 0.87.73 0.8
# plt.text(1.+0.3, 0.73, '0.08',size=fs)
# plt.text(2.5+0.3, 0.8, '0.05',size=fs)

plt.text(1.+0.3, 0.75, '16%',size=fs)
plt.text(2.5+0.5, 0.82, '8%',size=fs)
# plt.text(2.950, 0.882, '0.12',size=16)
plt.yticks( size=fs)#设置大小及加粗
#plt.legend( ncol=3, bbox_to_anchor=(1.05, 1.25),prop=font1)
plt.tight_layout()
plt.savefig('../figures/柱状图_显示到最高柱子的差距',format='png',bbox_inches='tight')
plt.show()


