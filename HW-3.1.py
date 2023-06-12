import random
import itertools

def find_items_for_backpack(items, max_weight):
    selected_items = []
    not_fitting_items = []
    total_weight = 0

    for item, weight in items.items():
        if total_weight + weight <= max_weight:
            selected_items.append(item)
            total_weight += weight
        else:
            not_fitting_items.append((item, weight))

    if len(not_fitting_items) > 0:
        print("Необходим рюкзак большей грузоподъемности или попросите Ваших друзей взять следующие предметы, которые не влезли в рюкзак:")
        for item, weight in not_fitting_items:
            print(f"{item} (Вес: {weight})")

    return selected_items, total_weight


def generate_item_combinations(items, max_weight):
    item_combinations = []
    item_keys = list(items.keys())

    for r in range(1, len(item_keys) + 1):
        combinations = list(itertools.combinations(item_keys, r))
        item_combinations.extend(combinations)

    filtered_combinations = []

    for combination in item_combinations:
        combination_weights = [items[item] for item in combination]
        if sum(combination_weights) <= max_weight:
            filtered_combinations.append(combination)

    return filtered_combinations


items = {
    "Спальный мещок": 2,
    "Палатка": 5,
    "Бутылка воды": 1,
    "Фонарик": 2,
    "Набор питания": 2,
    "Охотничий нож": 1,
    "Пневмотическое оружие": 1,
    "Компас": 1
}

max_weight = float(input("Введите вес вместимости рюкзака: "))

selected_items, total_weight = find_items_for_backpack(items, max_weight)

print("Выбранные предметы для рюкзака:")
for item in selected_items:
    print(item)

print("Общий вес выбранных предметов:", total_weight)

item_combinations = generate_item_combinations(items, max_weight)
max_combinations = len(item_combinations)
print("Максимальное количество вариантов заполнения рюкзака:", max_combinations)

answer = input("Хотите получить еще один список предметов? (да/нет): ")
if answer.lower() == "да" and item_combinations:
    next_items = item_combinations.pop(0)
    next_weight = sum([items[item] for item in next_items])
    while abs(next_weight - max_weight) > 1 and item_combinations:
        next_items = item_combinations.pop(0)
        next_weight = sum([items[item] for item in next_items])

    if abs(next_weight - max_weight) <= 1:
        print("\nДополнительный список выбранных предметов:")
        for item in next_items:
            print(item)
        print("Общий вес дополнительных предметов:", next_weight)
    else:
        print("\nНет подходящего списка предметов.")
elif answer.lower() == "да":
    print("\nНет доступных вариантов для второго списка предметов.")
else:
    print("\nПриятного путешествия!")
