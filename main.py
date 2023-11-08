import math
import random

instruction = str('THIS IS THE GAME OF TWONKY.\nYOU HAVE LANDED ON THE PLANET OF TWINKY AND\n'
                  'ITS KING (KONG:THEIR KING IS KING KONG) HAS CAPTURED YOU.\n'
                  'HE HAS PUT YOU IN A MAZE THAT IS 15 * 15 UNITS LONG.\n'
                  'YOU ARE IN THE DARK AND CANNOT SEE... YOU MUST GET TO THE OBJECTIVE SQUARE AND BE SET FREE.\n'
                  '     HAZARDS INCLUDE:\n'
                  'SQUARES THAT YOU CANNOT GO INTO (30).\n'
                  'SQUARES THAT RANDOMLY THROW YOU AROUND THE MAZE (22).\n'
                  'SQUARE THAT SETS UP A NEW MAZE AND ALL THATS IN IT (1)\n'
                  'MONSTER CALLED TWONKY THAT CHASES YOU AND WILL\n'
                  '    ABSORB YOU IF THE DISTANCE IT IS FROM YOU FALLS BELOW 2 UNITS.\n'
                  '    TWONKY IS ALSO IMMUNE TO ALL TRAPS INCLUDING WALLS.\n\n'
                  '    YOU CAN:\n'
                  'MOVE ONE SQUARE AT A TIME TO FIND THE OBJECTIVE OR ESCAPE FRON THE TWONKY.\n'
                  'SHOOT AT THE TWONKY ONE DIRECTION AT A TIME.\n'
                  '  IF THE TWONKY IS HIT, HE WILL BE REPLACED IN THE MAZE RANDOMLY.\n\n'
                  'IF THE TWONKY ABSORBS YOU...YOU LOSE.\n'
                  'IF YOU LAND ON THE OBJECTIVE SQUARE YOU WIN.\n\n'
                  'GOOD LUCK!\n')

print('TWONKY\nCREATIVE COMPUTING\nMORRISTOWN  NEW JERSEY\n\n')


# рассчет дистанции
def dictance(player, obj):
    D = math.sqrt(abs((obj[0] - player[0]) ** 2 + (obj[1] - player[1]) ** 2))
    return D


# рандомные координаты
def random_number():
    mass = []
    for i in range(2):
        number = random.randint(0, 14)
        mass.append(number)
    return mass


# присваивание рандомных координат на поле
def coordinate(n, pole):
    while True:
        obj = random_number()
        x, y = obj[0], obj[1]
        if pole[x][y] == 0:
            pole[x][y] = n
            break
        else:
            continue
    return obj


# создание поля
def pole_coordinate():
    pole = [[0 for x in range(15)] for y in range(15)]

    # координаты игрока
    player = coordinate(1, pole)

    # координаты стен
    for i in range(30):
        blocked = coordinate(2, pole)

    # координаты ловушек
    for i in range(22):
        relocation = coordinate(3, pole)

    # координаты cупер-ловушки
    super_trap = coordinate(4, pole)

    # координаты цели
    objective = coordinate(5, pole)

    # координаты twonky
    twonky = coordinate(6, pole)

    return player, blocked, relocation, super_trap, objective, twonky, pole


# смена координат твонки при движении
def twonky_activity(twonky, pole, R9, x_new, y_new):
    x = twonky[0]
    y = twonky[1]
    pole[x][y] = R9
    R9 = pole[x_new][y_new]
    pole[x_new][y_new] = 6
    twonky[0] = x_new
    twonky[1] = y_new
    print('TWONKY MOVES....\n')
    return twonky, R9


# смена координат игрока при движении
def player_activity(player, pole, x_new, y_new):
    x = player[0]
    y = player[1]
    pole[x][y] = 0
    pole[x_new][y_new] = 1
    player[0] = x_new
    player[1] = y_new
    print('MOVE ALLOWED.\n')
    return player


# движение twonky
def twonky_logic(player, twonky, pole, R9):
    if player[0] < twonky[0]:
        x_new = twonky[0] - 1
        y_new = twonky[1]
        twonky = twonky_activity(twonky, pole, R9, x_new, y_new)
    elif player[0] > twonky[0]:
        x_new = twonky[0] + 1
        y_new = twonky[1]
        twonky = twonky_activity(twonky, pole, R9, x_new, y_new)
    elif player[1] < twonky[1]:
        x_new = twonky[0]
        y_new = twonky[1] - 1
        twonky = twonky_activity(twonky, pole, R9, x_new, y_new)
    else:
        x_new = twonky[0]
        y_new = twonky[1] + 1
        twonky, R9 = twonky_activity(twonky, pole, R9, x_new, y_new)
    return twonky, R9


