def combat(character, enemy):
    print("----------------------------------")
    print(f"Te enfrentas a {enemy['name']}")
    print(f"Tu vida: {character['life']}")

    character['life'] -= enemy['damage']

    return character
