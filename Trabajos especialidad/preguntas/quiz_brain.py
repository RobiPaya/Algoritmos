from data import *
import question_model
import random as r
class quizbrain:
    def __init__(self,qtext,qanswer):
        self.text=qtext
        self.answer=qanswer
    def preguntasdisponibles(lista):
        numerodelapregunta=r.randint(1,50)
        if numerodelapregunta in lista:
            pass
        else:
            pregunta=question_model(preguntasdiccionario[numerodelapregunta]["question"],preguntasdiccionario[numerodelapregunta]["correct_answer"])
        return 

