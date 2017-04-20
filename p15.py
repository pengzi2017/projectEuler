#I want to solve the problem by simulating, but the result isn't that good.
import random

def move(x, y,degree):
    global way
    route = set()
    for i in range(0, degree):
        way = ""
        p0 = [0, 0]
        while p0 != [x, y]:
            if p0[0] == x:
                p0[1] += 1
                way += 'y'
            elif p0[1] == y:
                p0[0] += 1
                way += 'x'
            else:
                ran = random.randint(0, 1)
                if ran == 0:
                    p0[0] += 1
                    way += 'x'
                elif ran == 1:
                    p0[1] += 1
                    way += 'y'
        route.add(way)
    print(route)
    print('模拟后得到%s种路线'%len(route))

time=int(input('请输入模拟寻路的次数（关系到最终结果的准确度，建议在实际范围内设得大些）：'))
move(2, 2,time)
