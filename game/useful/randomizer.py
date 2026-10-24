import random

def randomize_sex(): 
    return random.choice(["Male", "Female"])

def randomize_age(grade):
    return random.choice([
        int(grade) + 6,
        int(grade) + 7,
        int(grade) + 8
    ])
    
def randomize_fantasy_first_name(gender):
    if gender == "Male":
        return random.choice(fantasy_male_names)
    elif gender == "Female":
        return random.choice(fantasy_female_names)
    elif gender == "Non-binary":
        return random.choice(fantasy_nonbinary_names)

    else:
        return random.choice(
            fantasy_male_names + fantasy_female_names + fantasy_nonbinary_names
        )

def randomize_fantasy_last_name():
    return random.choice(fantasy_last_names)

def randomize_fantasy_full_name(gender):
     return randomize_fantasy_first_name(gender) + randomize_fantasy_last_name()

def randomize_normal_first_name(gender):
    if gender == "Male":
        return random.choice(normal_male_names)
    elif gender == "Female":
        return random.choice(normal_female_names)
    elif gender == "Non-binary":
        return random.choice(normal_nonbinary_names)

    else:
        return random.choice(
            normal_male_names + normal_female_names + normal_nonbinary_names
        )

def randomize_normal_last_name():
    return random.choice(normal_last_names)

def randomize_normal_full_name(gender):
     return f"{randomize_normal_first_name(gender)}, {randomize_normal_last_name()}"

def randomize_fantasy_gender():
    if random.random() < 0.01:
        return random.choice(nonsense_genders)

    return random.choice(["Male", "Female", "Non-binary"])

def randomize_age_social_category(new_npc_age):
    if new_npc_age == 7:
        return "Seven"
    elif new_npc_age == 8:
        return "Eight"
    elif new_npc_age == 9:
        return "Nine"
    else:
        return random.choice(["Seven", "Eight", "Nine"])

def randomize_witch_npc(grade):
    new_npc_gender = randomize_fantasy_gender()
    new_npc_name = randomize_fantasy_full_name(new_npc_gender)
    new_npc_age = randomize_age(grade)
    category_name = randomize_age_social_category(new_npc_age)
    return new_npc_name, new_npc_gender, new_npc_age, category_name

def randomize_mbti2_npc():
    new_npc_gender = randomize_fantasy_gender()
    new_npc_name = randomize_normal_full_name(new_npc_gender)
    new_npc_type = randomize_mbti_type()
    return new_npc_name, new_npc_gender, new_npc_type


def randomize_kid_dialogue():
    dialogue = random.choice(kid_dialogue)

    print("\nPress Enter to Continue Dialogue\n")

    for line in dialogue:
        print(line)
        input()

def randomize_teacher_dialogue():
    dialogue = random.choice(teacher_dialogue)

    print("\nPress Enter to Continue Dialogue\n")

    for line in dialogue:
        print(line)
        input()

def randomize_magic_season():
    return random.choice(["Autumn", "Spring", "Winter", "Summer"])

def randomize_mbti_type():
    return random.choice(["INTJ", "INTP", "INFP", "INFJ", "ISTP", "ISFP", "ISTJ", "ISFJ", "ENTJ", "ENFJ", "ENTP", "ENFP", "ESTP", "ESFP", "ESTJ", "ESFJ"])


fantasy_male_names = [
    "Hawthorne", "Wood", "Stone", "Moss", "Heath", "Pike", "Flint", "Thorne",
    "Wing", "Fell", "Elm", "Wyrm", "Ashbourne", "Marrow", "Flame", "Drear",
    "Shade", "Devour", "Shallow", "Crook", "Yew", "Hawke", "Bramble", "Linden",
    "Hemlock", "Bracken", "Slate", "Shale", "Tor", "Hollow", "Scar", "Bane",
    "Brand", "Tundra", "Drift", "Elder", "Talus", "Talon", "Edge", "Strife",
    "Thorn", "Reed", "Oak", "Pine", "Dusk", "Clay", "Dune", "Grim",
    "Wraith", "Crypt", "Obsidian", "Cinder", "Gloom", "Shard", "Fang", "Claw",
    "Pelt", "Howl", "Roar", "Hawk", "Stag", "Fox", "Viper", "Storm",
    "Frost", "Pulse", "Crest", "Ridge", "Cross", "Marsh", "Beck", "Gold",
    "Fen", "Brave", "Raven", "Blight", "Grave", "Sable"
]

