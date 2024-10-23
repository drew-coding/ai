import math
def distance(x1,y1,x2,y2):
    dist=math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))
    return dist
def sumofDistance(x1,y1,px1,py1,px2,py2,px3,py3,px4,py4):
    d1=distance(x1,y1,px1,py1)
    d2=distance(x1,y1,px2,py2)
    d3=distance(x1,y1,px3,py3)
    d4=distance(x1,y1,px4,py4)
    return d1+d2+d3+d4
def newDistance(x1,y1,p1,p2,p3,p4):
    d1=[x1,y1]
    d1temp=sumofDistance(x1,y1,p1[0],p1[1],p2[0],p2[1],p3[0],p3[1],p4[0],p4[1])
    d1.append(d1temp)
    return d1
def newPoints(minimum,d1,d2,d3,d4):
    if d1[2]==minimum:
        return [d1[0],d1[1]]
    elif d2[2]==minimum:
        return [d2[0],d2[1]]
    elif d3[2]==minimum:
        return [d3[0],d3[1]]
    elif d4[2]==minimum:
        return [d4[0],d4[1]]
    
increment=0.5
startingPoint=[1,1]
p1=[1,5]
p2=[6,4]
p3=[5,2]
p4=[2,1]

SD=sumofDistance(startingPoint[0],startingPoint[1],p1[0],p1[1],p2[0],p2[1],p3[0],p3[1],p4[0],p4[1])
i=1
flag=True
while flag==True:
    d1=newDistance(startingPoint[0]+increment,startingPoint[1],p1,p2,p3,p4)
    d2=newDistance(startingPoint[0]-increment,startingPoint[1],p1,p2,p3,p4)
    d3=newDistance(startingPoint[0],startingPoint[1]+increment,p1,p2,p3,p4)
    d4=newDistance(startingPoint[0],startingPoint[1]-increment,p1,p2,p3,p4)
    print(i,'',round(startingPoint[0]),(startingPoint[1]))
    minimum=min(d1[2],d2[2],d3[2],d4[2])
    if minimum<SD:
        startingPoint=newPoints(minimum,d1,d2,d3,d4)
        SD=minimum
        i+=1
    else:
        flag=False
