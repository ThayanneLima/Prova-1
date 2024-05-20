import random

range_dos_numeros = 10_000_000

arranjo_100k = random.sample(range(1, range_dos_numeros), 100_000)


with open("./teste_desordenado/100_mil.txt", "w") as f:
    for number in arranjo_100k:
        f.write(str(number) + "\n")


arranjo_200k = random.sample(range(1, range_dos_numeros), 200_000)

with open("./teste_desordenado/200_mil.txt", "w") as f:
    for number in arranjo_200k:
        f.write(str(number) + "\n")

arranjo_300k = random.sample(range(1, range_dos_numeros), 300_000)

with open("./teste_desordenado/300_mil.txt", "w") as f:
    for number in arranjo_300k:
        f.write(str(number) + "\n")


arranjo_400k = random.sample(range(1, range_dos_numeros), 400_000)

with open("./teste_desordenado/400_mil.txt", "w") as f:
    for number in arranjo_400k:
        f.write(str(number) + "\n")


arranjo_500k = random.sample(range(1, range_dos_numeros), 500_000)

with open("./teste_desordenado/500_mil.txt", "w") as f:
    for number in arranjo_500k:
        f.write(str(number) + "\n")


arranjo_600k = random.sample(range(1, range_dos_numeros), 600_000)

with open("./teste_desordenado/600_mil.txt", "w") as f:
    for number in arranjo_600k:
        f.write(str(number) + "\n")


arranjo_700k = random.sample(range(1, range_dos_numeros), 700_000)

with open("./teste_desordenado/700_mil.txt", "w") as f:
    for number in arranjo_700k:
        f.write(str(number) + "\n")


arranjo_800k = random.sample(range(1, range_dos_numeros), 800_000)

with open("./teste_desordenado/800_mil.txt", "w") as f:
    for number in arranjo_800k:
        f.write(str(number) + "\n")


arranjo_900k = random.sample(range(1, range_dos_numeros), 900_000)

with open("./teste_desordenado/900_mil.txt", "w") as f:
    for number in arranjo_900k:
        f.write(str(number) + "\n")


arranjo_1mi = random.sample(range(1, range_dos_numeros), 1_000_000)

with open("./teste_desordenado/1_milhao.txt", "w") as f:
    for number in arranjo_1mi:
        f.write(str(number) + "\n")