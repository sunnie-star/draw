import numpy as np
import matplotlib.pyplot as plt
from function import bitrateTrans
from colors import (colors,fs,fls,fsmi)
"""
x=np.arange(2)  #两组
y1=[1454.45,2078.15
]
y1=[bitrateTrans(i) for i in y1]
y2=[899.2,1813.05
]
y2=[bitrateTrans(i) for i in y2]
total_size,n=0.5,2
width=total_size/n
plt.figure(1,figsize=(10,5))
plt.bar(x-width/2-0.05,y1,width=width, color='#36738E',label='VSiM') #VSim
plt.bar(x+width/2+0.05,y2,width=width,color='#F66A6A',label='Cubic') # Cubic

plt.ylim(30, 100)
plt.xlim(-0.7, 1.7)
plt.xticks(x,['Min QoE','Avg. QoE'],fontsize=34)
my_yticks= ['%.2f'%i for i in np.arange(0,2800,700)]
print(my_yticks)
plt.yticks(np.arange(30,100,20),fontsize=34)
# plt.title('(a)Topology 1',y=-0.5,fontsize=40,weight='bold',family='Times New Roman')
plt.ylabel('QoE',fontsize=34,weight='bold')
# for i in range(2):
#     plt.text(x[i]-width/2-0.05,y1[i]+50,'%.2f' % y1[i],ha='center',fontsize=34)
#     plt.text(x[i]+width/2+0.05, y2[i] + 50, '%.2f' % y2[i],ha='center', fontsize=34)
plt.legend(loc='upper left',fontsize=23)
plt.grid(axis='y',ls='--')

for i in range(2):    #  3组
    plt.text(x[i]-width/2-0.05, y1[i],'%.2f' % y1[i],ha='center',fontsize=10)
    plt.text(x[i]+width/2+0.05,    y2[i], '%.2f' % y2[i],ha='center', fontsize=10)

plt.tight_layout()
plt.savefig('Topology 1.png',format="png", bbox_inches='tight')
plt.savefig('Topology 1.pdf',format="pdf", bbox_inches='tight')

#  figure 2	Min QoE	Avg. QoE
# VSiM	1287.83 	1688.33
# Cubic	863.83 	1813.05
x=np.arange(2)  #两组
y1=[1287.83 ,	1688.33
]
y1=[bitrateTrans(i) for i in y1]
y2=[863.83 	,1813.05
]
y2=[bitrateTrans(i) for i in y2]
total_size,n=0.5,2
width=total_size/n
plt.figure(2,figsize=(10,5))
plt.bar(x-width/2-0.05,y1,width=width, color='#36738E',label='VSiM') #VSim
plt.bar(x+width/2+0.05,y2,width=width,color='#F66A6A',label='Cubic') # Cubic

plt.ylim(30, 100)
plt.xlim(-0.7, 1.7)
plt.xticks(x,['Min QoE','Avg. QoE'],fontsize=34)
# my_yticks= ['%.2f'%i for i in np.arange(0,2800,700)]
# print(my_yticks)
plt.yticks(np.arange(30,100,20),fontsize=34)
plt.ylabel('QoE',fontsize=34,weight='bold')
# plt.title('(b)Topology 2',y=-0.5,fontsize=40,weight='bold',family='Times New Roman')
# for i in range(2):
#     plt.text(x[i]-width/2-0.05,y1[i]+50,'%.2f' % y1[i],ha='center',fontsize=34)
#     plt.text(x[i]+width/2+0.05, y2[i] + 50, '%.2f' % y2[i],ha='center', fontsize=34)
plt.grid(axis='y',ls='--')
plt.legend(loc='upper left',fontsize=23)
for i in range(2):    #  3组
    plt.text(x[i]-width/2-0.05, y1[i],'%.2f' % y1[i],ha='center',fontsize=10)
    plt.text(x[i]+width/2+0.05,    y2[i], '%.2f' % y2[i],ha='center', fontsize=10)
plt.tight_layout()
plt.savefig('Topology 2.png',format="png", bbox_inches='tight') # 替换 plt.show()
plt.savefig('Topology 2.pdf',format="pdf", bbox_inches='tight')
"""

