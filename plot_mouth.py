import numpy as np
import matplotlib.pyplot as plt
# import math
from PIL import Image, ImageDraw

# annotate index number for lip points
def add_index(ax,text,x,y,v_offset=3,color='black'):
    ax.annotate(text,
                xy=(x, y),
                xytext=(0, v_offset),  # 3 points vertical offset
                textcoords='offset points',
                ha='center', # ha = 'left',
                va='bottom',
                color=color
               )

# draw height line
def draw_line(ax,x1,y1,x2,y2,color='black'):
    ax.annotate('', # empty text
                xy=(x1, y1),
                xytext=(x2, y2),
                ha='center', # ha = 'left',
                va='bottom',
                arrowprops=dict(edgecolor=color,arrowstyle="<->",linestyle='--') # facecolor=color,
               )

def plot_mouth():
    # obama open mouth
    top_lip = [(181, 359), (192, 339), (211, 332), (225, 336), (243, 333), (271, 342), (291, 364), (282, 363), (242, 346), (225, 347), (211, 345), (188, 358)]
    bottom_lip = [(291, 364), (270, 389), (243, 401), (223, 403), (207, 399), (190, 383), (181, 359), (188, 358), (210, 377), (225, 381), (243, 380), (282, 363)]

    # close mouth
    # top_lip = [(151, 127), (157, 126), (163, 126), (168, 127), (172, 127), (178, 127), (185, 129), (182, 129), (172, 130), (167, 130), (163, 129), (153, 127)]
    # bottom_lip = [(185, 129), (177, 133), (171, 135), (166, 135), (161, 134), (156, 132), (151, 127), (153, 127), (162, 129), (167, 130), (171, 130), (182, 129)]

    x1 = [ x for x,y in top_lip]
    y1 = [ y for x,y in top_lip]
    x2 = [ x for x,y in bottom_lip]
    y2 = [ y for x,y in bottom_lip]

    fig, ax = plt.subplots()
    ax.plot(x1, y1,color='green', marker='o')
    ax.plot(x2, y2,color='blue', marker='*')

    plt.gca().invert_yaxis()

    # add index number for top lip
    for i in range(12):
        x = top_lip[i][0]
        y = top_lip[i][1]
        add_index(ax,str(i),x,y,color='green',v_offset=5)

    # add index number for bottom lip
    for i in range(12):
        x = bottom_lip[i][0]
        y = bottom_lip[i][1]
        add_index(ax,str(i),x,y,color='blue',v_offset=-20)

    # draw line - top lip
    for i in [2,3,4]:
        x1 = top_lip[i][0]
        y1 = top_lip[i][1]
        x2 = top_lip[12-i][0]
        y2 = top_lip[12-i][1]
        draw_line(ax,x1,y1,x2,y2,color='green')

    # draw line - bottom lip
    for i in [2,3,4]:
        x1 = bottom_lip[i][0]
        y1 = bottom_lip[i][1]
        x2 = bottom_lip[12-i][0]
        y2 = bottom_lip[12-i][1]
        draw_line(ax,x1,y1,x2,y2,color='blue')

    # draw line - mouth
    for i in [8,9,10]:
        x1 = top_lip[i][0]
        y1 = top_lip[i][1]
        x2 = bottom_lip[18-i][0]
        y2 = bottom_lip[18-i][1]
        draw_line(ax,x1,y1,x2,y2,color='black')

    # annotate height
    # top lip height
    x = (top_lip[4][0] + top_lip[8][0])/2
    y = (top_lip[4][1] + top_lip[8][1])/2
    ax.annotate('lip height',
                xy=(x, y), xytext=(5,0), textcoords='offset points',
                ha='left', va='top',color='green')

    # bottom lip height
    x = (bottom_lip[2][0] + bottom_lip[10][0])/2
    y = (bottom_lip[2][1] + bottom_lip[10][1])/2
    ax.annotate('lip height',
                xy=(x, y), xytext=(5,0), textcoords='offset points',
                ha='left', va='bottom',color='blue')

    # mouth height
    x = (top_lip[8][0] + bottom_lip[10][0])/2
    y = (top_lip[8][1] + bottom_lip[10][1])/2
    ax.annotate('mouth height',
                xy=(x, y), xytext=(5,0), textcoords='offset points',
                ha='left', va='bottom',color='black')

    plt.show()
    # fig.savefig("test.png")

if __name__ == '__main__':
    plot_mouth()