fantasy_female_names = [
    "Azura", "Solara", "Mara", "Blair", "Briar", "Thalassa", "Evangeline",
    "Calista", "Morrigan", "Claire", "Isadora", "Maeve", "Rosalinda",
    "Anastasia", "Rose", "Clove", "Thistle", "Bloom", "Laurel", "Sorrel",
    "Dawn", "Glow", "Ember", "Lumen", "Halo", "Gleam", "Flare", "Bliss",
    "Aura", "Nova", "Skye", "Flicker", "Wisher", "Flutter", "Spark",
    "Silver", "Haven", "Charm", "Shine", "Muse", "Chime", "Good", "Ville", "Briar", "Skye",
]

fantasy_nonbinary_names = [
    "Avery", "Rowan", "Sage", "Riley", "Emery", "Quinn", "Wren", "River",
    "Arden", "Eden", "Lark", "Willow", "Clover", "Ash", "Robin", "Sunny",
    "Kit", "Pip", "Marlow", "Remy", "Ellis", "Jules", "Mika", "Skye",
    "Indigo", "Briar", "Fable", "Fern", "Starling", "Rune", "Sol",
 "Winter", "Aster", "Juniper", "Lumi", "Dusk", "Heart", "Rose", "Echo", "Whisper",
    "Sable", "Flare", "Sigil"
]

fantasy_last_names = [

    " Hush", " Still", " Low", " Doodle", " Shiver", " Gold", " Aura", " Nova",

    " Flicker", " Spark", " Rift", " Silver", " Reach", " Drift", " Flux", " Tide",

    " Mist", " Ward", " Ridge", " Fell", " Hollow", " Veil", " Cinder", " Dawn",

    " Ember", " Lumen", " Bloom", " Nori", " Moss", " Dove", " Stone", " Flint",

    " Vale", " Reed", " Cypress", " Moon", " Avery", " Rowan", " Sage", " Riley",

    " Emery", " Quinn", " Wren", " River", " Arden", " Eden", " Lark", " Willow",

    " Clover", " Ash", " Robin", " Sunny", " Kit", " Pip", " Marlow", " Remy",

    " Ellis", " Jules", " Mika", " Skye", " Indigo", " Briar", " Fable", " Fern",

    " Starling", " Rune", " Sol", " Winter", " Aster", " Juniper", " Lumi", " Dusk",

    " Heart", " Rose", " Echo", " Whisper", " Sable", " Flare", " Sigil",

    " Hawthorne", " Wood", " Heath", " Pike", " Thorne", " Wing", " Elm", " Wyrm",

    " Ashbourne", " Marrow", " Flame", " Drear", " Shade", " Devour", " Shallow",

    " Crook", " Yew", " Hawke", " Bramble", " Linden", " Hemlock", " Bracken",

    " Slate", " Shale", " Tor", " Scar", " Bane", " Brand", " Tundra", " Elder",

    " Talus", " Talon", " Edge", " Strife", " Thorn", " Oak", " Pine", " Clay",

    " Dune", " Grim", " Wraith", " Crypt", " Obsidian", " Gloom", " Shard", " Fang",

    " Claw", " Pelt", " Howl", " Roar", " Hawk", " Stag", " Fox", " Viper", " Storm",

    " Frost", " Pulse", " Crest", " Cross", " Marsh", " Beck", " Fen", " Brave",

    " Raven", " Blight", " Grave", " Azura", " Solara", " Mara", " Blair",

    " Thalassa", " Evangeline", " Calista", " Morrigan", " Claire", " Isadora",

    " Maeve", " Rosalinda", " Anastasia", " Clove", " Thistle", " Laurel", " Sorrel",

    " Glow", " Halo", " Gleam", " Bliss", " Wisher", " Flutter", " Haven", " Charm",

    " Shine", " Muse", " Chime", " Good", " Ville"
]


normal_male_names = [
    "James", "John", "Robert", "Michael", "William",
    "David", "Joseph", "Thomas", "Daniel", "Matthew",
    "Andrew", "Christopher", "Joshua", "Ryan", "Nicholas",
    "Ethan", "Noah", "Liam", "Benjamin", "Samuel",
    "Alexander", "Henry", "Jack", "Lucas", "Oliver",
    "Jacob", "Logan", "Nathan", "Caleb", "Owen",
    "Dylan", "Luke", "Gabriel", "Isaac", "Anthony",
    "Aaron", "Adam", "Charles", "Edward", "Evan",
    "Leo", "Mason", "Julian", "Connor", "Adrian",
    "Eli", "Miles", "Jason", "Peter", "Zachary",
    "Ian", "Cameron", "Jordan", "Tyler", "Max",
    "Cole", "Derek", "Eric", "Patrick", "Sean"
]

