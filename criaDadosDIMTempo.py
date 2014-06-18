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
# Script para criar os dados da tabela DIM_Tempo em picosegundos.

import sys

if __name__ == "__main__":

	args = sys.argv[1:]

	uso = """
uso:
criaDadosDIMTempo.py <Numero de valores para os picosegundos>
O numero nao pode ser menor que 1.
		"""

	if len(args) != 1:
		print uso 
		sys.exit(0)
	
	if args[0] < 1:
		print uso
		sys.exit(0)

	numero = int(args[0])

	comando = "INSERT INTO DIM_Tempo VALUES "
	
	valores = ""

	for i in range(numero):
		valores += "("+str(i+1)+"), "

	tamanho = len(valores)
	print comando+valores[:tamanho-2]+";"
