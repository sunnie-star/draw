# """
# import matplotlib.pyplot as plt
# import numpy as np
#
# if __name__ == '__main__':
#     font1 = {'family': 'Arial',
#              'weight': 'normal',
#              'size': 15,
#              }
#     font2 = {'family': 'Arial',
#              'weight': 'normal',
#              'size': 20,
#              }
#     # plt.style.use('ggplot')
#     bars_name = ["270P" + "\n" + "x4", "360P\nx3", "540P\nx2"]  # 柱子名称
#     # bars_name = ["270P" + "\n" + "x4", "360P\nx3", "540P\nx2"]  # 柱子名称
#     # f1score = [0.73*0.95, 0.72, 0.73]
#     # 2.5306122448979593
#     # 1.8877551020408163
#     # infer = [0.157,0.115,  0.081]
#     # #infer=[2.5306122448979593*i for i in infer]
#     # sr = [98,121.3, 210]
#     '''
# vgg  135.259ms    540M
#
# fasterrcnn  45.161ms 163M
#
# edsr:42.602ms          168M
#
# resnet50 29.539ms
#
# mobile-net 10.922ms      21M
#     '''
#     #
#
#     Reuse = [0,0, 0,0, 10.922]
#     sr = [0,0, 0,29.539, 0]
#     # sr=[1.8877551020408163*i for i in sr]
#     # Reuse = [75,150*0.75,   150]
#
#     # feature=[45*0.5,45*0.75,45]
#     feature = [0,0,42.602, 0, 0]
#     mm = [0,45.161, 0, 0, 0]
#     #
#     # drl=[135.259,0,0,0,0]
#
#     Reuse = [0, 0,0, 10.922]
#     sr = [0, 0,29.539, 0]
#     # sr=[1.8877551020408163*i for i in sr]
#     # Reuse = [75,150*0.75,   150]
#
#     # feature=[45*0.5,45*0.75,45]
#     feature = [0,42.602, 0, 0]
#     mm = [45.161, 0, 0, 0]
#
#     Reuse = [0, 0,0, 8.3]
#     sr = [0, 0,5.75, 0]
#     # sr=[1.8877551020408163*i for i in sr]
#     # Reuse = [75,150*0.75,   150]
#
#     # feature=[45*0.5,45*0.75,45]
#     feature = [0,1.31, 0, 0]
#     mm =[ 0.34, 0, 0, 0]
#
#
#     idx = 0
#     # all=infer[idx]+sr[idx]+Reuse[idx]+feature[idx]+drl[idx]
#     # print(infer[idx]/all,sr[idx]/all,Reuse[idx]/all,feature[idx]/all,drl[idx]/5/all)
#     # resuse=[0.01,0,0]
#     # labels = ["DRL", "Reuse", "Feature", "SR", "Infer"]  # 每个柱子的组成
#     labels = ["VGG", "Faster R-CNN", "EDSR","ResNet-50","MobileNetV3",  "Infer"]  # 每个柱子的组成
#     labels = ["NeuroScaler","AccDecoder",  "Reducto", "BiSwift"]
#     colors = ["06283D", "moccasin", "royalblue", "orchid"]  # 每个组成的颜色
#     # colors = ["gold", "darkorange", "firebrick", "darkmagenta"]
#     # colors = ["#A149FA", "#76BA99", "#FFD460", "#2D4059", "#EA5455"]  # 每个组成的颜色
#     colors = ["#A149FA", "#76BA99", "#FFD460", "#2D4059", "#EA5455"]
#     #             紫色            绿          黄          深蓝          红
#     colors = ["#EA5455", "#2D4059", "#FFD460", "#76BA99", "#A149FA"]
#     err_attr = {"elinewidth": 1, "ecolor": "black", "capsize": 6}
#     other = {
#         "title": "f1score and latency",  # 标题
#         "xlabel": "Scheme",  # 横坐标名称
#         "ylabel_left": "Streams",  # 纵坐标名称
#         # "ylabel_left": "Swapping time/ms",  # 纵坐标名称
#         "ylabel_right": "Latency(s)"
#     }
#     # std_err2 = [[0.3,0.3], 0.5*0.25, 0.45*0.25]
#     # std_err2=[[0.1*0.4,0.03,0.025],[0.04,0.03,0.025]]
#     xticks = np.arange(len(bars_name))
#
#     fig, ax = plt.subplots(figsize=(7, 4))
#     bar_width = 0.55
#     # , yerr=std_err2,error_kw=err_attr
#     # lns1 = ax.bar(xticks, f1score, width=bar_width, label=labels[0],error_kw=err_attr,color=colors[0],edgecolor='black', zorder=10)
#
#     # ax2 = ax.twinx()
#     xticks = np.arange(4)
#     bot = np.array(4) * 0.0
#     #
#     # lns0 = ax.bar(xticks + bar_width / 2, Reuse, width=bar_width, label=labels[1], color=colors[1], bottom=bot,
#     #               hatch="", edgecolor='black', zorder=4)
#     # bot += Reuse
#     # lns1 = ax.bar(xticks + bar_width / 2, sr, width=bar_width, label=labels[2], color=colors[2], bottom=bot,
#     #               hatch="", edgecolor='black', zorder=2)
#     # bot += sr
#     # lns2 = ax.bar(xticks + bar_width / 2, feature, width=bar_width, label=labels[3], color=colors[3], bottom=bot, hatch="",
#     #               edgecolor='black', zorder=3)
#     # bot += feature
#     #
#     # lns3 = ax.bar(xticks + bar_width/2, drl, width=bar_width, label=labels[4], color=colors[4], bottom=bot, hatch="",edgecolor='black', zorder=4)
#     # 下面这样是如果要图例中说明每个柱子的label  那么要一个一个画
#
#     # lns0 = ax.bar(xticks + bar_width / 2, drl, width=bar_width, label=labels[0], color=colors[0], bottom=bot,
#     #               hatch="", edgecolor='black', zorder=4)
#     # bot += drl
#     lns01 = ax.bar(xticks + bar_width / 2, mm, width=bar_width, label=labels[0], color=colors[0], bottom=bot,
#                   hatch="", edgecolor='black', zorder=4)
#     bot += mm
#     lns1 = ax.bar(xticks + bar_width / 2, feature, width=bar_width, label=labels[1], color=colors[1], bottom=bot,
#                   hatch="", edgecolor='black', zorder=2)
#     bot += feature
#     lns2 = ax.bar(xticks + bar_width / 2, sr, width=bar_width, label=labels[2], color=colors[2], bottom=bot, hatch="",
#                   edgecolor='black', zorder=3)
#     bot += sr
#
#     lns3 = ax.bar(xticks + bar_width/2, Reuse, width=bar_width, label=labels[3], color=colors[3], bottom=bot, hatch="",edgecolor='black', zorder=4)
#
#
#
#
#     # lns = ax.bar(xticks + bar_width/2, drl, width=bar_width, label=labels[0], color=colors[0], bottom=bot, hatch="",edgecolor='black', zorder=4)
#     # bot += drl
#     # lns5 = ax2.bar(xticks + bar_width, resuse, width=bar_width, label=labels[4], color=colors[4], bottom=bot,hatch="",edgecolor='black', zorder=5)
#     # bot += resuse
#     ax.set_ylabel(other["ylabel_left"], fontsize=20)
#     # ax2.set_ylabel(other["ylabel_right"], fontsize=23)
#     # ax.set_ylim(0.65, 0.76)
#     # ax.set_ylim(0, 0.2)
#     ax.tick_params(labelsize=15)
#     # ax2.tick_params(labelsize=18)
#
#     # lns = [lns,lns3, lns2,lns1,lns0]
#     # labs = [l.get_label() for l in lns]
#     # ax2.legend(lns, labs, fontsize=18)
#     # ax.legend(lns, labs, fontsize=15,labelspacing=1.5,handlelength=1.5,handletextpad=0.3, ncol=1,handleheight=1,bbox_to_anchor=(1.02, 0.85),frameon=False)
#     # ax2.set_title(other["title"], fontsize=20)
#     # ax2.set_xlabel(other["xlabel"])
#     # ax.set_xticks(xticks + bar_width / 2)
#     # ax.set_xticklabels(bars_name, fontsize=20)
#     # 网格线
#     plt.xticks([])
#     ax.spines['right'].set_visible(False)
#     ax.spines['top'].set_visible(False)
#     # ax.set_xlim(-0.3, 2.8)
#     plt.rcParams['hatch.linewidth'] = 2
#     ax.grid(axis='y', zorder=-1)
#     lns=[lns01,lns1,lns2,lns3]
#     labs = [l.get_label() for l in lns]
#     ax.legend()
#     # ax.legend(lns, labs, fontsize=18, labelspacing=1.5, handlelength=1.5, handletextpad=0.3, ncol=3, handleheight=1,
#     #           bbox_to_anchor=(1.2, 1.25), frameon=False)
#
#     plt.tight_layout()  # 让图片适应画布大小
#     plt.savefig("throughput.svg")
#     plt.savefig("throughput.pdf")
#     plt.show()
#
#



