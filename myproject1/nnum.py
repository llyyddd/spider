import random
def change_to_num(n):
    if (n == "若干" or n=="999"):
        sj = random.randint(1, 5)
        neednum = sj
    else:
        neednum = int(n)
    return neednum