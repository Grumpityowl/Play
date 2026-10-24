## social roles are for roles you are currently fulfilling. Such as mother, father, priest, kidnapped, master, doctor, student
## social category is what you are. Ex: Female, white, child, american
## social category is deeply salient to your identity, 
## while social roles are more circumstantial and can change over time. Social categories are often assigned at birth or based on inherent characteristics, while social roles are typically acquired through life experiences, choices, and societal expectations.
## While the category nine is acquired when you get your magic powers, it is still a category that defines your identity in the magical world. It is not a role that you can easily change or step out of, but rather a fundamental aspect of who you are as a witch.

class SocialConstruct:
    def __init__(self, name):
        self.name = name
        self.categories = {}

    def add_category(self, category):
        self.categories[category.name] = category

class SocialCategory:
    def __init__(self, name):
        self.name = name
        self.allowances = []
        self.restrictions = []
        self.obligations = []

def find_construct():
    print("Which social construct?")
    constructs = all_constructs

    for name in constructs:
        print(name)

    choice = input("> ").strip().title()

    if choice in constructs:
        return constructs[choice]

    else:
        return None

def find_category(construct):
    category = construct

    print("Which category?")
    for category_name in construct.categories:
        print(category_name)

    return category


def assign_category(current_sim, category):
    choice = input("> ").strip().title()

    if choice in category.categories:
        current_sim.set_category(
        category,
        category.categories[choice]
            )
    else:
            print(f"Invalid {category} category.")

def give_category_to_sim(current_sim):
    construct = find_construct()
    category = find_category(construct)
    assign_category(current_sim, category)

# Define your constructs
gender = SocialConstruct("Gender")

Male = SocialCategory("Male")
gender.add_category(Male)

Female = SocialCategory("Female")
gender.add_category(Female)


soul_type = SocialConstruct("Soul Type")

moonborn = SocialCategory("Moonborn")
soul_type.add_category(moonborn)
moonborn.obligations.append("Expected to marry")

sunborn = SocialCategory("Sunborn")
soul_type.add_category(sunborn)
sunborn.obligations.append("Expected to remain single")

all_constructs = {
    "Gender": gender,
    "Soul Type": soul_type,
}
