from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class HomeContratoScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeContratoScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=50, spacing=50)

        # Adiciona um título à tela inicial
        titulo = Label(
            text="Escolher entre PF e PJ",
            font_size=30,
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={"center_x": 0.5, "center_y": 0.3}  # Centraliza o título
        )
        layout.add_widget(titulo)

        # Campo clicável para navegar até a tela de Procuracao
        btn_contratopf = Button(
            text="Ir para Contrato em Pessoas Físicas",
            size_hint=(None, None),
            size=(230, 50),
            pos_hint={"center_x": 0.5, "center_y": 0.6},  # Ajuste na posição do botão
            on_press=self.ir_para_contrato_pf
        )
        layout.add_widget(btn_contratopf)

        # Campo clicável para navegar até a tela de Processo
        btn_contratopj = Button(
            text="Ir para Contrato em Pessoas Jurídicas",
            size_hint=(None, None),
            size=(230, 50),
            pos_hint={"center_x": 0.5, "center_y": 0.8},  # Ajuste na posição do botão
            on_press=self.ir_para_contrato_pj
        )
        layout.add_widget(btn_contratopj)
        
        btn_voltar = Button(
            text="<",
            size_hint=(None, None),
            size= (50,50),
            pos_hint={"x": 0.1, "y": 0.1},
            on_press=self.voltar
        )
        
        layout.add_widget(btn_voltar)

        # Adiciona o layout à tela
        self.add_widget(layout)
        
    def voltar(self, instance):
        
        self.manager.current = "home_screen"

    def ir_para_contrato_pf(self, instance):
        """
        Função para ir até a tela de contrato_PF_screen1
        """
        self.manager.current = "contrato_PF_screen1"
        
    def ir_para_contrato_pj(self, instance):
        """
        Função para ir até a tela de contrato_screen1
        """
        self.manager.current = "contrato_screen1"
