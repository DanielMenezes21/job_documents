from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.label import Label
from kivy.uix.widget import Widget

class FocusSwitchingTextInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.unfocus_color = [1, 1, 1, 1]  # Branco
        self.focus_color = [0.8, 0.8, 1, 1]  
        self.background_color = self.unfocus_color
    
    def on_focus(self, instance, value):
        self.background_color = self.focus_color if value else self.unfocus_color

    def keyboard_on_key_down(self, window, keycode, text, modifiers):
        if keycode[1] == "tab":
            self.focus = False
            next_widget = self.get_next_focusable()
            if next_widget:
                next_widget.focus = True
            return True
        return super().keyboard_on_key_down(window, keycode, text, modifiers)

    def get_next_focusable(self):
        next_widget = self.get_focus_next()
        while next_widget and isinstance(next_widget, TextInput) and next_widget.readonly:
            next_widget = next_widget.get_focus_next()
        return next_widget

class MaskedFocusSwitchingTextInput(FocusSwitchingTextInput):
    def __init__(self, max_length, mask, **kwargs):
        super().__init__(**kwargs)
        self.max_length = max_length
        self.mask = mask
        self.bind(text=self._on_text)

    def _on_text(self, instance, value):
        digits = ''.join(filter(str.isdigit, value))
        if len(digits) == self.max_length:
            self.text = self._apply_mask(digits)
            self.focus = False
            next_widget = self.get_next_focusable()
            if next_widget:
                next_widget.focus = True

    def insert_text(self, substring, from_undo=False):
        if len(self.text) >= self.max_length and not self.text.isdigit():
            return
        substring = ''.join(filter(str.isdigit, substring))
        if len(''.join(filter(str.isdigit, self.text))) + len(substring) > self.max_length:
            substring = substring[: self.max_length - len(self.text)]
        return super().insert_text(substring, from_undo)

    def _apply_mask(self, digits):
        masked_text = list(self.mask)
        digit_index = 0
        for i, char in enumerate(masked_text):
            if char == ' ' and digit_index < len(digits):
                masked_text[i] = digits[digit_index]
                digit_index += 1
        return ''.join(masked_text)

class FocusSwitchingSpinner(Spinner):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.unfocus_color = "atlas://data/images/defaulttheme/button"
        self.focus_color = "atlas://data/images/defaulttheme/button_pressed"
        self.background_normal = self.unfocus_color
    
    def on_focus(self, instance, value):
        self.background_normal = self.focus_color if value else self.unfocus_color

    def keyboard_on_key_down(self, window, keycode, text, modifiers):
        if keycode[1] == "tab":
            self.focus = False
            next_widget = self.get_focus_next()
            if next_widget:
                next_widget.focus = True
            return True
        return super().keyboard_on_key_down(window, keycode, text, modifiers)

"""class MyApp(App):
    def build(self):
        root = GridLayout(cols=1, padding=10, spacing=10)
        
        box1 = BoxLayout(orientation="horizontal", spacing=10)
        nome_input = FocusSwitchingTextInput(hint_text="Nome")
        sobrenome_input = FocusSwitchingTextInput(hint_text="Sobrenome")
        box1.add_widget(nome_input)
        box1.add_widget(sobrenome_input)
        
        box2 = BoxLayout(orientation="horizontal", spacing=10)
        cpf_input = MaskedFocusSwitchingTextInput(hint_text="CPF", max_length=11, mask="   .   .   -  ")
        cnpj_input = MaskedFocusSwitchingTextInput(hint_text="CNPJ", max_length=14, mask="  .   .   /    -  ")
        box2.add_widget(cpf_input)
        box2.add_widget(cnpj_input)
        
        box3 = BoxLayout(orientation="horizontal", spacing=10)
        spinner = FocusSwitchingSpinner(text="Escolha uma opção", values=("Opção 1", "Opção 2", "Opção 3"))
        box3.add_widget(Label(text="Categoria: "))
        box3.add_widget(spinner)
        
        root.add_widget(box1)
        root.add_widget(box2)
        root.add_widget(box3)
        
        return root

if __name__ == "__main__":
    MyApp().run()
"""