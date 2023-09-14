font1 = {'family' : 'Arial',
'weight' : 'normal',
'size'   : 15,
         }
font2 = {'family' : 'Arial',
'weight' : 'normal',
'size'   : 20,
         }
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from colors import cdic
df = pd.read_excel("/home/ubuntu/VideoAnalytics/workplace/DRL_SR_Infer/DRL_continuous/src/profile/obnum_acc_car.xlsx")
font1 = {'family' : 'Arial',
'weight' : 'normal',
'size'   : 20,
         }
font2 = {'family' : 'Arial',
'weight' : 'normal',
'size'   : 20,
         }
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# df = pd.read_excel("/home/ubuntu/VideoAnalytics/workplace/DRL_SR_Infer/DRL_continuous/src/profile/obnum_acc_car.xlsx")
# data=df.values
# data_360p = []
# data_540p = []
# data_720p = []
# data_360p_high = []
# data_540p_high = []
# data_720p_high = []
# # 生成一些随机数据
# for line in data:
#     data_360p.append(line[0])
#     data_540p.append(line[1])
#     data_720p.append(line[2])
#     data_360p_high.append(line[5])
#     data_540p_high.append(line[6])
#     data_720p_high.append(line[7])
# # 将数据放入一个列表中
# data = [data_360p[32:56], data_540p[32:56], data_720p[32:56],data_360p_high[17:31], data_540p_high[17:31], data_720p_high[17:31]]
#
# # 设定每个箱子的填充颜色
# colors = [cdic["red"], cdic["yellow"], cdic["blue"],cdic["red"], cdic["yellow"], cdic["blue"]]
#
#
#
# # 设定每个箱子的边框线颜色和填充颜色
# boxprops = dict(linestyle='-', linewidth=1.5, color='black')
# medianprops = dict(linestyle='-', linewidth=1.5, color='black')
# # 绘制箱图，并指定边框线颜色和填充颜色
# fig, ax = plt.subplots()
# boxplot = ax.boxplot(data,showfliers=False, boxprops=boxprops,medianprops=medianprops, patch_artist=True, widths=0.6)
#
# # 为每个箱子中的每个矩形设置填充颜色
# for i, box in enumerate(boxplot['boxes']):
#     box.set(facecolor=colors[i])
#
# # 设定图表标题和坐标轴标签
# #ax.set_title('Video Quality Comparison',font2)
# #ax.set_xlabel('Video Quality',font2)
# ax.set_ylabel('F1 score',font2)
#
# # 设置横坐标标签
# ax.set_xticklabels(['270p', '360p', '540p','270p', '360p', '540p'])
# plt.yticks([0.7,0.8,0.9,1.0], size=15)#设置大小及加粗
# plt.xticks( size=15)
# plt.tight_layout()
# # 显示图形
# plt.show()
data=df.values
data_360p = []
data_540p = []
data_720p = []
data_360p_high = []
data_540p_high = []
data_720p_high = []
# 生成一些随机数据
for line in data:
    data_360p.append(line[0])
    data_540p.append(line[1])
    data_720p.append(line[2])
    data_360p_high.append(line[5])
    data_540p_high.append(line[6])
    data_720p_high.append(line[7])
# 将数据放入一个列表中
# data = [data_360p[32:56], data_720p[32:56],data_360p[10:32], data_720p[10:32],]
# data = [data_360p[32:56], data_540p[32:56], data_720p[32:56],data_360p[10:32], data_540p[10:32], data_720p[10:32],]
data = [data_360p[32:56], data_540p[32:56], data_720p[32:56],data_360p[10:32], data_540p[10:32], data_720p[10:32]]
# data = [ data_720p[10:32], data_540p[10:32],data_360p[10:32], data_720p[32:56],data_540p[32:56],data_360p[32:56] ]
print(np.max(data_360p_high))
print(np.max(data_540p_high))
print(np.max(data_720p_high))
# 设定每个箱子的填充颜色
# colors = ['#A149FA', '#F66A6A', '#2D4059', '#A149FA', '#F66A6A', '#2D4059']
# colors = [cdic["red"],  cdic["blue"],cdic["red"],cdic["blue"]]
colors = [cdic["red"], cdic["yellow"], cdic["blue"],cdic["red"], cdic["yellow"], cdic["blue"]]
# 设定每个箱子的边框线颜色和填充颜色
boxprops = dict(linestyle='-', linewidth=1.5, color='black')
medianprops = dict(linestyle='-', linewidth=1.5, color='black')
# 绘制箱图，并指定边框线颜色和填充颜色
# fig, ax = plt.subplots()
fig, ax = plt.subplots(figsize=(5,3.5))
boxplot = ax.boxplot(data,showfliers=False, boxprops=boxprops,medianprops=medianprops, patch_artist=True, widths=0.6)
# boxplot = ax.boxplot(data[3:6],showfliers=False, boxprops=boxprops,medianprops=medianprops, patch_artist=True, widths=0.6)

# 为每个箱子中的每个矩形设置填充颜色
for i, box in enumerate(boxplot['boxes']):
    box.set(facecolor=colors[i])

# 设定图表标题和坐标轴标签
#ax.set_title('Video Quality Comparison',font2)
#ax.set_xlabel('Video Quality',font2)
ax.set_ylabel('F1 score',font2)
ax.set_yticks(np.arange(0,1.01,0.1))
ax.set_ylim((0.6,1.01))
# 设置横坐标标签
# ax.set_yticklabels(['270p', '540p','270p', '540p'])
# ax.set_xticklabels(['270p', '360p\nnum<5\nsize>10%', '540p','270p', '360p\nnum>30\nsize<1', '540p'])
# ax.set_xticklabels(['', 'num<5 & size>10%\nStream 1', '','', 'num>30 & size<1%\n Stream 2', ''])
ax.set_xticklabels(['', 'num<5 &\nsize>10%', '','', 'num>30 &\n size<1%', ''])
# ax.set_yticklabels(['540p', '360p', '270p','540p', '360p', '270p'])
# plt.text(0.4, 4.5, f'num<5\nsize>10%',font2)
#
# plt.text(0.4, 1, f"num>30\nsize<10%",font2)
 # plt.text(1,0.1, f'num<5\nsize>10%',font2)
import matplotlib.patches as mpatches
biswift_patch = mpatches.Patch(color=colors[0], label='270p',edgecolor="black")
neuro_patch = mpatches.Patch(color=colors[1], label='360p',edgecolor="black")
reducto_patch = mpatches.Patch(color=colors[2], label='540p',edgecolor="black")
plt.legend(handles=[biswift_patch, neuro_patch,reducto_patch],
# labelspacing = 1,
           fontsize=15,ncol=1,frameon=True,
                # edgecolor='black'
           )
plt.axvline(x=3.5, color='gray', linestyle='--')

plt.yticks( size=15)#设置大小及加粗
plt.xticks( size=15)

# plt.subplots_adjust(left=0.1)
# plt.subplots_adjust(bottom=0)
plt.tight_layout()
# plt.subplots_adjust(bottom=0.1)
# 显示图形
plt.savefig("xiangtu.svg",format="svg")
plt.savefig("xiangtu.pdf",format="pdf")
plt.show()