def shoot(player, s1, s2, twonky, pole, R9):
    r1 = player[0]
    r2 = player[1]
    print('Z A P --\n')
    while True:
        r1 = r1 + s1
        r2 = r2 + s2
        if r1 not in range(0, 14) or r2 not in range(0, 14):
            print('FIZZLE...\nSHOT LEFT MAZE.\nSHOT MISSED.\n')
        if pole[r1][r2] != 2:
            if pole[r1][r2] != 6:
                continue
            else:
                print(' OUCH!!\nTWONKY RETREATES.\n')
                pole[r1][r2] = R9
                twonky = coordinate(6, pole)
        else:
            print('YOU HIT WALL.\nSHOT MISSED.\n')
        return twonky, R9


try_again = ''
while try_again != 'n':
    while True:
        Q = input('DO YOU WANT INSTRUCTIONS (Y/N): ')
        if Q == 'y':
            print(instruction)
            break
        elif Q == 'n':
            break
        else:
            continue
    print('------------------------------------------\n')
    player, blocked, relocation, super_trap, objective, twonky, pole = pole_coordinate()
    R9 = 0

    while True:
        D_twonky = dictance(player, twonky)
        D_objective = dictance(player, objective)
        print(f'THE TWONKY IS \n{D_twonky} UNITS AWAY.\nTHE OBJECTIVE IS \n{D_objective} UNITS AWAY.\n')
        if D_twonky >= 2:
            move = input('MOVE OR SHOOT (M/S): ').lower()
            if move == 'm':
                rotation = input('WHICH WAY (F/B/R/L): ').lower()
                if rotation == 'f':
                    x_new = player[0]
                    y_new = player[1] - 1
                if rotation == 'b':
                    x_new = player[0]
                    y_new = player[1] + 1
                if rotation == 'l':
                    x_new = player[0] - 1
                    y_new = player[1]
                if rotation == 'r':
                    x_new = player[0] + 1
                    y_new = player[1]
                # move
                if x_new not in range(0, 14) or y_new not in range(0, 14):
                    print('THAT MOVE TAKES YOU OUT OF THE MAZE.\nMOVE NOT ALLOWED.\n')
                elif pole[x_new][y_new] == 0:
                    player_activity(player, pole, x_new, y_new)
                elif pole[x_new][y_new] == 2:
                    print('THAT SPACE IS BLOCKED.\n')
                elif pole[x_new][y_new] == 3:
                    pole[x_new][y_new] = 0
                    print("YOU'VE BEEN   R E L O C A T E D !!!\n")
                    player = coordinate(1, pole)
                elif pole[x_new][y_new] == 4:
                    print('   YOU HIT THE SUPER TRAP!! YOU GET A NEW MAZE.\n')
                    player, blocked, relocation, super_trap, objective, twonky, pole = pole_coordinate()
                elif pole[x_new][y_new] == 5:
                    print(
                        'I DONT BELIEVE IT BUT YOU WON THE GAME!\n'
                        'YOU GOT TO THE OBJECTIVE BEFORE\n   THE TWONKY GOT YOU!!\n')
                    break
                elif pole[x_new][y_new] == 6:
                    print('YOU STEPPED ON THE TWONKY!\n')
            if move == 's':
                rotation = input('WHICH WAY (F/B/R/L): ').lower()
                if rotation == 'f':
                    s1 = 0
                    s2 = -1
                if rotation == 'b':
                    s1 = 0
                    s2 = 1
                if rotation == 'l':
                    s1 = -1
                    s2 = 0
                if rotation == 'r':
                    s1 = 1
                    s2 = 0
                    x_new = player[0]
                    y_new = player[1]
                # shoot
                r1 = player[0]
                r2 = player[1]
                print('Z A P --\n')
                while True:
                    r1 = r1 + s1
                    r2 = r2 + s2
                    if r1 not in range(0, 14) or r2 not in range(0, 14):
                        print('FIZZLE...\nSHOT LEFT MAZE.\nSHOT MISSED.\n')
                        break
                    elif pole[r1][r2] != 2:
                        if pole[r1][r2] != 6:
                            continue
                        else:
                            print(' OUCH!!\nTWONKY RETREATES.\n')
                            pole[r1][r2] = R9
                            twonky = coordinate(6, pole)
                            break
                    else:
                        print('YOU HIT WALL.\nSHOT MISSED.\n')
                        break
            twonky_logic(player, twonky, pole, R9)
            continue
        else:
            print('> > > SCHLOORP !!! < < <\nTHE TWONKY JUST ABSORBED YOU !! YOU LOSE.')
            break
    try_again = input('TRY AGAIN (Y/N) ').lower()