normal_female_names = [
    "Emily", "Sarah", "Jessica", "Ashley", "Amanda",
    "Elizabeth", "Hannah", "Samantha", "Olivia", "Emma",
    "Sophia", "Isabella", "Mia", "Charlotte", "Amelia",
    "Ava", "Grace", "Chloe", "Lily", "Ella",
    "Abigail", "Madison", "Natalie", "Zoe", "Lucy",
    "Anna", "Claire", "Julia", "Megan", "Rachel",
    "Rebecca", "Lauren", "Alexandra", "Victoria", "Audrey",
    "Leah", "Nora", "Stella", "Alice", "Eva",
    "Maya", "Naomi", "Elena", "Catherine", "Rose",
    "Jasmine", "Lydia", "Paige", "Brooke", "Morgan",
    "Kayla", "Alyssa", "Faith", "Isabel", "Sophie",
    "Ivy", "Madeline", "Hailey", "Claire", "Diana"
]

normal_nonbinary_names = [
    "Alex", "Jordan", "Taylor", "Morgan", "Casey",
    "Riley", "Avery", "Jamie", "Cameron", "Parker",
    "Quinn", "Drew", "Reese", "Charlie", "Robin",
    "Sam", "Jesse", "Rowan", "Skyler", "Dakota",
    "Emerson", "Finley", "Hayden", "Kendall", "Logan",
    "Micah", "Payton", "Sage", "Shawn", "Toby",
    "Blake", "Cory", "Elliot", "Frankie", "Harley",
    "Jules", "Kai", "Lane", "Marley", "Noel",
    "Rory", "Sidney", "Spencer", "Tatum", "Cody",
    "Ari", "Ash", "Devin", "Ellis", "Reagan"
]

normal_last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones",
    "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
    "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
    "Thomas", "Taylor", "Moore", "Jackson", "Martin",
    "Lee", "Perez", "Thompson", "White", "Harris",
    "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson",
    "Walker", "Young", "Allen", "King", "Wright",
    "Scott", "Torres", "Nguyen", "Hill", "Green",
    "Adams", "Nelson", "Baker", "Hall", "Rivera",
    "Campbell", "Mitchell", "Carter", "Roberts", "Phillips",
    "Evans", "Turner", "Parker", "Collins", "Edwards",
    "Stewart", "Morris", "Murphy", "Cook", "Rogers",
    "Morgan", "Peterson", "Cooper", "Reed", "Bailey",
    "Bell", "Howard", "Ward", "Brooks", "Kelly",
    "Price", "Bennett", "Wood", "Barnes", "Ross",
    "Henderson", "Coleman", "Jenkins", "Perry", "Powell",
    "Long", "Patterson", "Hughes", "Flores", "Washington",
    "Butler", "Simmons", "Foster", "Gonzales", "Bryant",
    "Alexander", "Russell", "Griffin", "Diaz", "Hayes",
    "Myers", "Ford", "Hamilton", "Graham", "Sullivan"
]

nonsense_genders = [
    "Banana",
    "A Teacup",
    "Chair",
    "Tommorow",
    "Soup",
    "🦎",
    "The Feeling of Freshly Washed Sheets",
    "Thing",
    "A Constant Existential Crisis",
    "I'm a Witch but I'm Also Not a Witch?",
    "Three Raccoons in Trenchcoat",
    "Tax Evasion",
    "Triangle",
    "The Moon's Favorite",
    "Snack!",
    "What is Gender?",
    "(˶>⩊<˶)",
    "⚞^. .^⚟ ",
    "✨Special Snowflake✨",
    "Sponge",
    "None",
    "Yes",
    "Fairy",
    "No",
    "Maybe",
    "Danger 😎",
    "Classified Information",
    "Goblin",
    "Raven",
    "Very Small Dragon",
    "I'm a Dragon! RAWR!",
    "Soup Adjacent",
    "Lightswitch",
    "Snack",
    "The Second Half of a Rainbow",
    "Tree",
    "YAYYYYY",
    "Waffle",
    "Upside Down",
    "Sideways",
    "Unknown",
    "???",
    "Parking Ticket",
    "Blue",
    "Doorknob",
    "Four",
    "Princess",
    "Error 404",
    "Several Birds",
    "An Entire Swamp",
    "The Moon",
    "A Cryptid",
    "Some Sort of Fae",
    "A Haunted Victorian Child",
    "The Feeling of Rain",
    "A Forest",
    "An Ominous Presence",
    "The Color Purple",
    "A Crow With Responsibilities",
    "A Particularly Fancy Moth",
    "The Void",
    "Spiritually, A Frog",
    "The Space Between Things",
    "Hot Chocolate",
    "A Shade of Blue I Cannot Describe",
    "A Question Without an Answer",  
"The Vibe of an Empty Hallway",  
    "The Feeling of Almost Remembering a Dream",
    "An Idea With Legs",
]

