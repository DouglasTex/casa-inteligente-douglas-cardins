from transitions import Machine
from dispositivo import Dispositivo
from observer import Observer


class SistemaSeguranca(Dispositivo):
    states = ['desligado', 'armado_com_gente_em_casa', 'armado_sem_ninguem_em_casa']

    def __init__(self):
        self.machine = Machine(model=self, states=SistemaSeguranca.states, initial='desligado')
        self.machine.add_transition(trigger='armar_com_gente_em_casa',
                                    source='desligado',
                                    dest='armado_com_gente_em_casa')
        self.machine.add_transition(trigger='armar_sem_gente_em_casa',
                                    source='desligado',
                                    dest='armado_sem_ninguem_em_casa')
        self.machine.add_transition(trigger='desarmar',
                                    source=['armado_com_gente_em_casa', 'armado_sem_ninguem_em_casa'],
                                    dest='desligado')

    def status_atual(self):
        return f'Sistema de segurança está {self.state}'

    def update(self, message):
        print(f"Sistema de Segurança: {message}")