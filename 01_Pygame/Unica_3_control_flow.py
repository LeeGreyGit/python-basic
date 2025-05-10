# Python Basics Part 4
# Control Flow
# if statement

game_over = False
player_x = 0
enemy1_x = 3
enemy2_x = 5

player_x += 3

if player_x == enemy1_x or player_x == enemy2_x:
    game_over = True
else:
    enemy1_x += 1
    enemy2_x += 2
    
###
game_over
enemy1_x
enemy2_x

# Python Basics Part 5
# Control Flow
# Looping statements: while, for in

game_over = False
player_x = 0
enemy_x = 3
end_x = 10

while not game_over:
    print(player_x)
    print(enemy_x)
    print()
    if player_x == enemy_x:
        print('You have failed')
        game_over = True
    elif player_x >= end_x:
        print('You have won')
        game_over = True
    else:
        player_x += 2
        enemy_x += 1

player_x = 5
move_commands = [1, 4, -2, -1, 5, -2, 3]
for move in move_commands:
    player_x += move
    print(player_x)
print()
for i in range(0, len(move_commands), 2):
    print(move_commands[i])
