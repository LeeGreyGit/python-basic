# Pythonの基本 Part 3
# コレクション
# タプル、配列（リスト）、辞書

size = (100, 80)

height = size[0] # 高さ = 100
width = size[1] # 幅 = 80

print(size)
print(height)
print(width)

new_size = size + (150, ) # 長さは150
print(new_size)

print(len(new_size))
print(max(new_size))
print(min(new_size))

damage = [3, 5, 9, 10, 20]
first_damage = damage[0]
damage[0] = 5
print(damage)
print(first_damage)
damage.append(30)
damage.remove(9)

start_point = {'P1': 50, 'P2': 100, 'P3': 150}
print(start_point.keys())
print(start_point.values())
