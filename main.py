import requests
import streamlit as st

st.title("Painel Pessoal de Análise de Rede")
st.subheader('Desenvolvido por: Paulo Araújo')
 
mainRouter = None
mainRouter_statusCode = None
secondRouter = None
secondRouter_statusCode = None


try:
    secondRouter = requests.get('http://192.168.1.250')
    secondRouter_statusCode = secondRouter.status_code
    try:
        mainRouter = requests.get('http://192.168.1.1')
        mainRouter_statusCode = mainRouter.status_code
    except:
        mainRouter_statusCode = None
        st.error("O repetidor perdeu sinal com o roteador principal.")
#this section above is to check if the main router is reachable, if not it will show an error message

# O código acima é para verificar se o roteador principal está acessível, caso contrário, ao invés de declarar o status code, ele vai exibir uma mensagem de erro no front-end. 

except:
    secondRouter_statusCode = None
    mainRouter_statusCode = None
    st.error("O roteador secundário não está respondendo")
#this section above is to check if the second router is reachable, if not it will show an error message
# O código acima é para verificar se o roteador secundário está acessível, caso contrário, ao invés de declarar o status code, ele vai exibir uma mensagem de erro no front-end.

def checkMainRouter():
    if mainRouter_statusCode == 200:
        st.image('imgs/ac121-states/ac121.png', width=150)
    else:
        st.image('imgs/ac121-states/ac121black.png', width=150)

def checkSecondRouter():
    if mainRouter_statusCode == 200:
        st.image('imgs/ac12g-states/ac12g.png', width=150)
    else:
        st.image('imgs/ac12g-states/ac121black.png', width=150)

        




col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

with col1:
    st.image('imgs/computer.png', width=150)
with col2:
    if secondRouter_statusCode == 200:
        st.image('imgs/lines-states/greenline.png', width=150)
    else:
        st.image('imgs/lines-states/orangeline.png', width=150)
with col3:
   checkSecondRouter()
with col4:
    if secondRouter_statusCode == 200:
        st.image('imgs/lines-states/greenline.png', width=150)
    else:
        st.image('imgs/lines-states/orangeline.png', width=150)
with col5:
    if secondRouter_statusCode == 200:
        st.image('imgs/repeater-states/repeater.png', width=150)
    else:
        st.image('imgs/repeater-states/repeaterblack.png', width=150)
with col6:
    if mainRouter_statusCode == 200:
        st.image('imgs/lines-states/greenline.png', width=150)
    else:
        st.image('imgs/lines-states/orangeline.png', width=150)
with col7:
    checkMainRouter()