# coding=utf-8
import math


def inverse_kin(Sx, Sy, Sz, s):
    x1 = float(Sx)
    y = float(Sy)
    z1 = float(Sz)
    L13 = 84.72
    L2 = 41.04
    L5 = 200
    L6 = 214.8
    L7 = 45
    DX = 300
    DZ=50

    q1 = 17.657917590920615
    q2 = 152.68267192378207
    q3 = 0.0

    x = x1 + DX
    z=z1+DZ
    jj3 = math.atan2(y, x)
    a = (x ** 2 + y ** 2) ** 0.5 - L2 - L7
    b = z - L13
    c = (a ** 2 + b ** 2) ** 0.5
    sita2 = math.atan2(b, a)
    sita1 = math.acos((L5 ** 2 + c ** 2 - L6 ** 2) / (2 * L5 * c))
    jj2 = math.pi / 2 - sita1 - sita2
    sita3 = math.acos((L5 ** 2 + L6 ** 2 - c ** 2) / (2 * L5 * L6))
    jj1 = sita3 - jj2-math.atan2(28,72)
    j1d = jj1 * 180 / math.pi
    j2d = jj2 * 180 / math.pi
    j3d = jj3 * 180 / math.pi
    return -10 * (j1d * 45 / 11 - q1), -10 * (j2d * 45 / 11 - q2), 10 * (j3d * 45 / 21 - q3), s


#     return (j1d*45/11), j2d*45/11,(j3d*45/21),s


# j1小臂角度（0,180）.
# j2大臂角度（0,100）.
# j3底座角度（-180,180）.
def positive(j1, j2, j3):
    q1 = 17.657917590920615
    q2 = 152.68267192378207
    q3 = 0.0
    j1d = (-j1 + q1) * 11 / 45
    j2d = (-j2 + q2) * 11 / 45
    j3d = (j3 + q3) * 21 / 45
    L13 = 84.72
    L2 = 41.04
    L5 = 200
    L6 = 214.8
    L7 = 45
    DX = 300
    DZ=50

    jj1 = j1d * math.pi / 180+math.atan2(28,72)
    jj2 = j2d * math.pi / 180
    jj3 = j3d * math.pi / 180
    L = L2 + L5 * math.sin(jj2) + L6 * math.sin(jj1) + L7
    x1 = L * math.cos(jj3)
    y = L * math.sin(jj3)
    z1 = L13 + L5 * math.cos(jj2) - L6 * math.cos(jj1)
    x = x1 - DX
    z=z1-DZ
    return x, y, z


def transpos_kin(data):
    theata0 = float(data[0:6])
    theata1 = float(data[6:12])
    theata2 = float(data[12:18])
    # 这里还要吧电机转换为关节角度
    j1 = theata0;
    j2 = theata1;
    j3 = theata2
    print ("{},.{},{}".format(j1, j2, j3))
    x, y, z = positive(j1, j2, j3)

    return x, y, z


def calcuInLine(startPos, dstPos):
    deltax = [0 for i in range(3)]
    for i in range(3):
        deltax[i] = dstPos[i] - startPos[i]
    lenthx = 0.2*(deltax[0] ** 2 + deltax[1] ** 2 + deltax[2] ** 2) ** 0.5
    dirx = [deltax[i] / lenthx for i in range(3)]

    rstlist = []
    for i in range(100000):
        if(dirx[0]<=0):
            if startPos[0]+i * dirx[0]<dstPos[0]-1:
                break
        else:
            if startPos[0]+i * dirx[0]>dstPos[0]+1:
                break
        if(dirx[1]<=0):
            if startPos[1]+i * dirx[1]<dstPos[1]-1:
                break
        else:
            if startPos[1]+i * dirx[1]>dstPos[1]+1:
                break
        if(dirx[2]<=0):
            if startPos[2]+i * dirx[2]<dstPos[2]-1:
                break
        else:
            if startPos[2]+i * dirx[2]>dstPos[2]+1:
                break
        rstlist.append([startPos[0]+i * dirx[0], \
                        startPos[1]+i * dirx[1],startPos[2]+ i * dirx[2]])

    return rstlist




#(104.5918037564657, 152.68267192378207, 0.0, 0)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(calcuInLine([0, 0, 0], [100, 100, 100]))
    (j1,j2,j3,s)=(inverse_kin(0,0,0,0))
    print(positive(j1, j2, j3))
    print(inverse_kin(0,0,0,0))




