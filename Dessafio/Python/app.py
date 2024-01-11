
import openpyxl
# passos:
#  Entrar na planilha
workbook = openpyxl.load_workbook('lista_de_atendentes.xlsx')
sheet_produtos = workbook['Lista']
# 1 - copiar o nome da coluna 1 linha 1 da tabela
for linha in sheet_produtos.iter_rows(min_row=1):
    print(linha[0].value)
# 2- clicar no campo Login no site
# 3 - colar o que foi copiado da tabela.
# 3 - Clicar em pesquisar
# 4 - esperar 2 segundos
# 5- clicar no vinculos do usuario(desenho)
# 6 - esperar 3 segundos
# 7 - Clicar em "CODIGO ERP" pra colocar os que possui ERP para as primeiras linhas;
# 8 - Clicar DENOVO em "CODIGO ERP" pra colocar os que possui ERP para as primeiras linhas;
# 9 - Cliclar no cleck na coluna Vincular
# 10- clicar no botão Vincular prestadores;
# 11- Esperar 2 segundos;
# 12- clicar no botão "fechar";
# 13- Voltar uma pagina do navegador;
# 14 - Limpa o campo Filtro_Login (login);
# 15 - Cola o intem da coluna 1 linha 2 da tabela de excel.
# e repita os passos.
