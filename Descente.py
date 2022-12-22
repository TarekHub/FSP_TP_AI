# Question8 : Algorithme de Descente
import numpy as np
from Functions import cout_max, generate_solution, data_to_matrix, \
    read_txt_data, printConsole, climber_first_echange, climber_first_insere, \
    climber_best_insere, climber_best_echange, climber_worst_echange, climber_worst_insere

data = read_txt_data()
[N, M, T, D, S] = data_to_matrix(data)

[_solution, rn, rm] = generate_solution(N, M, D)
_cout = cout_max(_solution)[0]

size = 100

listLocalEchangeBest = np.empty(0)
listLocalInsereBest = np.empty(0)
listEvaluationLocalEchangeBest = np.empty(0)
listEvaluationLocalInsereBest = np.empty(0)

listLocalEchangeFirst = np.empty(0)
listLocalInsereFirst = np.empty(0)
listEvaluationLocalEchangeFirst = np.empty(0)
listEvaluationLocalInsereFirst = np.empty(0)

listLocalEchangeWorst = np.empty(0)
listLocalInsereWorst = np.empty(0)
listEvaluationLocalEchangeWorst = np.empty(0)
listEvaluationLocalInsereWorst = np.empty(0)

for i in range(size):
    # Appel de fonctions Climber First (Echange & Insere)
    coutFirstEchange, solutionFirstEchange, evaluationFirstEchange = climber_first_echange(_solution)
    coutFirstInsere, solutionFirstInsere, evaluationFirstInsere = climber_first_insere(_solution)

    # Moyenne
    listLocalEchangeFirst = np.append(listLocalEchangeFirst, coutFirstEchange)
    listLocalInsereFirst = np.append(listLocalInsereFirst, coutFirstInsere)
    # Evaluation
    listEvaluationLocalEchangeFirst = np.append(listEvaluationLocalEchangeFirst, evaluationFirstEchange)
    listEvaluationLocalInsereFirst = np.append(listEvaluationLocalInsereFirst, evaluationFirstInsere)

    # Appel de fonctions Climber Best (Echange & Insere)
    coutBestEchange, solutionBestEchange, evaluationBestEchange = climber_best_echange(_solution)
    coutBestInsere, solutionBestInsere, evaluationBestInsere = climber_best_insere(_solution)
    # Moyenne
    listLocalEchangeBest = np.append(listLocalEchangeBest, coutBestEchange)
    listLocalInsereBest = np.append(listLocalInsereBest, coutBestInsere)
    # Evaluation
    listEvaluationLocalEchangeBest = np.append(listEvaluationLocalEchangeBest, evaluationBestEchange)
    listEvaluationLocalInsereBest = np.append(listEvaluationLocalInsereBest, evaluationBestInsere)


    # Appel de fonctions Climber Worst (Echange & Insere)
    coutWorstEchange, solutionWorstEchange, evaluationWorstEchange = climber_worst_echange(_solution)
    coutWorstInsere, solutionWorstInsere, evaluationWorstInsere = climber_worst_insere(_solution)
    # Moyenne
    listLocalEchangeWorst = np.append(listLocalEchangeWorst, coutWorstEchange)
    listLocalInsereWorst = np.append(listLocalInsereWorst, coutWorstInsere)
    # Evaluation
    listEvaluationLocalEchangeWorst = np.append(listEvaluationLocalEchangeWorst, evaluationWorstEchange)
    listEvaluationLocalInsereWorst = np.append(listEvaluationLocalInsereWorst, evaluationWorstInsere)

    # Nouvelle Solution
    _solution = generate_solution(N, M, D)[0]

    print(i)

print('\n------Algorithme First-------')
printConsole('Echange', listLocalEchangeFirst, listEvaluationLocalEchangeFirst)
printConsole('Insere', listLocalInsereFirst, listEvaluationLocalInsereFirst)

print('\n------Algorithme Best-------')
printConsole('Echange', listLocalEchangeBest, listEvaluationLocalEchangeBest)
printConsole('Insere', listLocalInsereBest, listEvaluationLocalInsereBest)

print('\n------Algorithme Worst-------')
printConsole('Echange', listLocalEchangeWorst, listEvaluationLocalEchangeWorst)
printConsole('Insere', listLocalInsereWorst, listEvaluationLocalInsereWorst)
