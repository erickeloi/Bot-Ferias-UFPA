from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def credenciais():
    with open('account_info.txt', 'r') as arquivo:
        info = arquivo.read().split()
        email = info[0]
        password = info[1]
    return email, password


email, password = credenciais()

ano_atual = time.gmtime()[0]
mes_atual = time.gmtime()[1]
dia_atual = time.gmtime()[2]
# Data no Padrão Norte-Americano, 3 horas adiantado

tempo_decorrido_em_dias = (mes_atual - 1) * 30 + dia_atual
if ano_atual == 2022:
    tempo_decorrido_em_dias += 365

fim_periodo_2_ufpa_dias = 279

# Periodo 2 UFPA
# dias corridos de 01-01-2021 até 07/10/2021 = 279

# 24/06/2021 a 07/10/2021
# 105 dia(s) = 2° Período Letivo

# 7 dias de férias até o próximo período letivo ( 3° )
# dia 286 ele volta, 14/10/2021

fim_periodo_3_ufpa_dias = 403

# Periodo 3 UFPA
# dias corridos de 01-01-2021 até 08/02/2022 = 403

# 14/10/2021 a 08/02/2022
# 117 dia(s) = 3° Período Letivo

# Passou de 365, pois termina em 2022.

def texto_dos_bacanas():
    periodo = 2

    def texto_padrao_dias(dias_que_faltam, periodo_atual):
        return f"Faltam {dias_que_faltam} dias para as Férias (Término do {periodo_atual}° Período Letivo)"

    def texto_padrao_dia(periodo_atual):
        return f"Falta 1 dia para as Férias ( Término do {periodo_atual}° Período Letivo)"

    def texto_glorioso():
        return "Chegou o Glorioso Dia Meus Bacanos!!!"

    try:
        quantos_dias_faltam = fim_periodo_2_ufpa_dias - tempo_decorrido_em_dias

        if quantos_dias_faltam > 1:
            return texto_padrao_dias(quantos_dias_faltam, periodo)

        elif quantos_dias_faltam == 1:
            return texto_padrao_dia(periodo)

        elif quantos_dias_faltam == 0:
            return texto_glorioso()

        # Ele vai passar 7 dias desativado (Férias).

        if tempo_decorrido_em_dias >= 286:
            quantos_dias_faltam = fim_periodo_3_ufpa_dias - tempo_decorrido_em_dias
            periodo = 3

            if quantos_dias_faltam > 1:
                return texto_padrao_dias(quantos_dias_faltam, periodo)

            elif quantos_dias_faltam == 1:
                return texto_padrao_dia(periodo)

            elif quantos_dias_faltam == 0:
                return texto_glorioso()

    except:
        return "Aconteceu alguma coisa !!!"

# Começo da Automação

# Se você não quiser que o chrome inicie em FullScreen:
# Você pode comentar essas opções abaixo e tirar o argumento 'options=options' do driver
# (Assim como comentar o 'Options' lá em cima na Importação)
# Dessa forma, o chrome iniciara em modo janela


options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)

driver.get("https://twitter.com/login")

# Processo de Login

email_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input'
password_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input'
login_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span'

time.sleep(5)

driver.find_element_by_xpath(email_xpath).send_keys(email)
time.sleep(0.5)

driver.find_element_by_xpath(password_xpath).send_keys(password)
time.sleep(1)

driver.find_element_by_xpath(login_xpath).click()
time.sleep(0.5)

# Processo de Envio da Mensagem

twitter_post_xpath = '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div/span/div/div/span/span'
twitter_post_message = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div'
twitter_send_post_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span'

time.sleep(5)

driver.find_element_by_xpath(twitter_post_xpath).click()
time.sleep(3)

driver.find_element_by_xpath(twitter_post_message).send_keys(texto_dos_bacanas())
time.sleep(2)

driver.find_element_by_xpath(twitter_send_post_xpath).click()
time.sleep(1)
