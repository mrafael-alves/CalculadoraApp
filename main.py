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

    # Função que limpa o espaço de entra de texto
    def clear(self):
        self.ids.calc_input.text = '0'

    # Função que apaga o último caractere da caixa de texto
    def backspace(self):
        previous = self.ids.calc_input.text
        self.ids.calc_input.text = previous[:-1]

    # Função que registra o pressionar de uma tecla numérica
    def bt_press(self, button):
        previous = self.ids.calc_input.text

        # Apaga mensagem de erro ao clicar em um dígito
        if 'Error' in previous:
            previous = ''

        if previous == '0':
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{previous}{button}'

    # Função que registra os sinais de operações matemáticas (+,-,x,/)
    def operation(self, sign):
        previous = self.ids.calc_input.text
        self.ids.calc_input.text = f'{previous}{sign}'

    # Função que adiciona o separador decimal aos números
    def decimal(self):
        previous = self.ids.calc_input.text
        signs = ('+', '-', '/', '*')

        for sign in signs:
            # Caso haja operação na string E o último número NÃO tenha decimal
            if sign in previous and '.' not in previous.split(sign)[-1]:
                previous = f'{previous}.'
                self.ids.calc_input.text = previous
            # Caso já exista o sepador decimal
            elif '.' in previous:
                pass
            # Caso seja o primeiro número digitado
            else:
                previous = f'{previous}.'
                self.ids.calc_input.text = previous

    # Função que altera sinal de positivo e negativo de número
    def change_sign(self):
        previous = self.ids.calc_input.text

        if '-' in previous:
            self.ids.calc_input.text = f"{previous.replace('-', '')}"
        else:
            self.ids.calc_input.text = f'-{previous}'

    # Função que retorna o peso da porcentagem em decimal
    def percent(self):
        previous = self.ids.calc_input.text
        answer = float(previous) / 100.0
        self.ids.calc_input.text = str(answer)

    # Função que retorna o resultado da operação
    def equals(self):
        # Testa a operação digitada
        try:
            previous = self.ids.calc_input.text
            result = eval(previous)
            self.ids.calc_input.text = str(result)
        # Imprime erro caso o teste acima falhe
        except:
            self.ids.calc_input.text = 'Error'


# Classe que cria uma instância do Widget Calculadora
class CalculadoraApp(App):
    def build(self):
        return Calculadora()


if __name__ == '__main__':
    CalculadoraApp().run()
