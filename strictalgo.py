# Profession, Interests (up to 3), Availability - 24 hour time
aspiring = [
    {'Name': "Musa", 'Profession': "programming", 'Interests': ['AI', 'ML'], 'Availability': 12},
    {'Name': "George", 'Profession': "programming", 'Interests': ['AI', 'ML'], 'Availability': 12},
    {'Name': "Joseph", 'Profession': "programming", 'Interests': ['AI', 'ML'], 'Availability': 12}
]

executive = [
    {'Name': "Daniel", 'Profession': "programming", 'Interests': ['AI', 'ML'], 'Availability': 12, 'Frequency': 1}
]

chats = []

for prof in aspiring:
    for ex in executive:
        # Matching score - points awarded out of 10 that determine if a professional and executive are a good match
        Mscore = 0
        if prof['Profession'] == ex['Profession']:
            Mscore+=4
        if prof['Availability'] == ex['Availability']:
            Mscore+=3
        for i in range(2):
            if ex['Interests'].__contains__(prof['Interests'][i]):
                Mscore+=1

    # If matching score is high enough, and the executive has less than 3 already planned coffee chats, create another
    if Mscore > 7 and ex['Frequency'] < 3:
        chats.append ({'Aspiring': prof['Name'], 'Executive': ex['Name']})
        ex['Frequency'] += 1

# list out chats
print("Scheduled chats:")
for chat in chats:
    print(chat['Aspiring'], "and", chat['Executive'])