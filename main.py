import argparse
from casainteligente import CasaInteligente
from dispositivo_factory import DispositivoFactory


def main():
    parser = argparse.ArgumentParser(description="Sistema de Casa Inteligente")
    parser.add_argument('--limite', type=int, default=10, help='Limite de dispositivos da casa inteligente')
    args = parser.parse_args()

    casa_inteligente = CasaInteligente.instance(args.limite)
    factory = DispositivoFactory()

    while True:
        print("\n### Menu ###")
        print("1. Ver status dos dispositivos")
        print("2. Controlar dispositivos individuais")
        print("3. Adicionar dispositivo")
        print("4. Remover dispositivo")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print(f"\nStatus dos dispositivos: {casa_inteligente.contar_dispositivos_ligados()} estão ligados")
            for status in casa_inteligente.status_dispositivos():
                print(status)

        elif opcao == '2':
            print("\n### Controlar dispositivos individuais ###")
            print("1. Ligar luzes")
            print("2. Desligar luzes")
            print("3. Configurar modo do termostato")
            print("4. Armar/Desarmar sistema de segurança")

            controle = input("Escolha uma ação: ")

            if controle == '1':
                index = input("Índice da luz para ligar (t para todas): ")
                casa_inteligente.ligar_desligar_luz(index, "ligar")

            elif controle == '2':
                index = input("Índice da luz para desligar (t para todas): ")
                casa_inteligente.ligar_desligar_luz(index, "desligar")

            elif controle == '3':
                index = int(input("Índice do termostato: "))
                modo = input("Modo (aquecer/esfriar/desligar): ").lower()
                casa_inteligente.configura_termostato(index, modo)

            elif controle == '4':
                index = int(input("Índice do sistema de segurança: "))
                modo = input("Modo (armar_com_gente_em_casa/armar_sem_gente_em_casa/desarmar): ").lower()
                casa_inteligente.armar_desarmar_seguranca(index, modo)

            else:
                print("Opção inválida!")

        elif opcao == '3':
            print("\n### Adicionar dispositivo ###")
            tipo = input("Tipo de dispositivo (luz/termostato/sistema_seguranca): ").lower()

            try:
                dispositivo = factory.create_dispositivo(tipo)
            except:
                print(f"{tipo} não foi adicionado")
            else:
                casa_inteligente.adicionar_dispositivo(dispositivo)
                print(f"{tipo} adicionado(a) com sucesso!")

        elif opcao == '4':
            print("\n### Remover dispositivo ###")
            index = int(input("Índice do dispositivo para remover: "))
            if index < len(casa_inteligente.dispositivos):
                casa_inteligente.remover_dispositivo(index)
                print("Dispositivo removido com sucesso!")
            else:
                print("Índice inválido!")

        elif opcao == '5':
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
