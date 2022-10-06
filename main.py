from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window


# Define tamanho da janela do app
Window.size = (300,500)

# Constrói o app a partir do arquivo .kv
Builder.load_file('tela.kv')

# Classe contendo funções da calculadora
class Calculadora(Widget):
    def clear(self):
        self.ids.calc_input.text = '0'

# Classe que cria uma instância do Widget Calculadora
class CalculadoraApp(App):
    def build(self):
        return Calculadora()


if __name__ == '__main__':
    CalculadoraApp().run()
