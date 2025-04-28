import random

# Lista básica de pokémon
POKEMONS = [
    "Pikachu", "Charmander", "Bulbasaur", "Squirtle", "Eevee",
    "Jigglypuff", "Meowth", "Psyduck", "Snorlax", "Magikarp"
]

def list_pokemons():
    """Muestra todos los Pokémon disponibles."""
    print("Lista de Pokémon disponibles:")
    for idx, name in enumerate(POKEMONS, start=1):
        print(f"{idx}. {name}")

def catch_random_pokemon():
    """Atrapa un Pokémon aleatorio."""
    pokemon = random.choice(POKEMONS)
    print(f"¡Felicidades! Has atrapado a {pokemon}.")

def mensaje_prueba():
    print(" Modificación desde practica unir, Manuel S. ")

def main():
    print("¡Bienvenido al Mundo Pokémon!")
    print("¿Qué quieres hacer?")
    print("1. Listar Pokémon")
    print("2. Atrapar un Pokémon aleatorio")
    choice = input("Ingresa el número de tu elección: ")
    mensaje_prueba()

    if choice == "1":
        list_pokemons()
    elif choice == "2":
        catch_random_pokemon()
    else:
        print("Opción inválida. Por favor intenta de nuevo.")

if __name__ == "__main__":
    main()
