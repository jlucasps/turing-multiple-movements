# This Python file uses the following encoding: utf-8#
# ##############################################################################
# Trabalho de Teoria da Computação - COM 167
# Simulador de Máquinas de Turing com Múltiplos Movimentos
# Copyright 2009 - Hudson Flávio, João Lucas, Renan Martins
# Arquivo controller.py
# -> Esse arquivo implementa a classe Controller.
# ###############################################################################

from abnormally import Abnormally

class Turing:
	""" Classe responsável por receber a representação de uma máquina e fita
		e executa-la. Possui métodos que permitem a execução direta ou passo-a-passo.
	"""
	def __init__(self, tape, trans, blank, finalStates):
		"""Construtor da classe"""
		self.tape = tape
		self.trans = trans
		self.blank = blank
		self.finalStates = finalStates
		self.currentState = self.trans[0][0]
		self.currentPos = 0

	def executeTrans(self):
		"""Executa uma transição na máquina. Retorna True se a transição puder ser realizada,
		   senão retorna False."""

		#Lê um símbolo da fita.
		try:
			symbol = self.tape[self.currentPos]
		except IndexError, e:
			raise Abnormally("Fita vazia!!");
			
		count = 0
		notMove = True

		#Enquanto não mover e não analisar todas as transições possíveis,
		while (count < len(self.trans)) & notMove:
			t = self.trans[count]
			
			#verifica se o estado da transição que está sendo analisada é o estado em
			#que a máquina está; além disso, verifica se o símbolo lido está na transição.
			if (t[0] == str(self.currentState)) & (t[1] == symbol):
				#se sim, então escreve na fita o novo símbolo,
				self.tape[self.currentPos] = t[3]

				#muda o estado
				self.currentState = t[2]

				#e efetua deslocamento, verificando deslocamento à esquerda (se é possível).
				if t[4] == 'R':
					self.currentPos += int(t[5])
				else:
					self.currentPos -= int(t[5])
					if(self.currentPos < 0):
						raise Abnormally("Erro: Posição corrente da fita negativa.")
				#Insere brancos no final da fita, caso seja necessário.
				self.insertBlanks()
				notMove = False

			#Próxima transição a ser analisada.
			count += 1

		return not(notMove)

	def insertBlanks(self):
		"""Insere brancos no final da fita se a posição corrente ultrapassa
		   o tamanho atual da fita. Insere brancos até completar, e um a mais."""
		
		#Se posição corrente na fita for maior que o tamanho atual da mesma,
		if (self.currentPos + 1) > len(self.tape):
			#então deve-se acrescentar behind brancos no final da fita.
			behind = (self.currentPos + 1) - len(self.tape) + 1
			count = 0

			while count < behind:
				self.tape.append(self.blank)
				count += 1

	def printStep(self):
		"""Exibe a fita no i-esimo passo da simulacao."""

		print '\nConfiguracao da fita: ',

		count = 0
		while count < len(self.tape):
			if count == self.currentPos:
				print '_',

			print self.tape[count],
			count += 1

		print '\nEstado atual: ', self.currentState

	def isFinalState(self):
		"""Verifica se o estado corrente é um dos estados do conjunto de estados finais.
		   Retorna True se for, senão retorna False."""

		for state in self.finalStates:
			if state == self.currentState:
				return True

		return False
