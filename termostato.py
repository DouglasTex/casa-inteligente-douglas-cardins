from transitions import Machine
from dispositivo import Dispositivo
from observer import Observer


class Termostato(Dispositivo, Observer):
    states = ['desligado', 'aquecendo', 'esfriando']

    def __init__(self):
        self.machine = Machine(model=self, states=Termostato.states, initial='desligado')
        self.machine.add_transition(trigger='desligar', source=['aquecendo', 'esfriando'], dest='desligado')
        self.machine.add_transition(trigger='aquecer', source=['esfriando', 'desligado'], dest='aquecendo')
        self.machine.add_transition(trigger='esfriar', source=['aquecendo', 'desligado'], dest='esfriando')

    def status_atual(self):
        return f'Termostato está {self.state}'

    def update(self, message):
        print(f"Termostato: {message}")