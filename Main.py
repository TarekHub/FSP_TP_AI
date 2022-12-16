# Work done by : Boufar Tarek & Chouaha Bela
import copy as co
import random
from statistics import stdev
from tkinter import Tk, Canvas, Scrollbar

Height = 1500
Width = 600


# region Functions

# Fonction qui permet de visualiser l'ordonnancement d'une solution valide donnée
def AfficherSolution(sol, L_Cout):
    n = len(sol)
    m = len(sol[0])
    x = 1
    deltaY = 20
    deltaX = 50
    # repere (Machine, time)
    canvas.create_line(deltaX, Width-78, Height, Width-78, fill="black", width=4)
    canvas.create_line(deltaX, Width-78, deltaX, 0, fill="black", width=4)

    for i in range(n):
        y = Width - 100
        # generate random hexa-color
        color = ["#" + ''.join([random.choice('ABCDEF0123456789') for i in range(6)])]
        for j in range(m):
            start = deltaX + L_Cout[i][j] - sol[i][j]
            canvas.create_rectangle(start*x, y, (start + sol[i][j])*x, y + deltaY, fill=color, width=1)
            y = y - deltaY
            # Print Cout
            if i == n - 1 and j == m - 1:
                canvas.create_text((start + sol[i][j])*x, y, text=L_Cout[n - 1][m - 1])


def read_txt_data():
    with open('./Instance/20_5_01_ta001.txt', 'r') as f:
        lines = f.readlines()
    return lines


# Question1 : charger en mémoire les données
def data_to_matrix(d):
    nJobs = int(d[0])
    mMachines = int(d[1])
    seed = int(d[2])
    # Document length
    L = d.__len__()
    # Definition des tableaux
    D = [[0] * mMachines] * nJobs
    T = [0] * nJobs
    co = 0
    i = 5
    while i < L:
        D[co] = list(map(int, d[i].split()))
        T[co] = int(d[i - 1])
        i += 3
        co += 1
    return nJobs, mMachines, seed, T, D


# Question2: Fonction qui génére une solution aléatoire
def generate_random_solution(n, m, D):
    randN = list(range(0, n))
    randM = list(range(0, m))
    # Ordre aléatoire imposé sur les taches et les machines
    random.shuffle(randN)
    random.shuffle(randM)

    rand_Sol = [[0] * m] * n

    for i in range(n):
        x = D[i]
        job = [0] * m
        for j in range(m):
            # Imposer l'ordre des machines
            job[j] = x[randM[j]]
        # Imposer l'ordre des taches
        rand_Sol[randN[i]] = job
    return rand_Sol, randN, randM


# Question3: Calcule du coût d une solution
def cout_Max(sol):
    n = len(sol)
    m = len(sol[0])
    cout_list = [[0 for i in range(m)] for j in range(n)]

    for i in range(n):
        for j in range(m):
            if i > 0:
                if j > 0:
                    # 2 contraintes de pour éxécuter une tache :
                    # - La tache precedente (i-1) est achevée dans la  machine j ou je suis
                    # - La tache i est achevée dans la machine j-1
                    cout_list[i][j] = sol[i][j] + max(cout_list[i][j - 1], cout_list[i - 1][j])
                else:
                    cout_list[i][j] = sol[i][j] + cout_list[i - 1][j]
            # 1ere itération
            else:
                if j > 0:
                    cout_list[i][j] = sol[i][j] + cout_list[i][j - 1]
                else:
                    cout_list[i][j] = sol[i][j] + cout_list[i][j]

    return cout_list[n - 1][m - 1], cout_list


# Question4 : Permuter entre 2 positions
def echange(sol, t1, t2):
    # Out of boundaries
    if t2 not in range(1, len(sol) + 1) or (t1 not in range(1, len(sol) + 1)):
        return
    sol_result = co.copy(sol)
    # Permutation
    t = sol_result[t1 - 1]
    sol_result[t1 - 1] = sol_result[t2 - 1]
    sol_result[t2 - 1] = t
    return sol_result


# Question5 : Insérer un Job dans un position
def insere(sol, p_from, p_to):
    # Out of boundaries
    if p_from not in range(1, len(sol) + 1) or (p_to not in range(1, len(sol) + 1)):
        return
    sol_result = co.copy(sol)
    tache = sol_result[p_from - 1]
    sol_result.remove(tache)
    sol_result.insert(p_to - 1, tache)
    return sol_result


# Question6 : Modifier aléatoirement une solution
def marche_aleatoire(sol):
    minCout = cout_Max(sol)
    for i in range(1000):
        random.shuffle(sol)
        if minCout[0] > cout_Max(sol)[0]:
            minCout = cout_Max(sol)
            bestSol = co.copy(sol)
    return bestSol, minCout


# endregion


def PROG():
    AfficherSolution(rand_sol, rand_Cout[1])


data = read_txt_data()
[N, M, S, T, D] = data_to_matrix(data)
[solution, rN, rM] = generate_random_solution(N, M, D)
rand_sol, rand_Cout = marche_aleatoire(solution)
print("Cout Marche aléatoire : ", rand_Cout[0])


# Question7 : Tester marche random avec Echange & Insert
positions = list(range(1, N+1))
list_voisin_echange = list()
list_voisin_insert = list()
nbrVoisins = 1000
for i in range(nbrVoisins):
    # generate 2 different random positions
    p1, p2 = random.sample(positions, 2)
    voisin_echange = echange(rand_sol, p1, p2)
    voisin_insert = insere(rand_sol, p1, p2)
    # Cout du voisin
    list_voisin_echange.append(cout_Max(voisin_echange)[0])
    list_voisin_insert.append(cout_Max(voisin_insert)[0])


# Calculer l'ecart moyen de fitness
ecart_echange_echange = stdev(list_voisin_echange)
ecart_echange_insert = stdev(list_voisin_insert)
print("Ecart moyen de fitness pour l'opérateur de voisinage - Echange : ", ecart_echange_echange)
print("Ecart moyen de fitness pour l'opérateur de voisinage - Insert : ", ecart_echange_insert)




# region Fenetre
Mafenetre = Tk()
Mafenetre.geometry(str(Height) + "x" + str(Width))
scrollbar_h = Scrollbar(Mafenetre, orient='horizontal')
scrollbar_v = Scrollbar(Mafenetre, orient='vertical')

scrollbar_h.pack(side= "bottom", fill= "x")
scrollbar_v.pack(side= "right", fill= "x")


canvas = Canvas(Mafenetre, width=Height, height=Width,
                borderwidth=0, highlightthickness=0, bg="white")
canvas.pack()

scrollbar_h.config(command = canvas.xview)
scrollbar_v.config(command = canvas.yview)

Mafenetre.after(100, PROG)
Mafenetre.mainloop()
# endregion

# endregion
