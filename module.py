from random import randint

def Game():
    a = randint(1, 8)
    b = randint(1, 8)
    c = randint(1, 8)

    print(f"{a} {b} {c}")
    if a == b == c:
        return True
    else:
        return False


def Entry():
    x = input("if you are ready press Enter")
    return x



def decision():
    y = input("do you want to continue ? (y/n) : ")
    return y
