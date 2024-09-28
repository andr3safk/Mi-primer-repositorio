class Pokemon:
    def __init__(self, nombre, puntos_ataque, puntos_vida):
        self.__nombre = nombre
        self.__puntos_ataque = puntos_ataque
        self.__puntos_vida = puntos_vida

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def puntos_ataque(self):
        return self.__puntos_ataque

    @property
    def puntos_vida(self):
        return self.__puntos_vida

    @puntos_vida.setter
    def puntos_vida(self, puntos_vida):
        self.__puntos_vida = puntos_vida

    def atacar(self, oponente):
        daño = Batalla.calcular_daño(self.puntos_ataque, oponente.puntos_vida)
        oponente.puntos_vida -= daño
        return f"{self.nombre} ataca a {oponente.nombre} causando {daño} puntos de daño. Vida restante de {oponente.nombre}: {oponente.puntos_vida}"


class Entrenador:
    def __init__(self, nombre, equipo):
        self.__nombre = nombre
        self.__equipo = equipo  # Composición: un equipo de Pokémon

    @property
    def nombre(self):
        return self.__nombre

    @property
    def equipo(self):
        return self.__equipo

    def ordenar_ataque(self, mi_pokemon, pokemon_oponente):
        # Delegación: El entrenador delega el ataque al Pokémon
        return mi_pokemon.atacar(pokemon_oponente)


class Batalla:
    total_batallas = 0

    def __init__(self):
        Batalla.total_batallas += 1

    @staticmethod
    def calcular_daño(puntos_ataque, puntos_vida_oponente):
        # Fórmula simple de daño: ataque menos la mitad de la vida del oponente
        return max(0, puntos_ataque - (puntos_vida_oponente // 2))

    @classmethod
    def mostrar_total_batallas(cls):
        print(f"Total de batallas realizadas: {cls.total_batallas}")


# Función para crear un Pokémon con entrada de datos
def crear_pokemon():
    nombre = input("Ingrese el nombre del Pokémon: ")
    puntos_ataque = int(input(f"Ingrese los puntos de ataque de {nombre}: "))
    puntos_vida = int(input(f"Ingrese los puntos de vida de {nombre}: "))
    return Pokemon(nombre, puntos_ataque, puntos_vida)


# Función para realizar varias batallas
def iniciar_batallas():
    nombre_entrenador1 = input("Ingrese el nombre del primer entrenador: ")
    nombre_entrenador2 = input("Ingrese el nombre del segundo entrenador: ")

    print("\n--- Equipo del primer entrenador ---")
    equipo1 = [crear_pokemon() for _ in range(2)]
    print("\n--- Equipo del segundo entrenador ---")
    equipo2 = [crear_pokemon() for _ in range(2)]

    entrenador1 = Entrenador(nombre_entrenador1, equipo1)
    entrenador2 = Entrenador(nombre_entrenador2, equipo2)

    while True:
        print("\n--- Nueva Batalla ---")
        pokemon1 = entrenador1.equipo[0]
        pokemon2 = entrenador2.equipo[0]

        # Entrenador 1 ataca primero
        print(entrenador1.ordenar_ataque(pokemon1, pokemon2))

        if pokemon2.puntos_vida <= 0:
            print(f"{pokemon2.nombre} ha sido derrotado.")
            entrenador2.equipo.remove(pokemon2)
            if len(entrenador2.equipo) == 0:
                print(f"{entrenador2.nombre} se ha quedado sin Pokémon. ¡{entrenador1.nombre} gana!")
                break
        else:
            # Entrenador 2 ataca
            print(entrenador2.ordenar_ataque(pokemon2, pokemon1))
            if pokemon1.puntos_vida <= 0:
                print(f"{pokemon1.nombre} ha sido derrotado.")
                entrenador1.equipo.remove(pokemon1)
                if len(entrenador1.equipo) == 0:
                    print(f"{entrenador1.nombre} se ha quedado sin Pokémon. ¡{entrenador2.nombre} gana!")
                    break

        continuar = input("¿Quieres realizar el siguiente turno? (s/n): ")
        if continuar.lower() != 's':
            break

    Batalla.mostrar_total_batallas()


# Iniciar el sistema de batallas
iniciar_batallas()
