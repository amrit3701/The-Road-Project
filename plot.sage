import csv

temp = []
f = open('input.csv')
pointer = csv.reader(f, delimiter=',')
parsed = ((float(row[0]), float(row[1]))
            for row in pointer)
for i in parsed:
    temp.append(i)

a = []
f = open('output.csv')
pointer = csv.reader(f, delimiter=',')
parsed = ((float(row[0]), float(row[1]))
            for row in pointer)
for i in parsed:
    a.append(i)

b = []
f = open('output2.csv')
pointer = csv.reader(f, delimiter=',')
parsed = ((float(row[0]), float(row[1]))
            for row in pointer)
for i in parsed:
    b.append(i)

z1 = point(temp, color="red", size=10, legend_label="input points")
#z2 = line(temp, color="red", thickness=2)

z3 = point(a, color="blue", size=5, legend_label="distance points")
#z4 = line(a, color="blue", thickness=1)

z5 = point(b, color="black", size=15, legend_label="section points")

z=z1+z3+z5
z.set_legend_options(back_color=(0.9,0.9,0.9), shadow=False, loc=(.1,.9))

z.save('plotting.png')
