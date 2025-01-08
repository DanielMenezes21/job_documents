#main.py
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from telas.contrato_hono.contrato_screen1 import ProcessoScreen
from telas.contrato_hono.contrato_screen2 import Processo2Screen
from telas.procuracao.procuracao_queixa_crime.poderes_screen_qc import PoderesScreen
from telas.homepage.home_screen import HomeScreen
from telas.procuracao.procuracao_queixa_crime.procuracao_screen_qc import ProcuracaoScreen

class MyApp(ScreenManager): 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Adiciona as telas ao ScreenManager
        self.add_widget(HomeScreen(name="home_screen"))
        self.add_widget(PoderesScreen(name="poderes_screen"))
        self.add_widget(ProcessoScreen(name="contrato_screen1"))
        self.add_widget(Processo2Screen(name="contrato_screen2"))
        self.add_widget(ProcuracaoScreen(name="procuracao_screen"))
        
class MainApp(App):
    def build(self):
        # Retorna o ScreenManager configurado
        return MyApp()


if __name__ == "__main__":
    MainApp().run()

