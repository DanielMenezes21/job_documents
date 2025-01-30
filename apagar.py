from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.scrollview import ScrollView
from modules.logic_tab import FocusSwitchingTextInput

class CidadeApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Inicialização dos widgets
        self.label_quant = Label(text="Quantas cidades deseja digitar?")
        self.input_quant = FocusSwitchingTextInput(hint_text="Digite um número", multiline=False, size_hint_y=0.5 ,input_filter="int")
        self.btn_confirmar = Button(text="Confirmar", on_press=self.gerar_campos)

        # Layout para os campos de entrada das cidades (GridLayout dentro de ScrollView)
        self.layout_cidades = GridLayout(cols=1, spacing=5, size_hint_y=None)
        self.layout_cidades.bind(minimum_height=self.layout_cidades.setter('height'))

        # Adicionando a ScrollView para permitir rolagem quando muitos campos forem gerados
        scroll = ScrollView(size_hint=(1, 0.9), height=400)
        scroll.add_widget(self.layout_cidades)

        # Checkbox para marcar se as cidades serão iguais
        self.checkbox_igual = CheckBox(pos_hint={'center_x': 0.5, 'center_y': 0.7})
        self.checkbox_igual.bind(active=self.on_checkbox_active)

        # Botão para exibir as cidades digitadas
        self.btn_exibir = Button(text="Exibir Cidades", on_press=self.mostrar_cidades)
        self.btn_exibir.disabled = True  # Inicia desativado

        # Label para mostrar as cidades digitadas
        self.label_resultado = Label(text="")

        # Adicionando widgets na tela
        root.add_widget(self.label_quant)
        root.add_widget(self.input_quant)
        root.add_widget(self.btn_confirmar)
        root.add_widget(Label(text="Marque para preencher todas as cidades com a mesma"))
        root.add_widget(self.checkbox_igual)
        root.add_widget(scroll)  # Adiciona a ScrollView com os campos de cidade
        root.add_widget(self.btn_exibir)
        root.add_widget(self.label_resultado)

        # Inicializa a lista de campos de cidades
        self.campos_cidades = []

        return root

    def gerar_campos(self, instance):
        """Gera dinamicamente os campos de entrada para as cidades"""
        self.layout_cidades.clear_widgets()  # Limpa campos anteriores
        try:
            self.quantidade = int(self.input_quant.text)
            if self.quantidade > 0:
                self.campos_cidades = []  # Recria a lista de campos de cidade
                for i in range(self.quantidade):
                    campo = FocusSwitchingTextInput(hint_text=f"Digite o nome da cidade {i+1}", size_hint_y=None, height=30)
                    self.layout_cidades.add_widget(campo)
                    self.campos_cidades.append(campo)
                self.btn_exibir.disabled = False  # Ativa o botão de exibição
            else:
                self.label_resultado.text = "Por favor, digite um número maior que 0."
        except ValueError:
            self.label_resultado.text = "Insira um número válido!"

    def on_checkbox_active(self, instance, value):
        """Preenche todos os campos com a mesma cidade quando a checkbox é marcada"""
        if value:  # Se a checkbox foi marcada
            cidade_comum = self.campos_cidades[0].text if self.campos_cidades else ""
            for campo in self.campos_cidades:
                campo.text = cidade_comum

    def mostrar_cidades(self, instance):
        """Exibe as cidades digitadas pelo usuário"""
        cidades = [campo.text.strip() for campo in self.campos_cidades if campo.text.strip()]
        if cidades:
            self.label_resultado.text = f"Cidades digitadas:\n" + "\n".join(cidades)
        else:
            self.label_resultado.text = "Nenhuma cidade foi digitada."

if __name__ == "__main__":
    CidadeApp().run()
