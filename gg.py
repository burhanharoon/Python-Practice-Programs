import random


def generatePopulation():
    temp = ''
    initialPopulation = []
    for x in range(6):
        for y in range(10):
            temp = temp+str(random.randint(0, 1))
        initialPopulation.append(temp)
        temp = ''
    return initialPopulation


def fitnessOfChromosome(chromosome):
    count = 0
    for i in range(len(chromosome)):
        if chromosome[i] == '1':
            count = count+1
    return count


def calTotalFitness(population):
    total = 0
    for i in range(len(population)):
        total = total+population[i]
    return total


def fitnessRatio(chromFit, totalFitness):
    ratio = int(chromFit/totalFitness*100)
    return ratio


def rouletteChart(population, ratioList):
    rouletteMap = [ratioList[0]]
    length = len(population)
    for i in range(1, length):
        temp = rouletteMap[i-1]+ratioList[i]
        rouletteMap.append(temp)
    return rouletteMap


def newChromosomes(population, rouletteMap, totalRatio):
    newParent = []
    for i in range(6):
        temp = random.randint(0, totalRatio)
        # print("temp", temp)
        if temp <= rouletteMap[0]:
            # print("ok")
            newParent.append(population[0])
        elif temp > rouletteMap[0] and temp <= rouletteMap[1]:
            newParent.append(population[1])
        elif temp > rouletteMap[1] and temp <= rouletteMap[2]:
            newParent.append(population[2])
        elif temp > rouletteMap[2] and temp <= rouletteMap[3]:
            newParent.append(population[3])
        elif temp > rouletteMap[3] and temp <= rouletteMap[4]:
            newParent.append(population[4])
        elif temp > rouletteMap[4] and temp <= rouletteMap[5]:
            newParent.append(population[5])
    return newParent


def crossover(newParent):
    temp1 = ''
    temp2 = ''
    for i in range(3):
        temp = random.randint(0, 9)  # index
        for j in range(temp, 10):
            temp1 = temp1+newParent[i]
        for j in range(temp, 10):
            temp2 = temp2+newParent[i+1]

        for j in range(temp, 10):
            k = 0
            p = newParent[i]
            p[j] = temp2[k]
            k = k+1
        for j in range(temp, 10):
            k = 0
            newParent[i+1][j] = temp1[k]
            k = k+1


initialPopulation = generatePopulation()  # initial population
temp = 0
count = []  # (array) fitness of each chromomsome
totalFitness = 0  # fitness of population
ratioList = []
totalRatio = 0
rouletteMap = []
parents = []
crossoverParents = []

# Calculating fitness of each chromosome
for x in range(6):
    temp = fitnessOfChromosome(initialPopulation[x])
    count.append(temp)
    temp = 0
# Calculating total Fitness
totalFitness = calTotalFitness(count)

# Calculating fitnessRatio
for i in range(len(count)):
    ratioList.append(fitnessRatio(count[i], totalFitness))

# Calculating total Ratio
for i in range(len(ratioList)):
    totalRatio = totalRatio+ratioList[i]

# Calculating Roulette Chart
rouletteMap = rouletteChart(initialPopulation, ratioList)

# Generatign Pairs
parents = newChromosomes(initialPopulation, rouletteMap, totalRatio)

# # Crossover aing parents
# crossoverParents = crossover(parents)

print(initialPopulation)
print(count)
print(totalFitness)
print(ratioList)
print(totalRatio)
print("rouletteMap", rouletteMap)
print("Parents", parents)
print('crossoverPArents', crossoverParents)
