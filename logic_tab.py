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
    
class MaskedFocusSwitchingTextInput(FocusSwitchingTextInput):
    def __init__(self, max_length, mask, **kwargs):
        """
        Inicializa o TextInput com tamanho máximo e máscara.
        :param max_length: Quantidade máxima de dígitos permitidos (exemplo: 11 para CPF).
        :param mask: Máscara a ser aplicada após preencher o campo.
        """
        super().__init__(**kwargs)
        self.max_length = max_length
        self.mask = mask
        self.bind(text=self._on_text)

    def _on_text(self, instance, value):
        """
        Verifica o comprimento do texto e aplica a máscara ao completá-lo.
        """
        digits = ''.join(filter(str.isdigit, value))  # Filtra apenas números
        if len(digits) == self.max_length:  # Quando o campo está completo
            self.text = self._apply_mask(digits)
            self.focus = False  # Remove o foco do campo atual
            next_widget = self.get_next_focusable()  # Obtém o próximo widget focável
            if next_widget:
                next_widget.focus = True  # Move o foco para o próximo widget

    def insert_text(self, substring, from_undo=False):
        """
        Insere texto respeitando apenas números e o limite máximo de caracteres.
        """
        if len(self.text) >= self.max_length and not self.text.isdigit():
            return  # Impede inserções além do limite
        substring = ''.join(filter(str.isdigit, substring))  # Permite apenas números
        if len(''.join(filter(str.isdigit, self.text))) + len(substring) > self.max_length:
            substring = substring[: self.max_length - len(self.text)]  # Limita ao máximo
        return super().insert_text(substring, from_undo)

    def _apply_mask(self, digits):
        """
        Aplica a máscara ao texto.
        """
        masked_text = list(self.mask)
        digit_index = 0

        for i, char in enumerate(masked_text):
            if char == ' ' and digit_index < len(digits):
                masked_text[i] = digits[digit_index]
                digit_index += 1

        return ''.join(masked_text)



'''class MyApp(App):
    def build(self):
        """
        Cria a interface do aplicativo usando um GridLayout contendo BoxLayouts.
        """
        root = GridLayout(cols=1, padding=10, spacing=10)  # Layout principal

        # Primeiro BoxLayout com campos de entrada
        box1 = BoxLayout(orientation="horizontal", spacing=10)
        box1.add_widget(FocusSwitchingTextInput(hint_text="Nome"))  # Campo de texto normal
        box1.add_widget(FocusSwitchingTextInput(hint_text="Sobrenome"))  # Campo readonly

        # Segundo BoxLayout com campos de entrada
        box2 = BoxLayout(orientation="horizontal", spacing=10)
        box2.add_widget(MaskedFocusSwitchingTextInput(
            hint_text="CPF", max_length=11, mask="   .   .   -  "))

        # Campo de texto para CNPJ (14 dígitos)
        box2.add_widget(MaskedFocusSwitchingTextInput(
            hint_text="CNPJ", max_length=14, mask="  .   .   /    -  ")) 

        # Adiciona os BoxLayouts no GridLayout principal
        root.add_widget(box1)
        root.add_widget(box2)

        return root  # Retorna o layout principal para exibição


if __name__ == "__main__":
    MyApp().run()
'''