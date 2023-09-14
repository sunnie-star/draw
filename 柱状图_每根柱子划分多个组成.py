import matplotlib.pyplot as plt
import numpy as np


# if __name__ == '__main__':
#     font1 = {'family': 'Arial',
#              'weight': 'normal',
#              'size': 15,
#              }
#     font2 = {'family': 'Arial',
#              'weight': 'normal',
#              'size': 20,
#              }
#     #plt.style.use('ggplot')
#     bars_name = ["Reuse","LR", "SR"]  # 柱子名称
#     f1score = [0.73*0.95, 0.72, 0.73]
#     decode = [0,0.02220,  0.02124]
#     sr = [0,0,   0.05872]
#     infer = [0,0.03940,   0.04918]
#     resuse=[0.01,0,0]
#     labels = ["F1score", "Decode", "SR", "Infer","Reuse"]   # 每个柱子的组成
#     colors = ["06283D", "moccasin", "royalblue", "orchid"]  # 每个组成的颜色
#     # colors = ["gold", "darkorange", "firebrick", "darkmagenta"]
#     colors = ["#2D4059", "#EA5455", "#FFD460", "#F07B3F","#E0F9B5"]  # 每个组成的颜色
#     err_attr = {"elinewidth":1,"ecolor":"black", "capsize":6}
#     other = {
#         "title": "f1score and latency",  # 标题
#         "xlabel": "Scheme",  # 横坐标名称
#         "ylabel_left": "F1score",  # 纵坐标名称
#         "ylabel_right": "Latency(s)"
#     }
#     std_err2 = [[0.3,0.3], 0.5*0.25, 0.45*0.25]
#     std_err2=[[0.1*0.4,0.03,0.025],[0.04,0.03,0.025]]
#     xticks = np.arange(len(bars_name))*0.7
#
#     fig, ax = plt.subplots(figsize=(9, 4.5))
#     bar_width = 0.2
#     #, yerr=std_err2,error_kw=err_attr
#     lns1 = ax.bar(xticks, f1score, width=bar_width, label=labels[0],yerr=std_err2,error_kw=err_attr,color=colors[0],edgecolor='black', zorder=10)
#
#     ax2 = ax.twinx()
#     bot = np.array(len(bars_name))*0.0
#     lns2 = ax2.bar(xticks + bar_width, decode, width=bar_width, label=labels[1], color=colors[1], bottom=bot,hatch="",edgecolor='black', zorder=2)
#     bot += decode
#     lns3 = ax2.bar(xticks + bar_width, sr, width=bar_width, label=labels[2], color=colors[2], bottom=bot, hatch="",edgecolor='black', zorder=3)
#     bot += sr
#     lns4 = ax2.bar(xticks + bar_width, infer, width=bar_width, label=labels[3], color=colors[3], bottom=bot, hatch="",edgecolor='black', zorder=4)
#     bot += infer
#     lns5 = ax2.bar(xticks + bar_width, resuse, width=bar_width, label=labels[4], color=colors[4], bottom=bot,hatch="",edgecolor='black', zorder=5)
#     bot += resuse
#     ax.set_ylabel(other["ylabel_left"], fontsize=23)
#     ax2.set_ylabel(other["ylabel_right"], fontsize=23)
#     ax.set_ylim(0.65, 0.76)
#     ax2.set_ylim(0, 0.14)
#     ax.tick_params(labelsize=18)
#     ax2.tick_params(labelsize=18)
#
#     lns = [lns1, lns2, lns3, lns4,lns5]
#     labs = [l.get_label() for l in lns]
#     #ax2.legend(lns, labs, fontsize=18)
#     ax2.legend(lns, labs, fontsize=18,labelspacing=1.5,handlelength=1.5,handletextpad=0.3, ncol=1,handleheight=1,bbox_to_anchor=(1.19, 0.9),frameon=False)
#     #ax2.set_title(other["title"], fontsize=20)
#     # ax2.set_xlabel(other["xlabel"])
#     ax2.set_xticks(xticks + bar_width/2)
#     ax.set_xticklabels(bars_name,fontsize=23)
#      # 网格线fig
#
#     plt.rcParams['hatch.linewidth'] = 2
#     ax.grid(axis='y', zorder=-1)
#     plt.tight_layout()  # 让图片适应画布大小
#     plt.savefig("Motivation1_1.pdf")
#     plt.show()

