friends = {
    'Алексей': {'ручка', 'ноутбук', 'компас', 'фонарик', 'компас', 'спальник', 'рюкзак'},
    'Мария': {'компас', 'фотоаппарат', 'очки', 'палатка', 'переносной гриль', 'спальный мешок'},
    'Иван': {'компас', 'ручка', 'книга', 'термос', 'противомоскитная сетка', 'палатка'}
}

# Какие предметы взяли все три друга
common_items = set.intersection(*friends.values())

# Какие предметы уникальны, есть только у одного друга
unique_items = set.union(*friends.values()) - common_items

# Какие предметы есть у всех друзей кроме одного
missing_items = set()
for friend, items in friends.items():
    other_friends = set.union(*(friends[f] for f in friends if f != friend))
    missing = other_friends - items
    missing_items.update(missing)

print("Предметы, взятые всеми тремя друзьями:", common_items)
print("Уникальные предметы, есть только у одного друга:", unique_items)
print("Предметы, есть у всех кроме одного друга и имя друга, у которого данный предмет отсутствует:")
for item in missing_items:
    for friend, items in friends.items():
        if item not in items:
            print(f"Предмет: {item}, Отсутствует у друга: {friend}")
