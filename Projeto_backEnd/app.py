import streamlit as st
from supabase import create_client, Client
import streamlit.components.v1 as components

url = st.secrets["supabase"]["url"] # Cria uma variável atrelada a url no secrets.toml, na pasta.streamlit
key = st.secrets["supabase"]["key"] # Cria uma variável atrelada a key no secrets.toml, na pasta.streamlit

supabase: Client = create_client(url,key) # Cria o cliente do supabase utilizando as variáveis url e key
resposta = supabase.table("usuario").select("*").execute() # Realiza uma consulta na tabela "usuario" do supabase, selecionando todas as colunas
dados_usuario = resposta.data

st.write("---") # Print uma linha horizontal

st.write("Registro de usuário")
novo_usuario = st.text_input("Digite seu usuário") # Atribui a variável "novo_usuario" ao valor digitado
nova_senha = st.text_input("Digite sua senha*", type="password") # Atribui a variável "nova_senha" ao valor digitado
resposta = supabase.table("usuario").select("*").eq("nome_usuario", novo_usuario).execute() # Verifica se o nome de usuário digitado já consta no banco de dados

if st.button("Salvar usuario"): # "Caso o botão seja clicado, execute o código abaixo"
    if resposta.data: # "Se tiver algum resultado na pesquisa da variável resposta, isto é, se já existir um usuário igual ao digitado no banco de dados, barre a nova criação"
        st.error("Usuário já existe!")
        st.stop()
    novos_dados = {"nome_usuario": novo_usuario, "senha": nova_senha} 
    supabase.table("usuario").insert(novos_dados).execute() # Insere os dados do novo usuário na tabela "usuario" do supabase
    st.success("Usuário criado!")
    

st.write("---")
st.write("Deletar usuário")

delete_user = st.text_input("Digite o usuário que deseja deletar")

if st.button("Deletar usuário"):
    supabase.table("usuario").delete().eq("nome_usuario", delete_user).execute() #Caso o nome digitado seja o MESMO da tabela (eq), delete o usuário
    st.success("Usuário deletado!")

st.write("---")
st.write("Alteração de senha")

update_usuario = st.text_input("Insira o nome do usuário que deseja alterar a senha")
update_senha = st.text_input("Digite a nova senha", type="password")

if st.button("Alterar senha"):
    supabase.table("usuario").update({"senha": update_senha}).eq("nome_usuario", update_usuario).execute()
    st.success("Senha alterada!")
    
 