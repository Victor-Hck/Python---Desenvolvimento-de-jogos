monstros = ["monstro", "Rei"] # Array

def atacar():
    print("Atacar monstro")

def defender():
    print("defender o rei")

for i in monstros:
    if i == "monstro":
        atacar()
    elif i == "Rei":
        defender()