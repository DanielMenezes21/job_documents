import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from docx import Document

# Textos das cláusulas
TEXTOS_CLAUSULAS = {
    "Cláusula 1": (
        "(Descrever objetivo específico mais detalhado possível com número de processo, contrato, etc.)"
    ),
    "Cláusula 2": (
        "A presente contratação não resguarda qualquer relação com vinculação empregatícia."
    ),
    "Cláusula 3": (
        "Pelos serviços prestados e especificados na cláusula 1ª, "
        "o CONTRATADO receberá, a título de honorários advocatícios, "
        "o correspondente a {R$ valor ({valor em extenso} reais)}, "
        "da seguinte forma: R$ {valor em reais} de entrada no ato da assinatura "
        "deste instrumento contratual, {metodo de pagamento}, o restante em 23 "
        "parcelas iguais no valor de {valor da parcela} para todo dia {dia definido} de cada "
        "mês iniciando-se em {data de inicio}, por meio de {metodo de pagamento}."
    ),
}

class ClausulasApp(App):
    def build(self):
        self.placeholders = {
            "#CLAUSULA_1": "",
            "#CLAUSULA_2": "",
            "#CLAUSULA_3": "",
        }

        # Layout principal
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Spinner para seleção de cláusulas
        self.spinner = Spinner(
            text="Selecione a cláusula",
            values=list(TEXTOS_CLAUSULAS.keys()),
            size_hint=(1, 0.2),
        )
        self.spinner.bind(text=self.on_spinner_select)
        layout.add_widget(self.spinner)

        # TextInput para exibir e editar a cláusula selecionada
        self.text_input = TextInput(hint_text="Texto da cláusula", multiline=True, size_hint=(1, 0.6))
        layout.add_widget(self.text_input)

        # Botão para salvar documento
        save_button = Button(text="Salvar Documento", size_hint=(1, 0.2))
        save_button.bind(on_press=self.save_document)
        layout.add_widget(save_button)

        return layout

    def on_spinner_select(self, spinner, text):
        """
        Atualiza o TextInput com o texto da cláusula selecionada.
        """
        clause_key = f"Cláusula {list(TEXTOS_CLAUSULAS.keys()).index(text) + 1}"
        self.placeholders[f"#CLAUSULA{list(TEXTOS_CLAUSULAS.keys()).index(text) + 1}"] = self.text_input.text
        self.text_input.text = TEXTOS_CLAUSULAS.get(text, "")

    def save_document(self, instance):
        """
        Substitui os placeholders no documento modelo e salva o documento final.
        """
        # Atualiza os placeholders com os textos editados
        for idx, key in enumerate(self.placeholders.keys(), start=1):
            clausula_key = f"Cláusula {idx}"
            self.placeholders[key] = TEXTOS_CLAUSULAS.get(clausula_key, "")

        # Verifica se o arquivo modelo existe
        modelo_path = "teste_apagar.docx"
        if not os.path.exists(modelo_path):
            print(f"Arquivo {modelo_path} não encontrado!")
            return

        # Abre o documento modelo
        document = Document(modelo_path)

        # Substitui os placeholders no documento
        for paragraph in document.paragraphs:
            for placeholder, value in self.placeholders.items():
                if placeholder in paragraph.text:
                    paragraph.text = paragraph.text.replace(placeholder, value)

        # Salva o documento final
        final_path = "documento_final.docx"
        document.save(final_path)
        print(f"Documento salvo como {final_path}")
        os.startfile(final_path)

if __name__ == "__main__":
    ClausulasApp().run()
