import tweepy
from texto_do_tweet import *

# Integração com o Twitter usando Tweepy:

# 1. Informações da conta:
# Favor excluir os tokens e chaves antes de enviar pro github!!!
Consumer_Key = ''
Consumer_Secret_Key = ''
Access_Token = ''
Access_Secret_Token = ''
# Favor excluir os tokens e chaves antes de enviar pro github!!!

# 2. Autenticação
auth = tweepy.OAuthHandler(Consumer_Key, Consumer_Secret_Key)
auth.set_access_token(Access_Token, Access_Secret_Token)
api = tweepy.API(auth)


# Criando um Log caso algo dê errado.
def debug_text(local, error):
    texto_do_debug = open('texto do debug.txt', 'w')
    texto_do_debug.write(f"Deu erro no(a) {local}\n{error}\n")
    texto_do_debug.close()


# 3. Função que posta a mensagem do dia
def postar_mensagem_do_dia():
    local = "Função Postar Mensagem do Dia"
    try:
        mensagem_do_dia = texto_dos_bacanas()
        api.update_status(mensagem_do_dia)

    except Exception as error:
        debug_text(local, error)


# 4. Vendo se a mensagem já foi postada!
meus_posts_recentes = api.user_timeline()


def verificacao_de_tweet_duplicado():
    local = "Função Verificação De Tweet Duplicado"
    isPosted = False
    try:
        for post in meus_posts_recentes:
            if post.text == texto_dos_bacanas():
                isPosted = True
        return isPosted

    except Exception as error:
        debug_text(local, error)


def enviar_mensagem_direta(nome_de_usuario: str, texto: str):
    local = "Função Enviar_Mensagem_Direta"
    try:
        id_no_twitter = api.get_user(f"@{nome_de_usuario}").id
        api.send_direct_message(str(id_no_twitter), texto)

    except Exception as error:
        debug_text(local, error)


def main():
    local = "Função Main"
    try:
        if verificacao_de_tweet_duplicado():
            texto_da_mensagem = open('texto da mensagem.txt', 'w')
            texto_da_mensagem.write(f"O tweet de hoje já foi postado anteriormente, Não esquente sua cabeça!\nA "
                                    f"Mensagem do dia é {texto_da_mensagem}\n")
            texto_da_mensagem.close()

        elif not verificacao_de_tweet_duplicado():
            postar_mensagem_do_dia()

            texto_da_mensagem = open('texto da mensagem.txt', 'w')
            texto_da_mensagem.write(f"Mermão, tudo NO ESQUEMA!!! O de hoje foi pago agora!!!\n"
                                    f"A mensagem do dia é {texto_da_mensagem}\n")
            texto_da_mensagem.close()

    except Exception as error:
        debug_text(local, error)


main()
