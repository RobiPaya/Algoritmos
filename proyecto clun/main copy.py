import turtle
import pandas
import tkinter as tk
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "mapa.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
def estados():
    answer_state=entrada.get().title()
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv") 
        ventana.destroy
    entrada.delete(0,len(answer_state))
    ventana.title(f"{len(guessed_states)}/50 Estados correctos")
while len(guessed_states) < 50:
    ventana=tk.Tk()
    ventana.title(f"{len(guessed_states)}/50 Estados correctos")
    entrada=tk.Entry(ventana)
    entrada.pack(padx=50,pady=20)
    boton=tk.Button(ventana,text="OK",command=estados)
    boton.pack(padx=20)
    ventana.mainloop()
    
    