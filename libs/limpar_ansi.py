import re

ANSI_RE = re.compile(r'\x1b\[[0-9;]*m')

def limpar_ansi(texto: str) -> str:
    return ANSI_RE.sub('', texto)