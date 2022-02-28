from datetime import date

data_atual = date.today()
ano_atual = data_atual.year
mes_atual = data_atual.month
dia_atual = data_atual.day

# Lógica das Datas:

# Periodos Letivos - INTENSIVOS
# 2022.1
# yyyy-mm-dd
# 2022-01-03 ( inicio do 2022.1 - INTENSIVO )
# 2022-02-28 ( fim do 2022.1 - INTENSIVO )

fim_pl20221 = date(2022, 2, 28)

dias_faltando_fim_pl20221_aux = fim_pl20221 - data_atual

dias_faltando_fim_pl20221 = dias_faltando_fim_pl20221_aux.days

# Dias corridos = 56 dias
# Dias letivos = 49 dias ( Sábado também conta )

# 2022.3
# 2022-07-01 ( inicio do 2022.3 - INTENSIVO )
# 2022-08-31 ( fim do 2022.3 - INTENSIVO )

# 61 dias corridos
# 43 dias letivos

fim_pl20223 = date(2022, 8, 31)

dias_faltando_fim_pl20223_aux = fim_pl20223 - data_atual

dias_faltando_fim_pl20223 = dias_faltando_fim_pl20223_aux.days
# -------------------------------------------------

# Periodos Letivos - EXTENSIVOS
# 2022.2
# 2022-03-14 ( inicio do 2022.2 - EXTENSIVO )
# 2022-07-11 ( fim do 2022.2 - EXTENSIVO )

# 119 dias corridos
# 100 dias letivos

fim_pl20222 = date(2022, 7, 11)

dias_faltando_fim_pl20222_aux = fim_pl20222 - data_atual

dias_faltando_fim_pl20222 = dias_faltando_fim_pl20222_aux.days

# Periodos Letivos - EXTENSIVOS
# 2022.4
# 2022-08-22 ( inicio do 2022.4 - EXTENSIVO )
# 2022-12-21 ( fim do 2022.4 - EXTENSIVO )

# 121 dias corridos
# 100 dias letivos

fim_pl20224 = date(2022, 12, 21)

dias_faltando_fim_pl20224_aux = fim_pl20224 - data_atual

dias_faltando_fim_pl20224 = dias_faltando_fim_pl20224_aux.days


# -------------------------------------------------

# Lógica da Mensagem:


def texto_do_tweet():
    texto_final = str()

    def texto_padrao_dias(dias_que_faltam, periodo_atual):
        return f"Faltam {dias_que_faltam} dias para as Férias (Término do P.L. {periodo_atual})\n"

    def texto_padrao_dia(periodo_atual):
        return f"Falta 1 dia para as Férias (Término do P.L. {periodo_atual})\n"

    def texto_glorioso(periodo_atual):
        return f"Chegou o Glorioso Dia Meus Bacanos !!! (Férias - Acabou o P.L. {periodo_atual})\n"

    def texto_final_aux(periodo_atual, dias_que_faltam):
        texto_final_aux = str()

        if dias_que_faltam > 1:
            texto_final_aux += texto_padrao_dias(dias_que_faltam, periodo_atual)
        elif dias_que_faltam == 1:
            texto_final_aux += texto_padrao_dia(dias_que_faltam)
        elif dias_que_faltam == 0:
            texto_final_aux += texto_glorioso(periodo_atual)
        return texto_final_aux

    if ano_atual == 2022 and 1 <= mes_atual <= 2:
        periodo_letivo = '2022.1 - INTENSIVO'
        texto_final += texto_final_aux(periodo_letivo, dias_faltando_fim_pl20221)

    if ano_atual == 2022 and 3 <= mes_atual <= 7:
        if (mes_atual == 3 and dia_atual >= 14) or mes_atual > 3:
            periodo_letivo = '2022.2 - EXTENSIVO'
            texto_final += texto_final_aux(periodo_letivo, dias_faltando_fim_pl20222)

    if ano_atual == 2022 and 7 <= mes_atual <= 8:
        periodo_letivo = '2022.3 - INTENSIVO'
        texto_final += texto_final_aux(periodo_letivo, dias_faltando_fim_pl20223)

    if ano_atual == 2022 and 8 <= mes_atual <= 12:
        if (mes_atual == 8 and dia_atual >= 22) or mes_atual > 8:
            periodo_letivo = '2022.4 - EXTENSIVO'
            texto_final += texto_final_aux(periodo_letivo, dias_faltando_fim_pl20224)

    return texto_final

