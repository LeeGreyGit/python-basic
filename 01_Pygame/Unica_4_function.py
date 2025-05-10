# Pythonの基本 Part 6
# 関数
# 定義、引数の渡し方、関数の呼び出しと戻り値

x = 5
target_position = 3
print(x)

def move():
    global x
    x += 1
    
def move_2(steps):
    global x
    x += steps
    return
    
def check_collision():
    global x
    global target_position
    # 衝突をチェック
    if x == target_position:
        return True
    else:
        return False

move()
print(x)
move_2(-3)
print(x)

collision = check_collision()
print(collision)
