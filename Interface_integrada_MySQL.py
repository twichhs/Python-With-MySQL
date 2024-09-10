import customtkinter as ctk
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
import mysql.connector
def conexao():
    return mysql.connector.connect(
    host='localhost',
    user='root',
    password='Joao-14_12',
    database='logins',
)
def inserir_dados():
    db_conexao = conexao()
    cursor = db_conexao.cursor()
    Username = str(Username_teste.get()) 
    Password = str(PassWord_teste.get()) 
    comando = 'INSERT INTO usuários (username, codepass) VALUES (%s, %s)'
    cursor.execute(comando, (Username, Password))
    db_conexao.commit()
    cursor.close()
    db_conexao.close()

janela=ctk.CTk()
janela.geometry("500x300")
# janela.configure(background="#252629")   
janela.title("Python CTK")

login_teste = ctk.CTkLabel(janela, text="Login", font=("arial",16))
login_teste.pack(padx=10, pady=10)
# no custom se coloca o width e o height junto com a variavél logo de cara. Porem tem uma forma mais pratica de ajustar a posição dos elementos
Username_teste = ctk.CTkEntry(janela, placeholder_text="Username")
Username_teste.pack(padx= 10 , pady= 10)

PassWord_teste = ctk.CTkEntry(janela, placeholder_text="Password", show="*")
PassWord_teste.pack(padx= 10 , pady= 10)

caixa = ctk.CTkCheckBox(janela, text= "Remember Me")
caixa.pack(padx= 10 , pady= 10)

BOTAO = ctk.CTkButton(janela, text="Enter", command=inserir_dados)
BOTAO.pack(padx= 10, pady= 10)

# botao = ctk.CTkButton()
janela.mainloop()