jumbled_superheroes = ['DocToR_sTRAngE', 'sPidERmaN', 'MoOn_KnigHT', 'caPTAIN_aMERIca', 'hULK']
decoded_names = []
indices = []
name_lengths = []
for index, name in enumerate(jumbled_superheroes):
    decoded_names.append(name.lower().replace('_', ' '))
    indices.append(index)

name_lengths = list(map(lambda x: len(x), decoded_names))
new_indices = []
temp = list(name_lengths)
temp.sort()
for item in temp:
    for j in range(0, len(name_lengths)):
        if name_lengths[j] == item:
            new_indices.append(indices[j])
print("Phase 5 kickoff list:")
i = 1
for item in new_indices:
    print(f"{i}.{decoded_names[item].title()}")
    i += 1
