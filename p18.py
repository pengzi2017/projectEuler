#beta version

with open('p18_data.py','r') as f:
    text=f.readlines()

line=line.split() for line in text 
int(num) for num in [row for row in line]

s=0
x,y=0,0
for x in range(15):
    if line(x)[y]>= line(x)[y+1]：
        node=y
        maxer=line(x)[y]
    else:
        node=y+1
        maxer=line(x)[y+1]
    s+=maxer
    x,y=x+1,node

print(s)


