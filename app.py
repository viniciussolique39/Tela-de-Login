import customtkinter as ctk

ctk.set_appearance_mode('dark')

def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    if usuario == 'Vinícius' and senha == '25102005': 
        resultado_login.configure(text='Login feito com sucesso!',
        text_color='green')

    else:
        resultado_login.configure(text='Login Incorreto', text_color='red')
 

app = ctk.CTk()
app.title('Acesso ao Sistema')
app.geometry('300x300')

label_usuario = ctk.CTkLabel(app,text='Código/Usuário')
label_usuario.pack(pady=10)

campo_usuario = ctk.CTkEntry(app, placeholder_text='Digite seu Usuário')
campo_usuario.pack(pady=10)

label_senha = ctk.CTkLabel(app,text='Senha')
label_senha.pack(pady=10)

campo_senha = ctk.CTkEntry(app, placeholder_text='Digite sua Senha', show='*')
campo_senha.pack(pady=10)


botao_login = ctk.CTkButton(app,text='Ok', command=validar_login)
botao_login.pack(pady=10)


resultado_login =  ctk.CTkLabel(app, text='')
resultado_login.pack (pady=10)



app.mainloop()