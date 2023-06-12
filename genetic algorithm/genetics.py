import random
from deap import algorithms, base, creator, tools

items = {
    'Палатка': (3, 3),
    'Спальник': (2, 2),
    'Кружка': (1, 1),
    'Еда': (4, 4),
    'Книга': (2, 2),
    'Фонарик': (1, 1),
    'Топор': (5, 5),
    'Компас': (1, 1),
    'Первая помощь': (3, 3),
    'Термос': (2, 2),
    'Костерная решетка': (2, 2),
    'Походная одежда': (4, 4),
    'Карта местности': (1, 1),
    'Спички': (1, 1),
    'Нож': (1, 1),
    'Рюкзак': (2, 2),
    'Спальный мешок': (3, 3),
    'Туристическая котелок': (2, 2),
    'Газовая горелка': (1, 1),
    'Туристический коврик': (1, 1),
    'Подушка': (1, 1),
    'Зажигалка': (1, 1),
    'Комплект посуды': (3, 3),
    'Водонепроницаемые сумки': (2, 2),
    'Палка для ходьбы': (1, 1),
    'Солнцезащитные очки': (1, 1),
    'Защитный крем от солнца': (1, 1),
    'Москитная сетка': (1, 1),
    'Гамак': (2, 2),
    'Кресло-складушка': (2, 2),
    'Туалетная бумага': (1, 1)
}

hof = tools.HallOfFame(maxsize=10)

def evaluate(individual):
    weight = 0
    value = 0
    for i in range(len(individual)):
        if individual[i]:
            item_name = list(items.keys())[i]
            weight += items[item_name][0]
            value += items[item_name][1]
    if weight > max_capacity:
        return 0,
    return value,

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("attr_bool", random.randint, 0, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=len(items))
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", evaluate)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

def main():
    random.seed(42)

    population = toolbox.population(n=100)

    fitnesses = list(map(toolbox.evaluate, population))
    for ind, fit in zip(population, fitnesses):
        ind.fitness.values = fit

    for generation in range(50):
        offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.1)
        fits = toolbox.map(toolbox.evaluate, offspring)
        for ind, fit in zip(offspring, fits):
            ind.fitness.values = fit
        population = toolbox.select(offspring + population, k=len(population))

        top_individuals = tools.selBest(population, k=10)
        hof.update(top_individuals)

        best_fitness = hof[0].fitness.values[0]
        print("Поколение", generation+1, "- Лучшая приспособленность:", best_fitness)

    print("\nНайдено", len(hof), "возможных вариантов упаковки рюкзака:")
    for i, solution in enumerate(hof):
        print("Вариант", i+1, ":")
        for j in range(len(solution)):
            if solution[j]:
                print("-", list(items.keys())[j])
        print()

    choice = input("Желаете еще увидеть варианты упаковки? (да/нет): ")
    while choice.lower() == "да":
        new_solution = random.choice(hof)
        print("Случайный вариант:")
        for j in range(len(new_solution)):
            if new_solution[j]:
                print("-", list(items.keys())[j])
        print()
        choice = input("Желаете еще увидеть варианты упаковки? (да/нет): ")

if __name__ == "__main__":
    max_capacity = int(input("Введите вес рюкзака: "))
    main()
