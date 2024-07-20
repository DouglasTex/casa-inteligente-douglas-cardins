from luz import Luz
from sistema_seguranca import SistemaSeguranca
from termostato import Termostato


class DispositivoFactory:
    @staticmethod
    def create_dispositivo(tipo):
        if tipo == 'luz':
            return Luz()
        elif tipo == 'termostato':
            return Termostato()
        elif tipo == 'sistema_seguranca':
            return SistemaSeguranca()
        else:
            raise ValueError(f'Tipo de dispositivo desconhecido: {tipo}')
