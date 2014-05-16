#!/usr/bin/env python
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import sys
import csv

def parse_arg1(argumento):
	""" Recebe uma string com as colunas, separa os itens por , e retorna uma lista com as colunas """
	colunas = argumento.split(',')
	return colunas

if __name__ == "__main__":

	args = sys.argv[1:]
	uso = """ Uso: ajustaColunasDockingETH_TCL.py [-m]|[-e] <Nome das colunas separados por virgula> <Nome do Arquivo CSV de entrada> <Nome do Arquivo CSV de saida> 
 -[m]anter - Mantem apenas as colunas listadas no parametro subsequente 
 -[e]xcluir - Exclui apenas as colunas listadas no parametro subsequente"""

	if len(args) != 4:
		print uso
		sys.exit(0)

	if args[0] == '-m':
		modo = 1 # Mantem
	elif args[0] == '-e':
		modo = 2 # Exclui
	else:
		print uso
		sys.exit(0)

	colunas = parse_arg1(args[1])

	with open(args[2],"rb") as entrada:
		leitor = csv.DictReader(entrada, delimiter=',')
		saida = args[3] 
		with open(saida,"wb") as retorno:
			if modo == 1:
				escritor = csv.DictWriter(retorno, colunas, delimiter=',')
				# Escrevendo cabecalho
				escritor.writerow(dict((fn,fn) for fn in colunas))
				dicionario_escritor = []
				for l in leitor:
					linha_temp = dict()
					for i in colunas:
						linha_temp[i] = l[i]
					dicionario_escritor.append(linha_temp)
				for linha in dicionario_escritor:
					escritor.writerow(linha)
			elif modo == 2:
				# Removendo colunas do cabecalho
				campos = list(leitor.fieldnames)
				for i in colunas:
					campos.remove(i)
				escritor = csv.DictWriter(retorno, campos, delimiter=',')
				# Escrevendo cabecalho
				escritor.writeheader()
				for l in leitor:
					for i in colunas:
						del l[i]
					escritor.writerow(l)

