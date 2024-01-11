import math
def find_volume(d, h):
    r=d/2
    volume=math.pi*r*r*h
    result=volume*1000
    return result

print(int(find_volume(0.55,0.878)))