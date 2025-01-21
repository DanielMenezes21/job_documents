from telas.declaracao_hipo.PF.extracao_dec import *
import os
from kivy.uix.button import Button
from datetime import datetime
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup


def ir_para_home_dec(self, instance):
    """Voltar

    Função de voltar para a homescreen 
    """
    
    self.manager.current =  "home_screen"
    
def obter_dados(screen_instance, _):
    try:

        caminho_declaracao = os.path.join(os.path.dirname(__file__), "13_DECLARACAO_HIPOSSUFICIENCIA_PF_TESTE.docx")
        document = Document(caminho_declaracao)
        
        if not os.path.exists(caminho_declaracao):
            raise FileNotFoundError(f"Arquivo modelo não encontrado em: {caminho_declaracao}")
        # Gerar a data formatada
        data_agora = formatar_data(datetime.now())
        print(f"Data formatada obtida: {data_agora}")  # Debug para confirmar a data
        
        print(caminho_declaracao)

        placeholders = {
            "caminho_declaracao": caminho_declaracao,
            "#NOME_OUTORGANTE": screen_instance.nome_outorgante.text,
            "#PROFISSAO":screen_instance.profissao.text,
            "#SEC_RG":screen_instance.sec_rg.text,
            "#EST_RG": screen_instance.est_rg.text,
            "#OUTORGANTE_CPF": screen_instance.cpf.text,
            "#RG_OUTORGANTE": screen_instance.rg.text,
            "#CIDADE_OUTORGANTE": screen_instance.cidade.text,
            "#SIGLA_ESTADO_OUTORGANTE": screen_instance.estado.text,
            "#NACIONALIDADE": screen_instance.nacionalidade.text,
            "nome_arquivo": screen_instance.nome_arquivo.text,
            "#ENDERECO": screen_instance.endereco.text,
            "#ESTADO_CIVIL": screen_instance.estado_civil.text,
            "#CEP": screen_instance.cep.text,
            "#DATA_AGORA": data_agora,
        }
        
        def substituir_com_formatacao(paragrafo, placeholders):
            for run in paragrafo.runs:
                for placeholder, valor in placeholders.items():
                    if valor is None:
                        valor = ''
                        print(f"o placeholder {placeholder} está vazio")
                    if placeholder in run.text:
                        run.text = run.text.replace(placeholder, valor)
                        #print(f"substituindo {placeholder} por {valor}")

        # Substituir os placeholders no documento
        for paragraph in document.paragraphs:
            substituir_com_formatacao(paragraph, placeholders)
            print(f"substituindo {placeholders} no documento")

        # Substituir nas tabelas
        for tabela in document.tables:
            for linha in tabela.rows:
                for celula in linha.cells:
                    for paragrafo in celula.paragraphs:
                        substituir_com_formatacao(paragrafo, placeholders)

        # Salvar o documento final com o nome especificado
        nome_arquivo = screen_instance.nome_arquivo.text or "documento final"  # Usar nome_arquivo, se disponível
        caminho_salvamento = f"{nome_arquivo}.docx"
        mostrar_popup(
            screen_instance,
            "Sucesso",
            f"Documento salvo como {nome_arquivo}",
            placeholders,
            caminho_declaracao  # Aqui você passa o caminho do modelo da declaração
        )
        document.save(caminho_salvamento)
        os.startfile(caminho_salvamento)

    except Exception as e:
        print(f"Erro ao obter dados: {e}")
        return None
    
def mostrar_popup(screen_instance, titulo, mensagem, placeholders, caminho_declaracao):
    conteudo = BoxLayout(orientation='vertical', padding=10, spacing=10)
    conteudo.add_widget(Label(text=mensagem, halign='center'))
    btn_fechar = Button(text='Fechar', size_hint=(1, 0.3))
    btn_fechar.bind(on_press=lambda instance: popup.dismiss())
    conteudo.add_widget(btn_fechar)
    popup = Popup(title=titulo, content=conteudo, size_hint=(0.7, 0.5))
    popup.open()