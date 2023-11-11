import re
# regex possui case sensitive
# findall -> encontra todas as ocorrencias, retorna uma lista de ocorrencia
# search -> encontra a primeira ocorrencia, retorna o obj match
# sub -> substitui ocorrencia especificada, retorna a frase com a palavra substituida
# compile -> voce reutiliza a expressao, utilizando apenas as funcoes da lib, sem recompilar toda vez

regexp = re.compile(r'teste')
string = 'Este e um teste de expressoes teste regulares.'

# print(re.search(r'teste', string))
# print(re.findall(r'teste', string))
# print(re.sub(r'teste', 'ABCD', string, count=1)) # count=1 informa apenas a 1a word para substituir

# Igual as anteriores, mas ele nao recompila a expressao
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('ABCD', string, count=1))