# 	figure 3 Min QoE	Avg. QoE
# VSiM_wo_SP	1130.22 	1726.67
# VSiM	1300.67 	1949.22
fig, ax = plt.subplots(figsize=(7, 4))
x=np.arange(1,5,1.5)  #横轴坐标  1   2.5   4

# y1=[86.36,3]
# y2=[13.64,20]
# y3=[3,80]

# y1  2   3就是legend
y1=[88,25,3]
y2=[12,58.33,18.18]
y3=[3,16.67,81.82]
total_size,n=0.5,2
width=total_size/n
barwidth=0.3
# Rank 1st，Rank 2nd，Rank 3rd
#4193F7n藍色
#69CCC9綠色
#F6C859黃色
l1=ax.bar(x,y1,width=barwidth-0.05, color='#4193F7',label='Rank 1st')
l2=ax.bar(x+barwidth,y2,width=barwidth-0.05,color='#69CCC9',label='Rank 2nd') # Cubic
l3=ax.bar(x+barwidth*2,y3,width=barwidth-0.05, color='#F6C859',label='Rank 3rd')

# # 下面是写text的高度，要略高一点
# biash=3
# y1=np.array([88,25,3])+biash
# y2=np.array([12,58.33,18.18])+biash
# y3=np.array([3,16.67,81.82])+biash
# t1=[88,25,0]
# t2=[12,58.33,18.18]
# t3=[0,16.67,81.82]
# # y1=np.array([88,3])+biash
# # y2=np.array([12,18.18])+biash
# # y3=np.array([3,81.82])+biash
# # plt.text确定的位置是最后一行文字的左下角的位置
# x1=x-0.15
# x2=x+barwidth-0.15
# x3=x+barwidth*2-0.15
# for i in range(len(x)):
#     plt.text(x1[i],y1[i],f"{t1[i]}%",size=fsmi)  #第一条线
#     plt.text(x2[i],y2[i],f"{t2[i]}%",size=fsmi)  #第二条线
#     plt.text(x3[i],y3[i],f"{t3[i]}%",size=fsmi)  #第三个legend


ax.set_ylim(-1, 100,30)
ax.set_xlim(0.5, 5)
# edge-cloud collaboration和cloud-only
# x是最左边的柱子  xticks位置要在中间柱子比较好看
ax.set_xticks(x+barwidth,['local-remote\ncollaboration','local-only','remote-only'],fontsize=fs)
ax.set_yticks(np.arange(0,101,30),fontsize=fs)
ax.tick_params(labelsize=fs)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('none')
ax.grid(axis='y', zorder=-1)
# lns=[l1,l2,l3]
# labs = [l.get_label() for l in lns]
# ax.legend(lns, labs, fontsize=fsmi, labelspacing=1.5, handlelength=1.5, handletextpad=0.3, ncol=3, handleheight=1,
#           bbox_to_anchor=(1, 1.25), frameon=False)
ax.legend(fontsize=fs, labelspacing=1.5, handlelength=1.5, handletextpad=0.3, ncol=3, handleheight=1,
          bbox_to_anchor=(1, 1.25), frameon=False)

# plt.legend(loc='upper left',col=2,fontsize=25)
# for i in range(2):    #  3组
#     plt.text(x[i]-width/2-0.05, y2[i],'%.2f' % y2[i],ha='center',fontsize=10)
#     plt.text(x[i]+width/2+0.05,    y1[i], '%.2f' % y1[i],ha='center', fontsize=10)
plt.tight_layout()
plt.savefig('../figures/zhuzhuangtu.png',format="png", bbox_inches='tight') # 替换 plt.show()
plt.savefig('../figures/zhuzhuangtu.pdf',format="pdf", bbox_inches='tight')
plt.show()
#	figure 4 Min QoE	Avg. QoE
# VSiM_wo_BA	978.25 	1909.03
# VSiM	1300.67 	1949.22


