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


# Strict
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
                    # Trouvé a voisin améliorant
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
    # Tant qu'on trouve un voisin améliorant
    while rechercher:
        rechercher = False
        # Le nombre de voisins = n² - 2n + 1 :
        for i in range(1, n + 1):
            j = 1
            while j < n + 1:
                if j == i or j == i - 1:
                    j += 1
                # j vérifie la contrainte de coordonnées(i, j) pour insertion
                else:
                    evaluation += 1
                    voisin = insere(solution, i, j)
                    coutVoisin = cout_max(voisin)[0]
                    if cout > coutVoisin:
                        # a trouvé un voisin améliorant
                        rechercher = True
                        cout = coutVoisin
                        localSolution = co.copy(voisin)
                    # incrémenter j
                    j += 1
        # redéfinir solution pour le meilleur (best) voisin améliorant
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
        # Le nombre de voisins = n² - 2n + 1 :
        for i in range(1, n + 1):
            j = 1
            while j < n + 1:
                if j == i or j == i - 1:
                    j += 1
                # j vérifie la contrainte de coordonnées(i, j) pour insertion
                else:
                    evaluation += 1
                    voisin = insere(solution, i, j)
                    coutVoisin = cout_max(voisin)[0]
                    if cout > coutVoisin:
                        # On trouve un voisin améliorant
                        rechercher = True
                        cout = coutVoisin
                        solution = co.copy(voisin)
                        # On quite les 2 boucles (while et for)
                        break
                    # incrémenter j
                    j += 1
            else:
                # Continue if the inner loop wasn't broken.
                continue
                # Inner loop was broken, break the outer.
            break
    return cout, solution, evaluation


def climber_worst_echange(sol):
    solution = co.copy(sol)
    localSolution = co.copy(sol)
    n = len(solution)
    cout = cout_max(solution)[0]
    # Init : le plut petit possible
    coutWorstAmeliorant = 0
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
                if cout > coutVoisin > coutWorstAmeliorant:
                    # Trouver un voisin moin bon améliorant
                    rechercher = True
                    coutWorstAmeliorant = coutVoisin
                    localSolution = co.copy(voisin)
        # redéfinir le voisin le moin bon
        solution = localSolution
        cout = cout_max(solution)[0]
        coutWorstAmeliorant = 0
    return cout_max(solution)[0], solution, evaluation


def climber_worst_insere(sol):
    solution = co.copy(sol)
    worstSolution = co.copy(sol)
    n = len(solution)
    cout = cout_max(solution)[0]
    # Init : le plut petit possible
    coutWorst = 0
    evaluation = 0
    rechercher = True
    # Tant qu'on trouve un voisin améliorant
    while rechercher:
        rechercher = False
        # Le nombre de voisins = n² - 2n + 1 :
        for i in range(1, n + 1):
            j = 1
            while j < n + 1:
                if j == i or j == i - 1:
                    j += 1
                else:
                    evaluation += 1
                    voisin = insere(solution, i, j)
                    coutVoisin = cout_max(voisin)[0]
                    if cout > coutVoisin > coutWorst:
                        # Trouver un voisin moin bon améliorant
                        rechercher = True
                        coutWorst = coutVoisin
                        worstSolution = co.copy(voisin)
                    # incrémenter j
                    j += 1
        # redéfinir la solution égale au voisin le moin bon
        solution = worstSolution
        cout = cout_max(solution)[0]
        coutWorst = 0
    return cout_max(solution)[0], solution, evaluation


# Non-Strict
def climber_bestNS_echange(sol):
    solution = co.copy(sol)
    localSolution = co.copy(sol)
    # precedenteSolution = co.copy(sol)
    # Taille de la solution
    n = len(solution)
    cout = cout_max(solution)[0]
    evaluation = 0
    rechercher = True
    # Après 1 M évaluation
    while rechercher and evaluation < 1000000:
        rechercher = False
        # Le nombre de voisins = (n² - n) / 2 :
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                evaluation += 1
                voisin = echange(solution, i, j)
                """
                if np.array_equal(voisin, precedenteSolution):
                    continue
                """
                coutVoisin = cout_max(voisin)[0]
                if cout >= coutVoisin:
                    # A trouvé un voisin améliorant non-strict
                    rechercher = True
                    cout = coutVoisin
                    localSolution = co.copy(voisin)
        # precedenteSolution = solution
        solution = localSolution
        print(evaluation, cout)
    return cout, solution, evaluation


def climber_bestNS_insere(sol):
    solution = co.copy(sol)
    localSolution = co.copy(sol)
    # Taille de la solution
    n = len(solution)
    cout = cout_max(solution)[0]
    rechercher = True
    evaluation = 0
    # Tant qu'on trouve un voisin améliorant
    while rechercher:
        rechercher = False
        # Le nombre de voisins = n² - 2n + 1 :
        for i in range(1, n + 1):
            j = 1
            while j < n + 1:
                if j == i or j == i - 1:
                    j += 1
                # j vérifie la contrainte de coordonnées(i, j) pour insertion
                else:
                    evaluation += 1
                    voisin = insere(solution, i, j)
                    coutVoisin = cout_max(voisin)[0]
                    if cout >= coutVoisin:
                        # a trouvé un voisin améliorant
                        rechercher = True
                        cout = coutVoisin
                        localSolution = co.copy(voisin)
                    # incrémenter j
                    j += 1
        # redéfinir solution pour le meilleur (best) voisin améliorant
        solution = localSolution
        print(evaluation, cout)
    return cout, solution, evaluation


