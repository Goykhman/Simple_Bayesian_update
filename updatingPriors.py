import numpy as np
np.random.seed()

import matplotlib.pyplot as plt

def generatePrior(N):
    '''
    Gives prior probability distribution for the parameter taking values
    between 0 and 1 inclusive.
    
    Generate random prior for N points between 0 and 1 inclusive.
    
    Then prior[i] gives prior probability of the parameter = i / (N - 1.0)
    '''
    prior = np.random.random(N)
    return prior / np.sum(prior)

def tossCoin():
    '''
    0 tails
    1 heads
    '''
    r = np.random.random()
    if r <= 0.5:
        return 1
    else:
        return 0

def updateCoin(prior, toss):
    '''
    Prior and posterior are probabilities of toss = 1.
    '''
    posterior = []
    N = len(prior)
    if toss == 1:
        posterior = [(i / (N - 1.0)) * prior[i] for i in range(N)]
    elif toss == 0:
        posterior = [(1 - i / (N - 1.0)) * prior[i] for i in range(N)]
    return posterior / np.sum(posterior)

N = 1001
            
prior = generatePrior(N)

for _ in range(10000):
    toss = tossCoin()
    prior = updateCoin(prior, toss)
    
x = [i / (N - 1.0) for i in range(N)]
posterior = prior
plt.plot(x, posterior)
plt.savefig('posterior.pdf')

maxProb = 0
maxPosterior = 0
for i in range(N):
    if posterior[i] > maxPosterior:
        maxPosterior = posterior[i]
        maxProb = i / (N - 1.0)
        
print maxProb, maxPosterior
    
    