if __name__ == '__main__':
    font1 = {'family': 'Arial',
             'weight': 'normal',
             'size': 15,
             }
    font2 = {'family': 'Arial',
             'weight': 'normal',
             'size': 20,
             }
    #plt.style.use('ggplot')
    bars_name = ["8Mbps","16Mbps"]  # 柱子名称
    #f1score = [0.73*0.95, 0.72, 0.73]
    '''
    vgg 135.259ms
    mobile-net 10.922ms
    fasterrcnn 45.161ms
    resnet50 29.539ms
    '''
    # [0.57619838, 0.072588312, 0.18942, 0.002, 0.001]
    # [0.45334743, 0.123422222, 0.177877778, 0.002, 0.001]


    #2.5306122448979593
    #1.8877551020408163


    drl_low = [10,10]
    #infer=[2.5306122448979593*i for i in infer]
    transmit = [879,453]
    #sr=[0,0.115,0,0]
    # sr=[1.8877551020408163*i for i in sr]
    Reuse = [181,177]
    #reuse=[1,1-0.157,  1-0.115,1-0.081]
    infer=[103,123]
    #feature=[ 0.157,0, 0]
    drl_high=[15,15]

    # a = [0.879086674, 0.103088889, 0.1813, 0.002, 0.001]

    # a = [0.45334743, 0.123422222, 0.177877778, 0.002, 0.001]

    drl_low = [20,20]
    #infer=[2.5306122448979593*i for i in infer]
    transmit = [879,453]
    #sr=[0,0.115,0,0]
    # sr=[1.8877551020408163*i for i in sr]
    Reuse = [181,177]
    #reuse=[1,1-0.157,  1-0.115,1-0.081]
    infer=[103,123]
    #feature=[ 0.157,0, 0]
    drl_high=[10,10]

    idx=0
    #all=infer[idx]+sr[idx]+Reuse[idx]+feature[idx]+drl[idx]
    #print(infer[idx]/all,sr[idx]/all,Reuse[idx]/all,feature[idx]/all,drl[idx]/5/all)
    reuse=[0.01,0]
    labels = ["DRL_high", "DRL_low","Infer", "Transmit", "Reuse"]   # 每个柱子的组成
    colors = ["06283D", "moccasin", "royalblue", "orchid"]  # 每个组成的颜色
    # colors = ["gold", "darkorange", "firebrick", "darkmagenta"]
    colors = ["#A149FA", "#76BA99", "#FFD460", "#2D4059","#EA5455"]  # 每个组成的颜色
    #colors = ["#EA5455", "#EA5455", "#EA5455", "#EA5455", "#EA5455"]
    err_attr = {"elinewidth":1,"ecolor":"black", "capsize":6}
    other = {
        "title": "f1score and latency",  # 标题
        "xlabel": "Scheme",  # 横坐标名称
        "ylabel_left": "Latency(ms)",  # 纵坐标名称
        "ylabel_right": "Latency(s)"
    }
    # std_err2 = [[0.3,0.3], 0.5*0.25, 0.45*0.25]
    # std_err2=[[0.1*0.4,0.03,0.025],[0.04,0.03,0.025]]
    xticks = np.arange(len(bars_name))*1.1

    fig, ax = plt.subplots(figsize=(7, 5.5))
    bar_width = 0.5
    #, yerr=std_err2,error_kw=err_attr
    #lns1 = ax.bar(xticks, f1score, width=bar_width, label=labels[0],error_kw=err_attr,color=colors[0],edgecolor='black', zorder=10)

    #ax2 = ax.twinx()
    bot = np.array(len(bars_name))*0.0

    lns0 = ax.bar(xticks + bar_width/2, Reuse, width=bar_width, label=labels[4], color=colors[1], bottom=bot, hatch="",edgecolor='black', zorder=4)
    bot += Reuse
    lns1 = ax.bar(xticks + bar_width/2, transmit, width=bar_width, label=labels[3], color=colors[2], bottom=bot,hatch="",edgecolor='black', zorder=2)
    bot += transmit
    lns2 = ax.bar(xticks + bar_width/2, infer, width=bar_width, label=labels[2], color=colors[3], bottom=bot, hatch="",edgecolor='black', zorder=3)
    bot += infer
    lns3 = ax.bar(xticks + bar_width/2, drl_low, width=bar_width, label=labels[1], color=colors[4], bottom=bot, hatch="",edgecolor='black', zorder=4)
    bot += drl_low
    lns = ax.bar(xticks + bar_width/2, drl_high, width=bar_width, label=labels[0], color=colors[0], bottom=bot, hatch="",edgecolor='black', zorder=4)
    bot += drl_high
    # lns5 = ax.bar(xticks + bar_width, reuse, width=bar_width, label=labels[4], color=colors[4], bottom=bot,hatch="",edgecolor='black', zorder=5)
    # bot += reuse
    fls=26
    ax.set_ylabel(other["ylabel_left"], fontsize=fls)
    #ax2.set_ylabel(other["ylabel_right"], fontsize=23)
    #ax.set_ylim(0.65, 0.76)
    ax.set_ylim(0, 1300)
    fs = 21
    ax.tick_params(labelsize=fs)
    #ax2.tick_params(labelsize=18)

    lns = [lns,lns3, lns2,lns1,lns0]
    labs = [l.get_label() for l in lns]
    #ax2.legend(lns, labs, fontsize=18)
    # ax.legend(lns, labs, fontsize=fls,labelspacing=1.5,handlelength=1.5,handletextpad=0.3, ncol=1,handleheight=1,bbox_to_anchor=(1.02, 0.85),frameon=False)
    # ax.legend(lns, labs, fontsize=fls,labelspacing=0.4,handlelength=1.3,handletextpad=0.2, ncol=3,handleheight=1,bbox_to_anchor=(1.2, -0.1),frameon=False)



    ax.legend(lns, labs, fontsize=fls,labelspacing=0.2,handlelength=1.3,handletextpad=0.2,bbox_to_anchor=(1.1, -0.1),frameon=False,ncol=3,columnspacing=0.5)
    # ax2.set_title(other["title"], fontsize=20)
    # ax2.set_xlabel(other["xlabel"])
    ax.set_xticks(xticks + bar_width/2)
    ax.set_xticklabels(bars_name,fontsize=fls)
     # 网格线
    # ax.axhline(y=1, color='gray', linestyle='--',xmin=0, xmax=1)
    # ax.annotate("", xy=(1.275, 0.837), xytext=(1.275, 1),
    #             arrowprops=dict(arrowstyle='<->', lw=2))
    # ax.text(1.05, 0.915, '15.7%', fontsize=15, color='black',bbox=dict(facecolor='white', edgecolor='white', pad=0.5))
    # ax.annotate('', xy=(2.275, 0.88), xytext=(2.275, 1),
    #             arrowprops=dict(arrowstyle='<->', lw=2))
    # 百分比 [0.7536263097866543, 0.0883763811861355, 0.1554254591786935, 0.0017145665656778102, 0.0008572832828389051]
    # 0.7576474299999999
    # 百分比 [0.5983619980074374, 0.16290192128019232, 0.2347764553230254, 0.0026397502595633436, 0.0013198751297816718]

    ax.text(0.6, 1160, '0.1%', fontsize=fs, color='black')
    ax.text(0.6, 1040, '0.2%', fontsize=fs, color='black')
    ax.text(0.6, 930, '8.8%', fontsize=fs, color='black')
    ax.text(0.6, 600, '75.4%', fontsize=fs, color='black')
    ax.text(0.6, 80, '15.5%', fontsize=fs, color='black')


    ax.text(1.7, 870, '0.1%', fontsize=fs, color='black')
    ax.text(1.7, 760, '0.3%', fontsize=fs, color='black')
    ax.text(1.7, 640, '16.3%', fontsize=fs, color='black')
    ax.text(1.7, 350, '59.8%', fontsize=fs, color='black')
    ax.text(1.7, 80, '23.5%', fontsize=fs, color='black')

    # ax.text(0.6, 1100, '0.08%', fontsize=15, color='black')
    # ax.text(0.6, 1020, '0.17%', fontsize=15, color='black')
    # ax.text(0.6, 940, '10.0%', fontsize=15, color='black')
    # ax.text(0.6, 600, '74.4%', fontsize=15, color='black')
    # ax.text(0.6, 80, '15.3%', fontsize=15, color='black')
    # ax.text(1.7, 810, '0.1%', fontsize=15, color='black')
    # ax.text(1.7, 730, '0.26%', fontsize=15, color='black')
    # ax.text(1.7, 650, '12.4%', fontsize=15, color='black')
    # ax.text(1.7, 350, '45.3%', fontsize=15, color='black')
    # ax.text(1.7, 80, '17.7%', fontsize=15, color='black')
    # ax.annotate('', xy=(3.275, 0.915), xytext=(3.275, 1),
    #             arrowprops=dict(arrowstyle='<->', lw=2))
    # ax.text(3.15, 0.948, '8.1%', fontsize=15, color='black', bbox=dict(facecolor='white', edgecolor='white', pad=0.5))
    #ax.spines['right'].set_visible(False)
    #ax.spines['top'].set_visible(False)
    ax.set_xlim(-0.3, 2.2)
    plt.rcParams['hatch.linewidth'] = 2
    # ax.grid(axis='y', zorder=-1)
    plt.tight_layout()  # 让图片适应画布大小
    plt.savefig("break_latency.svg")
    plt.savefig("break_latency.pdf")
    plt.show()