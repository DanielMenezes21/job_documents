# funcoes_procuracao.py
from telas.procuracao.PJ.procuracao_queixa_crime.pj_funcoes_poderes_qc import *
from telas.procuracao.PJ.procuracao_queixa_crime.pj_poderes_screen_qc import PoderesQCPJScreen
from datetime import datetime
from logic_tab import FocusSwitchingTextInput

def on_nacionalidade_change(screen_instance, spinner, text):
    if text == "Outro":
        screen_instance.nacionalidade_input.text = ""
        screen_instance.nacionalidade_input.readonly = False
    else:
        inscrita_o = screen_instance.inscrita_o_spinner.text
        if inscrita_o == "Feminino":
            screen_instance.nacionalidade_input.text = "brasileira"
            screen_instance.inscrita_o_spinner.text = "inscrita"
        else:
            screen_instance.nacionalidade_input.text = "brasileiro"
            screen_instance.inscrita_o_spinner.text = "inscrito"
        screen_instance.nacionalidade_input.readonly = True
        
# Adicione um atributo de controle ao objeto da tela
def on_cnpj_change(self, instance, value):
    if getattr(self, "_updating_cnpj", False):
        return

    self._updating_cnpj = True
    try:
        # Aplica a máscara
        texto_mascarado = FocusSwitchingTextInput.aplicar_mascara_cnpj(value)
        if texto_mascarado != instance.text:
            instance.text = texto_mascarado
            # Move o cursor para o final
            instance.cursor = (len(texto_mascarado), 1)
    finally:
        self._updating_cnpj = False

def on_cpf_change(self, instance, value):
    if getattr(self, "_updating_cpf", False):
        return

    self._updating_cpf = True
    try:
        texto_mascarado = FocusSwitchingTextInput.aplicar_mascara_cpf(value)
        if texto_mascarado != instance.text:
            instance.text = texto_mascarado
            # Move o cursor para o final
            instance.cursor = (len(texto_mascarado), 0)
    finally:
        self._updating_cpf = False

def on_cep_change(self, instance, value):
    if getattr(self, "_updating_cep", False):
        return

    self._updating_cep = True
    try:
        texto_mascarado = FocusSwitchingTextInput.aplicar_mascara_cep(value)
        if texto_mascarado != instance.text:
            instance.text = texto_mascarado
            # Move o cursor para o final
            instance.cursor = (len(texto_mascarado), 0)
    finally:
        self._updating_cep = False


def ir_para_procuracao(self, instance):
    
    self.manager.current =  "home_procuracao_screen"

def obter_dados(screen_instance):
    try:
        caminho_modelo = os.path.join(os.path.dirname(__file__), "11_PROCURACAO_PJ_CQ_TESTE.docx")
        
        if not os.path.exists(caminho_modelo):
            raise FileNotFoundError(f"Arquivo modelo não encontrado em: {caminho_modelo}")
        # Gerar a data formatada
        data_agora = formatar_data(datetime.now())
        print(f"Data formatada obtida: {data_agora}")
        
        print(caminho_modelo)

        dados = {
            "caminho_modelo": caminho_modelo,
            "nome_outorgante": screen_instance.nome_outorgante.text,
            "nome_empresa": screen_instance.nome_empresa.text,
            "cnpj": screen_instance.cnpj.text,
            "end_empresa": screen_instance.end_empresa.text,
            "cep_empresa": screen_instance.cep_empresa.text,
            "cpf": screen_instance.cpf.text,
            "rg": screen_instance.rg.text,
            "cidade_outorgante": screen_instance.cidade_outorgante_input.text,
            "sigla_estado_outorgante": screen_instance.sigla_estado_outorgante_input.text,
            "inscrita_o": screen_instance.inscrita_o_spinner.text,
            "nacionalidade": screen_instance.nacionalidade_input.text,
            "nome_arquivo": screen_instance.nome_arquivo_input.text,
            "endereco": screen_instance.endereco.text,
            "estado_civil": screen_instance.estado_civil.text,
            "cep": screen_instance.cep.text,
            "data_agora": data_agora,
        }

        print(f"Dados coletados: {dados}")  # Verificar todos os dados coletados
        return dados

    except Exception as e:
        print(f"Erro ao obter dados: {e}")
        return None

def ir_para_poderes(screen_instance, instance):
    """
    Navega para a tela PoderesScreen e envia os dados coletados.
    """
    dados = obter_dados(screen_instance)
    if dados:
        poderes_screen = screen_instance.manager.get_screen("poderes_queixa_crime_pj_screen")
        poderes_screen.poderes_atualizar_dados(dados)  # Certifique-se de que o nome corresponde
        screen_instance.manager.current = "poderes_queixa_crime_pj_screen"

