# This Python file uses the following encoding: utf-8#
# ##############################################################################
# Trabalho de Teoria da Computação - COM 167
# Simulador de Máquinas de Turing com Múltiplos Movimentos
# Hudson Flávio, João Lucas, Renan Martins
# Arquivo main.py
# -> Este arquivo não implementa nenhuma classe. 
#	 É responsável pela execução do programa (interação com o usuario)
# ###############################################################################

from parser import *
from turing import Turing
from abnormally import Abnormally

class MainTuring:
	
	def menu(self):
		######################################################
		#  Opção para configuração da máquina.
		######################################################

		exit = False
		while not(exit):

			optionMachine =  input('Escolha o modo de entrada da máquina.\n1- Via arquivo.\n2- Via teclado\n3- Sair.\n_')
	
			while (optionMachine < 1) | (optionMachine > 3):
				optionMachine =  input('Escolha o modo de entrada da máquina.\n1- Via arquivo.\n2- Via teclado\n3- Sair.\n_')
		
			if optionMachine == 1:
				fileExists = False
				while(not fileExists):
			
					print 'Indique onde está o arquivo de configuração da máquina: '
					machineFilePath = raw_input(':')
	
					try:
						p = ParserMachine(machineFilePath)
				
						print 'Tipo: ', p.typeMachine.replace('\n', '')
						print 'Nome: ', p.nameMachine.replace('\n', '')
						print 'Info: ', p.info.replace('\n', '') 
						print 'Numero de Estados: ', p.nStates
						print 'Inicio da Fita: ', p.startTape.replace('\n', '')
						print 'Branco: ', p.blank.replace('\n', '')
						print 'Estados Finais: ', p.finalStates 
						print 'Alfabeto de Entrada: ', p.alphaInput
						print 'Transições: ', p.trans

						fileExists = True
					except IOError, e:
						print e
		
				self.trans = p.trans
				self.blank = p.blank
				self.finalStates = p.finalStates
				
			elif optionMachine == 2:
				numTrans = raw_input('Entre com o número de transições:\n_')
				trans = []

				pk = ParserKeyboard()

				for i in range(int(numTrans)):
					transAtual = raw_input('Entre com a transição ' + str(i + 1) + ' da seguinte forma:\n[est. anterior, \'simb lido\', est. posterior, \'simb escrito\', \'direcao\', \'deslocamento\']\n_')
					trans.append(pk.getList(transAtual))
		
				self.trans = trans
				self.blank = raw_input('Indicador de espaco em branco:\n_')
		
				finalStates = raw_input('Entre com os estados finais da seguinte forma: [E1, E2, E4, ...]\n_')
		
				self.finalStates = pk.getList(finalStates)
				
			else:
				exit = True


			######################################################
			#  Opção para simulação.
			######################################################
	
			while not(exit):
		
				optionSimulation = input('Escolha o modo de execução:\n1- Simulacao passo-a-passo.\n2- Simulacao direta.\n3- Outra máquina.\n4- Sair.\n_')
	
				while (optionSimulation < 1) | (optionSimulation > 4):
					optionSimulation = input('Escolha o modo de execução:\n1- Simulacao passo-a-passo.\n2- Simulacao direta.\n3- Outra máquina.\n4- Sair.\n_')
	
				if optionSimulation == 3:
					break
				elif optionSimulation == 4:
					exit = True
	
				######################################################
				#  Opção para leitura da fita.
				######################################################
				while not(exit):
		
					optionTape = input('Escolha o modo de entrada da fita:\n1- Entrar com a fita via teclado.\n2- Entrar com a fita via arquivo.\n3- Outro modo de execução.\n4- Sair.\n_')
		
					while (optionTape < 1) | (optionTape > 4):
						optionTape = input('Escolha o modo de entrada da fita:\n1- Entrar com a fita via teclado.\n2- Entrar com a fita via arquivo.\n3- Outro modo de execução.\n4- Sair.\n_')
					
					if optionTape == 1:
						tape = []
						userInput = raw_input(':')

						for x in userInput:
							tape.append(x)
						
						self.tape = tape
					
					elif optionTape == 2:
		
						fileExists = False
						while(not fileExists):
							userInput = raw_input('Indique onde está o arquivo de configuração da fita: ')
			
							try:
								pTape = ParserTape(userInput)
								self.tape = pTape.read()
								fileExists = True
							except IOError, e:
								print e
						
					elif (optionTape == 3) | (optionTape == 4):
						if optionTape == 4:
							exit = True
						break
			
					######################################################
					#  Execução da máquina.
					######################################################
			
					t = Turing(self.tape, self.trans, self.blank, self.finalStates)
					if optionSimulation == 1:
						next = True
						t.printStep()

						while next:
							#Executa uma transição:
							try:
								if t.executeTrans():
									#Se transição foi feita, então mostra resultado.
									t.printStep()
	
									#Verifica com usuário se quer continuar.
									cont = raw_input('\nContinuar? (<e> para terminar; <enter> para continuar): ')
	
									#Se a entrada for e, termina simulação passo-a-passo.
									if cont == 'e':
										next = False
								else:
									#Se transição não puder ser feita, então termina (máquina parou).
									next = False
							except Abnormally, e:
								print e
								next = False

						print '\nMaquina parou. ',
						if t.isFinalState():
							print 'Palavra foi aceita.'
						else:
							print 'Palavra não foi aceita.'

					elif optionSimulation == 2:
						t.printStep()
		
						try:
							while t.executeTrans():
								t.printStep()
	
							print '\nMaquina parou. ',
							if t.isFinalState():
								print 'Palavra foi aceita.'
							else:
								print 'Palavra não foi aceita.\n'
				
						except Abnormally, e:
							print e


desc = """Este programa simula a execução de uma máquina de Turing com múltiplos movimentos.
Escolha um modo de entrada da configuração da máquina. A seguir, escolha o modo de execução
e, antes de acompanhar a execução da máquina, escolha o modo de entrada da fita.\n"""

print desc

main = MainTuring()
main.menu()


