from ClienteView import ClienteView
from Cliente import Cliente
import PySimpleGUI as sg 

def Validacao():
    nome = input('Digite o nome do cliente: ')
                while True :
                    codigo = int(input('Digite o código do cliente: '))
                    try:
                        codigo = int(codigo)
                        break
                    except:
                        print('Codigo inválido!')
    return nome, codigo                   
class ClienteController:
    def __init__(self):
        self.__telaCliente = ClienteView(self)
        self.__clientes = {} #lista de objetos Cliente

    def inicia(self):
        self.__telaCliente.tela_consulta()
        
        # Loop de eventos
        rodando = True
        resultado = ''
        while rodando:
            event, values = self.__telaCliente.le_eventos()

            if event == sg.WIN_CLOSED:
                rodando = False
            elif event == 'Cadastrar':
                nome, codigo = Validacao()
                        
                cliente = Cliente(nome, codigo)
                self.__clientes[codigo] = cliente
                
            elif event == 'Consultar':
                nome, codigo = Validacao()
                cliente_cod = self.busca_codigo(codigo)
                cliente_nom = self.busca_nome(nome)
                if
            if resultado != '':
                dados = str(resultado)
                self.__telaCliente.mostra_resultado(dados)

        self.__telaCliente.fim()


    def busca_codigo(self, codigo):
        try:
            return self.__clientes[codigo]
        except KeyError:
            raise KeyError

    # cria novo OBJ cliente e adiciona ao dict
    def adiciona_cliente(self, codigo, nome):
        self.__clientes[codigo] = Cliente(codigo, nome)
    
    def busca_nome(self, nome):
        for key, val in self.__clientes.items():
            if val.nome == nome:
                return key 

        raise LookupError
