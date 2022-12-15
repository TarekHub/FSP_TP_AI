# Work done by : Boufar Tarek & Chouaha Bela
import random


# region Functions

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
def cout_Max(n, m, sol):
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

    return cout_list[n - 1][m - 1]


# Question4 : Echanger 2 positions
def echange(sol, t1, t2):
    # Out of boundaries
    if t2 not in range(0, len(sol)) or (t1 not in range(0, len(sol))):
        return
    # Permutation
    t = sol[t1]
    sol[t1] = sol[t2]
    sol[t2] = t
    return sol


# Question5 : Insérer un Job dans un position


# endregion

# region Main
data = read_txt_data()
[N, M, S, T, D] = data_to_matrix(data)
[solution, rN, rM] = generate_random_solution(N, M, D)
cout = cout_Max(N, M, solution)

#solechange = echange(solution, 2, 1)

print("Ordre de taches : ", rN, " \nOrdre de machines : ", rM)
print("Solution initiale ", D)
print("Solution aléatoire ", solution)
print(cout)

"""
print(N, " job,", M, " machines", "seed : ", S)
print("Dates fin souhaitées :", T)
print("Temps d'éxécutions:", D)
"""
# endregion
