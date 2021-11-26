import random
import os


def clear(): return os.system('cls')


clear()


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
    for i in range(len(population)):
        temp = random.randint(0, totalRatio)
        if temp <= rouletteMap[0]:
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


def crossover(population):
    crossoverParents = []
    for i in range(0, 6, 2):
        index = random.randint(0, 9)  # index
        # print("Index {} ".format(index))
        # # temp1 contains the string to be interchanged with 2nd pair
        # temp1 = population[i][index:len(population[i])]
        # # temp2 contains the string to be interchanged with 1st pair
        # temp2 = population[i+1][index:len(population[i+1])]
        # result = population[i][:index]+temp2
        # crossoverParents.append(result)
        # result = population[i+1][:index]+temp1
        # crossoverParents.append(result)

        unchange1 = population[i][:index]
        unchange2 = population[i+1][:index]
        # print("Unchange1 {} Unchange2 {}".format(unchange1, unchange2))
        temp1 = population[i][index:len(population[i])]
        temp2 = population[i+1][index:len(population[i+1])]
        result = unchange1+temp2
        crossoverParents.append(result)
        result = ''
        result = unchange2+temp1
        crossoverParents.append(result)

    return crossoverParents


def mutation(population):
    newPopulation = []
    for i in range(len(population)):
        index = random.randint(0, 9)  # index
        value = str(random.randint(0, 1))  # value
        temp = population[i][:index]+value+population[i][index+1:]
        # print("Index {} Value {} Mutation {}".format(index, value, temp))
        newPopulation.append(temp)
        temp = ''
    return newPopulation


initialPopulation = generatePopulation()  # initial population


totalFitness = 0  # fitness of population


tries = 0

while totalFitness <= 20:

    fitnesses = []  # (array) fitness of each chromomsome
    ratioList = []
    totalRatio = 0
    rouletteMap = []
    parents = []  # pair of parents after roulette mapping
    crossoverParents = []
    mutationParents = []

    # Calculating fitness of each chromosome
    for i in range(len(initialPopulation)):
        temp = fitnessOfChromosome(initialPopulation[i])
        fitnesses.append(temp)
        temp = 0

    # Calculating total Fitness
    totalFitness = calTotalFitness(fitnesses)

    # Calculating fitnessRatio
    for i in range(len(fitnesses)):
        ratioList.append(fitnessRatio(fitnesses[i], totalFitness))

    # Calculating total Ratio
    for i in range(len(ratioList)):
        totalRatio = totalRatio+ratioList[i]

    # Calculating Roulette Chart
    rouletteMap = rouletteChart(initialPopulation, ratioList)

    # Generatign Pairs
    parents = newChromosomes(initialPopulation, rouletteMap, totalRatio)

    # Generating new parents after crossover
    crossoverParents = crossover(parents)

    mutationParents = mutation(crossoverParents)

    initialPopulation = []
    initialPopulation = mutationParents

    tries = tries+1

print("No of tries", tries)
print("Population", initialPopulation)
print("Fitness of each chromosome", fitnesses)
print("Total Fitness", totalFitness)
print("Ratio of each chromosome", ratioList)
print("Total Ratio", totalRatio)
print("Roulette Map", rouletteMap)
print("New Parents", parents)
print('Crossover Parents', crossoverParents)
print('Mutation Parents', mutationParents)
