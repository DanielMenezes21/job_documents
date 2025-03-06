from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import SlideTransition
from modules.resource_path import BackgroundImage

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        with self.canvas.before:
            self.background = BackgroundImage()
            self.bind(size=self._update_background, pos=self._update_background)

        titulo = Label(
            text="Tela Inicial",
            font_size=30,
            font_name="BELL.TTF",
            color="yellow",
            size_hint_y=0.20,
        )
        layout.add_widget(titulo)

        btn_procuracao = Button(
            text="Ir para Procuração",
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={"center_x": 0.5, "top": 0.6}, 
            on_press=self.ir_para_procuracao
        )
        layout.add_widget(btn_procuracao)

        btn_contrato = Button(
            text="Ir para Contrato",
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={"center_x": 0.5, "top": 0.4},  
            on_press=self.ir_para_contrato
        )
        layout.add_widget(btn_contrato)
        
        btn_declaracao = Button(
            text="Ir para Declaração",
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={"center_x": 0.5, "top": 0.2},
            on_press=self.ir_para_declaracao
        )
        layout.add_widget(btn_declaracao)

        self.add_widget(layout)

    def _update_background(self, *args):
        self.background.size = self.size
        self.background.pos = self.pos

    def ir_para_procuracao(self, instance):
        """
        Função para ir até a tela de ProcuracaoScreen
        """
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = "home_procuracao_screen"
        
    def ir_para_contrato(self, instance):
        """
        Função para ir até a tela de ProcessoScreen
        """
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = "home_contrato_screen"
        
    def ir_para_declaracao(self, instance):
        """
        Função para ir até a tela de DadosPessoaisPF
        """
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = "homepage_declaracao"
        
    
