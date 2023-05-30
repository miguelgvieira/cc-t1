from antlr4 import *
from lexer.AlgumaLexer import AlgumaLexer
from error_handling import ERROR_HANDLING

"""
    Classe responsável por analisar o arquivo de entrada e gerar o arquivo de saída
    com os tokens encontrados.

    O método error_handling é chamado quando um erro léxico é encontrado. Ele recebe
    o token que causou o erro e escreve no arquivo de saída a mensagem de erro
    correspondente.

    O método analyse_file recebe o arquivo de entrada e o arquivo de saída e chama
    o analisador léxico para cada token do arquivo de entrada. Quando o token EOF
    é encontrado, o loop é encerrado.

    Exemplo de uso:
    ```
    lexer = AlgumaLexerAnalyzer()
    lexer.analyse_file("input_file.txt", "output_file.txt")
    ```

    O analisador léxico tem sua lógica implementado em dist/AlgumaLexer.py, criada pelo
    ANTLR, utilizando a gramática definida em AlgumaLexer.g4.

    O arquivo AlgumaLexer.py é gerado automaticamente pelo ANTLR, não deve ser alterado.
    
"""
class AlgumaLexerAnalyzer():

    # Método chamado quando um erro léxico é encontrado
    def error_handling(self, t):
        self.output_stream.write(ERROR_HANDLING[AlgumaLexer.symbolicNames[t.type]](t))

    def analyse_file(self, input_file, output_file):
        self.input_stream = FileStream(input_file, encoding='utf-8')
        self.output_stream = open(output_file, 'w')
        lexer = AlgumaLexer(self.input_stream)

        while True:
            t = lexer.nextToken()
            if t.type == Token.EOF:
                break

            # Estamos analizando se o token é um erro léxico contido em ERROR_HANDLING.keys()
            # Se for, chamamos o método error_handling
            # A variável ERROR_HANDLING é um dicionário que contém as mensagens de erro
            # correspondentes a cada erro léxico
            elif AlgumaLexer.symbolicNames[t.type] in ERROR_HANDLING.keys():
                self.error_handling(t)
                break

            # Se não for um erro léxico, escrevemos no arquivo de saída o token encontrado
            # O token é representado por uma tupla (texto, tipo)
            # No caso do token ser um identificador, o tipo é o próprio texto
            elif AlgumaLexer.symbolicNames[t.type] == "WILDCARD":
                self.output_stream.write(f"<'{t.text}','{t.text}'>\n")
            else:
                self.output_stream.write(f"<'{t.text}',{AlgumaLexer.symbolicNames[t.type]}>\n")

        self.output_stream.close()