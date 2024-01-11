
import openpyxl
import pyperclip
import pyautogui
from time import sleep
# passos:
#  Entrar na planilha
workbook = openpyxl.load_workbook(
    'C:\Abner\Estudos\HTML-CSS\Dessafio\Python\lista_de_atendentes.xlsx')
sheet_produtos = workbook['Lista']
# 1 - copiar o nome da coluna 1 linha 1 da tabela
for linha in sheet_produtos.iter_rows(min_row=1):
    login_colaborador = (linha[0].value)
    pyperclip.copy(login_colaborador)

# 2- clicar no campo Login no site
    pyautogui.click(701, 477, duration=1)
# 3 - colar o que foi copiado da tabela.
    pyautogui.hotkey('ctrl', 'v')
# 3 - Clicar em pesquisar
    pyautogui.click(1331,624, duration=2)
    sleep(2)
# 5- clicar no vinculos do usuario(desenho)
    pyautogui.click(1293, 734, duration=2)
# 6 - esperar 3 segundos
    sleep(2)
# 7 - Clicar em "CODIGO ERP" pra colocar os que possui ERP para as primeiras linhas;
    pyautogui.click(911, 732, duration=2)
    sleep(2)
# 8 - Clicar DENOVO em "CODIGO ERP" pra colocar os que possui ERP para as primeiras linhas;
    pyautogui.click(936, 732, duration=2)
# 9 - Cliclar no cleck na coluna Vincular
# 10- clicar no botão Vincular prestadores;
# 11- Esperar 2 segundos;
# 12- clicar no botão "fechar";
# 13- Voltar uma pagina do navegador;
# 14 - Limpa o campo Filtro_Login (login);
# 15 - Cola o intem da coluna 1 linha 2 da tabela de excel.
# e repita os passos.
