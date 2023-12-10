def print_max_pokemon(pokemon):
    name, type, hp = pokemon
    print(f"{name} has the highest HP ({hp}) for type {type}.")


def get_pokemons():
    pokemons = []
    while True:
        name = input("Name: ")
        if name == '':
            break
        else:
            type = input("Type: ")
            hp = int(input("HP: "))
            pokemons.append((name, type, hp))
    return pokemons


def get_best_pokemon(pokemons):
    type = input("Get max HP for type: ")
    max_hp = float("-inf")
    max_pokemon = None
    for pokemon in pokemons:
        if pokemon[2] >= max_hp and pokemon[1] == type:
            max_hp = pokemon[2]
            max_pokemon = pokemon

    return max_pokemon


def main():
    pokemons = get_pokemons()
    max_pokemon = get_best_pokemon(pokemons)
    print_max_pokemon(max_pokemon)


if __name__ == '__main__':
    main()
