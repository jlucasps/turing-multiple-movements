# This Python file uses the following encoding: utf-8#
# ##############################################################################
# Trabalho de Teoria da Computação - COM 167
# Simulador de Máquinas de Turing com Múltiplos Movimentos
# Hudson Flávio, João Lucas, Renan Martins
# Arquivo parser.py
# -> Este arquivo implementa tres classes: ParserMachine, ParserTape e ParserKeyboard
# ###############################################################################

class ParserMachine:
	"""Classe que representa um parser do arquivo que representa uma máquina.
	   É responsável por receber o caminho de um arquivo, gerar a popular as estruturas
	   de dados que representam os componentes da maquina.
	"""

	def __init__(self, fileName):
		"""Construtor para ler arquivo de configuração"""
		#Tipo de maquina abstrata (MT, MTMH, MPilhas, MPost, etc.)
		self.typeMachine = ''

		#Nome da maquina (breve descricao)
		self.nameMachine = ''

		#Informacoes para o usuario (\n seguinifica quebra de linha)
		self.info = ''

		#Quantidade de estados
		self.nStates = 0

		#Indicador de inicio da fita (em branco indica que nao ha indicacao)
		self.startTape = ''

		# Indicador de espaco em branco
		self.blank = '%'

		#Estados finais (Array de estados finais. Lembrando que o primeiro estado sempre sera q0)
		self.finalStates = []

		#Alfabeto de entrada
		self.alphaInput = []

		#Transicoes(ORDEM: estado anterior, simbolo lido, estado posterior, simbolo escrito, movimento na fita)
		self.trans = []

		#Arquivo de configuração fileName.
		self.fileName = fileName
		self.parser()

	def parser(self):
		"""Função para analisar o arquivo de entrada. É a espinha dorsal da análise
		   do arquivo."""
		self.fileName = open(self.fileName, 'r+')
		#Leitura do arquivo, armazenando cada linha como um elemento de uma lista.
		conf = self.fileName.readlines()
		self.fileName.close()
		count = 0

		#Para cada linha do arquivo (que é um elemento da lista),
		for line in conf:
			
			#Se o primeiro caractere for diferente de '#', então não é comentário.
			if line[0] != '#':

				#Se houver substring tipo,
				if 'tipo' in line:

					#Divide string em duas, usando como limitador o '=' e pega a
					#segunda substring.
					self.typeMachine = line.split('=')[1]

				#Se houver substring 'nome', equivalente acima.
				elif 'nome' in line:
					self.nameMachine = line.split('=')[1]

				#Se houver substring 'informacoes', equivalente acima.
				elif 'informacoes' in line:
					self.info = line.split('=')[1]

				#Se houver substring 'qtes_estados', equivalente acima, convertendo
				#o resultado para inteiro.
				elif 'qtes_estados' in line:
					self.nStates = int(line.split('=')[1])

				elif 'branco' in line:
					self.blank = (line.split('=')[1]).replace(' ','').replace('\'','').replace('\n','')

				elif 'estados_finais' in line:
					s = line.split('=')[1]
					s = s.replace('[','').replace(']','')
					s = s.split(',')

					for x in s:
						self.finalStates.append(x.replace(' ','').replace('\n',''))

				elif 'alfabeto_entrada' in line:
					s = line.split('=')[1]
					s = s.replace('[','').replace(']','').replace(' ','')
					s = s.replace('\'','').replace('\n','')
					s = s.split(',')

					for x in s:
						self.alphaInput.append(x)

				elif 'transicoes' in line:
					t = conf[count:len(conf)]
					t = self.cleanTransitions(t)
					self.trans = t		

			count += 1

	def cleanTransitions(self,string):
		"""Remove caracteres desnecessários de cada transição da lista de transições."""
		#Remove primeira e últimas linhas do conjunto de transições.
		del string[0]
		string.pop()
	
		lista = []
		#Adiciona à lista apenas as listas contendo os elementos da transição
		for i in range(len(string)):
			lista.append(self.trim(string[i]))
	
		return lista
	
	def trim(self,string):
		"""Remove caracteres desnecessários de uma transição."""
		string = string.replace('[','')
		string = string.replace(']','')
		string = string.replace('\n','')
		string = string.replace('\'','')
		lista = []

		for x in string.split(','):
			lista.append(x)
	
		lista.pop()
	
		return lista

class ParserTape:
	""" Classe que representa um parser de uma Fita.
		É responsável por receber o caminho de um arquivo(com a fita), criar, popular e retornar 
		a estrutura de dados que representa uma fita no sistema.
	"""
	def __init__(self, fileName):
		self.tape = []
		self.fileName = fileName
		
	def read(self):
		self.f = open(self.fileName, 'r+')
		line = self.f.readline().replace('\n','')

		for l in line:
			self.tape.append(l)
			
		self.f.close()
		return self.tape
	
class ParserKeyboard:
	"""Classe que representa um parser dos dados recebidos via teclado.
	   É responsável por receber uma String, tratá-la (dividir em várias strings), criar e popular uma lista com as strings tratadas.
	"""
	def getList(self, string):
		string = string.replace('[','')
		string = string.replace(']','')
		string = string.replace('\n','')
		string = string.replace('\'','')
		
		lista = []
		
		for x in string.split(','):
			lista.append(x)
			
		return lista
		
