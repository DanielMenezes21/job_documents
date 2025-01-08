from telas.contrato_hono.funcoes_contrato_s1 import *
from telas.contrato_hono.extracao_contrato import *
from datetime import datetime
from telas.homepage.home_screen import HomeScreen

def on_sec_rg_change(self, spinner, text):
    """
    Atualiza o campo da secretaria com base na seleção do Spinner.
    """
    if text == "Outro":
        self.sec_rg_input.text = ""  # Limpa o campo
        self.sec_rg_input.readonly = False  # Permite edição
    else:
        self.sec_rg_input.text = "SSP"
        self.sec_rg_input.readonly = True
    
def ir_para_homepage(self, instance):
    
    self.manager.current =  "home_screen"

def on_nacionalidade_change(self, spinner, text):
    """
    Atualiza o campo de nacionalidade com base na seleção do Spinner.
    """
    if text == "Outro":
        self.nacionalidade_input.text = ""  # Limpa o campo
        self.nacionalidade_input.readonly = False  # Permite edição
    else:
        # Ajusta a nacionalidade conforme o gênero selecionado
        inscrita_o = self.inscrita_o_spinner.text
        if inscrita_o == "Feminino":
            self.nacionalidade_input.text = "brasileira"
            # Atualiza o valor de #INSCRITA(O)
            self.inscrita_o_spinner.text = "inscrita"
        else:
            self.nacionalidade_input.text = "brasileiro"
            # Atualiza o valor de #INSCRITA(O)
            self.inscrita_o_spinner.text = "inscrito"
        self.nacionalidade_input.readonly = True  # Torna não editável

def obter_dados(screen_instance):
    try:
        data_agora = formatar_data(datetime.now())
        print(f"Data formatada obtida: {data_agora}")
        dados = {
            "caminho_modelo": screen_instance.caminho_modelo,
            "nome_contratante": screen_instance.nome_contratante.text,
            "rg": screen_instance.rg.text,
            "sec_rg": screen_instance.sec_rg_input.text,
            "cpf": screen_instance.contratante_cpf.text,
            "cidade_contratante": screen_instance.cidade_contratante.text,
            "sigla_estado_contratante": screen_instance.sigla_estado_contratante.text,
            "inscrita_o": screen_instance.inscrita_o_spinner.text,
            "nacionalidade": screen_instance.nacionalidade_input.text,
            "est_rg_input": screen_instance.est_rg_input.text,
            "data_agora": data_agora
        }
    
        print(f"Dados coletados: {dados}") 
        return dados

    except Exception as e:
        print(f"Erro ao obter dados: {e}")
        return None

def ir_para_processo2(screen_instance, instance):
    """
    Função para navegar para a tela de edição de poderes.
    """
    dados = obter_dados(screen_instance)
    if dados:
        # Enviar todos os dados para a tela de poderes
        poderes_screen = screen_instance.manager.get_screen("processo2_screen")
        poderes_screen.poderes_atualizar_dados(dados)  # Passa todos os dados para a tela de poderes
        poderes_screen.caminho_modelo = dados["caminho_modelo"]  # Passa o caminho do arquivo modelo
        screen_instance.manager.current = "processo2_screen"
