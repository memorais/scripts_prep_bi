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

import csv
import math
import sys

def pega_arquivo(nome_arquivo):
	""" Abre o arquivo e retorna uma lista com o conteudo """
	lista_arquivo = []
	arquivo = open(nome_arquivo, 'r')
	for linha in arquivo:
		lista_arquivo.append(linha)
	arquivo.close()
	return lista_arquivo

def pega_arquivo_csv(nome_arquivo):
	""" Abre o arquivo, salva o csv em um dicionario e retorna o dicionario """
	arquivo = open(nome_arquivo, 'rb')
	dicionario_residuos = csv.DictReader(arquivo, delimiter=',')
	# arquivo.close()
	return dicionario_residuos

def calcula_distancia(residuox, residuoy, residuoz, ligantex, ligantey, ligantez):
	""" Recebe as coordenadas e calcula a distancia euclidiana entre os pontos. Retorna o valor da distancia em angstrom """
	distancia = (((residuox-ligantex)**2)+((residuoy-ligantey)**2)+((residuoz-ligantez)**2))
	retorno = math.sqrt(distancia)
	return retorno

if __name__ == "__main__":

	args = sys.argv[1:]

	uso = """
uso:
calculaDistancia.py <Lista de residuos> <Lista de ligantes> <Arquivo CSV com as informacoes>
		"""

	if len(args) != 3:
		print uso 
		sys.exit(0)

	residuos = args[0]
	ligantes = args[1]
	arquivo_csv = args[2]

	print "Snapshot,Residuo,Ligante,Distancia,Classificacao"

	lista_residuos = pega_arquivo(residuos)
	lista_ligantes = pega_arquivo(ligantes)
	dicionario_residuos = pega_arquivo_csv(arquivo_csv)

	for snapshot in dicionario_residuos:
		for residuo_chave in lista_residuos:
			for ligante in lista_ligantes:
				# Montando chave dos residuos x,y,z
				tamanho_residuo = len(residuo_chave)-1
				residuox = residuo_chave[0:tamanho_residuo]+'_x'
				residuoy = residuo_chave[0:tamanho_residuo]+'_y'
				residuoz = residuo_chave[0:tamanho_residuo]+'_z'

				# Montando chave dos ligantes
				tamanho_ligante = len(ligante)-1
				ligantex = ligante[0:tamanho_ligante]+'_x'
				ligantey = ligante[0:tamanho_ligante]+'_y'
				ligantez = ligante[0:tamanho_ligante]+'_z'

				# Pegando o valor dos residuos e ligantes para calculo
				valor_residuox = float(snapshot[residuox])
				valor_residuoy = float(snapshot[residuoy])
				valor_residuoz = float(snapshot[residuoz])
				valor_ligantex = float(snapshot[ligantex])
				valor_ligantey = float(snapshot[ligantey])
				valor_ligantez = float(snapshot[ligantez])
				
				# Excluindo H
				divisaox = residuox.split('_')
				divisaoy = residuoy.split('_')
				divisaoz = residuoz.split('_')

				if divisaox[2][0] != 'H' or divisaoy[2][0] != 'H' or divisaoz[2][0] != 'H':
	
					distancia = calcula_distancia(valor_residuox,valor_residuoy,valor_residuoz,valor_ligantex,valor_ligantey,valor_ligantez)

					if distancia < 4:
						residuoformat = residuo_chave.rstrip()
						residuolista = residuoformat.split('_')
						liganteformat = ligante.rstrip()
						ligantelista = liganteformat.split('_')
						if distancia <= 2:
							print snapshot['SS']+','+residuolista[0]+'_'+residuolista[1]+','+ligantelista[0]+','+str(round(distancia,2))+','+'<=2'
						else:
							print snapshot['SS']+','+residuolista[0]+'_'+residuolista[1]+','+ligantelista[0]+','+str(round(distancia,2))+','+'2-4'
					# saida.append({'Snapshot': snapshot['SS'], 'Residuo': residuo_chave.rstrip(), 'Ligante': ligante.rstrip(), 'Distancia': distancia});

	# print saida