kid_dialogue = [
    (
        "Do you have a favorite animal?",
        "Yeah.",
        "Which one?",
        "Dragons aren't animals.",
        "They are if you ask nicely."
    ),

    (
        "I found a really cool rock.",
        "Where?",
        "Outside.",
        "Can I see it?",
        "No."
    ),

    (
        "Do you like frogs?",
        "Yes.",
        "Good.",
        "Why?",
        "No reason."
    ),

    (
        "What's your favorite color?",
        "Purple.",
        "That's a good one.",
        "What's yours?",
        "Blue."
    ),

    (
        "I think I could beat you in a race.",
        "You don't even know how fast I am.",
        "Exactly.",
        "That's not how that works.",
        "We'll find out."
    ),

    (
        "I don't like this chair.",
        "Why?",
        "It knows what it did.",
        "What did it do?",
        "I don't want to talk about it."
    ),

    (
        "What are you doing?",
        "Nothing.",
        "Can I help?",
        "No.",
        "Okay."
    ),

    (
        "I forgot what I was going to say.",
        "Okay.",
        "Thanks.",
        "For what?",
        "I don't know."
    ),

    (
        "Do you want to work together?",
        "Sure.",
        "Okay.",
        "I'm terrible at this.",
        "Me too."
    ),

    (
        "Do you want to come outside during break?",
        "Sure.",
        "Okay. It's a plan.",
        "A plan?",
        "A very important plan."
    ),

    (
        "Look what I drew.",
        "What is it?",
        "A horse.",
        "Oh.",
        "It's supposed to be a horse."
    ),

    (
        "My pencil broke.",
        "Do you need another one?",
        "No.",
        "Why not?",
        "I can fix it."
    ),

    (
        "I think I'm good at math.",
        "Really?",
        "Yeah.",
        "How good?",
        "I can count to one hundred."
    ),

    (
        "Do you have any siblings?",
        "Yeah.",
        "Are they annoying?",
        "Very.",
        "Mine too."
    ),

    (
        "What's your favorite food?",
        "I don't know.",
        "How do you not know?",
        "There's too many.",
        "Fair."
    ),

    (
        "I saw a really big bird outside.",
        "How big?",
        "Really big.",
        "That's not a measurement.",
        "Biggerer than you."
    ),

    (
        "Do you want to hear a secret?",
        "Sure.",
        "I forgot it.",
        "Oh.",
        "I'll remember eventually."
    )
]

