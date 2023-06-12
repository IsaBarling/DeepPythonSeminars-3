from deap import base, creator, tools, algorithms
import random
import numpy as np
MAX_WEIGHT = 25

items = {
    'Палатка': (15, 10),
    'Спальник': (7, 10),
    'Кружка': (1, 1),
    'Еда': (10, 20),
    'Книга': (3, 2),
    'Фонарик': (2, 5),
    'Топор': (5, 10),
    'Компас': (1, 10),
    'Первая помощь': (4, 20),
    'Термос': (2, 5),
    'Костерная решетка': (5, 5),
    'Походная одежда': (7, 15),
    'Карта местности': (1, 10),
    'Спички': (1, 1),
    'Нож': (2, 10),
    'Рюкзак': (3, 10),
    'Спальный мешок': (4, 15),
    'Туристическая котелок': (2, 5),
    'Газовая горелка': (3, 10),
    'Туристический коврик': (2, 5),
    'Подушка': (2, 1),
    'Зажигалка': (1, 5),
    'Комплект посуды': (5, 10),
    'Водонепроницаемые сумки': (3, 10),
    'Палка для ходьбы': (2, 5),
    'Солнцезащитные очки': (1, 2),
    'Защитный крем от солнца': (1, 2),
    'Москитная сетка': (2, 5),
    'Гамак': (7, 10),
    'Кресло-складушка': (5, 1),
    'Туалетная бумага': (1, 1)
}


# инициализация фитнес-функции и индивидуума
creator.create("Fitness", base.Fitness, weights=(-1.0, 1.0))
creator.create("Individual", list, fitness=creator.Fitness)

toolbox = base.Toolbox()

# инициализация атрибутов (0 или 1)
toolbox.register("attr_bool", random.randint, 0, 1)

# инициализация индивидуумов и популяции
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, len(items))
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evalKnapsack(individual):
    weight = sum(individual[i] * list(items.values())[i][0] for i in range(len(individual)))
    value = sum(individual[i] * list(items.values())[i][1] for i in range(len(individual)))
    if weight > MAX_WEIGHT:
        return MAX_WEIGHT, 0
    return weight, value

toolbox.register("evaluate", evalKnapsack)
toolbox.register("mate", tools.cxOnePoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selNSGA2)

def main():
    pop = toolbox.population(n=50)
    hof = tools.HallOfFame(1)
    #stats = tools.Statistics(lambda ind: ind.fitness.values)
    #stats.register("avg", np.mean, axis=0)
    #stats.register("std", np.std, axis=0)
    #stats.register("min", np.min, axis=0)
    #stats.register("max", np.max, axis=0)

    #pop, logbook = algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=40, stats=stats, halloffame=hof)
    pop, logbook = algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=40,  halloffame=hof, verbose=False)
    return pop, logbook, hof

if __name__ == "__main__":
    good = 0
    bad = 0
    for i in range(50):
        pop, log, hof = main()
        #print("Best individual is: %s\nwith fitness: %s" % (hof[0], hof[0].fitness))
        l = []
        for i in items:
            l.append(i)
        total = 0
        listofitems = ""
        for n in range(0, len(hof[0])):
            if(hof[0][n] == 1):
                total += items[l[n]][0]
                listofitems += l[n] + ","
            #total += items[l[i]][0]
        if(total > MAX_WEIGHT):
            bad +=1
        else:
            good += 1
        print("Best individual is: %s\nwith fitness: %s" % (listofitems, hof[0].fitness))
        print("Общая масса\t\t" + str(total))
    print(good, bad)
