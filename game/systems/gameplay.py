import systems.save_file as save_file
import systems.household_file as household_file
import systems.social_constructs as social_constructs
import helper.prints as prints

def start_up():
    active_household = save_file.load_household(save_file.get_active_save_file())
    #world_name = input("What would you like to name your world? ").strip()
    world_name = "Blorbles"

    if active_household == None:
        household_name = input("What would you like to name your household? ")
        active_household = household_file.Household(household_name)

    if not active_household.members:
        sim = household_file.create_sim()
        active_household.add_member(sim)
        save_file.save_household(active_household)
        save_file.save_active_household(active_household)

    if active_household is not None:
        household_file.households.append(active_household)
    current_sim = active_household.members[0]
    print(f"Welcome back to {active_household.name}!")
    gameplay_loop(current_sim, active_household, world_name, household_file.households, household_file.household)

def gameplay_loop(current_sim, active_household, world_name, households, household):
    while True:
        prints.print_World(household, world_name, households)
        answer = input(
            "          What shall we do today?\n"
            "\n"
            "          [A] ✿  Have Baby\n"
            "          [C] ❋  Fish\n"
            "          [D] ♡  Create a Sim\n"
            "          [E] ⚝  Switch/Create Household\n"
            "          [F] ✎  Notes\n"
            "          [G]     Assign Social Category\n"
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
            prints.print_households(households)
            current_sim = household_file.switchsim(active_household, households)
            prints.print_households(households)
            partner_sim = household_file.switchsim(active_household, households)

            if partner_sim is not None and partner_sim is not current_sim:
                current_sim.make_baby(partner_sim)
            else:
                print("Choose a different Sim as the other parent.")

        elif answer == "C":
            prints.print_households(households)
            if current_sim is None:
                print("Select a Sim first.")
                continue

            current_sim = household_file.switchsim(active_household, households)

            if current_sim is not None:
                activities.fish(current_sim)

        elif answer == "D":
            sim = household_file.create_sim()
            household = household_file.find_household(active_household, households)
            household.add_member(sim)

            if sim is not None:
                current_sim = sim

        elif answer == "E":
            save_file.manage_households(households)
            current_sim = (
                active_household.members[0]
            )

        elif answer == "G":
            prints.print_households(households)
            current_sim = household_file.switchsim(active_household, households)

            if current_sim is None:
                continue

            social_constructs.give_category_to_sim(current_sim)
            save_file.save_household(current_sim.household)


        else:
            print("Invalid choice. Please select A-F or END.")

    return current_sim

