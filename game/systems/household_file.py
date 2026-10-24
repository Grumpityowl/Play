import useful.randomizer as randomizer
import useful.prints as prints
import systems.save_file as save_file
import json
import os

global households, household, current_sim
households = []
current_sim = None
household = None


SAVE_FILE = "family_save.json"
ACTIVE_HOUSEHOLD_FILE = "active_household.json"

class Household:
    def __init__(self, name, notes=None, save_file=save_file.SAVE_FILE):
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
        self.social_categories = []
        self.skills = []
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
        gender = "Female"
        age = 18
    else:
        sex = input("What is your sim's sex? ").strip()
        gender = input("What is your sim's gender? ").strip()
        age = int(input("What is your sim's age? "))

    sim = Person(name, sex, temperment = randomizer.randomizetemperment(), gender=gender, age=age)
    
    return sim

def create_household(households):
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

def load_household(save_file=SAVE_FILE):
    if not os.path.exists(save_file):
        return None

    try:
        with open(save_file, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (json.JSONDecodeError, OSError) as error:
        print(f"Could not load {save_file}: {error}")
        return None

    household = Household(
        data.get("name", "Unnamed Household"),
        notes=data.get("Notes"),
        save_file=save_file,
    )

    for person_data in data.get("members", []):
        name = person_data.get("name", "Unnamed Sim")
        sex = person_data.get("sex", "Female")
        gender = person_data.get("gender", sex)
        age = person_data.get("age", 18)
        temperment = person_data.get("temperment", "blissful")
        person = Person(
                name,
                sex,
                temperment = temperment,
                gender=gender,
                age=age,
                notes=person_data.get("notes"),
            )

        person.money = person_data.get("money", 0)

        household.members.append(person)
        person.household = household

    return household

def start_up():
    active_household = save_file.load_household(save_file.get_active_save_file())
    world_name = input("What would you like to name your world? ").strip()

    if active_household == None:
        household_name = input("What would you like to name your household? ")
        active_household = Household(household_name)

    if not active_household.members:
        sim = create_sim()
        active_household.add_member(sim)
        save_file.save_household(active_household)
        save_file.save_active_household(active_household)

    if active_household is not None:
        households.append(active_household)
    current_sim = active_household.members[0]
    print(f"Welcome back to {active_household.name}!")
    gameplay_loop(current_sim, active_household, world_name, households, household)


def gameplay_loop(current_sim, active_household, world_name, households, household):
    while True:
        prints.print_World(household, world_name, households)
        answer = input(
            "          What shall we do today?\n"
            "\n"
            "          [A] ✿  Have Baby\n"
            "          [B] ❀  Learn Skill\n"
            "          [C] ❋  Fish\n"
            "          [D] ♡  Create a Sim\n"
            "          [E] ⚝  Switch/Create Household\n"
            "          [F] ✎  Notes\n"
            "\n"
            "          Type END to leave the game.\n"
            "\n"
            "      ──────── ⋆｡°✩°｡⋆ ────────\n"
            "\n"
            "          Cast your choice: "
        ).strip().upper()
        
        if answer == "END":
            break

        elif answer == "A":
            prints.print_households()
            current_sim = switchsim(active_household)
            prints.print_households()
            partner_sim = switchsim(active_household)

            if partner_sim is not None and partner_sim is not current_sim:
                current_sim.make_baby(partner_sim)
            else:
                print("Choose a different Sim as the other parent.")

        elif answer == "C":
            if current_sim is None:
                print("Select a Sim first.")
                continue

            current_sim = switchsim(active_household)

            if current_sim is not None:
                activities.fish(current_sim)

        elif answer == "D":
            sim = create_sim()
            household = find_household(active_household, households)
            household.add_member(sim)

            if sim is not None:
                current_sim = sim

        elif answer == "E":
            save_file.manage_households(households)
            current_sim = (
                active_household.members[0]
            )

        elif answer == "F":
            sim.update_notes()

        else:
            print("Invalid choice. Please select A-F or END.")

    return current_sim