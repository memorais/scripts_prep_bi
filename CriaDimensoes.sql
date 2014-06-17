-- Criação das dimensoes para os residuos
create table DIM_R1 (
Nome char(30) not null,
Id numeric(10) not null,
constraint ID_DIM_R1 primary key (Id));

create table DIM_R2 (
Nome char(30) not null,
Id numeric(10) not null,
constraint ID_DIM_R2 primary key (Id));

create table DIM_R3 (
Nome char(30) not null,
Id numeric(10) not null,
constraint ID_DIM_R3 primary key (Id));

create table DIM_R4 (
Nome char(30) not null,
Id numeric(10) not null,
constraint ID_DIM_R4 primary key (Id));

create table DIM_R5 (
Nome char(30) not null,
Id numeric(10) not null,
constraint ID_DIM_R5 primary key (Id));

create table DIM_R6 (
Nome char(30) not null,
Id numeric(10) not null,
constraint ID_DIM_R6 primary key (Id));

create table DIM_R7 (
Nome char(30) not null,
Id numeric(10) not null,
constraint ID_DIM_R7 primary key (Id));

create table DIM_R8 (
Nome char(30) not null,
Id numeric(10) not null,
constraint ID_DIM_R8 primary key (Id));

create table DIM_R9 (
Nome char(30) not null,
Id numeric(10) not null,
constraint ID_DIM_R9 primary key (Id));

create table DIM_R10 (
Nome char(30) not null,
Id numeric(10) not null,
constraint ID_DIM_R10 primary key (Id));

create table DIM_Ligante (
Descricao char(30),
Id numeric(10) not null,
constraint ID_DIM_Ligante primary key (Id));

create table DIM_Grupo (
Descricao char(30) not null,
IdAgrupamento numeric(10) not null,
Id numeric(10) not null,
constraint ID_DIM_Grupo primary key (Id));

create table DIM_Tempo (
Instante numeric(10) not null,
constraint ID_DIM_Tempo primary key (Instante));

create table DIM_Modelo_Dinamico (
Id numeric(10) not null,
Descricao char(60) not null,
constraint ID_DIM_Modelo_Dinamico primary key (Id));

create table DIM_Experimento (
Id numeric(10) not null,
Descricao char(60) not null,
DataHora date not null,
constraint ID_DIM_Experimento primary key (Id));

-- Tabela FATO

create table FATO (
FEB numeric(6,2) not null,
RMSD numeric(6,2) not null,
NumeroConexoesR1 numeric(8) not null,
NumeroConexoesR2 numeric(8) not null,
NumeroConexoesR3 numeric(8) not null,
NumeroConexoesR4 numeric(8) not null,
NumeroConexoesR5 numeric(8) not null,
NumeroConexoesR6 numeric(8) not null,
NumeroConexoesR7 numeric(8) not null,
NumeroConexoesR8 numeric(8) not null,
NumeroConexoesR9 numeric(8) not null,
NumeroConexoesR10 numeric(8) not null,
IdModeloDinamico numeric(10) not null,
Instante numeric(10) not null,
IdLigante numeric(10) not null,
IdR1 numeric(10) not null,
IdR2 numeric(10) not null,
IdR3 numeric(10) not null,
IdR4 numeric(10) not null,
IdR5 numeric(10) not null,
IdR6 numeric(10) not null,
IdR7 numeric(10) not null,
IdR8 numeric(10) not null,
IdR9 numeric(10) not null,
IdR10 numeric(10) not null,
IdGrupo numeric(10) not null,
IdExperimento numeric(10) not null,
constraint FK_Modelo_Dinamico foreign key (IdModeloDinamico) references DIM_Modelo_Dinamico,
constraint FK_Instante foreign key (Instante) references DIM_Tempo,
constraint FK_Ligante foreign key (IdLigante) references DIM_Ligante,
constraint FK_IdR1 foreign key (IdR1) references DIM_R1,
constraint FK_IdR2 foreign key (IdR2) references DIM_R2,
constraint FK_IdR3 foreign key (IdR3) references DIM_R3,
constraint FK_IdR4 foreign key (IdR4) references DIM_R4,
constraint FK_IdR5 foreign key (IdR5) references DIM_R5,
constraint FK_IdR6 foreign key (IdR6) references DIM_R6,
constraint FK_IdR7 foreign key (IdR7) references DIM_R7,
constraint FK_IdR8 foreign key (IdR8) references DIM_R8,
constraint FK_IdR9 foreign key (IdR9) references DIM_R9,
constraint FK_IdR10 foreign key (IdR10) references DIM_R10,
constraint FK_Grupo foreign key (IdGrupo) references DIM_Grupo,
constraint FK_Experimento foreign key (IdExperimento) references DIM_Experimento);