teacher_dialogue = [
    [
        "You: I don't know what to do.",
        "Teacher: Then do not begin with knowing.",
        "Teacher: Begin with looking.",
        "You: Looking at what?",
        "Teacher: Whatever you have been overlooking."
    ],

    [
        "You: I keep getting it wrong.",
        "Teacher: Good.",
        "You: Good?",
        "Teacher: A mistake is the world whispering, 'Not quite this way.'",
        "Teacher: Listen to it."
    ],

    [
        "You: Can you show me how?",
        "Teacher: I can show you where to look.",
        "You: But you won't show me the answer?",
        "Teacher: The answer will mean more when your own hands find it."
    ],

    [
        "You: I can't make the spell work.",
        "Teacher: What does the spell want?",
        "You: I don't know.",
        "Teacher: Then be still.",
        "Teacher: Magic is often quieter than the one trying to command it."
    ],

    [
        "You: I don't understand.",
        "Teacher: That is a perfectly good place to begin.",
        "Teacher: Understanding rarely arrives when we chase it.",
        "Teacher: Sit with the question awhile."
    ],

    [
        "You: Why doesn't this work?",
        "Teacher: Perhaps it is working.",
        "You: It is?",
        "Teacher: Perhaps it is simply doing something you have not yet learned to see."
    ],

    [
        "You: Which one is correct?",
        "Teacher: Which one do you believe is correct?",
        "You: I don't know.",
        "Teacher: Then you have found today's lesson."
    ],

    [
        "You: I need help.",
        "Teacher: Of course.",
        "Teacher: But tell me first—what have you discovered?"
    ],

    [
        "You: I forgot what you taught us.",
        "Teacher: Did you forget?",
        "You: Yes.",
        "Teacher: Then perhaps you remembered something more important."
    ],

    [
        "You: It's impossible!",
        "Teacher: Nothing is impossible merely because it has refused you once.",
        "You: It has refused me six times.",
        "Teacher: Then you have six pieces of information."
    ],

    [
        "You: I'm not good at this.",
        "Teacher: Not yet.",
        "You: What's the difference?",
        "Teacher: Time."
    ],

    [
        "You: Everyone else understands.",
        "Teacher: The river does not hurry because the other rivers are faster.",
        "Teacher: Follow your own current."
    ],

    [
        "You: Oh!",
        "Teacher: Ah.",
        "You: I understand now!",
        "Teacher: I know.",
        "You: How did you know?",
        "Teacher: Your face told me before your words did."
    ],

    [
        "You: I did it!",
        "Teacher: You did.",
        "You: You helped me!",
        "Teacher: I only opened the door.",
        "Teacher: You were the one who walked through."
    ],

    [
        "Teacher: The wind does not push the leaves where they must go.",
        "Teacher: It simply moves, and the leaves learn to follow."
    ],

    [
        "Teacher: A seed does not become a tree by being told what a tree should be."
    ],

    [
        "Teacher: Listen before you reach.",
        "Teacher: The answer may already be moving toward you."
    ],

    [
        "Teacher: When the water refuses your path, do not argue with the river.",
        "Teacher: Ask where it wishes to go."
    ],

    [
        "Teacher: You are not behind.",
        "Teacher: You are simply standing somewhere different."
    ]
]

temperments = [
    "Old Soul",
    "Free Spirit",
    "Natural Leader",
    "Peacemaker",
    "Troublemaker",
    "People-Pleaser",
    "Show-Off",
    "Wallflower",
    "Bookish",
    "Adventurous",
    "Rebellious",
    "Protective",
    "Explosive",
    "Selfish",
    "Self Possessed",
    "Passionate",
    "Charming",
    "Cold",
    "Kindhearted",
    "Hardheaded",
    "Nosy",
    "Quirky",
    "Shy",
    "Sociable",
    "Clingy",
    "Independent",
    "Affectionate",
    "Aloof",
    "Friendly",
    "Suspicious",
    "Trusting",
    "Attention-Seeking",
    "Reserved",
    "Charming",
    "Dramatic (Emotional)",
    "Dramatic (Theater Kid)",
    "Emotional (Introverted)",
    "Emotional (Extroverted)",
    "Cheerful",
    "Serious",
    "Melancholic",
    "Sensitive",
    "Stoic",
    "Even-Tempered",
    "Moody",
    "Anxious",
    "Fearless",
    "Easily Frustrated",
    "Content",
    "Passionate",
    "Calm",
    "Curious",
    "Cautious",
    "Reckless",
    "Patient",
    "Impatient",
    "Stubborn",
    "Easygoing",
    "Demanding",
    "Obedient",
    "Defiant",
    "Restless",
    "Lazy",
    "Energetic",
    "Quiet",
    "Fussy",
    "Imaginative",
    "Observant",
    "Dreamy",
    "Serious-Minded",
    "Thoughtful",
    "Distractible",
    "Focused",
    "Inquisitive",
    "Practical",
    "Self-Absorbed",
    "Perceptive",
    "Forgetful",
    "Mischievous",
    "Gentle",
    "Intense",
    "Odd",
    "Eager",
    "Wary",
    "Bold",
    "Timid",
    "Playful",
    "Competitive",
    "Generous",
    "Protective",
    "Academic",
    "Melodramatic",
    "Fiery",
    "Silly",
    "Sweetheart",
    "Wistful",
    "Little Angel",
    "Honor Student",
    "Good Girl/Boy",
    "Drama Queen",
    "Intimidating",
    "Gentle Giant",
    "Approuchable",
    "Talkative",
    "Always Asking Questions",
    "Always Moving",
    "Social",
    "Volitile",
]
def randomizetemperment():
    temperment = random.choice(temperments)
    return temperment