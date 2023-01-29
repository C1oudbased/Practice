# Dictionary to store demon stats
demons = {
    "Jack Frost": {"Race": "Fairy", "Weak to": "Fire", "Absorbs": "Ice", "Blocks": "Nothing", "Resists": "Nothing", "Reflects": "Nothing" },
    "Succubus": {"Race": "Night", "Weak to": "Light", "Absorbs": "Nothing", "Blocks": "Dark", "Resists": "Fire/Ice/Elec/Force", "Reflects": "Nothing" },
    "Slime": {"Race": "Foul", "Weak to": "Fire/Light", "Absorbs": "Nothing", "Blocks": "Dark", "Resists": "Physical", "Reflects": "Nothing" }
}

# Function to display demon stats
def display_stats(demon_name):
    if demon_name in demons:
        demon = demons[demon_name]
        print(f"Race: {demon['Race']}")
        print(f"Weak to: {demon['Weak to']}")
        print(f"Absorbs: {demon['Absorbs']}")
        print(f"Blocks: {demon['Blocks']}")
        print(f"Resists: {demon['Resists']}")
        print(f"Reflects: {demon['Reflects']}")
    else:
        print(f"Demon not found: {demon_name}")

# Splash art and welcome message
print("Welcome to the world of shadows, where demons gather...")
print("Enter the name of a demon to show the stats of the demon. Ex: Jack Frost, Slime, Succubus, etc.")
# Get demon name from user input
demon_name = input("Enter demon name: ")

# Display demon stats
display_stats(demon_name)