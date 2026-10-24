## social roles are for roles you are currently fulfilling. Such as mother, father, priest, kidnapped, master, doctor, student
## social category is what you are. Ex: Female, white, child, american
## social category is deeply salient to your identity, 
## while social roles are more circumstantial and can change over time. Social categories are often assigned at birth or based on inherent characteristics, while social roles are typically acquired through life experiences, choices, and societal expectations.
## While the category nine is acquired when you get your magic powers, it is still a category that defines your identity in the magical world. It is not a role that you can easily change or step out of, but rather a fundamental aspect of who you are as a witch.
   
class Social_Constructs:
    def __init__(self, name):
        self.name = name
        self.restrictions = []
        self.allowances = []
        self.obligations = []

    def add_obligation(self, obligation):
        self.obligations.append(obligation)

    def add_allowance(self, allowance):
        self.allowances.append(allowance)

    def add_restriction(self, restriction):
        self.restrictions.append(restriction)

    def has_allowance(person, allowance):
        for category in person.social_categories:
            if allowance in category.allowances:
                return True
        return False


gender = Social_Constructs("Gender")
youth = Social_Constructs("Youth")

