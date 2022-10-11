from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window


# Define tamanho da janela do app
Window.size = (300, 500)

# Constrói o app a partir do arquivo .kv
Builder.load_file('tela.kv')

# Classe contendo funções da calculadora
class Calculadora(Widget):

    # função que limpa o espaço de entra de texto
    def clear(self):
        self.ids.calc_input.text = '0'

    # função que registra o pressionar de uma tecla numérica
    def btPress(self, button):
        previous = self.ids.calc_input.text

        if previous == '0':
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{previous}{button}'

    # função que registra os sinais de operações matemáticas (+,-,x,/)
    def operation(self, sign):
        previous = self.ids.calc_input.text
        self.ids.calc_input.text = f'{previous}{sign}'



# Classe que cria uma instância do Widget Calculadora
class CalculadoraApp(App):
    def build(self):
        return Calculadora()


if __name__ == '__main__':
    CalculadoraApp().run()
