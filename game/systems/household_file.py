import helper.prints as prints
import helper.randomizer as randomizer
import systems.social_constructs as social_constructs

global households, household, current_sim
households = []
current_sim = None
household = None

SAVE_FILE = "family_save.json"
ACTIVE_HOUSEHOLD_FILE = "active_household.json"

class Household:
    def __init__(self, name, notes=None, save_file=SAVE_FILE):
        self.name = name
        self.members = []
        self.home = None
        self.inventory = []
        self.notes = notes
        self.save_file = save_file

    def add_member(self, person):
        self.members.append(person)
        person.household = self

def find_household(household, households):
    for X in households:
        print(household.name)
    print("A. New Household")

    name = input("Which household do you want? (Type A to get their own household)")
    if name.lower() == "a":
        meow = input("What would you like to name your household? ").strip()
        household = Household(meow)
        households.append(household)
        return household

    elif household.name.lower() == name.lower():
        return household
    
    else:
        print(f"Could not find a household named {name}.")
        return None

class Person:
    def __init__(self, name, sex, temperment, gender=None, age=18, job=None, place_of_work=None, money=0, household=None, notes = None):
        self.name = name
        self.sex = sex
        self.temperment = temperment
        self.gender = gender if gender is not None else sex
        self.age = age
        self.place_of_work = place_of_work
        self.money = money
        self.job = job
        self.household = household
        self.social_categories = {}
        self.social_roles = []
        self.family = []
        self.children = []
        self.parents = []
        self.victims = []
        self.inventory = []
        self.relationships = []
        self.academic_concepts = []
        self.notes = notes

    def make_baby(self, partner, cheat=False):
        if cheat:
            sex = input("Pick a sex!: ")
        else:
            sex = randomizer.randomize_sex()

        print(f"The baby is a {sex}.")

        baby_name = input("What would you like to name the baby? ") 
        baby = Person(baby_name, sex, temperment=randomizer.randomizetemperment(), age=0)

        self.children.append(baby)
        partner.children.append(baby)

        baby.parents.append(self)
        baby.parents.append(partner)

        if self.household is not None:
            self.household.add_member(baby)

        print(f"The baby is named {baby_name}.")
        prints.printstats(baby)

        return baby
    
    def kidnap(self, victim):
        victim.add_social_role("Victim")

        if self.household is not None:
            self.household.add_member(victim)
            self.victims.append(victim)

    def add_social_role(self, role):
        if role not in self.social_roles:
            self.social_roles.append(role)

    def remove_social_role(self, role):
        if role in self.social_roles:
            self.social_roles.remove(role)

    def set_category(self, construct, category):
        if category.name not in construct.categories:
            raise ValueError(
                f"{category.name} is not a category "
                f"of {construct.name}"
            )
        self.social_categories[construct.name] = category

    def get_category(self, construct):
        return self.social_categories.get(construct.name)

    def go_to_work(self, hours_worked=8):
        if self.job:
            daily_pay = self.job.pay * hours_worked
            self.money += daily_pay
            print(f"{self.name} worked {hours_worked} hours!")
            print(f"You earned: ${daily_pay}")   

    def print_inventory(self):
        for item in self.inventory:
            print(f"- {item.name}: ${item.price}")

def create_sim():
    name = input("Name your sim: ")

    if name.lower() == "generic":
        name = "Dawn Moonburrow"
        sex = "Female"
        sprinkles = "Female"
        age = 18
    else:
        sex = input("What is your sim's sex? ").strip()
        sprinkles = input("What is your sim's gender? ").strip()
        age = int(input("What is your sim's age? "))

    sim = Person(
        name,
        sex,
        temperment=randomizer.randomizetemperment(),
        age=age
    )

    category = social_constructs.convert_input_to_gender(sprinkles)

    if category is not None:
        sim.set_category(social_constructs.gender, category)
    else:
        print("That gender doesn't exist!")

    return sim

def create_household(households):
    import systems.save_file as save_file

    name = input("What would you like to name your household? ").strip()

    household = Household(name)
    households.append(household)

    new_sim = create_sim()
    household.add_member(new_sim)

    save_file.save_household(household)
    save_file.save_active_household(household)

    return household

def find_sim(name, households):
    for household in households:
        for member in household.members:
            if member.name.lower() == name.lower():
                return member

    print(f"Could not find a sim named {name}.")
    return None

def switchsim(active_household, households):
    print("\nWho would you like to perform this action?")
    for person in active_household.members:
        prints.printstats(person)

    choice = input("\n> ")

    new_sim = find_sim(choice, households)

    if new_sim is not None:
        print(f"\nYou are now playing as {new_sim.name}.")
        return new_sim