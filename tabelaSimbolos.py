hashTable = {
    "operadores_logicos": ["<", ">", "==", "!=", "<=", ">=", "and", "or"],
    "operadores_aritmeticos": ["+", "-", "*", "/"],
    "operadores_atribuicao": ["="],
    "operadores_especiais": ["(", ")", ":", ";", ",", "{", "}", "[", "]"],
}

todos_operadores = (hashTable["operadores_logicos"] + hashTable["operadores_aritmeticos"] +
                    hashTable["operadores_especiais"])
