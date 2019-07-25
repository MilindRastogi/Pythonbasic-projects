print("Welcome to tic tac toe \n")
z=1
m=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
def board(m):
    print("\n"*100)
    print(m[1] + '|' + m[2] + '|' +m[3])
    print("------")
    print(m[4] + '|' + m[5] + '|' + m[6])
    print("------")
    print(m[7] + '|' + m[8] + '|' + m[9])
a= input("Are you ready to play : yes or no ? \n")
while a=="yes":
    b=input("Player 1: Do you want to be X or O ?")
    if b=="X":
        print("Player2= 'O'")
        print("Game begins:")
        board(m)
        while True:
            c= int(input("chose your next chance from (1-9)"))
            m[c]=b
            board(m)
            z=z+1
            if z%2==0:
                b='O'
            else:
                b='X'
            if z%2!=0:
                if m[1] == m[2] == m[3] == 'O' or m[4] == m[5] == m[6] == 'O' or m[7] == m[8] == m[9] == 'O' or m[1] == m[4] == m[
                    7] == 'O' or m[2] == m[5] == m[8] == 'O' or m[3] == m[6] == m[9] == 'O' or m[1] == m[5] == m[9] == 'O' or m[3] == m[5] == m[7] == 'O':
                        print("Congratulations Player 2 has won the game")
                        a=input("Are you ready to play again : yes or no")
                        if a=='yes':
                            m=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
                            continue
                        else:
                            break
            elif  m[1] == m[2] == m[3] == 'X' or m[4] == m[5] == m[6] == 'X' or m[7] == m[8] == m[9] == 'X' or m[1] == m[4] == m[
                    7] == 'X' or m[2] == m[5] == m[8] == 'X' or m[3] == m[6] == m[9] == 'X' or m[1] == m[5] == m[9] == 'X' or m[3] == m[5] == m[7] == 'X':
                print("Congratulations Player 1 has won the game")
                a=input("Are you ready to play again: yes or no")
                if a == 'yes':
                    m = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ',' ']
                    continue
                else:
                    break
            elif z==10 :
                print("Game has tied")
                a=input("Are you ready to play again : yes or no")
                if a == 'yes':
                    m = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ',' ']
                    continue
                else:
                    break
    elif b=='O':
        print("Player2= 'X'")
        print(" Game begins:")
        board(m)
        while True:
            c = int(input("chose your next chance from (1-9)"))
            m[c] = b
            board(m)
            z = z + 1
            if z % 2 == 0:
                b = 'X'
            else:
                b = 'O'
            if z % 2 != 0:
                if m[1] == m[2] == m[3] == 'X' or m[4] == m[5] == m[6] == 'X' or m[7] == m[8] == m[9] == 'X' or m[1] == m[4] == m[7] == 'X' or m[2] == m[5] == m[8] == 'X' or m[3] == m[6] == m[9] == 'X' or m[1] == m[5] == m[
                    9] == 'X' or m[3] == m[5] == m[7] == 'X':
                    print("Congratulations Player 2 has won the game")
                    a = input("Are you ready to play again : yes or no")
                    if a == 'yes':
                        m = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ',' ']
                        continue
                    else:
                        break
            elif m[1] == m[2] == m[3] == 'O' or m[4] == m[5] == m[6] == 'O' or m[7] == m[8] == m[9] == 'O' or m[1] == m[
                4] == m[7] == 'O' or m[2] == m[5] == m[8] == 'O' or m[3] == m[6] == m[9] == 'O' or m[1] == m[5] == m[
                9] == 'O' or m[3] == m[5] == m[7] == 'O':
                print("Congratulations Player 1 has won the game")
                a=input("Are you ready to play again : yes or no")
                if a == 'yes':
                    m = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ',' ']
                    continue
                else:
                    break
            elif z == 10:
                print("Game has tied")
                a = input("Are you ready to play again : yes or no")
                if a == 'yes':
                    m = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ' ]
                    continue
                else:
                    break












