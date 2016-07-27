import csv
from math import sqrt,pow

f = open('input.csv')

pointer = csv.reader(f, delimiter=',')

temp = []

for i in pointer:
    temp.append(i)

dis_list = []
slop_list = []

for i in range(len(temp)-1):
    coor1 = temp[i]
    coor2 = temp[i+1]
    dis = sqrt(pow((float(coor2[0]) - float(coor1[0])),2)+pow((float(coor2[1]) - float(coor1[1])), 2))
#    print dis
    dis_list.append(dis)
#    print("coor2[1]: %s" %coor2[1])
#    print("coor1[1]: %s" %coor1[1])
#    print("coor2[0]: %s" %coor2[0])
#    print("coor1[0]: %s" %coor1[0])
#    print "next points"
#    slop = float()
#    slop = float((float(coor2[1]) - float(coor1[1]))/(float(coor2[0]) - float(coor1[0])))
#    slop_list.append(slop)

P_list = []
lenght=5
currentp=0;
i=0;
section= 5
while(i<(len(temp)-1)):
    currentp=lenght+currentp;
    if(currentp>dis_list[i]):
        i = i+1
#        print(i)
        currentp=0;
        continue
    # Center points
    x_new = float(float(temp[i+1][0]) - float(temp[i][0]))
    y_new = float(float(temp[i+1][1]) - float(temp[i][1]))
    u = float(sqrt(float(pow(x_new, 2)) + float(pow(y_new, 2))))
#    print("x_new: %s, y_new: %s" %(x_new, y_new))
#    print("u: %s" %u)
    x_new = (float(x_new/u) * currentp) + float(temp[i][0])
    y_new = (float(y_new/u) * currentp) + float(temp[i][1])

#    print("%s, %s" %(x_new, y_new))
    x_new1 = float(x_new - float(temp[i][0]))
    x_new2 = float(float(temp[i+1][0]) - x_new)
    y_new1 = float(y_new - float(temp[i][1]))
    y_new2 = float(float(temp[i+1][1]) - y_new)
#   print("x_new1: %s, x_new2: %s, y_new1: %s, y_new2: %s" %(x_new1, x_new2, y_new1, y_new2))
    if x_new1 == 0 and x_new2 == 0:
        P1y = currentp
        P1x = section
    elif y_new1 == 0 and y_new2 == 0:
        P1y = section
        P1x = currentp
    else:
        c = y_new2/x_new2
        d = c * y_new + x_new * float(temp[i+1][0])
        check = float(y_new1 - (x_new1 * c))
        if check != 0:
            print("new")
            P1y = ((y_new * y_new1) + (x_new - d) * x_new1)/check
            P1x = d - P1y * c
            P1x = float(float(P1x) - x_new)
            P1y = float(float(P1y) - float(y_new))
            u = float(sqrt(float(pow(P1x, 2)) + float(pow(P1y, 2))))
#    print("x_new: %s, y_new: %s" %(x_new, y_new))
#    print("u: %s" %u)
            P1x = (float(P1x/u) * section) + float(x_new)
            P1y = (float(P1y/u) * section) + float(y_new)
            print("%s, %s" % (P1x, P1y))

