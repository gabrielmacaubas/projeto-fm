import csv
from quick_sort import *
from bubble import *
from merge import *
from insertion import *
import sys
import time

sys.setrecursionlimit(4000)

def carregar_dados():
    with open("./dadosjp.csv", 'r') as file:
        csvreader = csv.reader(file)
        primeiro = True

        for row in csvreader:
            if primeiro:
                primeiro = False

                continue

            a = row[0].split(";")

            dados.append([a[0], (float(a[1]) + float(a[2]) + float(a[3]) + float(a[4]) + float(a[5])) / 5])


def imprimir_dados(dados):
    for linha in dados:
        print(linha[0], "|", linha[1]) 


# bubble sort
dados = []
carregar_dados()
start_time = time.time()

bubble_sort(dados)
#imprimir_dados(dados)
print("tempo bubble: ", time.time() - start_time)


# quick sort
dados = []
carregar_dados()
start_time = time.time()

quick_sort(dados, 0, len(dados)-1)
#imprimir_dados(dados)
print("tempo quick: ", time.time() - start_time)

# merge sort

dados = []
carregar_dados()
start_time = time.time()

merge_sort(dados)
#imprimir_dados(dados)
print("tempo merge sort: ", time.time() - start_time)

# insertion sort

dados = []
carregar_dados()
start_time = time.time()

insertion_sort(dados)
#imprimir_dados(dados)
print("tempo insertion sort: ", time.time() - start_time)
