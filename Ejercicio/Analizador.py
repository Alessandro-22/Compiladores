import ply.lex as lex

tokens = (
    'IDENTIFIER',
    'NUMBER',
    'LITERAL',
    'ID',
    'TEXT',
    'OPER_SUM',
    'OPER_SUB',
    'OPER_MUL',
    'OPER_DIV',
    'LEFT_P',
    'RIGHT_P',
    'LEFT_A',
    'RIGHT_A',
    'KEY_LEFT',
    'KEY_RIGHT',
    'EQUAL',
    'EQUAL_DIF',
    'MENOR',
    'MAYOR',
    'WHILE',
    'FOR',
    'IF',
    'INT',
    'DOUBLE',
    'ELSE',
    'DO',
    'COMMENT',
    'BOOL_TYPE',
    'BOOL',
    'FUNCTION',
    'SHOW',
    'RETURN',
    'STRING',
    '2PUNTOS',  
)

# Define reserved words
reserved = {
    'loop': 'WHILE',
    'four': 'FOR',
    'ifi': 'IF',
    'int': 'INT',
    'doplet': 'DOUBLE',
    'else': 'ELSE',
    'do': 'DO',
    'chaycama': 'FUNCTION',
    'invoca': 'SHOW',
    'devolver': 'RETURN',
    'bu': 'BOOL',
    'true': 'BOOL_TYPE',
    'false': 'BOOL_TYPE',
}

# Regular expression 
t_OPER_SUM = r'\+'
t_OPER_SUB = r'-'
t_OPER_MUL = r'\*'
t_OPER_DIV = r'/'
t_LEFT_P = r'\('
t_RIGHT_P = r'\)'
t_LEFT_A = r'\['
t_RIGHT_A = r'\]'
t_KEY_LEFT = r'\{'
t_KEY_RIGHT = r'\}'
t_EQUAL = r'='
t_EQUAL_DIF = r'!='
t_MENOR = r'<'
t_MAYOR = r'>'
t_COMMENT = r'//.*'
t_2PUNTOS = r':'

# Expresion regular para los numeros
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    if '.' in t.value:
        t.value = float(t.value)
        t.type = 'DOUBLE'
    else:
        t.value = int(t.value)
        t.type = 'INT'
    return t

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    if t.value in reserved:
        if reserved[t.value] == 'BOOL_TYPE':
            t.type = 'BOOL_TYPE'
        else:
            t.type = reserved[t.value]
    else:
        t.type = 'IDENTIFIER'
    return t
 # expresion para los textos dentro de comillas
def t_TEXT(t):
    r'\'[^\']*\'|\"[^\"]*\"'
    t.type = 'TEXT'
    return t
#expresion para el tippo de boolean
def t_BOOL_TYPE(t):
    r'true|false'
    t.type = 'BOOL_TYPE'
    return t

def t_STRING(t):
    r'cad'
    t.type = 'STRING'
    return t

# rastrea los numeros de linea en el codigo
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

t_ignore = ' \t'

#lexer
lexer = lex.lex()

# lee el archivo
def read_input(filename):
    with open(filename, 'r') as file:
        return file.read()

# Test 
def test_lexer(input_data):
    lexer.input(input_data)
    token_list = []
    while True:
        tok = lexer.token()
        if not tok:
            break  
        token_list.append({'type': tok.type, 'value': tok.value, 'line': tok.lineno, 'position': tok.lexpos})
    return token_list

# Main function
if __name__ == '__main__':
    filename = 'Test.txt'  
    input_data = read_input(filename)
    token_list = test_lexer(input_data)
    # Imprime los tokens 
    for token in token_list:
        print(f"{token['type']} {token['value']} {token['line']} {token['position']}")
