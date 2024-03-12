#aqui está o código arrumado seguindo as diretrizes do PEP 8 e PEP 484:
class TrataStrings:
    def __init__(self, text: str) -> None:
        self.text = text

    def get_text(self) -> str:
        return self.text

    def mostrar_dir(self):
        return dir(self.text)

    def normalizar_palavras_chave(self,curriculo):
        palavras_chave = {
            "python": "PYTHON",
            "javascript": "JAVASCRIPT",
            "sql": "SQL",
            "machine learning": "MACHINE LEARNING"
        }

        # Substituir cada palavra-chave pelo seu equivalente em maiúsculas
        for palavra, palavra_maiuscula in palavras_chave.items():
            curriculo = curriculo.replace(palavra, palavra_maiuscula)

        return curriculo







"""
  
Uma situação prática onde str.maketrans() e str.translate()
poderiam ser úteis no mercado de trabalho seria em um sistema
de processamento de currículos,
onde precisamos analisar e padronizar informações.

Suponha que estamos construindo um sistema de análise de currículos
e queremos normalizar as palavras-chave de habilidades técnicas
encontradas nos currículos recebidos.
Por exemplo, queremos converter todas as ocorrências de "Python"
para "PYTHON", "JavaScript" para "JAVASCRIPT", etc.

"""
