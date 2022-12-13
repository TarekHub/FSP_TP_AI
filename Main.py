# Work done by : Boufar Tarek & Chouaha Bela
import random


# region Functions
def read_txt_data():
    with open('./Instance/20_5_01_ta001.txt', 'r') as f:
        lines = f.readlines()
    return lines


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

# Fonction qui génére une solution aléatoire
def generate_random_solution(n, m, T):
    rand = list(range(1, m+1))
    random.shuffle(rand)




# endregion

# region Main
data = read_txt_data()
[N, M, S, T, D] = data_to_matrix(data)
generate_random_solution(N, M, D)


print(N, " job,", M, " machines", "seed : ", S)
print("Dates fin souhaitées :", T)
print("Temps d'éxécutions:", D)
# endregion
