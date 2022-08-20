import random

TARGET = "DONEANDARPI"

def mutated_genes():
    GENEs = '''Sajal Debnath'''
    gene = random.choice(GENEs)
    # print(gene)
    return gene


def create_gnome():
    global TARGET
    gnome_len = len(TARGET)
    print(gnome_len)
    print("Gene is : ")
    gene = [mutated_genes() for _ in range(gnome_len)]
    return gene 


for i in range(5):
    gnome = create_gnome()
    print(gnome)


def name():
    return "Sajal"

x = 5
lst_s = [name() for _ in range(x)]
    # print("sajal") 

print(lst_s)

ls = []
print(lst_s[:2])

ls.extend(lst_s[:2])

prob = random.random()
print(prob)