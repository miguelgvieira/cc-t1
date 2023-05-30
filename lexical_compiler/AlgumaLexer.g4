lexer grammar AlgumaLexer;


// O tipo WILDCARD é usado quando temos um operador com o próprio nome.
WILDCARD :	'algoritmo' | 'declare' | ':' | 'literal' | 'inteiro' | 'leia'
	| 'escreva' | ',' | 'fim_algoritmo' | '(' | ')' | '<-' | '+' | '-'
	| '*' | '/' | '..' | 'real' | '%' | '>' | '<' | '<>' | '>=' | '<='
	| '=' | 'se' | 'entao' | 'fim_se' | 'senao' | 'enquanto' | 'faca'
	| 'fim_enquanto' |  '^' | '.' | '[' | ']' | 'registro' | 'fim_registro'
	| 'e' | 'nao' | 'logico' | 'ou' | 'caso' | 'seja' | 'para' | 'ate' 
	| 'fim_para' | 'fim_caso' | '&' | 'tipo' | 'procedimento' | 'var'
	| 'funcao' | 'retorne' | 'fim_funcao' | 'fim_procedimento' | 'constante'
	| 'verdadeiro' | 'falso'
	; 

// Números
// Como visto em aula, primeiro precisamos testar para inteiros, depois para real
INT	: /*('+'|'-')?*/('0'..'9')+
 	;
FLOAT : /*('+'|'-')?*/('0'..'9')+ ('.' ('0'..'9')+)?
 	;

// Identificadores
IDENT : ('a'..'z'|'A'..'Z' | '_') ('_' | 'a'..'z'|'A'..'Z'|'0'..'9')*
	;

// Cadeia de caracteres
CADEIA 	: '"' ( ESC_SEQ | ~('"'|'\\' | '\n') )* '"'
	;

ESC_SEQ	: '\\"';

// Comentários são identificados por chaves
COMENTARIO
    :   ('{' ~('\n'|'\r' | '}')* '\r'?  '}') -> skip
    ;

// Espaços em branco são ignorados.
WS  :   ( ' '
        | '\t'
        | '\r'
        | '\n'
        ) -> skip
    ;

// Detecção de erros.
UNCLOSED_CHAIN : '"' ~('"')* '\r'? '\n'
	;
UNCLOSED_COMMENT
	: '{' ~('}')* '\r'? '\n'
    ;

GENERAL_ERROR : . 
	;