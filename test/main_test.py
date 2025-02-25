from kivymd.app import MDApp
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from funcoes_busca import buscar_pessoas_por_nome
from kivy.graphics import Rectangle, Color
from kivymd.uix.button import MDIconButton
from kivymd.uix.card import MDCard
from logic_tab import FocusSwitchingTextInput, MaskedFocusSwitchingTextInput

class PesquisaApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=10, spacing=10, **kwargs)
        
        self.background = Color(rgba=(0, 0, 0, 1))
        
        self.search_button = MDIconButton(icon="magnify", size_hint=(0.2, 0.2), pos_hint={"center_x": 0.95, "center_y": 0.5})
        self.search_button.bind(on_release=self.open_search_popup)
        
        self.search_card = MDCard(
        size_hint=(None, None),
        size=(64, 64),  # Tamanho da "caixa"
        elevation=4,  # Efeito de sombra
        radius=[16],  # Bordas arredondadas
        padding=10,
        pos_hint={"center_x": 0.95, "center_y": 0.5}
        )
        self.search_card.bind(on_release=self.open_search_popup)
        self.search_card.add_widget(self.search_button)  # Adiciona o botão dentro da "caixa"
        
        self.nome_input = FocusSwitchingTextInput(hint_text="Nome", multiline=False)
        self.cpf_input = MaskedFocusSwitchingTextInput(hint_text="CPF", multiline=False, mask="   .   .   -  ", max_length=11)
        self.rg_input = FocusSwitchingTextInput(hint_text="RG", multiline=False)
        self.endereco_input = FocusSwitchingTextInput(hint_text = "endereco", multiline = False)
        self.est_civil_input = FocusSwitchingTextInput(hint_text = "estado civil", multiline = False)
        
        self.add_widget(self.search_card)
        self.add_widget(self.nome_input)
        self.add_widget(self.cpf_input)
        self.add_widget(self.rg_input)
        self.add_widget(self.endereco_input)
        self.add_widget(self.est_civil_input)
        
    def open_search_popup(self, instance):
        self.pesquisa_input = TextInput(hint_text="Digite um nome ou CPF...", multiline=False, size_hint=(1, 0.18), height=30)
        self.pesquisa_input.bind(text=self.atualizar_lista)
        
        self.scroll = ScrollView()
        self.lista = MDList()
        self.scroll.add_widget(self.lista)
        
        popup_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        popup_layout.add_widget(self.pesquisa_input)
        popup_layout.add_widget(self.scroll)
        
        self.popup = Popup(title="Pesquisar Cliente", content=popup_layout, size_hint=(0.9, 0.9))
        self.popup.open()

    def atualizar_lista(self, instance, value):
        self.lista.clear_widgets()
        for nome, cpf, rg, endereco, estado_civil in buscar_pessoas_por_nome(self.pesquisa_input.text.strip()):
            item = OneLineListItem(text=f"{nome} - {cpf}")
            item.bind(on_release=lambda x: self.preencher_campos(x.text))
            self.lista.add_widget(item)
    
    def preencher_campos(self, texto):
        nome, cpf = texto.split(" - ")
        for nome_bd, cpf_bd, rg_bd, endereco_bd, estado_civil_bd in buscar_pessoas_por_nome(cpf):
            if cpf_bd == cpf:
                self.nome_input.text = nome_bd
                self.cpf_input.text = cpf_bd
                self.rg_input.text = rg_bd
                self.endereco_input.text = endereco_bd
                self.est_civil_input.text = estado_civil_bd
                self.popup.dismiss()
                break

class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return PesquisaApp()

if __name__ == "__main__":
    MyApp().run()