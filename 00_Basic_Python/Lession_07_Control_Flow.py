# Lession 7 : If

game_over = False
P_x = 0
E1_x = 3
E2_x = 5

P_x += 3

if P_x == E1_x or P_x == E2_x:
    game_over = True
# Else if : elif
else:
    E1_x += 1
    E2_x += 2

###
# print(game_over)
# print(E1_x)
# print(E2_x)

# Lession 8 : while, for in


# While : can use continue, break
game_over = False
P_x = 0
E_x = 3
goal_x = 10

while not game_over:
    print(P_x)
    print(E_x)
    print()
    if P_x == E_x:
        print('Game Over')
        game_over = True
    elif P_x >= goal_x:
        print('Win')
        game_over = True
    else:
        P_x += 2
        E_x += 1
print()

# For in
P_x = 5
move_list = [1, 4, -2, -1, 5, -2, 3]

for move in move_list:
    P_x += move
    print(P_x)
print()

# range : start from value 1 to length value 2 with step is value 3
for i in range(0,len(move_list),2):
    print(move_list[i])
    
        
        
