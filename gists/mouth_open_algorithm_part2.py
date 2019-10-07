def get_mouth_height(top_lip, bottom_lip):
    sum=0
    for i in [8,9,10]:
        # distance between two near points up and down
        distance = math.sqrt( (top_lip[i][0] - bottom_lip[18-i][0])**2 + 
                              (top_lip[i][1] - bottom_lip[18-i][1])**2   )
        sum += distance
    return sum / 3
