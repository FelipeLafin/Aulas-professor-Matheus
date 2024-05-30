import zipfile

NOME_ARQUIVO = "senha_bitcoin.zip"
zip_file = zipfile.ZipFile(NOME_ARQUIVO, 'r')


def extrair_arquivo_zip_com_senha(senha):
	try:
		zip_file.extractall(path='.', pwd=senha.encode('utf-8'))
		return True
	except:
		pass
	return False
tentativas = 0
lista = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz" #Números e letras que serão testados

#Possibilidades de 3 dígitos e não precisa verificar pois só tem 3 dígitos
for a in lista: #Primeira coluna
	for b in lista: #Segunda coluna
		for c in lista: #Terceira coluna
			#O programa "pulará" todas as sequencias numericas e inversas de 3 caracteres.
			sequencia_3 = ((a == "0") and (b == "1") and (c == "2")) or ((a == "1") and (b == "2") and (c == "3")) or ((a == "2") and (b == "3") and (c == "4")) or ((a == "3") and (b == "4") and (c == "5")) or ((a == "4") and (b == "5") and (c == "6")) or ((a == "5") and (b == "6") and (c == "7")) or ((a == "6") and (b == "7") and (c == "8")) or ((a == "7") and (b == "8") and (c == "9"))
			inversa_3 = ((a == "2") and (b == "1") and (c == "0")) or ((a == "3") and (b == "2") and (c == "1")) or ((a == "4") and (b == "3") and (c == "2")) or ((a == "5") and (b == "4") and (c == "3")) or ((a == "6") and (b == "5") and (c == "4")) or ((a == "7") and (b == "6") and (c == "5")) or ((a == "8") and (b == "7") and (c == "6")) or ((a == "9") and (b == "8") and (c == "7"))
			if ((sequencia_3) or (inversa_3)):
				continue
			if (a == b == c): #Caso os valores de a,b e c sejam iguais o programa "pulará" o valor.
				continue
			else:
				tentativas += 1
				print(str(a)+str(b)+str(c))
				senha = str(a)+str(b)+str(c)
				extraido = extrair_arquivo_zip_com_senha(senha) #Se a senha for correta, o programa extrai o arquivo.
				if extraido:
					print(" ")
					print("A senha era", senha,"e foram necessárias: ", tentativas, "tentativas.")
					exit()

#A partir daqui são as possibilidades de 4 dígitos				
for x in lista: #Primeira coluna
	for y in lista: #Segunda coluna
		for z in lista: #Terceira coluna
			for w in lista: #Quarta coluna
				# Linha de código para pular todas as sequencias numericas e inversas de 4 caracteres.
				sequencia_4 = ((x == "0") and (y == "1") and (z == "2") and (w == "3")) or ((x == "1") and (y == "2") and (z == "3") and (w == "4")) or ((x == "2") and (y == "3") and (z == "4") and (w == "5")) or ((x == "3") and (y == "4") and (z == "5") and (w == "6")) or ((x == "4") and (y == "5") and (z == "6") and (w == "7")) or ((x == "5") and (y == "6") and (z == "7") and (w == "8")) or ((x == "6") and (y == "7") and (z == "8") and (w == "9"))
				inversa_4 = ((x == "3") and (y == "2") and (z == "1") and (w == "0")) or ((x == "4") and (y == "3") and (z == "2") and (w == "1")) or ((x == "5") and (y == "4") and (z == "3") and (w == "2")) or ((x == "6") and (y == "5") and (z == "4") and (w == "3")) or ((x == "7") and (y == "6") and (z == "5") and (w == "4")) or ((x == "8") and (y == "7") and (z == "6") and (w == "5")) or ((x == "9") and (y == "8") and (z == "7") and (w == "6"))
				if ((sequencia_4) or (inversa_4)):
					continue
				if ((x == y == z) or (x == y == w) or (y == z == w) or (x == z == w) or (x == y == z == w)):
					continue
				else:
					maiusculo = x.isupper() or y.isupper() or z.isupper() or w.isupper() #Verifica se tem letras maiúsculas
					minusculo = x.islower() or y.islower() or z.islower() or w.islower() #Verifica se tem letras minúsculas
					numero = x.isalpha() or y.isalpha() or z.isalpha() or w.isalpha() #Verifica se tem números
					print(str(x)+str(y)+str(z)+str(w)) #Escreve a senha no terminal
					valido = maiusculo and minusculo and numero
					senha = str(x)+str(y)+str(z)+str(w) #Senha correta
					if valido:
						tentativas += 1 #Adiciona 1 na tentativa para cada possibilidade de senha
						extraido = extrair_arquivo_zip_com_senha(senha) #Extrai o arquivo
						if extraido: #Mensagem que será exibida quando o arquivo for extraído.
							print(" ")
							print("------------------------------------------------------------------------------")
							print("ARQUIVO EXTRAÍDO verifique o local de salvamento do arquivo descriptografado")
							print("SENHA: ", senha,)
							print("TENTATIVAS: ", tentativas)
							print("------------------------------------------------------------------------------")
							exit()
