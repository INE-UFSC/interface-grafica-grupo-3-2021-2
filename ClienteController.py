from ClienteView import ClienteView
from Cliente import Cliente
import PySimpleGUI as sg


class ClienteController:
    def __init__(self):
        self.__telaCliente = ClienteView(self)
        self.__clientes = {}  # lista de objetos Cliente

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
                nome = str(values['nome'])
                try:
                    codigo = int(values['codigo'])
                    cliente = Cliente(nome, codigo)
                    self.__clientes[codigo] = cliente
                    resultado = 'Cliente cadastrado'
                except:
                    resultado = 'Código deve ser um número inteiro'
                    
            elif event == 'Consultar':
                nome = str(values['nome'])
                try:
                    codigo = int(values['codigo'])
                    try:
                        cliente_obj = self.busca_codigo(codigo)
                        resultado = cliente_obj.__str__()
                    except KeyError:
                        resultado = 'Não encontrado'
                except:
                    resultado = 'Código deve ser um número inteiro'
                
                if nome != '':
                    try:
                        cliente_cod = self.busca_nome(nome)
                        resultado = f'Nome: {nome}, Codigo: {cliente_cod}'
                    except LookupError:
                        resultado = 'Não encontrado'

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
