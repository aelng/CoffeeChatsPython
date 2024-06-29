# Profession, Interests (up to 3), Hobbies (up to 3)
aspiring = [
    {'Name': "Musa", 'Profession': "programming", 'Interests': ['AI', 'ML', 'Cloud Computing'], 'Hobbies': ['Basketball', 'Chess', "Golf"]},
    {'Name': "George", 'Profession': "programming", 'Interests': ['AI', 'ML', 'Cloud Computing'], 'Hobbies': ['Basketball', 'Chess', "Golf"]},
    {'Name': "Joseph", 'Profession': "programming", 'Interests': ['AI', 'ML', 'jo'], 'Hobbies': ['Basketball', 'Chess', "Golf"]}
]

# 5 days per week, start time to end time (24-hour format)
aspireav = {
    'Musa': [[8, 17], [8, 17], [8, 17], [8, 17], [8, 17]],
    'George': [[8, 17], [8, 17], [8, 17], [8, 17], [8, 17]],
    'Joseph': [[8, 17], [8, 17], [8, 17], [8, 17], [8, 17]],
}

executive = [
    {'Name': "Daniel", 'Profession': "programming", 'Interests': ['AI', 'ML', 'Cloud Computing'], 'Hobbies': ['Basketball', 'Chess', "Golf"]}
]

execav = {
    'Daniel': [[8, 9], [2, 2], [2, 2], [2, 2], [2, 2]],
}

rankings = []

for ex in executive:
    rankings.append({'Name': ex['Name'], 'people': []})

chats = []

for ex in executive:
    for prof in aspiring:

        # Matching score - points awarded out of 10 that determine if a professional and executive are a good match
        Mscore = 0
        if prof['Profession'] == ex['Profession']:
            Mscore+=4
        for i in range(3):
            if ex['Interests'].__contains__(prof['Interests'][i]):
                Mscore+=1
        for i in range(3):
            if ex['Hobbies'].__contains__(prof['Hobbies'][i]):
                Mscore+=1

        # Placing aspiring professional on a list of the executives coffee chat rankings (with a frequency cut off)
        for ran in rankings:
            if ran['Name'] == ex['Name']:
                new_pair = (prof['Name'], Mscore)
                ran['people'].append(new_pair)

        # Sorting the aspiring professionals by matching score
        for ran in rankings:
            if ran['Name'] == ex['Name']:
                ran['people'] = sorted(ran['people'], key=lambda x: (x[1], x[0]))
                ran['people'].reverse()

for ex in executive:
    freq = 0  # The number of meetings scheduled already (maximizes at 2)
    # Scheduling coffee chats with aspiring professionals that have the highest matching score and the same availability
    for ran in rankings:
        if ran['Name'] == ex['Name']:
            for j in ran['people']:
                aspname = j[0]
                execname = ran['Name']
                for i in range(5):
                    if aspireav[aspname][i][0] >= execav[execname][i][0] and aspireav[aspname][i][0] <= execav[execname][i][1] or aspireav[aspname][i][1] >= execav[execname][i][0] and aspireav[aspname][i][1] <= execav[execname][i][1]:
                        if freq < 2:
                            freq+=1
                            chats.append(execname + " and " + aspname)
                            break

# List out coffee chats
print("Coffee chats:")
for chat in chats:
    print(chat)