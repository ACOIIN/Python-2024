import random

class Ataque:
    def __init__(self, nombre, tipo, potencia):
        self.nombre = nombre
        self.tipo = tipo
        self.potencia = potencia

    def __str__(self):
        return f"{self.nombre} ({self.tipo}) - Potencia: {self.potencia}"

class Pokemon:
    def __init__(self, nombre, tipo, estadisticas, ataques):
        self.nombre = nombre
        self.tipo = tipo
        self.estadisticas = estadisticas
        self.salvaje = True
        self.ataques = ataques
        self.puntos_salud = estadisticas["salud"]

    # Método para simular un ataque
    def atacar(self, otro_pokemon):
        ataque = self.elegir_ataque()
        print(f"{self.nombre} ha atacado a {otro_pokemon.nombre}")
        otro_pokemon.recibir_dano(ataque.potencia)

    # Método para simular un grito o sonido
    def gritar(self):
        print(f"{self.nombre}: Grrr...")

    def elegir_ataque(self):
        # print lista de ataques
        print(f"{self.nombre} tiene los siguientes ataques:")
        # for con contador para la eleccion
        for i, ataque in enumerate(self.ataques):
            print(f"{i+1}. {ataque}")

        while True:
            # recibir input de la opcion
            opcion = input("Elige un ataque: ")
            # validar opcion
            if opcion.isdigit() and 1 <= int(opcion) <= len(self.ataques):
                return self.ataques[int(opcion) - 1]
            else:
                print("Opción no válida. Elige un número válido.")

    def recibir_dano(self, dano):
        self.puntos_salud -= dano
        if self.puntos_salud <= 0:
            print(f"{self.nombre} ha sido derrotado.")
            self.puntos_salud = 0

    def esta_vivo(self):
        return (self.puntos_salud > 0)

    def __str__(self):
        return f"{self.nombre} ({self.puntos_salud}/{self.estadisticas['salud']})"

class EntrenadorPokemon:
    def __init__(self, nombre, equipo):
        self.nombre = nombre
        self.equipo = equipo  # Lista de objetos Pokemon
        self.pokemon_activo = equipo[0]

    # Método para añadir un Pokémon al equipo del entrenador
    def capturar_pokemon(self, pokemon):
        if pokemon.salvaje:
            if len(self.equipo) < 6:
                if random.random() < 0.5:
                    pokemon.salvaje = False
                    self.equipo.append(pokemon)
                    print(f"{self.nombre} ha capturado a {pokemon.nombre}")
                else:
                    print(f"{self.nombre} ha fallado en capturar a {pokemon.nombre}")
            else:
                print(f"{self.nombre} ya tienes el máximo de Pokémons en tu equipo")
        else:
            print(f"{pokemon.nombre} es de otro entrenador!!!")

    # Método para mostrar el equipo del entrenador
    def mostrar_equipo(self):
        print(f"Entrenador {self.nombre} tiene los siguientes Pokémon:")
        for pokemon in self.equipo:
            print(f"- {pokemon.nombre}")

    def cambiar_pokemon(self):
        # Le vas a dar la opción al usario de elegir por cuál pokemon
        # cambiar al pokemon_activo
        print(f"Entrenador {self.nombre} tiene los siguientes Pokémon:")
        for i, pokemon in enumerate(self.equipo):
            if pokemon.esta_vivo():
                print(f"{i+1}. {pokemon.nombre}")
            else:
                print(f"{i+1}. {pokemon.nombre} (Derrotado)")

        while True:
            opcion = input("Elige un Pokémon: ")
            if opcion.isdigit() and 1 <= int(opcion) <= len(self.equipo):
                if self.equipo[int(opcion) - 1].esta_vivo():
                    if self.pokemon_activo == self.equipo[int(opcion) - 1]:
                        print("Este es el pokemon activo, elige otro")
                    else:
                        self.pokemon_activo = self.equipo[int(opcion) - 1]
                        return
                else:
                    print("El Pokémon ha sido derrotado. Elige otro.")
            else:
                print("Opción no válida. Elige un número válido.")

    def atacar(self, otro_entrenador):
        self.pokemon_activo.atacar(otro_entrenador.pokemon_activo)

    def sigue_jugando(self):
        return any(pokemon.esta_vivo() for pokemon in self.equipo)

    def __str__(self):
        return f"Entrenador {self.nombre} {self.pokemon_activo}"

class BatallaPokemon:
    def __init__(self, entrenador1, entrenador2):
        self.entrenadores = [entrenador1, entrenador2]

    def iniciar_batalla(self):
        print("¡Comienza la batalla!")
        turno = 0  # 0 para entrenador1, 1 para entrenador2
        while True:
            print(self.entrenadores[0])
            print(self.entrenadores[1])
            print(f"Turno del entrenador: {self.entrenadores[turno].nombre}")
            # elegir entre atacar o cambiar pokemon

            opcion = input("¿Quieres atacar o cambiar de Pokémon? (atacar/cambiar): ")
            while opcion.lower() not in ["atacar", "cambiar"]:
                print("Opción no válida. Elige 'atacar' o 'cambiar'.")
                opcion = input("¿Quieres atacar o cambiar de Pokémon? (atacar/cambiar): ")
            if opcion.lower() == "atacar":
                self.entrenadores[turno].atacar(self.entrenadores[(turno + 1) % 2])
                if (not self.entrenadores[(turno + 1) % 2].pokemon_activo.esta_vivo()) and self.entrenadores[(turno + 1) % 2].sigue_jugando():
                        self.entrenadores[(turno + 1) % 2].cambiar_pokemon()
            elif opcion.lower() == "cambiar":
                self.entrenadores[turno].cambiar_pokemon()
            turno = (turno + 1) % 2
            if not self.entrenadores[turno].sigue_jugando():
                print(f"Entrenador {self.entrenadores[turno].nombre} perdio")
                print(f"Entrenador {self.entrenadores[(turno + 1) % 2].nombre} ganooo!!!")
                break

# Crear algunos ataques
ataque1 = Ataque("Impactrueno", "Eléctrico", 40)
ataque2 = Ataque("Arañazo", "Normal", 20)
ataque3 = Ataque("Llamarada", "Fuego", 90)
ataque4 = Ataque("Surf", "Agua", 150)

# Crear Pokémon con sus ataques
pikachu = Pokemon("Pikachu", "Eléctrico", {"salud": 100, "ataque": 55, "defensa": 40}, [ataque1, ataque2])
charizard = Pokemon("Charizard", "Fuego", {"salud": 150, "ataque": 84, "defensa": 78}, [ataque3, ataque2])
blastoise = Pokemon("Blastoise", "Agua", {"salud": 150, "ataque": 83, "defensa": 100}, [ataque4, ataque2])

# Crear entrenadores con sus equipos
ash = EntrenadorPokemon("Ash", [pikachu, charizard])
gary = EntrenadorPokemon("Gary", [blastoise])

# Iniciar la batalla
batalla = BatallaPokemon(ash, gary)
batalla.iniciar_batalla()
