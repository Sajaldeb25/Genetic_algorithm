import random

TARGET = "DONEANDARPI"

def mutated_genes():
    GENEs = "Sajal Debnath"
    gene = random.choice(GENEs)
    print(gene)
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