#miliang 修改过的stream  吞吐量图
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    font1 = {'family': 'Arial',
             'weight': 'normal',
             'size': 15,
             }
    font2 = {'family': 'Arial',
             'weight': 'normal',
             'size': 20,
             }
    # plt.style.use('ggplot')
    bars_name = ["270P" + "\n" + "x4", "360P\nx3", "540P\nx2"]  # 柱子名称
    # bars_name = ["270P" + "\n" + "x4", "360P\nx3", "540P\nx2"]  # 柱子名称
    # f1score = [0.73*0.95, 0.72, 0.73]
    # 2.5306122448979593
    # 1.8877551020408163
    # infer = [0.157,0.115,  0.081]
    # #infer=[2.5306122448979593*i for i in infer]
    # sr = [98,121.3, 210]
    '''
vgg  135.259ms    540M

fasterrcnn  45.161ms 163M

edsr:42.602ms          168M

resnet50 29.539ms    

mobile-net 10.922ms      21M
    '''
    #

    Reuse = [0,0, 0,0, 10.922]
    sr = [0,0, 0,29.539, 0]
    # sr=[1.8877551020408163*i for i in sr]
    # Reuse = [75,150*0.75,   150]

    # feature=[45*0.5,45*0.75,45]
    feature = [0,0,42.602, 0, 0]
    mm = [0,45.161, 0, 0, 0]
    #
    # drl=[135.259,0,0,0,0]

    Reuse = [0, 0,0, 10.922]
    sr = [0, 0,29.539, 0]
    # sr=[1.8877551020408163*i for i in sr]
    # Reuse = [75,150*0.75,   150]

    # feature=[45*0.5,45*0.75,45]
    feature = [0,42.602, 0, 0]
    mm = [45.161, 0, 0, 0]

    Reuse = [0, 0,0, 8.3]
    sr = [0, 0,5.7, 0]
    # sr=[1.8877551020408163*i for i in sr]
    # Reuse = [75,150*0.75,   150]

    # feature=[45*0.5,45*0.75,45]
    # feature = [0,1.31, 0, 0]
    feature = [0,1.2603109187036432, 0, 0]
    # mm =[ 0.34, 0, 0, 0]
    mm =[1.31, 0, 0, 0]



    Reuse = [0, 0,0, 9]
    sr = [0, 0,7, 0]
    # sr=[1.8877551020408163*i for i in sr]
    # Reuse = [75,150*0.75,   150]

    # feature=[45*0.5,45*0.75,45]
    # feature = [0,1.31, 0, 0]
    feature = [0, 1, 0, 0]
    # mm =[ 0.34, 0, 0, 0]
    mm =[1, 0, 0, 0]

    idx = 0
    # all=infer[idx]+sr[idx]+Reuse[idx]+feature[idx]+drl[idx]
    # print(infer[idx]/all,sr[idx]/all,Reuse[idx]/all,feature[idx]/all,drl[idx]/5/all)
    # resuse=[0.01,0,0]
    # labels = ["DRL", "Reuse", "Feature", "SR", "Infer"]  # 每个柱子的组成
    labels = ["VGG", "Faster R-CNN", "EDSR","ResNet-50","MobileNetV3",  "Infer"]  # 每个柱子的组成
    labels = ["NeuroScaler*","AccDecoder",  "Reducto", "BiSwift"]
    colors = ["06283D", "moccasin", "royalblue", "orchid"]  # 每个组成的颜色
    # colors = ["gold", "darkorange", "firebrick", "darkmagenta"]
    # colors = ["#A149FA", "#76BA99", "#FFD460", "#2D4059", "#EA5455"]  # 每个组成的颜色
    colors = ["#A149FA", "#76BA99", "#FFD460", "#2D4059", "#EA5455"]
    #             紫色            绿          黄          深蓝          红
    colors = ["#EA5455", "#2D4059", "#FFD460", "#76BA99", "#A149FA"]
    err_attr = {"elinewidth": 1, "ecolor": "black", "capsize": 6}
    other = {
        "title": "f1score and latency",  # 标题
        "xlabel": "Scheme",  # 横坐标名称
        "ylabel_left": "Streams",  # 纵坐标名称
        # "ylabel_left": "Swapping time/ms",  # 纵坐标名称
        "ylabel_right": "Latency(s)"
    }
    # std_err2 = [[0.3,0.3], 0.5*0.25, 0.45*0.25]
    # std_err2=[[0.1*0.4,0.03,0.025],[0.04,0.03,0.025]]
    xticks = np.arange(len(bars_name))

    fig, ax = plt.subplots(figsize=(5, 3))
    bar_width = 0.55
    # , yerr=std_err2,error_kw=err_attr
    # lns1 = ax.bar(xticks, f1score, width=bar_width, label=labels[0],error_kw=err_attr,color=colors[0],edgecolor='black', zorder=10)

    # ax2 = ax.twinx()
    xticks = np.arange(4)
    bot = np.array(4) * 0.0
    #
    # lns0 = ax.bar(xticks + bar_width / 2, Reuse, width=bar_width, label=labels[1], color=colors[1], bottom=bot,
    #               hatch="", edgecolor='black', zorder=4)
    # bot += Reuse
    # lns1 = ax.bar(xticks + bar_width / 2, sr, width=bar_width, label=labels[2], color=colors[2], bottom=bot,
    #               hatch="", edgecolor='black', zorder=2)
    # bot += sr
    # lns2 = ax.bar(xticks + bar_width / 2, feature, width=bar_width, label=labels[3], color=colors[3], bottom=bot, hatch="",
    #               edgecolor='black', zorder=3)
    # bot += feature
    #
    # lns3 = ax.bar(xticks + bar_width/2, drl, width=bar_width, label=labels[4], color=colors[4], bottom=bot, hatch="",edgecolor='black', zorder=4)
    # 下面这样是如果要图例中说明每个柱子的label  那么要一个一个画

    # lns0 = ax.bar(xticks + bar_width / 2, drl, width=bar_width, label=labels[0], color=colors[0], bottom=bot,
    #               hatch="", edgecolor='black', zorder=4)
    # bot += drl
    labels = ["NeuroScaler*", "AccDecoder", "Reducto", "BiSwift"]
    cb={
        "bi":"#EA5455", #红色
        "ac":"#2D4059",  # 黑色
        "re": "#76BA99", #绿色
        "ne":"#FFD460", # 黄色
    }
    lns01 = ax.bar(xticks + bar_width / 2, mm, width=bar_width, label=labels[0], color=cb["ne"], bottom=bot,
                  hatch="", edgecolor='black', zorder=4)
    bot += mm
    lns1 = ax.bar(xticks + bar_width / 2, feature, width=bar_width, label=labels[1], color=cb["ac"], bottom=bot,
                  hatch="", edgecolor='black', zorder=2)
    bot += feature
    lns2 = ax.bar(xticks + bar_width / 2, sr, width=bar_width, label=labels[2], color=cb["re"], bottom=bot, hatch="",
                  edgecolor='black', zorder=3)
    bot += sr

    lns3 = ax.bar(xticks + bar_width/2, Reuse, width=bar_width, label=labels[3], color=cb["bi"], bottom=bot, hatch="",edgecolor='black', zorder=4)




    # lns = ax.bar(xticks + bar_width/2, drl, width=bar_width, label=labels[0], color=colors[0], bottom=bot, hatch="",edgecolor='black', zorder=4)
    # bot += drl
    # lns5 = ax2.bar(xticks + bar_width, resuse, width=bar_width, label=labels[4], color=colors[4], bottom=bot,hatch="",edgecolor='black', zorder=5)
    # bot += resuse
    ax.set_ylabel(other["ylabel_left"], fontsize=20)
    # ax2.set_ylabel(other["ylabel_right"], fontsize=23)
    ax.set_ylim(0,10)
    # ax.set_ylim(0, 0.2)
    ax.tick_params(labelsize=15)
    # ax2.tick_params(labelsize=18)

    # lns = [lns,lns3, lns2,lns1,lns0]
    # labs = [l.get_label() for l in lns]
    # ax2.legend(lns, labs, fontsize=18)
    # ax.legend(lns, labs, fontsize=15,labelspacing=1.5,handlelength=1.5,handletextpad=0.3, ncol=1,handleheight=1,bbox_to_anchor=(1.02, 0.85),frameon=False)
    # ax2.set_title(other["title"], fontsize=20)
    # ax2.set_xlabel(other["xlabel"])
    # ax.set_xticks(xticks + bar_width / 2)
    # ax.set_xticklabels(bars_name, fontsize=20)
    # 网格线
    ax.text(0.15,1.2, "1x",fontsize=15,zorder=30)
    ax.text(1.15, 1.2, "1x", fontsize=15, zorder=30)
    ax.text(2.15, 7.2, "7x", fontsize=15, zorder=30)
    ax.text(3.15, 9.2, "9x", fontsize=15, zorder=30)
    plt.xticks([])
    #ax.spines['right'].set_visible(False)
    #ax.spines['top'].set_visible(False)
    # ax.set_xlim(-0.3, 2.8)
    plt.rcParams['hatch.linewidth'] = 2
    ax.grid(axis='y', zorder=-1)
    lns=[lns01,lns1,lns2,lns3]
    labs = [l.get_label() for l in lns]
    ax.legend(fontsize=15)
    # ax.legend(lns, labs, fontsize=18, labelspacing=1.5, handlelength=1.5, handletextpad=0.3, ncol=3, handleheight=1,
    #           bbox_to_anchor=(1.2, 1.25), frameon=False)

    plt.tight_layout()  # 让图片适应画布大小
    plt.savefig("throughput.svg")
    plt.savefig("throughput.pdf")
    plt.show()




