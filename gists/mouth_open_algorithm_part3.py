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
