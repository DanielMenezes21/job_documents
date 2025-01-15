from telas.contrato_hono.PJ.funcoes_contrato_s2 import *
from telas.contrato_hono.PJ.extracao_contrato import *
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
        caminho_modelo = os.path.join(os.path.dirname(__file__), "10_MODELO_CONTRATACAO_PJ_TESTE - Copia.docx")
        
        if not os.path.exists(caminho_modelo):
            raise FileNotFoundError(f"Arquivo modelo não encontrado em: {caminho_modelo}")
        
        data_agora = formatar_data(datetime.now())
        print(f"Data formatada obtida: {data_agora}")
        dados = {
            "caminho_modelo": caminho_modelo,
            "nome_arquivo": screen_instance.nome_arquivo.text,
            "numero": screen_instance.num_contrato.text,
            "nome_contratante": screen_instance.nome_contratante.text,
            "nome_empresa": screen_instance.nome_empresa.text,
            "cnpj": screen_instance.cnpj.text,
            "end_empresa": screen_instance.end_empresa.text,
            "cep_empresa": screen_instance.cep_empresa.text,
            "cidade_emp": screen_instance.cid_empresa.text,
            "estado_emp": screen_instance.est_empresa.text,
            "cpf": screen_instance.contratante_cpf.text,
            "rg": screen_instance.contratante_rg.text,
            "cidade_contratante": screen_instance.cidade_contratante.text,
            "sigla_estado_contratante": screen_instance.sigla_estado_contratante.text,
            "cep_contratante": screen_instance.cep_cont.text,
            "estado_civil": screen_instance.estado_civil.text,
            "inscrita_o": screen_instance.inscrita_o_spinner.text,
            "nacionalidade": screen_instance.nacionalidade_input.text,
            "sec_rg": screen_instance.sec_rg.text,
            
            "data_agora": data_agora
        }
    
        print(f"Dados coletados: {dados}") 
        return dados

    except Exception as e:
        print(f"Erro ao obter dados 2: {e}")
        return None

def ir_para_processo2(screen_instance, instance):
    """
    Função para navegar para a tela de edição de poderes.
    """
    dados = obter_dados(screen_instance)
    if dados:
        # Enviar todos os dados para a tela de poderes
        poderes_screen = screen_instance.manager.get_screen("contrato_screen2")
        poderes_screen.poderes_atualizar_dados(dados)  # Passa todos os dados para a tela de poderes
        poderes_screen.caminho_modelo = dados["caminho_modelo"]  # Passa o caminho do arquivo modelo
        screen_instance.manager.current = "contrato_screen2"
