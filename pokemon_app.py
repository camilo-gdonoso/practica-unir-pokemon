import random

# Lista básica de pokémon
POKEMONS = [
    "Pikachu", "Charmander", "Bulbasaur", "Squirtle", "Eevee",
    "Jigglypuff", "Meowth", "Psyduck", "Snorlax", "Magikarp"
]

def list_pokemons():
    """Muestra los Pokémon disponibles."""
    print("Lista de Pokémon disponibles:")
    for idx, name in enumerate(POKEMONS, start=1):
        print(f"{idx}. {name}")

def catch_random_pokemon():
    """Prueba tu suerte atrapando un Pokémon aleatorio."""
    pokemon = random.choice(POKEMONS)
    chance = random.random()  # genera un número entre 0 y 1 para agregarle aleatoriedad a la captura
    if chance < 0.75: # El usuario tendrá 75% de oportunidad para capturar un pokemon
        print(f"¡Felicidades! Has atrapado a {pokemon}.")
    else:
        print(f"¡Oh no! {pokemon} se escapó. Mejor suerte la próxima vez.")


def mensaje_prueba():
    print(" Modificación desde practica unir, Manuel S. ")


def search_pokemon(name):
    """Buscar pokemon por nombre"""
    if name.capitalize() in POKEMONS:
         print(f"¡{name.capitalize} ya existe!")
    else:
         print(f"¡{name.capitalize} no existe!")


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
