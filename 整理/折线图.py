import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patches as mpatches
import numpy as np

import pandas as pd

from colors import (colors,font1,font2,fls,fs)

if __name__ == '__main__':
    labels = ["f1score", "decode", "SR", "infer","reuse"]   # 每个柱子的组成
    other = {
        "title": "",  # 标题
        "xlabel": "Scheme",  # 横坐标名称
        "ylabel_left": "F1-score",  # 纵坐标名称
        "ylabel_right": "Size(KB)"
    }
    fig, ax = plt.subplots(figsize=(9, 3))
    x=np.arange(0,78)
    np.random.seed(0)
    y1=np.random.rand(78)
    y2 = np.random.rand(78)
    y3 = np.random.rand(78)
    y4 = np.random.rand(78)
    l1,=ax.plot(x, y1,color=colors["blue"],linewidth=3.0, linestyle='-', markeredgewidth=0.01, label='BiSwift', zorder=25)
    l2,=ax.plot(x, y2, color=colors["red"],linewidth=3.0,linestyle='--', markeredgewidth=0.01, label='AccDecoder', zorder=20)
    l3,=ax.plot(x, y3,color=colors["yellow"],linewidth=3.0, linestyle='--', markeredgewidth=0.01, label='Reducto', zorder=20)
    l4, = ax.plot(x, y4, color=colors["green"],linewidth=3.0, linestyle='--', markeredgewidth=0.01, label=f'NeuroScaler*', zorder=20)

    ax.set_ylabel(other["ylabel_left"], fontsize=fls)
    #ax2.set_ylabel(other["ylabel_right"], fontsize=14)
    ax.set_ylim(0.2, 1.0)
    ax.set_xlim(0., 80)
    #ax2.set_ylim(0, 350)
    ax.tick_params(labelsize=fs)
    #lns = [lns1, lns2, lns3, lns4,lns5]
    # labs = [l.get_label() for l in lns]
    # #ax2.legend(lns, labs, fontsize=18)
    #ax2.legend( fontsize=14.5)
    #ax2.set_title(other["title"], fontsize=1200)
    # ax2.set_xlabel(other["xlabel"])
    #ax2.set_xticks(xticks + bar_width/2)
    #ax.set_xticklabels(bars_name,fontsize=20)
     # 网格线
    ax.set_xlabel('Chunk index',font2)

    # 下面注释掉的这些是为了双轴，首先将所有轴的图例统一放到一起
    # lines = []
    # labels = []
    # axLine, axLabel = ax.get_legend_handles_labels()
    # lines.extend(axLine)
    # labels.extend(axLabel)
    #axLine, axLabel = ax2.get_legend_handles_labels()
    #lines.extend(axLine)
    #labels.extend(axLabel)
    #  plt.legend(lines, labels,ncol=2,fontsize=fls)
    ax.legend(fontsize=15, bbox_to_anchor=(1, 1))

    # border_color = mcolors.to_rgb('darkgray')
    # border_color = tuple(c * 0.5 for c in border_color)
    # lns = [l1, l2, l3,l4]
    # labs = [l.get_label() for l in lns]
    # # plt.legend(lns, labs,handlelength=2, handleheight=1,edgecolor=border_color, loc='upper right',
    # #            labelspacing=1.25, frameon=False,fontsize=18,
    # #            prop=font1,ncol=1,bbox_to_anchor=(1, 1.))
    # plt.legend(lns, labs, handlelength=2, handleheight=1, edgecolor=border_color,
    #            labelspacing=1.25, frameon=False, fontsize=18,
    #            prop=font1, ncol=1, bbox_to_anchor=(1, 1.))



    # plt.legend(lns, labs,handlelength=2, handleheight=1,edgecolor=border_color, loc='best',
    #            labelspacing=1.25, frameon=False,fontsize=20,
    #            prop=font1,ncol=3)
    # plt.rcParams['hatch.linewidth'] = 2
    ax.tick_params(labelsize=fs)
    #ax.grid(axis='y', zorder=1)
    plt.tight_layout()  # 让图片适应画布大小
    plt.savefig("折线.png")
    plt.show()