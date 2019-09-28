from graph import *
import numpy as np

windowSize(1000,6000)
canvasSize(1000,600)
def ellips( a, b, x0, y0):
    """
    ellips_
    :param a : -size_gorizontal_line
    :param b : -size_vertical_line
    :param x0: -x coordinate_of_ellips_center
    :param y0: -y coordinate_of_ellips_center
    """
    p = ([])
    a=abs(a)
    b=abs(b)
    for x in np.arange(-(a) + x0, (a) + x0, 1):
        p.append([x, np.sqrt(b**2*(1-(x-x0)**2/a**2))+y0])
    for x in np.arange((a) + x0, -(a) + x0, -1):
        p.append([x, -np.sqrt(b**2*(1-(x-x0)**2/a**2))+y0])
    polygon(p)

def bear(x0,y0,N):
    ellips(70/N,40/N,230/N+x0,90/N+y0)#head
    ellips( 100/N, 200/N, 300/N+x0,300/N+y0)#body
    ellips(70/N,60/N,190/N+x0,450/N+y0)#bigger_leg
    ellips(60/N,20/N,120/N+x0,500/N+y0)#small_leg

    ellips(10/N,10/N,280/N+x0,60/N+y0)#eyer
    ellips(40/N,20/N,200/N+x0,200/N+y0)#hand
    line(160/N+x0,90/N+y0,170/N+x0,95/N+y0)#lips_nearest_to_nose
    line(170/N+x0,95/N+y0,220/N+x0,95/N+y0)#lips_not_nearest
    brushColor('black')
    ellips(5/N,5/N,160/N+x0,80/N+y0)#nose
    ellips(5/N,5/N,240/N+x0,70/N+y0)#eye
def fucking_fish(x0,y0,N):
    N=N/2
    brushColor('red')
    polygon([(x0+31/N,y0+9/N),(x0+45/N,y0),(x0+39/N,y0+20/N),(x0+31/N,y0+9/N)])

    line(x0-3/N,y0+9/N,x0-5/N,y0)
    brushColor('red')
    polygon([(x0-3/N,y0+9/N), (x0-5/N,y0-10/N),(x0+5/N,y0-7/N),(x0,y0+9/N),(x0-3/N,y0+9/N)])
    polygon([(x0-5/N,y0+9/N),(x0-10/N,y0+30/N),(x0,y0+26/N),(x0-2/N,y0+9/N),(x0-5/N,y0+9/N)])
    polygon([(x0+5/N,y0+9/N),(x0+5/N,y0+30/N),(x0+10/N,y0+26/N),(x0+8/N,y0+9/N),(x0+5/N,y0+9/N)])

    brushColor('grey')
    ellips(30/N,10/N,x0+5/N,y0+10/N)

    brushColor('blue')
    ellips(5/N,5/N,x0-7/N,y0+9/N)
    brushColor('white')
    ellips(2/N,2/N,x0-7/N,y0+9/N)

def lake(x0,y0,N):
    brushColor('grey')
    ellips(100/N,30/N,150/N+x0,520/N+y0)#outside_contr
    brushColor('green')
    ellips(90/N,25/N,150/N+x0,525/N+y0)#inside_conter

def fishing_rod(x0,y0,N):
    """
    parts of fishing rod from bears hand to the lake
    :param x0: смещение по Х
    ;param y0: смещение по У
    """
    penSize(3)
    line(440/N+x0,300/N+y0,410/N+x0,220/N+y0)
    line(410/N+x0,220/N+y0,320/N+x0,120/N+y0)
    line(320/N+x0,120/N+y0,280/N+x0,80/N+y0)
    line(280/N+x0,y0+80/N,x0+200/N,y0+50/N)
    penSize(1)
    line(200/N+x0,50/N+y0,200/N+x0,510/N+y0)

def picture(x0,y0,N):
    fishing_rod(0+x0,y0+0,N)
    bear(250/N+x0,50/N+y0,N)
    lake(0+x0,0+y0,N)

    fucking_fish(90/N+x0,570/N+y0,N)
    fucking_fish(140/N+x0,560/N+y0,N)
    fucking_fish(170/N+x0,585/N+y0,N)
    fucking_fish(100/N+x0,450/N+y0,N)
    fucking_fish(140/N+x0,450/N+y0,N)
brushColor('blue')
rectangle (0, 0,2000 , 300)
brushColor('white')
rectangle (0,300,2000,2000)
picture(300,300,2)
picture(50,200,4)
picture(500,400,1)
picture(570,200,4)

brushColor('yellow')
ellips(100,100,600,100)
brushColor('blue')
ellips(90,90,600,100)
brushColor('yellow')
polygon([(600,-1),(600,200),(610,200),(610,0)])
polygon([(500,100),(700,100),(700,110),(500,110)])
run()
