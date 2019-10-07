import math

def get_lip_height(lip):
    sum=0
    for i in [2,3,4]:
        # distance between two near points up and down
        distance = math.sqrt( (lip[i][0] - lip[12-i][0])**2 +
                              (lip[i][1] - lip[12-i][1])**2   )
        sum += distance
    return sum / 3
