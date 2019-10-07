from mouth_open_algorithm import get_lip_height, get_mouth_height, check_mouth_open

# obama open mouth
top_lip = [(181, 359), (192, 339), (211, 332), (225, 336), (243, 333), (271, 342), (291, 364), (282, 363), (242, 346), (225, 347), (211, 345), (188, 358)]
bottom_lip = [(291, 364), (270, 389), (243, 401), (223, 403), (207, 399), (190, 383), (181, 359), (188, 358), (210, 377), (225, 381), (243, 380), (282, 363)]

# close mouth
# top_lip = [(151, 127), (157, 126), (163, 126), (168, 127), (172, 127), (178, 127), (185, 129), (182, 129), (172, 130), (167, 130), (163, 129), (153, 127)]
# bottom_lip = [(185, 129), (177, 133), (171, 135), (166, 135), (161, 134), (156, 132), (151, 127), (153, 127), (162, 129), (167, 130), (171, 130), (182, 129)]

print('top_lip height:', get_lip_height(top_lip))
print('bottom_lip height:', get_lip_height(bottom_lip))
print('mouth height:', get_mouth_height(top_lip,bottom_lip))
print('Is mouth open:', check_mouth_open(top_lip,bottom_lip) )

