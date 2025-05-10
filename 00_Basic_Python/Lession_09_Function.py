# Lession 9 : Function

P_x = 5
E_x = 3
print(P_x)
def move():
    global P_x
    P_x += 1

def move_2(step):
    global P_x
    P_x += step
    return

def check():
    global P_x
    global E_x
    if P_x == E_x:
        return True
    else:
        return False

move()
print(P_x)
move_2(-3)
print(P_x)

test = check()
print(test)