# analysis.py
# -----------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question2():
    # Fatores de desconto mais alto, incentivam o agente a explorar os
    # estados em busca de uma recompensa melhor. Ao alterar o Noise,
    # fazemos com que o agente tenha maior probabilidade de alcançar 
    # essa utilidade.
    answerDiscount = 0.9
    answerNoise = 0
    return answerDiscount, answerNoise

def question3a():
    # O agente deve ser incentivado a pegar recompensas mais cedo atra- 
    # vés de um fator de desconto baixo. Além disso, o agente deve ser
    # incentivado a pegar o caminho mais curto com uma recompensa de vi
    # baixa e um noise baixo (o que representa um risco menor de errar)
    answerDiscount = 0.1
    answerNoise = 0
    answerLivingReward = 0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3b():
    answerDiscount = 0.1
    answerNoise = 0.1
    answerLivingReward = 0.1
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3c():
    # O fator de desconto deve ser alto para que se incentive a ir bus
    # car a recompensa mais longe, além disso para incentivar o caminho
    # mais curto deve-se inibir os movimentos errados com um ruído baixo
    # e uma recompensa de vida baixa. (Desconto de 1 fazem que o agente
    # não busque ir atrás da recompensa)

    answerDiscount = 0.9
    answerNoise = 0
    answerLivingReward = 0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3d():
    # O fator de desconto deve ser alto para que se incentive a ir bus
    # car a recompensa mais longe, além disso para incentivar o caminho
    # mais longo, fazendo que haja uma probabilidade significativa de 
    # ruído aliado a um incentivo de vida descente.

    answerDiscount = 0.9
    answerNoise = 0.2
    answerLivingReward = 0.5
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3e():
    # Deve-se desincentivar o agente a chegar a um estado terminal através
    # de um fator de deconto muito baixo e uma recompensa de vida alta. O
    # ruído baixo impede que o agente receba baixas recompensas sem querer.

    answerDiscount = 0
    answerNoise = 0
    answerLivingReward = 1
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question8():
    answerEpsilon = None
    answerLearningRate = None
    # return answerEpsilon, answerLearningRate
    return 'NOT POSSIBLE'
    # If not possible, return 'NOT POSSIBLE'

if __name__ == '__main__':
    print('Answers to analysis questions:')
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print('  Question %s:\t%s' % (q, str(response)))
