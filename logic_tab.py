from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class FocusSwitchingTextInput(TextInput):
    def keyboard_on_key_down(self, window, keycode, text, modifiers):
        """
        Intercepta os eventos de teclado e permite alternar o foco com a tecla Tab.
        """
        if keycode[1] == "tab":  # Verifica se a tecla pressionada é Tab
            self.focus = False  # Remove o foco do widget atual
            next_widget = self.get_next_focusable()  # Obtém o próximo widget focável
            if next_widget:
                next_widget.focus = True  # Define o próximo widget como focado
            return True  # Impede o processamento padrão do evento
        return super().keyboard_on_key_down(window, keycode, text, modifiers)

    def get_next_focusable(self):
        """
        Encontra o próximo widget focável que não está configurado como readonly.
        """
        next_widget = self.get_focus_next()  # Obtém o próximo widget na hierarquia de foco
        # Continua buscando enquanto o próximo widget for readonly
        while next_widget and isinstance(next_widget, TextInput) and next_widget.readonly:
            next_widget = next_widget.get_focus_next()  # Busca o próximo na sequência
        return next_widget  # Retorna o próximo widget válido ou None


class MyApp(App):
    def build(self):
        """
        Cria a interface do aplicativo usando um GridLayout contendo BoxLayouts.
        """
        root = GridLayout(cols=1, padding=10, spacing=10)  # Layout principal

        # Primeiro BoxLayout com campos de entrada
        box1 = BoxLayout(orientation="horizontal", spacing=10)
        box1.add_widget(FocusSwitchingTextInput(hint_text="Nome"))  # Campo de texto normal
        box1.add_widget(FocusSwitchingTextInput(hint_text="Sobrenome", readonly=True))  # Campo readonly

        # Segundo BoxLayout com campos de entrada
        box2 = BoxLayout(orientation="horizontal", spacing=10)
        box2.add_widget(FocusSwitchingTextInput(hint_text="RG"))  # Campo de texto normal
        box2.add_widget(FocusSwitchingTextInput(hint_text="CPF", readonly=True))  # Campo readonly

        # Adiciona os BoxLayouts no GridLayout principal
        root.add_widget(box1)
        root.add_widget(box2)

        return root  # Retorna o layout principal para exibição


if __name__ == "__main__":
    MyApp().run()
