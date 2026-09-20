#IPO
# input
# input three subject marks
# processing 
# output


# Algorithom

# start
# read first subject marks
# read second subject marks
# read third subject marks
# check pass or fail
# print result
# stop

# python

math=int(input("Enter math marks"))
phy=int(input("Enter physics marks"))
hindi=int(input("Enter hindi marks"))
average=(math+phy+hindi)/3
if average>=40:
    print("Pass")
else:
    print("Fail")