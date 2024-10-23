def water_jug(jug1,jug2):
    max1=5
    max2=7
    goal=4
    print('%d\t%d'%(jug1,jug2))
    if(jug1==goal or jug2==goal):
        return
    elif(jug2==max2):
        water_jug(jug1,0)
    elif(jug1!=0 and jug2==0):
        water_jug(0,jug1)
    elif(jug1==0):
        water_jug(max1,jug2)
    elif(jug1<(max2-jug2)):
        water_jug(0,(jug1+jug2))
    else:
        water_jug(jug1-(max2-jug2),(max2-jug2)+jug2)
print('Jug 1\tJug 2')
water_jug(0,0)

