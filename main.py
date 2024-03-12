from tratastrings import TrataStrings

def main():
    trata = TrataStrings("Hello World!")
    print("String passada...")
    print(trata.get_text())
    print("Mostrando os recursos de strings")
    print(trata.mostrar_dir())
    #mostrando o texto letras maísculas
    print("Mostra maíscula..")
    print(trata.get_text().upper())
    texto = trata.get_text()
    texto_sem_a_primeira_letra = texto[1:]
    print("Mostra o texto sem a primeira letra")
    print(texto_sem_a_primeira_letra)
    pegando_world = texto[0:5]
    print("Mostrando apenas a palavra world")
    print(pegando_world)
    print("# Usando a função dir() para listar os métodos e atributos do objeto")
    print(vars(trata))

    # Currículo recebido
    curriculo = "Experiência com python, javascript e SQL. Conhecimento em machine learning."

    # Normalizar palavras-chave no currículo
    print("Mostrar normalizado...")
    print(trata.normalizar_palavras_chave(curriculo))

if __name__ == "__main__":
    main()


