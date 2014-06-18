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
# 

import sys
import csv

def pega_arquivo_csv(nome_arquivo):
        """ Abre o arquivo, salva o csv em um dicionario e retorna o dicionario """
	dicionario = {}
        arquivo = open(nome_arquivo, 'rb')
        dicionario = csv.DictReader(arquivo, delimiter=',')
	return dicionario

def gera_sql_insert(dicionario, nome_dimensao):
	""" Recebe um dicionario e gera o SQL de insercao """
	campos = ""
	valores = ""

	header = dicionario.fieldnames
	# Composicao dos campos
	for i in range(len(header)):
		# Veriicando se e a ultima linha
		if i == (len(header)-1):
			campos += header[i]
		else:
			campos += header[i]+", "

	for linha in dicionario:
		linha_valores = ""
		for h in header:
			linha_valores += "\'"+linha[h]+"\', "
		tamanho_linha = len(linha_valores)
		valores += "("+linha_valores[:tamanho_linha-2]+"), "

	tamanho_total = len(valores)
	comando = "INSERT INTO "+nome_dimensao+" ("+campos+") VALUES "+valores[:tamanho_total-2]+";"
	return comando

def resgata_numero_contatos(dicionario, snapshot, nome_residuo, nome_ligante):
	""" Recebe um dicionario dos arquivos sumarizados, snapshot, nome do residuo e nome do ligante. Retorna o numero de contatos encontrados para esta configuracao """
	for linha in dicionario:
		if ((linha['Snapshot'] == snapshot) and (linha['Residuo'] == nome_residuo) and (linha['Ligante'] == nome_ligante)):
			return linha['Total']
	return "0"

if __name__ == "__main__":

	args = sys.argv[1:]

	uso = """
Uso: 
criaDadosFato.py <DIM Ligante> <DIM Grupo> <DIM Modelo Dinamico> <DIM Experimento> <CSV Residuos mais importantes> <Arquivos Sumarizados> <Arquivo CSV Principal>
		"""

	if len(args) != 7:
		print uso 
		sys.exit(0)
	dim_ligante = pega_arquivo_csv(args[0])
	dim_grupo = pega_arquivo_csv(args[1])
	dim_modelo = pega_arquivo_csv(args[2])
	dim_experimento = pega_arquivo_csv(args[3])

	print gera_sql_insert(dim_ligante, "DIM_Ligante")
	print gera_sql_insert(dim_grupo, "DIM_Grupo")
	print gera_sql_insert(dim_modelo, "DIM_Modelo_Dinamico")
	print gera_sql_insert(dim_experimento, "DIM_Experimento")

	dim_residuos = pega_arquivo_csv(args[4])

	# Dicionario de ligantes
	dim_ligante = pega_arquivo_csv(args[0])
	ligantes_dict = {}
	for linha in dim_ligante:
		ligantes_dict[linha['Id']] = linha['Nome']

	residuos_id = []
	residuos_nome = []
	cont = 0
	for linha in dim_residuos:
		residuos_id.append(linha['Id'])
		residuos_nome.append(linha['Nome'])
		print "INSERT INTO DIM_R"+str(cont+1)+" (Id, Nome) VALUES ("+linha['Id']+", \'"+linha['Nome']+"\');"
		cont = cont+1

	arquivos_sumarizados = list(pega_arquivo_csv(args[5]))
	arquivo_principal = pega_arquivo_csv (args[6])

	for linha in arquivo_principal:
		instante = linha['SS']
		idr1 = residuos_id[0]
		idr2 = residuos_id[1]
		idr3 = residuos_id[2]
		idr4 = residuos_id[3]
		idr5 = residuos_id[4]
		idr6 = residuos_id[5]
		idr7 = residuos_id[6]
		idr8 = residuos_id[7]
		idr9 = residuos_id[8]
		idr10 = residuos_id[9]
		id_modelo_dinamico = '1'
		id_grupo = '1'
		id_experimento = '1'
		for ligante in ligantes_dict.iterkeys():
			numero_conexoes_r1 = resgata_numero_contatos(arquivos_sumarizados, instante, residuos_nome[0], ligantes_dict[ligante])
			numero_conexoes_r2 = resgata_numero_contatos(arquivos_sumarizados, instante, residuos_nome[1], ligantes_dict[ligante])
			numero_conexoes_r3 = resgata_numero_contatos(arquivos_sumarizados, instante, residuos_nome[2], ligantes_dict[ligante])
			numero_conexoes_r4 = resgata_numero_contatos(arquivos_sumarizados, instante, residuos_nome[3], ligantes_dict[ligante])
			numero_conexoes_r5 = resgata_numero_contatos(arquivos_sumarizados, instante, residuos_nome[4], ligantes_dict[ligante])
			numero_conexoes_r6 = resgata_numero_contatos(arquivos_sumarizados, instante, residuos_nome[5], ligantes_dict[ligante])
			numero_conexoes_r7 = resgata_numero_contatos(arquivos_sumarizados, instante, residuos_nome[6], ligantes_dict[ligante])
			numero_conexoes_r8 = resgata_numero_contatos(arquivos_sumarizados, instante, residuos_nome[7], ligantes_dict[ligante])
			numero_conexoes_r9 = resgata_numero_contatos(arquivos_sumarizados, instante, residuos_nome[8], ligantes_dict[ligante])
			numero_conexoes_r10 = resgata_numero_contatos(arquivos_sumarizados, instante, residuos_nome[9], ligantes_dict[ligante])
			feb = linha[ligantes_dict[ligante]+"BESTFEB"]
			rmsd = linha[ligantes_dict[ligante]+"BESTRMSD"]
			id_ligante = ligante
			
			comando = "INSERT INTO FATO (FEB, RMSD, NumeroConexoesR1, NumeroConexoesR2, NumeroConexoesR3, NumeroConexoesR4, NumeroConexoesR5, NumeroConexoesR6, NumeroConexoesR7, NumeroConexoesR8, NumeroConexoesR9, NumeroConexoesR10, IdModeloDinamico, Instante, IdLigante, IdR1, IdR2, IdR3, IdR4, IdR5, IdR6, IdR7, IdR8, IdR9, IdR10, IdGrupo, IdExperimento) VALUES ("+feb+", "+rmsd+", "+numero_conexoes_r1+", "+numero_conexoes_r2+", "+numero_conexoes_r3+", "+numero_conexoes_r4+", "+numero_conexoes_r5+", "+numero_conexoes_r6+", "+numero_conexoes_r7+", "+numero_conexoes_r8+", "+numero_conexoes_r9+", "+numero_conexoes_r10+", "+id_modelo_dinamico+", "+instante+", "+id_ligante+", "+idr1+", "+idr2+", "+idr3+", "+idr4+", "+idr5+", "+idr6+", "+idr7+", "+idr8+", "+idr9+", "+idr10+", "+id_grupo+", "+id_experimento+");"
			print comando
