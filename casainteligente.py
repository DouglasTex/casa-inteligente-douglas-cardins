from functools import reduce
from luz import Luz
from sistema_seguranca import SistemaSeguranca
from termostato import Termostato


class CasaInteligente:
    _instance = None

    def __init__(self, limite_dispositivos):
        self._instance = None
        self.dispositivos = []
        self.limite = limite_dispositivos
        self.observers = []

    @classmethod
    def instance(cls, limite_dispositivos):
        if cls._instance is None:
            cls._instance = cls(limite_dispositivos)
        return cls._instance

    def adicionar_dispositivo(self, dispositivo):
        if len(self.dispositivos) >= self.limite:
            print("Limite de dispositivos atingido!")
        else:
            self.dispositivos.append(dispositivo)
            self.adicionar_observador(dispositivo)
            self.notificar_observadores(f"Novo dispositivo adicionado: {dispositivo.status_atual()}")

    def remover_dispositivo(self, index):
        self.remover_observador(self.dispositivos[index])
        del self.dispositivos[index]

    def adicionar_observador(self, observador):
        self.observers.append(observador)

    def remover_observador(self, observador):
        self.observers.remove(observador)

    def notificar_observadores(self, message):
        for observer in self.observers:
            observer.update(message)

    def status_dispositivos(self):
        return [dispositivo.status_atual() for dispositivo in self.dispositivos]

    def desligar_todas_luzes(self):

        def desligar_luz(dispositivo):
            if isinstance(dispositivo, Luz) and dispositivo.state == 'ligada':
                dispositivo.desligar()
            return dispositivo

        self.dispositivos = list(map(desligar_luz, self.dispositivos))

    def ligar_todas_luzes(self):

        def desligar_luz(dispositivo):
            if isinstance(dispositivo, Luz) and dispositivo.state == 'desligada':
                dispositivo.ligar()
            return dispositivo

        self.dispositivos = list(map(desligar_luz, self.dispositivos))

    def ligar_desligar_luz(self, index, modo):
        if index == "t":
            if modo == "ligar":
                self.ligar_todas_luzes()
            else:
                self.desligar_todas_luzes()
        else:
            index = int(index)
            dispositivo = self.dispositivos[index]
            if isinstance(dispositivo, Luz):
                if modo == "ligar":
                    dispositivo.ligar()
                elif modo == "desligar":
                    dispositivo.desligar()
                else:
                    print("Algo deu errado no ligar_desligar_luz()")
            else:
                print("instância do index fornecido não é uma luz")

    def contar_dispositivos_ligados(self):

        def is_ligado(dispositivo):
            return (isinstance(dispositivo, Luz) and dispositivo.state == 'ligada') or \
                (isinstance(dispositivo, Termostato) and dispositivo.state != 'desligado') or \
                (isinstance(dispositivo, SistemaSeguranca) and dispositivo.state != 'desligado')

        return reduce(lambda count, dispositivo: count + 1 if is_ligado(dispositivo) else count, self.dispositivos, 0)

    def obter_dispositivos_ligados(self):

        def is_ligado(dispositivo):
            return (isinstance(dispositivo, Luz) and dispositivo.state == 'ligada') or \
                (isinstance(dispositivo, Termostato) and dispositivo.state != 'desligado') or \
                (isinstance(dispositivo, SistemaSeguranca) and dispositivo.state != 'desligado')

        return list(filter(is_ligado, self.dispositivos))

    def desligar_dispositivo(self, index):
        if index < len(self.dispositivos):
            if isinstance(self.dispositivos[index], SistemaSeguranca):
                self.dispositivos[index].desarmar()
            else:
                self.dispositivos[index].desligar()

    def armar_desarmar_seguranca(self, index, modo):
        dispositivo = self.dispositivos[index]
        if isinstance(dispositivo, SistemaSeguranca):
            if modo == "armar_com_gente_em_casa":
                dispositivo.armar_com_gente_em_casa()
            elif modo == "armar_sem_gente_em_casa":
                dispositivo.armar_sem_gente_em_casa()
            elif modo == "desarmar":
                dispositivo.desarmar()
            else:
                print("Algo deu errado no armar_desarmar_seguranca()")
        else:
            print("instância do idex fornecido não é um sistema de segurança")

    def configura_termostato(self, index, modo):
        dispositivo = self.dispositivos[index]
        if isinstance(dispositivo, Termostato):
            if modo == "aquecer":
                dispositivo.aquecer()
            elif modo == "esfriar":
                dispositivo.esfriar()
            elif modo == "desligar":
                dispositivo.desligar()
            else:
                print("Algo deu errado no configura_termostato()")
        else:
            print("instância do index fornecido não é um termostato")


