# TP réalisé par : Boufar Tarek & Chouaha Bela
import numpy as np
import copy as co


# Lecture des données
def read_txt_data():
    with open('./Instance/20_5_01_ta001.txt', 'r') as f:
        lines = f.readlines()
    return lines


# Question1 : charger en mémoire les données
def data_to_matrix(d):
    n = int(d[0])
    m = int(d[1])
    seed = int(d[2])
    # Taille du document
    L = d.__len__()
    # Initialisation des tableaux
    D = np.zeros((n, m))
    T = np.zeros(n)
    co = 0
    i = 5
    while i < L:
        D[co] = list(map(int, d[i].split()))
        T[co] = int(d[i - 1])
        i += 3
        co += 1
    return n, m, T, D, seed


# Question2: Fonction qui génére une solution aléatoire et valide
def generate_solution(n, m, D):
    randn = np.arange(0, n)
    randm = np.arange(0, m)
    # Ordre aléatoire imposé sur les taches et les machines
    np.random.shuffle(randn)
    np.random.shuffle(randm)
    solution = np.zeros((n, m))
    for i in range(n):
        x = D[i]
        job = np.zeros(m)
        for j in range(m):
            # Imposer ordre des machines
            job[j] = x[randm[j]]
        # Imposer ordre des taches
        solution[randn[i]] = job
    return solution, randn, randm


# Question3: Calcule du coût d une solution
def cout_max(sol):
    n = len(sol)
    m = len(sol[0])
    coutList = np.zeros((n, m))

    for i in range(n):
        for j in range(m):
            if i > 0:
                if j > 0:
                    # 2 contraintes de pour éxécuter une tache :
                    # - La tache precedente (i-1) est achevée dans la  machine j ou je suis
                    # - La tache i est achevée dans la machine j-1
                    coutList[i, j] = sol[i][j] + max(coutList[i, j - 1], coutList[i - 1, j])
                else:
                    coutList[i][j] = sol[i, j] + coutList[i - 1, j]
            # 1ere itération
            else:
                if j > 0:
                    coutList[i][j] = sol[i, j] + coutList[i, j - 1]
                else:
                    coutList[i][j] = sol[i, j] + coutList[i, j]

    return coutList[n - 1, m - 1], coutList


# Question4 : Permuter entre 2 positions
def echange(solution, p1, p2):
    # Out of boundaries
    if p2 not in range(1, len(solution) + 1) or (p1 not in range(1, len(solution) + 1)):
        return
    solResult = co.copy(solution)
    # Permutation
    t = solution[p1 - 1]
    solResult[p1 - 1] = solResult[p2 - 1]
    solResult[p2 - 1] = t
    return solResult


# Question5 : Insérer un Job dans un position
def insere(solution, p1, p2):
    # Out of boundaries
    if p1 not in range(1, len(solution) + 1) or (p2 not in range(1, len(solution) + 1)):
        return
    solResult = co.copy(solution)
    tache = solResult[p1 - 1]
    solResult = np.delete(solResult, p1 - 1, axis=0)
    solResult = np.insert(solResult, p2 - 1, tache, axis=0)
    return solResult


def marche_aleatoire(solution):
    minCout = cout_max(solution)
    for i in range(1000):
        np.random.shuffle(solution)
        if minCout[0] > cout_max(solution)[0]:
            minCout = cout_max(solution)
            bestSol = co.copy(solution)
    return bestSol, minCout


def climber_best_echange(sol):
    solution = co.copy(sol)
    localSolution = co.copy(sol)
    # Taille de la solution
    n = len(solution)
    cout = cout_max(solution)[0]
    rechercher = True
    evaluation = 0
    # Tant qu'on trouve un minimum local
    while rechercher:
        rechercher = False
        # Le nombre de voisins = (n² - n) / 2 :
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                evaluation += 1
                voisin = echange(solution, i, j)
                coutVoisin = cout_max(voisin)[0]
                if cout > coutVoisin:
                    # Trouvé a voisin optimal
                    rechercher = True
                    cout = coutVoisin
                    localSolution = co.copy(voisin)
        solution = localSolution
    return cout, solution, evaluation


def climber_best_insere(sol):
    solution = co.copy(sol)
    localSolution = co.copy(sol)
    # Taille de la solution
    n = len(solution)
    cout = cout_max(solution)[0]
    rechercher = True
    evaluation = 0
    # Tant qu'on trouve un minimum local
    while rechercher:
        rechercher = False
        # Le nombre de voisins = (n² - n) / 2 :
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                evaluation += 1
                voisin = insere(solution, i, j)
                coutVoisin = cout_max(voisin)[0]
                if cout > coutVoisin:
                    # Trouvé a voisin optimal
                    rechercher = True
                    cout = coutVoisin
                    localSolution = co.copy(voisin)
        solution = localSolution
    return cout, solution, evaluation


def climber_first_echange(sol):
    solution = co.copy(sol)
    # Taille de la solution
    n = len(solution)
    cout = cout_max(solution)[0]
    rechercher = True
    evaluation = 0
    # Tant qu'on trouve un minimum local
    while rechercher:
        rechercher = False
        # Le nombre de voisins = (n² - n) / 2 :
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                evaluation += 1
                voisin = echange(solution, i, j)
                coutVoisin = cout_max(voisin)[0]
                if cout > coutVoisin:
                    # On trouve un voisin optimal
                    rechercher = True
                    cout = coutVoisin
                    solution = co.copy(voisin)
                    # On quite les 2 boucles
                    break
            else:
                # Continue if the inner loop wasn't broken.
                continue
                # Inner loop was broken, break the outer.
            break
    return cout, solution, evaluation

def climber_first_insere(sol):
    solution = co.copy(sol)
    # Taille de la solution
    n = len(solution)
    cout = cout_max(solution)[0]
    rechercher = True
    evaluation = 0
    # Tant qu'on trouve un minimum local
    while rechercher:
        rechercher = False
        # Le nombre de voisins = (n² - n) / 2 :
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                evaluation += 1
                voisin = insere(solution, i, j)
                coutVoisin = cout_max(voisin)[0]
                if cout > coutVoisin:
                    # On trouve un voisin optimal
                    rechercher = True
                    cout = coutVoisin
                    solution = co.copy(voisin)
                    # On quite les 2 boucles
                    break
            else:
                # Continue if the inner loop wasn't broken.
                continue
                # Inner loop was broken, break the outer.
            break
    return cout, solution, evaluation
