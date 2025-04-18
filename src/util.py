from CFG import *
import os
import subprocess

import random
import re

def remove_whitespace(code):
    token_pattern = r'"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'|//.*?$|/\*.*?\*/|[_a-zA-Z]\w*|\d+|\S'
    tokens = re.findall(token_pattern, code, flags=re.MULTILINE | re.DOTALL)
    result = []
    for tok in tokens:
        if result and ((result[-1][-1].isalnum() or result[-1][-1] == '_') and (tok[0].isalnum() or tok[0] == '_')):
            result.append(' ')
        result.append(tok)
    return ''.join(result)