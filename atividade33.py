# Lista original
lista = list(range(16))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Intervalo de 1 a 9
intervalo_1_9 = lista[1:10]

# Intervalo de 8 a 13
intervalo_8_13 = lista[8:14]

# Números pares
numeros_pares = [num for num in lista if num % 2 == 0]

# Números ímpares
numeros_impares = [num for num in lista if num % 2 != 0]

# Todos os múltiplos de 2, 3 e 4
multiplos_2 = [num for num in lista if num % 2 == 0]
multiplos_3 = [num for num in lista if num % 3 == 0]
multiplos_4 = [num for num in lista if num % 4 == 0]
multiplos_totais = set(multiplos_2) | set(multiplos_3) | set(multiplos_4)

# Lista reversa
lista_reversa = lista[::-1]

# Razão entre a soma do intervalo de 10 a 15 pelo intervalo de 3 a 9
soma_intervalo_10_15 = sum(lista[10:16])  # Soma de 10 a 15
soma_intervalo_3_9 = sum(lista[3:10])      # Soma de 3 a 9
razao = float(soma_intervalo_10_15) / soma_intervalo_3_9 if soma_intervalo_3_9 != 0 else None

# Exibindo os resultados
print("Intervalo de 1 a 9:", intervalo_1_9)
print("Intervalo de 8 a 13:", intervalo_8_13)
print("Números pares:", numeros_pares)
print("Números ímpares:", numeros_impares)
print("Todos os múltiplos de 2, 3 e 4:", sorted(multiplos_totais))
print("Lista reversa:", lista_reversa)
print("Razão entre a soma do intervalo de 10 a 15 pelo intervalo de 3 a 9:", razao)