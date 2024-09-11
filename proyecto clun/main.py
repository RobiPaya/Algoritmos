import turtle
import pandas

def cacacaca(x,y,num,x2,y2):
    t.goto(x,y)
    t.write(num)
    t.goto(x2,y2)
    t.write(f"{num}.")
    
screen = turtle.Screen()
screen.title("Caca juego")
image = "mapa.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Estados Correctos",
                                    prompt="Estado").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.speed(0)
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
    if "Aguascalientes" in guessed_states:
        cacacaca(-27,-48,1,-337,-102)
    if "Guanajuato" in guessed_states:
        cacacaca(-1,-77,2,-337,-122)
    if "Querétaro" in guessed_states:
        cacacaca(25,-82,3,-337,-142)
    if "Hidalgo" in guessed_states:
        cacacaca(51,-87,4,-337,-162)
    if "Tlaxcala" in guessed_states:
        cacacaca(70,-110,5,-337,-182)
    if "México" in guessed_states:
        cacacaca(32,-110,6,-337,-202)
    if "Distrito Federal" in guessed_states:
        cacacaca(47, -114, 7, -337, -222)
    if "Morelos" in guessed_states:
        cacacaca(50, -126, 8 ,-337, -242)