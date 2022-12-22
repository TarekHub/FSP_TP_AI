# Question9 : Algorithme de Descente Non-Stricte
import numpy as np

from Functions import cout_max, generate_solution, data_to_matrix, \
    read_txt_data, printConsole, climber_bestNS_echange, climber_bestNS_insere, climber_firstNS_echange, \
    climber_firstNS_insere, climber_NS_echange

data = read_txt_data()
[N, M, T, D, S] = data_to_matrix(data)
size = 100
[_solution, rn, rm] = generate_solution(N, M, D)

listLocalEchangeBest = np.empty(0)
listLocalInsereBest = np.empty(0)
listEvaluationLocalEchangeBest = np.empty(0)
listEvaluationLocalInsereBest = np.empty(0)

listLocalEchangeFirst = np.empty(0)
listLocalInsereFirst = np.empty(0)
listEvaluationLocalEchangeFirst = np.empty(0)
listEvaluationLocalInsereFirst = np.empty(0)

listLocalEchangeNS = np.empty(0)
listLocalInsereNS = np.empty(0)
listEvaluationLocalEchangeNS = np.empty(0)
listEvaluationLocalInsereNS = np.empty(0)

for i in range(5):
    """
    # Appel de fonctions Climber Best  NS (Echange & Insere)
    # coutBestEchange, solutionFirstEchange, evaluationBestEchange = climber_bestNS_echange(_solution)
    coutBestInsere, solutionBestEchange, evaluationBestInsere = climber_bestNS_insere(_solution)
    # Moyenne
    # listLocalEchangeBest = np.append(listLocalEchangeBest, coutBestEchange)
    listLocalInsereBest = np.append(listLocalInsereBest, coutBestInsere)
    # Evaluation
    # listEvaluationLocalEchangeBest = np.append(listEvaluationLocalEchangeBest, evaluationBestEchange)
    listEvaluationLocalInsereBest = np.append(listEvaluationLocalInsereBest, evaluationBestInsere)
    """
    """
    # Appel de fonctions Climber First NS (Echange & Insere)
    coutFirstEchange, solutionFirstEchange, evaluationFirstEchange = climber_firstNS_echange(_solution)
    coutFirstInsere, solutionFirstInsere, evaluationFirstInsere = climber_firstNS_insere(_solution)
    # Moyenne
    listLocalEchangeFirst = np.append(listLocalEchangeFirst, coutFirstEchange)
    listLocalInsereFirst = np.append(listLocalInsereFirst, coutFirstInsere)
    # Evaluation
    listEvaluationLocalEchangeFirst = np.append(listEvaluationLocalEchangeFirst, evaluationFirstEchange)
    listEvaluationLocalInsereFirst = np.append(listEvaluationLocalInsereFirst, evaluationFirstInsere)
    """
    # Appel de fonctions Climber NS (Echange & Insere)
    coutNSEchange, solutionNSEchange, evaluationNSEchange = climber_NS_echange(_solution)
    #coutFirstInsere, solutionFirstInsere, evaluationFirstInsere = climber_firstNS_insere(_solution)
    # Moyenne
    listLocalEchangeNS = np.append(listLocalEchangeNS, coutNSEchange)
    #listLocalInsereFirst = np.append(listLocalInsereFirst, coutFirstInsere)
    # Evaluation
    listEvaluationLocalEchangeNS = np.append(listEvaluationLocalEchangeNS, evaluationNSEchange)
    #listEvaluationLocalInsereFirst = np.append(listEvaluationLocalInsereFirst, evaluationFirstInsere)


    _solution = generate_solution(N, M, D)[0]

# print('\n------Algorithme Best-------')
# printConsole('Echange', listLocalEchangeBest, listEvaluationLocalEchangeBest)
# printConsole('Insere', listLocalInsereBest, listEvaluationLocalInsereBest)

#print('\n------Algorithme First-------')
#printConsole('Echange', listLocalEchangeFirst, listEvaluationLocalEchangeFirst)
#printConsole('Insere', listLocalInsereFirst, listEvaluationLocalInsereFirst)

print('\n------Algorithme NS-------')
printConsole('Echange', listLocalEchangeNS, listEvaluationLocalEchangeNS)
#printConsole('Insere', listLocalInsereFirst, listEvaluationLocalInsereFirst)
