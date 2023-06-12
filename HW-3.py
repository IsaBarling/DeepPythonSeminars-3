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
