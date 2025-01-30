import random

first_names = [
    "Liam", "Noah", "Oliver", "Elijah", "James", "William", "Benjamin", "Lucas", "Henry", "Alexander",
    "Mason", "Michael", "Ethan", "Daniel", "Jacob", "Logan", "Jackson", "Levi", "Sebastian", "Mateo",
    "Jack", "Owen", "Theodore", "Aiden", "Samuel", "Joseph", "John", "David", "Wyatt", "Matthew",
    "Luke", "Asher", "Carter", "Julian", "Grayson", "Leo", "Jayden", "Gabriel", "Isaac", "Lincoln",
    "Anthony", "Hudson", "Dylan", "Ezra", "Thomas", "Charles", "Christopher", "Jaxon", "Maverick", "Josiah",
    "Isaiah", "Andrew", "Elias", "Joshua", "Nathan", "Caleb", "Ryan", "Adrian", "Miles", "Eli",
    "Nolan", "Christian", "Aaron", "Cameron", "Ezekiel", "Colton", "Luca", "Landon", "Hunter", "Jonathan",
    "Santiago", "Axel", "Easton", "Cooper", "Jeremiah", "Angel", "Roman", "Connor", "Jameson", "Robert",
    "Greyson", "Jordan", "Ian", "Carson", "Jaxson", "Leonardo", "Nicholas", "Dominic", "Austin", "Everett",
    "Brooks", "Xavier", "Kai", "Jose", "Parker", "Adam", "Jace", "Wesley", "Kayden", "Silas",
    "Bennett", "Declan", "Waylon", "Weston"
]

last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
    "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
    "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson",
    "Walker", "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores",
    "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter", "Roberts",
    "Gomez", "Phillips", "Evans", "Turner", "Diaz", "Parker", "Cruz", "Edwards", "Collins", "Reyes",
    "Stewart", "Morris", "Morales", "Murphy", "Cook", "Rogers", "Gutierrez", "Ortiz", "Morgan", "Cooper",
    "Peterson", "Bailey", "Reed", "Kelly", "Howard", "Ramos", "Kim", "Cox", "Ward", "Richardson",
    "Watson", "Brooks", "Chavez", "Wood", "James", "Bennett", "Gray", "Mendoza", "Ruiz", "Hughes",
    "Price", "Alvarez", "Castillo", "Sanders", "Patel", "Myers", "Long", "Ross", "Foster", "Jimenez",
    "Powell", "Jenkins", "Perry", "Russell"
]

occupations = [
    "Accountant", "Actor", "Architect", "Artist", "Astronomer", "Athlete", "Author", "Baker", "Barber", "Bartender",
    "Biologist", "Blacksmith", "Bricklayer", "Bus Driver", "Butcher", "Carpenter", "Cashier", "Chef", "Chemical Engineer", "Civil Engineer",
    "Coach", "Computer Programmer", "Construction Worker", "Consultant", "Counselor", "Dancer", "Dentist", "Designer", "Doctor", "Driver",
    "Economist", "Electrician", "Engineer", "Farmer", "Fashion Designer", "Firefighter", "Fisherman", "Flight Attendant", "Florist", "Geologist",
    "Graphic Designer", "Hairdresser", "Historian", "Hotel Manager", "Human Resources Manager", "Industrial Designer", "Interpreter", "Investigator", "IT Specialist", "Journalist",
    "Judge", "Lawyer", "Librarian", "Lifeguard", "Locksmith", "Logistician", "Machine Operator", "Makeup Artist", "Marine Biologist", "Marketing Manager",
    "Mathematician", "Mechanical Engineer", "Medical Assistant", "Meteorologist", "Microbiologist", "Musician", "Nurse", "Nutritionist", "Occupational Therapist", "Optometrist",
    "Painter", "Paramedic", "Pharmacist", "Photographer", "Physical Therapist", "Physician", "Pilot", "Plumber", "Police Officer", "Politician",
    "Professor", "Psychologist", "Radiologist", "Real Estate Agent", "Receptionist", "Reporter", "Research Scientist", "Restaurant Manager", "Roofer", "Salesperson",
    "Secretary", "Security Guard", "Social Worker", "Software Developer", "Soldier", "Statistician", "Surgeon", "Surveyor", "Teacher", "Technician",
    "Translator", "Travel Agent", "Truck Driver", "Veterinarian", "Video Editor", "Waiter", "Web Developer", "Welder", "Writer", "Zoologist"
]

addresses = [
    "@gmail.com", "@outlook.com", "@hotmail.com", "@byui.edu"
]


def new_fake_person():
    person = f"{random.choice(first_names)} {random.choice(last_names)}, {random.choice(occupations)}"
    return person

#make the file, loop 1 million times generating new names and occupations
def create_file():
    with open("milly.csv", "w") as file:
        count = 0
        while count < 1000000:
            file.write(new_fake_person() + "\n")
            count +=1

if __name__ == '__main__':
    create_file()