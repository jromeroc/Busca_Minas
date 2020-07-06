#!/user/bin/python
# -*- coding: utf-8 -*-
import os.path
import time
import random

def main():
    instructions()
    matriz = create_matriz()
    start_game(matriz)

def instructions():
    os.system('cls')
    print('Las matrices se caracterizan por "almacenar datos separados en una cuadricula" ')
    print('Donde en cada cuadro de la cuadricula se almacena un dato y puedes saber que \n el dato en una cuadricula consultando su coordenada en la cuadricula.')

    print('Para este juego BUSCAMINAS sigue los siguientes pasos')
    print('1. Indica cuantas columnas va a tener tu cuadricula.')
    print('2. Indica cuantas filas va a tener tu cuadricula.')
    print('3. Se van a generar datos booleanos para cada cuadro de la cuadricula')
    print('4. Debes escoger 3 coordenadas indicando columna y fila si seleccionas una con dato 1 ó True perderás')
    print('5. Solamante ganas si aciertas los tres datos')

    input("Presiona una tecla para continuar. ")
    os.system('cls')

def create_matriz():
    print('*'*50)
    print("Prepara tu matriz")
    print('-'*50)
    cols = int(input('\nDe cuantas columnas quieres tu matriz: '))
    rows = int(input('De cuantas filas quieres tu matriz: '))
    
    grid = []
    for i in range(0, rows):
        grid.append([])
        for j in range(0, cols):
                grid[i].append([])
                val = random.choice((0, 1))
                grid[i][j] = val
    return grid

def view_grid(grid):
    for i in range(len(grid)):
        line = ''
        for j in range(len(grid[i])):
            line += "0" if j else 'X'
        print(str(i)+" "+line)

def start_game(grid):
    view_grid(grid)
    print("Selecciona tu primera coordenada")
   
    score = 0
    finish = False
    while score <= 3 or finish :
        u_col = int(input("Columna: "))
        u_row = int(input("Fila: "))

        if(not grid[u_col][u_row]):
            print("La coordenada no existe")
            os.system('cls')

        if(grid[u_col][u_row]):
            score += 1
            print("Vas {} aciertos faltan {}.".format(score, 3-score))
            if score >2:
                print("Lo lograste")
                finish = True
        else:
            print ("Perdiste")
            finish = True

if __name__ == '__main__':
	main()
