def general_error(t):
    return f"Linha {t.line}: {t.text} - simbolo nao identificado\n"

def unclosed_chain(t):
    return f"Linha {t.line}: cadeia literal nao fechada\n"

def unclosed_comment(t):
    return f"Linha {t.line}: comentario nao fechado\n"

ERROR_HANDLING = {
    'GENERAL_ERROR': general_error,
    'UNCLOSED_CHAIN': unclosed_chain,
    'UNCLOSED_COMMENT': unclosed_comment,
}