import math

def get_lip_height(lip):
    sum=0
    for i in [2,3,4]:
        # distance between two near points up and down
        distance = math.sqrt( (lip[i][0] - lip[12-i][0])**2 +
                              (lip[i][1] - lip[12-i][1])**2   )
        sum += distance
    return sum / 3

def get_mouth_height(top_lip, bottom_lip):
    sum=0
    for i in [8,9,10]:
        # distance between two near points up and down
        distance = math.sqrt( (top_lip[i][0] - bottom_lip[18-i][0])**2 + 
                              (top_lip[i][1] - bottom_lip[18-i][1])**2   )
        sum += distance
    return sum / 3

def check_mouth_open(top_lip, bottom_lip):
    top_lip_height =    get_lip_height(top_lip)
    bottom_lip_height = get_lip_height(bottom_lip)
    mouth_height =      get_mouth_height(top_lip, bottom_lip)

    # if mouth is open more than lip height * ratio, return true.
    ratio = 0.5
    if mouth_height > min(top_lip_height, bottom_lip_height) * ratio:
        return True
    else:
        return False
