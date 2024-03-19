people : list[str] = ['Abir', 'Abit', 'Raihan Mahmud', 'Aditto']

long_names: list[str] = []

for person in people:
    if len(person)>7:
        long_names.append(person)

long_names_comp: list[str] = [person for person in people if len(person)>7]

print(f'Long Names{long_names}')
print(f'Long Names with list comprehension{long_names_comp}')