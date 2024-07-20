from transitions import Machine
from dispositivo import Dispositivo
from observer import Observer


class Luz(Dispositivo, Observer):
    states = ['desligada', 'ligada']

    def __init__(self):
        self.machine = Machine(model=self, states=Luz.states, initial='desligada')
        self.machine.add_transition(trigger='ligar', source='desligada', dest='ligada')
        self.machine.add_transition(trigger='desligar', source='ligada', dest='desligada')

    def status_atual(self):
        return f'Luz está {self.state}'

    def update(self, message):
        print(f"Luz: {message}")
