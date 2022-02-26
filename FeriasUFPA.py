import os
import tweepy
from texto_do_tweet import *

# Integração com o Twitter usando Tweepy:

# 1. Informações da conta:
# Favor Adicione os tokens e chaves como variaveis do ambiente!!!
# Isso pode ser feito usando o comado export no linux e setx no windows
Consumer_Key = os.environ["CONSUMER_KEY"]
Consumer_Secret_Key = os.environ["CONSUMER_SECRET_KEY"]
Access_Token = os.environ["ACCESS_TOKEN"]
Access_Secret_Token = os.environ["ACCESS_SECRET_TOKEN"]

# 2. Autenticação
auth = tweepy.OAuthHandler(Consumer_Key, Consumer_Secret_Key)
auth.set_access_token(Access_Token, Access_Secret_Token)
api = tweepy.API(auth)

mensagem_do_dia = texto_do_tweet()

# 3. Função que posta a mensagem do dia
def postar_mensagem_do_dia():
    try:
        api.update_status(mensagem_do_dia)
    except Exception as e:
        api.update_status(f"Apareceu o seguinte erro: {e}\nPor favor avisar o Erick Herói !!!")


# 4. Vendo se a mensagem já foi postada!
def verificacao_de_tweet_duplicado():
    foiPostado = False

    meus_posts_recentes = api.user_timeline()

    for post in meus_posts_recentes:
        if post.text == mensagem_do_dia:
            foiPostado = True
    return foiPostado


# 5. Função que envia mensagem no direct (Opcional - Para testes)
def enviar_mensagem_direta(nome_de_usuario: str, texto: str):
    id_no_twitter = api.get_user(f"@{nome_de_usuario}").id
    api.send_direct_message(str(id_no_twitter), texto)

# 6. Função Principal
def main():
    if not verificacao_de_tweet_duplicado():
        postar_mensagem_do_dia()


if __name__ == "__main__":
    main()
