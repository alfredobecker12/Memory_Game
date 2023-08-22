import random
import copy
import time
import os

symb = ['!', '!', '@', '@', '$', '$', '%', '%', '&', '&', '*', '*', ':', ':', '>', '>',
                '<', '<', '!!', '!!', '##', '##', '@@', '@@', '$$', '$$', '%%', '%%', '&&', '&&',
                '**', '**', '::', '::', '>>', '>>', '<<', '<<', 'ç', 'ç', '+', '+', '-', '-',
                '(', '(', ')', ')', '0', '0', '1', '1', '2', '2', '3', '3', '4', '4', '5', '5',
                '6', '6', '7', '7', '8', '8', '9', '9', '10', '10', 'A', 'A', 'S', 'S', 'D', 'D',
                'F', 'F', 'G', 'G', 'H', 'H', 'J', 'J', 'K', 'K', 'L', 'L', 'Z', 'Z', 'X', 'X',
                'C', 'C', 'V', 'V', 'B', 'B', 'Y', 'Y']


def get_difficult(symb):
    symbol = []
    while True:
        diff = input("\nBem-vindo ao jogo da memória. Em qual dificuldade você quer jogar?\n1 - facil\n2 - medio\n3 - dificil\nResposta: ")
        if diff == '1':
            for i in range(16):
                symbol.append(symb[i])
                lines, columns, time, lives = 4, 4, 15, 3
            return symbol, lines, columns, time, lives
        elif diff == '2':
            for i in range(36):
                symbol.append(symb[i])
                lines, columns, time, lives = 6, 6, 20, 5
            return symbol, lines, columns, time, lives
        elif diff == '3':
            symbol = symb.copy()
            lines, columns, time, lives = 10, 10, 30, 7
            return symbol, lines, columns, time, lives
        else:
            print("Dificuldade invalida. Escolha 1, 2 ou 3.")



symbols, lines, columns, showtime, lives = get_difficult(symb)


def show_opened_table(table1, showtime):
    print_table(table1)
    for i in range(showtime, 0, -1):
        print(f"\rVocê tem {i} segundos restantes.", end= '', flush= True)
        time.sleep(1)

    os.system('cls')

def table(symbols):
    matriz = []
    line = []
    all_symbols = symbols.copy()
    for j in range(lines):
        for i in range(columns):
            value = random.choice(all_symbols)
            all_symbols.remove(value)
            line.append(value)
        matriz.append(line)
        line = []

    return matriz


def pseudotable():
    pseudomatriz = []
    line = []
    for j in range(lines):
        for i in range(columns):
            line.append(".")
        pseudomatriz.append(line)
        line = []

    return pseudomatriz


def print_table(matriz):
    for j in range(lines):
        count = 0
        for i in matriz[j]:
            if count != 10:
                print(f" {i:2} ", end='|')
            else:
                print(f" {i} ", end='')
            count += 1
        print()
    print("\n")

def found_coordinates(line1, col1, line2, col2, right_coordinates):
    right_coordinates.append(''.join(map(str, [line1, col1, line2, col2])))
    return right_coordinates


def show_table(table1, invisibletableprint, line1, col1, line2, col2):
    value1, value2 = table1[line1][col1], table1[line2][col2]
    showtable = copy.deepcopy(invisibletableprint)
    showtable[line1][col1], showtable[line2][col2] = value1, value2
    print_table(showtable)


def correct_symbol(table1, invisibletableprint, line1, col1, line2, col2):
    value = table1[line1][col1]
    invisibletableprint[line1][col1], invisibletableprint[line2][col2] = value, value

    return invisibletableprint


def verify_symbol(table1, invisibletable, right_coordinates):
    print_table(invisibletable)
    while True:
        line1, col1 = int(input("1° Coordenada\nLinha: ",)) - 1, int(input("Coluna: ")) - 1
        line2, col2 = int(input("\n2° Coordanada\nLinha: ")) - 1, int(input("Coluna: ")) - 1
        if (line1 == line2) and (col1 == col2):
            print("Não é possível comparar uma coordenada com ela mesma.\n")
        elif line1 < 0 or line1 >= lines or col1 < 0 or col1 >= columns \
                or line2 < 0 or line2 >= lines or col2 < 0 or col2 >= columns:
            print("Coordenadas inválidas. Tente novamente.\n")
        elif ''.join(map(str, [line1, col1, line2, col2])) in right_coordinates:
            print("Você já encontrou esses símbolos, tente novamente.\n")
        else:
            break

    if table1[line1][col1] == table1[line2][col2]:
        newtable = correct_symbol(table1, invisibletable, line1, col1, line2, col2)
        found_coordinates(line1, col1, line2, col2, right_coordinates)
        print("Par correto !")
        return 1, newtable
    else:
        show_table(table1, invisibletable, line1, col1, line2, col2)
        print("Você errou, tente novamente caso tenha vidas.")
        return -1, 'None'


def game(lives):
    right_coordinates = []
    extra_life = 0
    invisibletable = pseudotable()
    table1 = table(symbols)
    show_opened_table(table1, showtime)
    while lives > 0:
        print(f"\nYou have {lives} lives.")
        life, strangetable = verify_symbol(table1, invisibletable, right_coordinates)
        if strangetable != 'None':
            invisibletable = strangetable.copy()
        else:
            print()
        if life < 0:
            lives += life
            life = 0

        extra_life += life
        if extra_life == 3:
            lives += 1
            extra_life = 0

        if table1 == invisibletable:
            print(f"Você venceu!\n")
            break
    print("Fim de jogo.")


def main():
    init = input("\n\nPressione Enter para iniciar ou q+Enter para sair.")
    if init == 'q':
        quit()

    game(lives)


main()
