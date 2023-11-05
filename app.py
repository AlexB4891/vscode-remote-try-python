# ROCK PAPER SCISSORS GAME

# Vamos a crear una lista con los elemntos rock, paper,sissors
tools = ["rock", "paper", "scissors"]

# Creamos una función para tomar un elemento aleatorio de la lista tools
def random_tool():
    import random

    return random.choice(tools)

def rps_game(selection):
    respuesta = random_tool()

    # Unir selection y respuesta en una lista
    lista = [selection, respuesta]

    # Controlemos que selection no sea distinto a rock, paper o scissors
    # Si el elemento esta fuera del vector entonces validador será FALSE
    validador = selection in tools

    # Si validador es FALSE entonces se imprime el mensaje
    if validador == False:
        solution = "Invalid selection"

    # Si validador es TRUE entonces comparamos selection y respuesta
    # Si son iguales imprimimos "Tie"
    # Si no son iguales entonces comparamos selection y respuesta
    # rock gana a scissors
    # scissors gana a paper
    # paper gana a rock

    if validador == True:
        if selection == respuesta:
            solution = "Tie"
        else:   
            if selection == "rock" and respuesta == "scissors":
                solution = "You win"
            elif selection == "scissors" and respuesta == "paper":
                solution = "You win"
            elif selection == "paper" and respuesta == "rock":
                solution = "You win"
            else:
                solution = "You lose"

    lista.append(solution)

    return(lista)             


def replay(desicion):
    if desicion == "yes":
        return 1
    else:
        return 0

counter = 1
puntos = 0
while counter >0:
    selection = rps_game(input("Enter a tool:"))

    if(selection[2] == "You win"): 
        puntos += 1
        
    print(selection)

    print("Round", counter,", you have", puntos, "points")
    
    desicion = replay(input("Do you want to play again? (yes/no)"))

    if  desicion == 1:
        counter += 1
    else:
        counter = 0
        print("Bye!")


