'''Matching Characters . ^ $ * + ? {} [] \ | ! ()
| -> pipe <-: significa 'OU'
. -> dot <-: significa qualquer caractere(ele so nao reconhece quebra de linha)
[] -> brackets <-: significa conjunto, por exemplo um conjunto de caracteres
a-zA-z0-9 -> range de a ate z(em minusculas) e range de A ate Z (em maiusculas) e numeros de 0 a 9
flags sao algo que muda o comportamento de como a regex funciona, exemplo:
    flags=re.I ou re.IGNORECASE(same thing), ela vai ignorar o case sensitive
'''
import re
text = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''
print(re.findall(r'João|Maria|ad....s', text))
print(re.findall(r'João|joão|Maria|ad....s', text))
print(re.findall(r'[Jj]oão|[Mm]aria|[Aa]d....s', text))
print(re.findall(r'[a-zA-Z0-9]aria', text))
print(re.findall(r'[a-zA-Z0-9]aria|[a-zA-Z0-9]oão', text))
print(re.findall(r'jOãO|mAriA', text, flags=re.I))
