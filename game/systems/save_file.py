import json
import os
import systems.household_file as household_file
import systems.social_constructs as social_constructs

SAVE_FILE = "family_save.json"
ACTIVE_HOUSEHOLD_FILE = "active_household.json"


def load_household(save_file=SAVE_FILE):
    if not os.path.exists(save_file):
        return None

    try:
        with open(save_file, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (json.JSONDecodeError, OSError) as error:
        print(f"Could not load {save_file}: {error}")
        return None

    household = household_file.Household(
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
        person = household_file.Person(
                name,
                sex,
                temperment = temperment,
                gender=gender,
                age=age,
                notes=person_data.get("notes"),
            )

    person.money = person_data.get("money", 0)
    person.social_categories = {}

    household.members.append(person)
    person.household = household

    for construct_name, category_name in person_data.get(
        "social_categories", {}
    ).items():
        construct = social_constructs.all_constructs.get(construct_name)

        if construct and category_name in construct.categories:
            person.set_category(
                construct,
                construct.categories[category_name]
            )
        else:
            print(
                f"Could not restore social category "
                f"{category_name!r} for {construct_name!r}."
            )

    return household


def save_household(household):
    if household is None:
        return

    data = {
        "name": household.name,
        "Notes": household.notes,
        "members": [
            {
                "name": person.name,
                "sex": person.sex,
                "gender": person.gender,
                "age": person.age,
                "temperment": person.temperment,
                "social_categories": {
                    construct_name: category.name
                    for construct_name, category in person.social_categories.items()
                },                
                "money": person.money,
            }
            for person in household.members
        ],
    }

    with open(household.save_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def save_active_household(household):
    with open(ACTIVE_HOUSEHOLD_FILE, "w", encoding="utf-8") as file:
        json.dump({"save_file": household.save_file}, file, indent=4)


def get_active_save_file():
    if os.path.exists(ACTIVE_HOUSEHOLD_FILE):
        try:
            with open(ACTIVE_HOUSEHOLD_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)
            save_file = data.get("save_file", SAVE_FILE)
            if os.path.exists(save_file):
                return save_file
        except (json.JSONDecodeError, OSError):
            pass
    return SAVE_FILE

def manage_households(households):
    global household_file, current_sim

    while True:
        print("\n══════ HOUSEHOLD MANAGER ══════")
        print("[B] Create a new household")
        print("[C] Go back")
        
        choice = input("> ").upper()

        if choice == "B":
            name = input("What is the new household's name? ").strip()

            if not name:
                print("Please enter a name.")
                continue

            filename_name = "".join(
                c.lower() if c.isalnum() else "_"
                for c in name
            ).strip("_")

            if not filename_name:
                filename_name = "world"

            filename = f"household_{filename_name}.json"
            counter = 2

            while os.path.exists(filename):
                filename = f"household_{filename_name}_{counter}.json"
                counter += 1

            household = household_file.Household(name, save_file=filename)
            households.append(household)
            sim = household_file.create_sim()
            household.add_member(sim)
            save_household(household)
            save_active_household(household)

            print(f"Created {name}!")
            print(f"Save file: {filename}") 
            print("Created a new household!")
            return

        elif choice == "C":
            return

        else:
            print("Invalid choice.")