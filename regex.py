import re

texto = """Ao buscarem uma melhor compreensão e interpretação automatizada
de textos, as técnicas de processamento de linguagem natural (PLN) se
deparam com o desafio de compreender variações em palavras com
sentidos próximos, como no caso da língua portuguesa e de suas diversas
formas de flexão verbal e nominal. Nesse contexto, as expressões
regulares se apresentam como uma solução robusta e elegante para
detectar padrões variados em textos.

Neste capítulo, você identificará a importância das expressões regulares
como recurso para o PLN, conhecerá os tipos de metacaracteres e
implementará suas primeiros expressões regulares usando a linguagem
de programação Python"""

# Metacaracteres representantes.
padrão_busca1 = r"[^a-z]caract[a-z]{1,4}"
padrão_busca2 = r".{1,2}tacaract[a-z]{1,4}"

resultado1 = re.search(padrão_busca1, texto)
print("Resultado para padrão_busca1:", resultado1.group() if resultado1 else "Nenhum resultado encontrado")

resultado2 = re.search(padrão_busca2, texto)
print("Resultado para padrão_busca2:", resultado2.group() if resultado2 else "Nenhum resultado encontrado")

# Metacaracteres quantificadores
padrão_busca3 = r"co.*"
resultado3 = re.search(padrão_busca3, texto)
print("Resultado para padrão_busca3:", resultado3.group() if resultado3 else "Nenhum resultado encontrado")

padrão_busca4 = r"compreensã[a-z]?"
resultado4 = re.search(padrão_busca4, texto)
print("Resultado para padrão_busca4:", resultado4.group() if resultado4 else "Nenhum resultado encontrado")

padrão_busca5 = r"expressõ[a-z]+"
resultado5 = re.search(padrão_busca5, texto)
print("Resultado para padrão_busca5:", resultado5.group() if resultado5 else "Nenhum resultado encontrado")

# Metacaracteres Âncoras
padrão_busca6 = r'^[Aa].*'
resultado6 = re.search(padrão_busca6, texto)
print("Resultado para padrão_busca6:", resultado6.group() if resultado6 else "Nenhum resultado encontrado")

padrão_busca7 = r'[Pp][a-z]*$'
resultado7 = re.search(padrão_busca7, texto)
print("Resultado para padrão_busca7:", resultado7.group() if resultado7 else "Nenhum resultado encontrado")

# Outros

padrão_busca8 = r'expressões|regulares'
resultado8 = re.search(padrão_busca8, texto)
print("Resultado para padrão_busca8:", resultado8.group() if resultado8 else "Nenhum resultado encontrado")

padrão_busca9 = r'(expressões|regulares)'
resultado9 = re.findall(padrão_busca9, texto)
print("Resultado para padrão_busca8:", resultado9 if resultado9 else "Nenhum resultado encontrado")

texto2 = "Carros voando."

padrão_busca10 = r'[Vv].*\.$'
resultado10 = re.search(padrão_busca10, texto2)
print("Resultado para padrão_busca10: ", resultado10.group() if resultado10 else "Nenhum resultado encontrado")