# Question8 : Algorithme de Descente
import numpy as np
from Functions import climber_best_echange, climber_best_insere, cout_max, generate_solution, data_to_matrix, \
    read_txt_data, climber_first_echange, climber_first_insere

data = read_txt_data()
[N, M, T, D, S] = data_to_matrix(data)

[_solution, rn, rm] = generate_solution(N, M, D)
_cout = cout_max(_solution)[0]

size = 100
listLocalEchange = np.empty(0)
listLocalInsere = np.empty(0)

listEvaluationLocalEchange = np.empty(0)
listEvaluationLocalInsere = np.empty(0)
for i in range(size):
    # Appel de fonctions Climber Best (Echange & Insere)
    coutBestEchange, solutionBestEchagne, evaluationBestEchange = climber_best_echange(_solution)
    coutBestInsere, solutionBestInsere, evaluationBestInsere = climber_best_insere(_solution)
    # Moyenne
    listLocalEchange = np.append(listLocalEchange, coutBestEchange)
    listLocalInsere = np.append(listLocalInsere, coutBestInsere)
    # Evaluation
    listEvaluationLocalEchange = np.append(listEvaluationLocalEchange, evaluationBestEchange)
    listEvaluationLocalInsere = np.append(listEvaluationLocalInsere, evaluationBestInsere)
    # Nouvelle Solution
    _solution = generate_solution(N, M, D)[0]

print('\n------Algorithme Best-------')
print('\nOpérateur - Echange - 100 itérations : ')
print('Meilleur solution : ', np.min(listLocalEchange))
print('Moyenne de solutions : ', np.mean(listLocalEchange))
print('Nombre moyen d évaluations', np.mean(listEvaluationLocalEchange))
print('')
print('Opérateur - Insere - 100 itérations : ')
print('Meilleur solution : ', np.min(listLocalInsere))
print('Moyenne de solutions : ', np.mean(listLocalInsere))
print('Nombre moyen d évaluations', np.mean(listEvaluationLocalInsere))

listLocalEchange = np.empty(0)
listLocalInsere = np.empty(0)

listEvaluationLocalEchange = np.empty(0)
listEvaluationLocalInsere = np.empty(0)

for i in range(size):
    # Appel de fonctions Climber First (Echange & Insere)
    coutFirstEchange, solutionFirstEchagne, evaluationFirstEchange = climber_first_echange(_solution)
    coutFirstInsere, solutionFirstInsere, evaluationFirstInsere = climber_first_insere(_solution)

    # Moyenne
    listLocalEchange = np.append(listLocalEchange, coutFirstEchange)
    listLocalInsere= np.append(listLocalInsere, coutFirstInsere)
    # Echange
    listEvaluationLocalEchange = np.append(listEvaluationLocalEchange, evaluationFirstEchange)
    listEvaluationLocalInsere = np.append(listEvaluationLocalInsere, evaluationFirstInsere)
    # Nouvelle Solution
    _solution = generate_solution(N, M, D)[0]

print('\n------Algorithme First-------')
print('\nOpérateur - Echange - 100 itérations : ')
print('Meilleur solution : ', np.min(listLocalEchange))
print('Moyenne de solutions : ', np.mean(listLocalEchange))
print('Nombre moyen d évaluations', np.mean(listEvaluationLocalEchange))
print('')
print('Opérateur - Insere - 100 itérations : ')
print('Meilleur solution : ', np.min(listLocalInsere))
print('Moyenne de solutions : ', np.mean(listLocalInsere))
print('Nombre moyen d évaluations', np.mean(listEvaluationLocalInsere))
