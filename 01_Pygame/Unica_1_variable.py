# Pythonの基本 Part 1
# 変数
# 4つの基本データ型: int, float, boolean, string

name = "ブリ"

# .....

x_pos = 5
y_pos = 10

# print(speed)

is_game_over = False

# print(type(is_game_over))

speed = 2.5


# Pythonの基本 Part 2
# 演算
# 代入演算: = not
# 算術演算: + - * / % // += -= *= /= **
# 条件演算: > >= < <= != ==

new_x_pos = x_pos # new_x_pos = 5
is_not_game_over = not is_game_over # is_not_game_over = True

new_x_pos = x_pos + speed # new_x_pos = 7.5
full_name = 'シャケ ' + name # full_name = ''

mod = x_pos % 2 # mod = 1
div = x_pos // 2 # div = 2

square = x_pos ** 2 # square = 25

# x_pos = x_pos + speed # x_pos = 7.5
x_pos += speed 
