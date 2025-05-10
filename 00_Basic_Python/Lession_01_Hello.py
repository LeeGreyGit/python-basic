# レッスン3：こんにちは（Hello）

input_name = input('名前を入力してください: ')

output = 'こんにちは ' + input_name

print(output)
print(f"こんにちは {input_name}")

# レッスン4：基本的なデータ型：int、float、boolean、string

# 文字列（string）
name = 'AAA'
print(name)

# name = "AAA"
# name = None

# 整数（int）
x_pos = 5
y_pos = 10

# 浮動小数点数（float）
speed = 2.5

print(speed)

# 真偽値（boolean）
is_game_over = False

# データ型を確認
print(type(is_game_over))
print(type(speed))

# speed = 'dklfjdslkjdkljsdlak'
# print(type(speed))

# レッスン5：数学演算
# 代入、否定
# 数学演算：+ - * / % // += -= *= /= ** （※ ** はべき乗）
# 条件演算子：> >= < <= != ==

new_x_pos = x_pos  # new_x_pos = 5
is_not_game_over = not is_game_over  # is_not_game_over = True

new_x_pos = x_pos + speed  # new_x_pos = 5 + 2.5 = 7.5
full_name = '名前: ' + name  # full_name = '名前: AAA'

mod = x_pos % 2  # mod = 1（2で割った余り）
div = x_pos // 2  # div = 2（整数除算）

square = x_pos ** 2  # square = 25（5の2乗）

# x_pos = x_pos + speed # x_pos = 7.5
x_pos += speed  # x_pos に speed を加算（x_pos = 7.5）