"""

######################################3fig 带宽图
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    font1 = {'family': 'Arial',
             'weight': 'normal',
             'size': 15,
             }
    font2 = {'family': 'Arial',
             'weight': 'normal',
             'size': 20,
             }
    # plt.style.use('ggplot')
    bars_name = ["270P" + "\n" + "x4", "360P\nx3", "540P\nx2"]  # 柱子名称
    # bars_name = ["270P" + "\n" + "x4", "360P\nx3", "540P\nx2"]  # 柱子名称
    # f1score = [0.73*0.95, 0.72, 0.73]
    # 2.5306122448979593
    # 1.8877551020408163
    # infer = [0.157,0.115,  0.081]
    # #infer=[2.5306122448979593*i for i in infer]
    # sr = [98,121.3, 210]
    '''
vgg  135.259ms    540M

fasterrcnn  45.161ms 163M

edsr:42.602ms          168M

resnet50 29.539ms

mobile-net 10.922ms      21M
    '''
    #

    Reuse = [0,0, 0,0, 10.922]
    sr = [0,0, 0,29.539, 0]
    # sr=[1.8877551020408163*i for i in sr]
    # Reuse = [75,150*0.75,   150]

    # feature=[45*0.5,45*0.75,45]
    feature = [0,0,42.602, 0, 0]
    mm = [0,45.161, 0, 0, 0]
    #
    # drl=[135.259,0,0,0,0]

    Reuse = [0, 0,0, 10.922]
    sr = [0, 0,29.539, 0]
    # sr=[1.8877551020408163*i for i in sr]
    # Reuse = [75,150*0.75,   150]

    # feature=[45*0.5,45*0.75,45]
    feature = [0,42.602, 0, 0]
    mm = [45.161, 0, 0, 0]



    total=3.71
    Reuse = [0, 0,0, 2.29/total]
    sr = [0, 0,2.93/total, 0]
    # sr=[1.8877551020408163*i for i in sr]
    # Reuse = [75,150*0.75,   150]

    # feature=[45*0.5,45*0.75,45]
    feature = [0,2.93/total, 0, 0]
    mm =[ 3.71/total, 0, 0, 0]
    print(mm)


    idx = 0
    # all=infer[idx]+sr[idx]+Reuse[idx]+feature[idx]+drl[idx]
    # print(infer[idx]/all,sr[idx]/all,Reuse[idx]/all,feature[idx]/all,drl[idx]/5/all)
    # resuse=[0.01,0,0]
    # labels = ["DRL", "Reuse", "Feature", "SR", "Infer"]  # 每个柱子的组成
    labels = ["VGG", "Faster R-CNN", "EDSR","ResNet-50","MobileNetV3",  "Infer"]  # 每个柱子的组成
    labels = ["NeuroScaler*","AccDecoder",  "Reducto", "BiSwift"]
    colors = ["06283D", "moccasin", "royalblue", "orchid"]  # 每个组成的颜色
    # colors = ["gold", "darkorange", "firebrick", "darkmagenta"]
    # colors = ["#A149FA", "#76BA99", "#FFD460", "#2D4059", "#EA5455"]  # 每个组成的颜色
    colors = ["#A149FA", "#76BA99", "#FFD460", "#2D4059", "#EA5455"]
    #             紫色            绿          黄          深蓝          红
    colors = ["#EA5455", "#2D4059", "#FFD460", "#76BA99", "#A149FA"]

    err_attr = {"elinewidth": 1, "ecolor": "black", "capsize": 6}
    other = {
        "title": "f1score and latency",  # 标题
        "xlabel": "Scheme",  # 横坐标名称
        "ylabel_left": "Normalized BW cost",  # 纵坐标名称
        # "ylabel_left": "Swapping time/ms",  # 纵坐标名称
        "ylabel_right": "Latency(s)"
    }
    # std_err2 = [[0.3,0.3], 0.5*0.25, 0.45*0.25]
    # std_err2=[[0.1*0.4,0.03,0.025],[0.04,0.03,0.025]]
    xticks = np.arange(len(bars_name))

    fig, ax = plt.subplots(figsize=(5, 3))
    bar_width = 0.55
    # , yerr=std_err2,error_kw=err_attr
    # lns1 = ax.bar(xticks, f1score, width=bar_width, label=labels[0],error_kw=err_attr,color=colors[0],edgecolor='black', zorder=10)

    # ax2 = ax.twinx()
    xticks = np.arange(4)
    bot = np.array(4) * 0.0
    #
    # lns0 = ax.bar(xticks + bar_width / 2, Reuse, width=bar_width, label=labels[1], color=colors[1], bottom=bot,
    #               hatch="", edgecolor='black', zorder=4)
    # bot += Reuse
    # lns1 = ax.bar(xticks + bar_width / 2, sr, width=bar_width, label=labels[2], color=colors[2], bottom=bot,
    #               hatch="", edgecolor='black', zorder=2)
    # bot += sr
    # lns2 = ax.bar(xticks + bar_width / 2, feature, width=bar_width, label=labels[3], color=colors[3], bottom=bot, hatch="",
    #               edgecolor='black', zorder=3)
    # bot += feature
    #
    # lns3 = ax.bar(xticks + bar_width/2, drl, width=bar_width, label=labels[4], color=colors[4], bottom=bot, hatch="",edgecolor='black', zorder=4)
    # 下面这样是如果要图例中说明每个柱子的label  那么要一个一个画

    # lns0 = ax.bar(xticks + bar_width / 2, drl, width=bar_width, label=labels[0], color=colors[0], bottom=bot,
    #               hatch="", edgecolor='black', zorder=4)
    # bot += drl
    cb={
        "bi":"#EA5455", #红色
        "ac":"#2D4059",  # 黑色
        "re": "#76BA99", #绿色
        "ne":"#FFD460", # 黄色
    }
    labels = ["NeuroScaler*", "AccDecoder", "Reducto", "BiSwift"]
    lns01 = ax.bar(xticks + bar_width / 2, mm, width=bar_width, label=labels[0], color=cb["ne"], bottom=bot,
                  hatch="", edgecolor='black', zorder=4)
    bot += mm
    lns1 = ax.bar(xticks + bar_width / 2, feature, width=bar_width, label=labels[1], color=cb["ac"], bottom=bot,
                  hatch="", edgecolor='black', zorder=2)
    bot += feature
    lns2 = ax.bar(xticks + bar_width / 2, sr, width=bar_width, label=labels[2], color=cb["re"], bottom=bot, hatch="",
                  edgecolor='black', zorder=3)
    bot += sr

    lns3 = ax.bar(xticks + bar_width/2, Reuse, width=bar_width, label=labels[3], color=cb["bi"], bottom=bot, hatch="",edgecolor='black', zorder=4)




    # lns = ax.bar(xticks + bar_width/2, drl, width=bar_width, label=labels[0], color=colors[0], bottom=bot, hatch="",edgecolor='black', zorder=4)
    # bot += drl
    # lns5 = ax2.bar(xticks + bar_width, resuse, width=bar_width, label=labels[4], color=colors[4], bottom=bot,hatch="",edgecolor='black', zorder=5)
    # bot += resuse
    ax.set_ylabel(other["ylabel_left"], fontsize=20)
    # ax2.set_ylabel(other["ylabel_right"], fontsize=23)
    # ax.set_ylim(0.65, 0.76)
    # ax.set_ylim(2, 4.5)
    ax.set_ylim(0.4, 1.3)
    ax.tick_params(labelsize=15)
    # ax2.tick_params(labelsize=18)

    # lns = [lns,lns3, lns2,lns1,lns0]
    # labs = [l.get_label() for l in lns]
    # ax2.legend(lns, labs, fontsize=18)
    # ax.legend(lns, labs, fontsize=15,labelspacing=1.5,handlelength=1.5,handletextpad=0.3, ncol=1,handleheight=1,bbox_to_anchor=(1.02, 0.85),frameon=False)
    # ax2.set_title(other["title"], fontsize=20)
    # ax2.set_xlabel(other["xlabel"])
    # ax.set_xticks(xticks + bar_width / 2)
    # ax.set_xticklabels(bars_name, fontsize=20)
    # 网格线
    plt.xticks([])
    #ax.spines['right'].set_visible(False)
    #ax.spines['top'].set_visible(False)
    # ax.set_xlim(-0.3, 2.8)
    plt.rcParams['hatch.linewidth'] = 2
    ax.grid(axis='y', zorder=-1)
    lns=[lns01,lns1,lns2,lns3]
    labs = [l.get_label() for l in lns]
    # ax.legend(fontsize=15,ncol=2,  bbox_to_anchor=(0.99, 1.25),columnspacing=0.3,labelspacing=.35)
    ax.legend(fontsize=15,ncol=1,columnspacing=0.3,labelspacing=.35,loc='best')
    # ax.legend(lns, labs, fontsize=18, labelspacing=1.5, handlelength=1.5, handletextpad=0.3, ncol=3, handleheight=1,
    #           bbox_to_anchor=(1.2, 1.25), frameon=False)
    # ax.text(0.075,3.8, "3.71",fontsize=15,zorder=30)
    # ax.text(1.05, 3., "2.93", fontsize=15, zorder=30)
    # ax.text(2.05, 3., "2.93", fontsize=15, zorder=30)
    # ax.text(3.05, 2.33, "2.29", fontsize=15, zorder=30)
    # ax.spines['right'].set_visible(False)
    # ax.spines['top'].set_visible(False)
    plt.tight_layout()  # 让图片适应画布大小
    plt.savefig("baseline_band.svg")
    plt.savefig("baseline_band.pdf")
    plt.show()


"""