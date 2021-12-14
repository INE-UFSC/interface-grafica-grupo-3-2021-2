import PySimpleGUI as sg 

# View do padrão MVC
class ClienteView():
    def __init__(self, controlador):
        self.__controlador = controlador
        self.__container = []
        self.__window = sg.Window("Consulta de clientes", self.__container ,font=("Helvetica", 14))

    def tela_consulta(self):
        #FIX ME - implementar a GUI e colocar em self.__container
        sg.theme('Dark Amber')
        self.__container = [[sg.Text('Digite o nome ou o código do cliente e clique na ação desejada:')],
                            [sg.Text('Nome:'), sg.InputText(key='nome')],
                            [sg.Text('Código:'), sg.InputText(key='codigo')],
                            [sg.Submit('Cadastrar'), sg.Submit('Consultar')],
                            [sg.Text('', key='resultado')]
                            ]
        self.__window = sg.Window("Consulta de clientes", self.__container ,font=("Helvetica", 14))

    def mostra_resultado(self, resultado): 
        self.__window.Element('resultado').Update(resultado)
        self.__window.Element('nome').Update('')
        self.__window.Element('codigo').Update('')

    def le_eventos(self):
        return self.__window.read()

    def fim(self):
        self.__window.close()
