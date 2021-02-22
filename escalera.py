import itertools
import os

#Mediante una primera lista de 1's se crean distintas listas segun cantidad de 1's y 0's
#Se coloca un 2 al principio y se elimina un 1 creando  las diferentes posibilidades para luego permutar

def listar_pasos(nro_escalones):
    listaInicialUnos = []
    listaAcumuladoraPasos = []
    for i in range(nro_escalones):
        listaInicialUnos.append(1)  # listaInicialUnos empieza con todos los elementos en 1
    listaCopia = listaInicialUnos[:]  # listaCopia es una copia de la lista inicial para poder acumular valores
    listaAcumuladoraPasos.append(listaCopia)  # listaAcumuladoraPasos es un acumulador de las copias
    for i in range(nro_escalones):
        if 1 in listaInicialUnos and listaInicialUnos[-2] != 2:  # Comprobar que no sea el último elemento
            listaInicialUnos[i] = 2  # Agregar 2 al primer elemento de listaInicialUnos
            listaInicialUnos.remove(1)  # Eliminar un elemento de listaInicial
            listaCopia = listaInicialUnos[:]
            listaAcumuladoraPasos.append(listaCopia)
    return listaAcumuladoraPasos

#Se permuta cada una de las listas segun la fórmula de permutación con repetición

def permutar_repeticion(lista_posibilidades):
    listaAcumuladoraPasos = []
    for i in lista_posibilidades:
        listaPermutada = itertools.permutations(i)  # Obtener permutaciones con repetición con elementos del parámetro
        conjuntodeLista = set(listaPermutada)  # SET para eliminar elementos repetidos
        listaAuxiliar = list(conjuntodeLista)
        listaAcumuladoraPasos.append(listaAuxiliar)
    lista_retorno = list(itertools.chain(*listaAcumuladoraPasos))  # Unificar elementos de un tipo
    return lista_retorno


def principal():
    cant_escalones = 2
    salir = ''

    while salir != 'S' and salir != 's' and cant_escalones > 1:
        cant_escalones = int(input('Ingrese la cantidad de escalones: '))
        lista_pasos = listar_pasos(cant_escalones)
        listado_permutado = (permutar_repeticion(lista_pasos))
        print('Existen', len(listado_permutado), 'formas de subir')
        print(*listado_permutado, sep='\n')
        salir = input('Desea SALIR?S/N: ')
        os.system("cls")

principal()
