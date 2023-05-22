import characters
import paths
import combat


def main():
    print('Bienvenido a Star Wars RPG')

    print('Selecciona un personaje:')
    for i, character in enumerate(characters.characters):
        print(f"{i + 1}. {character['name']}")

    character_index = int(input('Ingresa el número del personaje: '))
    character = characters.characters[character_index - 1]

    print(f"Has seleccionado a {character['name']}")

    print('Selecciona un camino:')
    for i, path in enumerate(paths.paths):
        print(f"{i + 1}. {path['name']}")

    path_index = int(input('Ingresa el número del camino: '))
    path = paths.paths[path_index - 1]

    print(f"Has seleccionado el camino {path['name']}")

    print(f"Te encuentras en {path['description']}")

    print('Enfrentarás a los siguientes enemigos:')
    for enemy in path['enemies']:
        print(f"{enemy['name']}")

    print('¿Deseas continuar?')
    print('1. Sí')
    print('2. No')

    option = int(input('Ingresa el número de la opción: '))

    if option == 1:
        print('¡Que la fuerza te acompañe!')
        perdido = False
        for enemy in path['enemies']:
            caracter = combat.combat(character, enemy)
            if (caracter['life'] <= 0):
                perdido = True
                break

            print(f"Vida de {character['name']}: {character['life']}")
            print(f"Haz perdido {enemy['damage']} puntos de vida")

        print("----------------------------------")
        if (perdido):
            print('Has perdido')
        else:
            print('Has ganado')
            print(f'Tu vida final es {character["life"]}')

    elif option == 2:
        print('Adiós')
    else:
        print('Opción inválida')


main()
