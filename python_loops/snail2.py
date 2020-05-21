height=int(input("height: "))
increase=int(input("inc: "))
decrease=int(input("dec: "))
distance=increase
day=1
while distance<height:
    distance=distance-decrease+increase
    day+=1
print(day)