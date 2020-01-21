# 导入所需模块
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from lxml import etree
import base64
import urllib
from create_p import *
def make(jj):
    if jj == "人工智能":
        j = "Rjob"
    elif jj == "大数据":
        j = "Djob"
    elif jj == "嵌入式":
        j = "Jjob"
    elif jj == "Python":
        j = "Pjob"
    zt(j)
    buf = BytesIO()
    plt.savefig(buf)
    plot_data = buf.getvalue()

    com(j)
    bu = BytesIO()
    plt.savefig(bu)
    plot_data1 = bu.getvalue()

    jt(j)
    # figure 保存为二进制文件
    buffer = BytesIO()
    plt.savefig(buffer)
    plot_data2 = buffer.getvalue()

    ct(j)
    # figure 保存为二进制文件
    buff = BytesIO()
    plt.savefig(buff)
    plot_data3 = buff.getvalue()

    nn(j)
    # figure 保存为二进制文件
    buffe = BytesIO()
    plt.savefig(buffe)
    plot_data4 = buffe.getvalue()
    return plot_data, plot_data1, plot_data2,plot_data3,plot_data4