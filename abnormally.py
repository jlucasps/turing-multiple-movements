# This Python file uses the following encoding: utf-8#
# ##############################################################################
# Trabalho de Teoria da Computaçao - COM 167
# Simulador de Máquinas de Turing com Múltiplos Movimentos
# Hudson Flávio, João Lucas, Renan Martins
# Arquivo abnormally.py
# -> Este arquivo implementa a classe Abnormally (Exception)s
# ###############################################################################

class Abnormally(Exception):
	"""Classe que representa uma anormalidade na execução da máquina."""
	def __init__(self, value):
		self.value = value
		
	def __str__(self):
		return repr(self.value)
	
