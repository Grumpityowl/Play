
def printstats(person):
    social = ""

    if person.social_categories:
        categories = []

        for construct_name, category in person.social_categories.items():
            categories.append(f"{construct_name}: {category.name}")

        social = ", " + ", ".join(categories)

    print(
        f"Name: {person.name}, "
        f"Personality: {person.temperment}"
        f"{social}, "
        f"Money: {person.money}"
    )


def print_family(person):
        print(f"Name: {person.name}")
        print(f"Sex: {person.sex}")

        print("\nParents:")
        for person in person.parents:
            print(f"- {person.name}")

        print("\nChildren:")
        for person in person.children:
            print(f"- {person.name}")

        print("\nFamily:")
        for person in person.family:
            print(f"- {person.name}")

def print_household(person):
    print("\nHousehold:")
    if person.household is not None:
        for member in person.household.members:
            print(
                f"  - {member.name}, Age: {member.age}, "
                f"Sex: {member.sex}, Money: ${member.money}"
            )
    else:
        print("No household")

def print_World(household, world_name, households):
    print(f"\n═══════ ✧ {world_name} ✧ ═══════")

    for household in households:
        print(f"\n⌂ Household: {household.name}")

        if not household.members:
            print("  No members.")
            continue

        for person in household.members:
            printstats(person)

    print("\n═════════════════════════")

def print_households(households):
    for household in households:
        print(f"\n{household.name}:")
        for member in household.members:
            print_household(member)

def print_household_finances(person):
    if person.household:
        total = 0
        for person in person.household.members:
            total += person.money
        print(f"Household Finances: ${total}")

def printclassroom(classroom):
    print(f"\n{classroom.name} - Grade {classroom.grade} - Magic Season: {classroom.magic_season}\n")
    print("TEACHERS")

    for witch in classroom.teachers:
        print(witch.name, "-", witch.gender)

    print("\nSTUDENTS")

    for _, witch in enumerate(classroom.students):
        print(
            _ + 1,
            "-",
            witch.name,
            "-",
            witch.gender,
                            )