import random
from datetime import datetime

def bogosort(l):
    count = 0
    while not in_order(l):
        random.shuffle(l)
        count += 1
        print(l)
    print("Bogo took: "+str(count)+" iterations!")
    return l


def in_order(l):
    if not l:
        return True
    last = l[0]
    for x in l[1:]:
        if x < last:
            return False
        last = x
    return True

start = datetime.now()
bogosort([9,8,7,6,5,4,3,2,1,0])
print("Bogosort took: "+str(datetime.now() - start))