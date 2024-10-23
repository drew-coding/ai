def TOH(n,fromPole,withPole,toPole):
    if(n==1):
        print("Moving disk from ",fromPole," to ",toPole)
    else:
        TOH(n-1,fromPole,toPole,withPole)
        print("Movingh disk from ",fromPole," to ",toPole)
        TOH(n-1,withPole,fromPole,toPole)
num=int(input("Enter the number of disk :"))
TOH(num,"A","B","C")
    
