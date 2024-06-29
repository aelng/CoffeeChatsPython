# Generation of 15 random aspiring professionals, and 3 random executives
# Properties and availability will be randomized, names are to be assumed as unique
# Check README for file save formatting explanation

import random

# File writer
f = open("testcase.txt", "a")

names = [
    "James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda",
    "William", "Elizabeth", "David", "Barbara", "Richard", "Susan", "Joseph",
    "Jessica", "Thomas", "Sarah", "Charles", "Karen", "Christopher", "Nancy",
    "Daniel", "Lisa", "Matthew", "Ahmed", "Musa", "Betty", "Donald", "Sandra",
    "Mark", "Ashley", "Paul", "Dorothy", "Steven", "Kimberly", "Andrew", "Emily",
    "Kenneth", "Donna", "Joshua", "Michelle", "Kevin", "Carol", "Brian", "Amanda",
    "George", "Melissa", "Edward", "Ali", "Ronald", "Stephanie", "Timothy",
    "Rebecca", "Jason", "Sharon", "Jeffrey", "Laura", "Ryan", "Cynthia", "Jacob",
    "Mustafa", "Gary", "Amy", "Nicholas", "Angela", "Eric", "Arwa", "Jonathan",
    "Anna", "Stephen", "Brenda", "Larry", "Pamela", "Justin", "Nicole", "Scott",
    "Emma", "Brandon", "Helen",
]

interests = [
    "Artificial Intelligence",
    "Machine Learning",
    "Data Structures",
    "Algorithms",
    "Computer Networks",
    "Operating Systems",
    "Databases",
    "Cyber Security",
]

hobbies = [
    "Reading",
    "Cooking",
    "Gardening",
    "Painting",
    "Photography",
    "Traveling",
    "Hiking",
    "Cycling",
]

# Creating boolean array to assure unique names
taken = []
for i in range(80):
    taken.append(False)

# Generating 15 different aspiring professionals and saving to testcase.txt file
for i in range(15):
    rand = random.randint(0, 79)
    if taken[rand]:
        while taken[rand]:
            rand = random.randint(0, 79)
    f.write(names[rand])
    taken[rand] = True
    for i in range(3):
        rand = random.randint(0, 7)
        f.write(interests[rand])
    for i in range(3):
        rand = random.randint(0, 7)
        f.write(hobbies[rand])

