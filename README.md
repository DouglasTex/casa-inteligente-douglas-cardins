# Sistema de Casa Inteligente

## Visão Geral do Projeto

O Sistema de Casa Inteligente é uma aplicação em Python que simula a integração e o controle de dispositivos em uma casa inteligente. Ele utiliza conceitos de programação funcional e o padrão de design Observer para gerenciar dispositivos como luzes, termostatos e sistemas de segurança. Os usuários podem interagir com o sistema através de uma interface de linha de comando (CLI) para adicionar, remover e controlar dispositivos, bem como visualizar o status dos dispositivos atuais.

## Instruções para Configurar e Executar o Projeto

### Pré-requisitos

Certifique-se de ter o Python 3.7 ou superior instalado em sua máquina.

### Passos para Configuração

1. Navegue até o diretório do projeto:
   ```sh
   cd casa-inteligente-douglas-cardins
    ```

## Executando o Projeto

Para iniciar a aplicação, execute o seguinte comando na linha de comando, substituindo <limite_dispositivos> pelo número máximo de dispositivos que a casa inteligente pode suportar:
   ```sh
   python casa_inteligente.py --limite <limite_dispositivos>
   ```

## Descrições dos Principais Componentes e Padrões de Design Utilizados

### Componentes Principais

1. Classe Dispositivo:
    
Classe abstrata que define a interface básica para todos os dispositivos.


2. Classe Luz:

Representa uma luz que pode ser ligada ou desligada.

Implementa a interface Observer para receber notificações de mudanças.

3. Classe Termostato:

Representa um termostato que pode aquecer, esfriar ou desligar.

Implementa a interface Observer para receber notificações de mudanças.

4. Classe SistemaSeguranca:

Representa um sistema de segurança que pode ser armado ou desarmado.

Implementa a interface Observer para receber notificações de mudanças.

5. Classe CasaInteligente:

Singleton que gerencia os dispositivos adicionados à casa inteligente.
Implementa métodos para adicionar, remover e controlar dispositivos.
Permite adicionar observadores que serão notificados sobre mudanças no estado dos dispositivos.

### Padrões de Design Utilizados

1. Observer:
   1. Utilizado para permitir que objetos (observadores) recebam notificações de mudanças em outro objeto (sujeito). No projeto, a CasaInteligente notifica os dispositivos observadores sobre mudanças no sistema.

2. Singleton:
   1. Garante que apenas uma instância da CasaInteligente seja criada durante a execução do programa.

3. State Machine:
   1. Implementada com a biblioteca transitions para gerenciar os estados dos dispositivos como Luz, Termostato e SistemaSeguranca.