def climber_firstNS_echange(sol):
    solution = co.copy(sol)
    # Taille de la solution
    n = len(solution)
    # Nombre de voisins pour l echange
    N = int(((n ** 2) - n) / 2)
    cout = cout_max(solution)[0]
    rechercher = True
    evaluation = 0
    # Tant qu'on trouve un minimum local
    while rechercher and evaluation < 100000:
        print(evaluation, ' - ', cout)
        rechercher = False
        # Le nombre de voisins = (n² - n) / 2 :
        # Générer tous les voisins
        k = 0
        listVoisins = np.zeros([N, n, len(sol[0])])
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                voisin = echange(solution, i, j)
                listVoisins[k] = voisin
                k += 1
        C = N
        for i in range(C):
            # Choisir un voisin aléatoire
            evaluation += 1
            idx = np.random.randint(C)
            voisinAleatoire = listVoisins[idx]
            s = listVoisins.shape[0]
            coutVoisin = cout_max(voisinAleatoire)[0]
            if cout >= coutVoisin:
                rechercher = True
                cout = coutVoisin
                solution = co.copy(voisinAleatoire)
                break
            # Supprimer l element de la liste des voisins
            else:
                listVoisins = np.delete(listVoisins, idx, axis=0)
                C = C - 1
    return cout, solution, evaluation


def climber_firstNS_insere(sol):
    solution = co.copy(sol)
    # Taille de la solution
    n = len(solution)
    # Le nombre de voisins pour l insertion = (n² - 2n + 1)
    N = int(((n ** 2) - 2 * n + 1))
    cout = cout_max(solution)[0]
    rechercher = True
    evaluation = 0
    # Tant qu'on trouve un minimum local
    while rechercher and evaluation < 100000:
        print(evaluation, ' - ', cout)
        rechercher = False
        # Le nombre de voisins = (n² - 2n + 1)
        # Générer tous les voisins
        k = 0
        listVoisins = np.zeros([N, n, len(sol[0])])
        for i in range(1, n + 1):
            j = 1
            while j < n + 1:
                if j == i or j == i - 1:
                    j += 1
                else:
                    voisin = insere(solution, i, j)
                    listVoisins[k] = voisin
                    k += 1
                    j += 1
        C = N
        for i in range(C):
            # Choisir un voisin aléatoire
            evaluation += 1
            idx = np.random.randint(C)
            voisinAleatoire = listVoisins[idx]
            s = listVoisins.shape[0]
            coutVoisin = cout_max(voisinAleatoire)[0]
            if cout >= coutVoisin:
                rechercher = True
                cout = coutVoisin
                solution = co.copy(voisinAleatoire)
                break
            # Supprimer l element de la liste des voisins
            else:
                listVoisins = np.delete(listVoisins, idx, axis=0)
                C = C - 1
    return cout, solution, evaluation



def climber_NS_echange(sol):
    solution = co.copy(sol)
    # Taille de la solution
    n = len(solution)
    # Nombre de voisins pour l echange
    N = int(((n ** 2) - n) / 2)
    cout = cout_max(solution)[0]
    rechercher = True
    evaluation = 0
    # Tant qu'on trouve un minimum local
    while rechercher and evaluation < 100000:
        print(evaluation, ' - ', cout)
        rechercher = False
        # Le nombre de voisins = (n² - n) / 2 :
        # Générer tous les voisins
        k = 0
        listVoisins = np.zeros([N, n, len(sol[0])])
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                voisin = echange(solution, i, j)
                listVoisins[k] = voisin
                k += 1
        C = N
        for i in range(C):
            # Choisir un voisin aléatoire
            evaluation += 1
            idx = np.random.randint(C)
            voisinAleatoire = listVoisins[idx]
            s = listVoisins.shape[0]
            coutVoisin = cout_max(voisinAleatoire)[0]
            if cout == coutVoisin:
                rechercher = True
                cout = coutVoisin
                solution = co.copy(voisinAleatoire)
                break
            # Supprimer l element de la liste des voisins
            else:
                listVoisins = np.delete(listVoisins, idx, axis=0)
                C = C - 1
    return cout, solution, evaluation


def printConsole(operateur, listCout, listEvaluation):
    print('\nOpérateur -', operateur, '- 100 itérations : ')
    print('Meilleur solution : ', np.min(listCout))
    print('Moyenne de solutions : ', np.mean(listCout))
    print('Nombre moyen d évaluations', np.mean(listEvaluation))
