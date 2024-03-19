from tkinter import Listbox, Scrollbar, filedialog, messagebox
import customtkinter
import pyperclip

def atualizar_cor(*args):
    # Obtém os valores atuais dos sliders
    r = int(SVermelho.get())
    g = int(SVerde.get())
    b = int(SAzul.get())
    
    # Atualiza os labels com os valores atuais
    LVermelho.configure(text=f'Vermelho: {r}')
    LVerde.configure(text=f'Verde: {g}')
    LAzul.configure(text=f'Azul: {b}')
    
    # Converte os valores para uma string de cor hexadecimal
    hex_cor = f'#{r:02x}{g:02x}{b:02x}'
    
    # Atualiza a cor de fundo de PCor com a nova cor
    PCor.config(bg=hex_cor)
    EHexa.delete(0, 'end')
    EHexa.insert('end', hex_cor)
    ERGB.delete(0, 'end')
    ERGB.insert('end', f'{r}, {g}, {b}')

def carregar_rgb():
    Ref = EnomeRGB.get()  # Obtém o texto da entrada EnomeRGB
    codigo_rgb = ERGB.get()  # Obtém o texto da entrada ERGB

    # Verifica se o nome e o código RGB não estão vazios
    if Ref and codigo_rgb:
        Ref = f"{Ref}{codigo_rgb}"  # Formata o texto a ser adicionado à lista
        Lcodico.insert('end', Ref)  # Adiciona o texto à lista Lcodico
    else:
        messagebox.showwarning("Campos Vazios", "Por favor, preencha todos os campos.")

def carregar_Hexa():
    Ref = Enome.get()  # Obtém o texto da entrada Enome
    codigo_Hexa = EHexa.get()  # Obtém o texto da entrada EHexa

    # Verifica se o nome e o código RGB não estão vazios
    if Ref and codigo_Hexa:
        Ref = f"{Ref}{codigo_Hexa}"  # Formata o texto a ser adicionado à lista
        Lcodico.insert('end', Ref)  # Adiciona o texto à lista Lcodico    
    else:
        messagebox.showwarning("Campos Vazios", "Por favor, preencha todos os campos.")

def limpar():
    # Verificar se há valores nos campos antes de limpar
    if EnomeRGB.get() != '' or ERGB.get() != '' or Enome.get() != '' or EHexa.get() != '':
        # Definir os valores padrão para os sliders
        SVermelho.set(0)
        SVerde.set(0)
        SAzul.set(0)

        # Atualizar os labels com os valores padrão
        LVermelho.configure(text='Vermelho: 0')
        LVerde.configure(text='Verde: 0')
        LAzul.configure(text='Azul: 0')

        # Limpar a entrada EnomeRGB e ENome
        EnomeRGB.delete(0, 'end')
        EnomeRGB.insert(0, 'Referência Ex Co1')  # Define o placeholder text novamente
        Enome.delete(0, 'end')
        Enome.insert(0, 'Referência Ex Co1')  # Define o placeholder text novamente

        # Limpar a entrada ERGB
        ERGB.delete(0, 'end')
        ERGB.insert(0, 'Código RGB')  # Define o placeholder text novamente
        EHexa.delete(0, 'end')
        EHexa.insert(0, 'Código hexadecimal')  # Define o placeholder text novamente

        # Limpar a lista Lcodico
        Lcodico.delete(0, 'end')

        # defenir o Backcolor de PCor para Cor padrão 
        PCor.config(bg=co1)
    else:
        messagebox.showinfo("Campos Vazios", "Não há valores para limpar.")

def guardar_codico():
    if Lcodico.size() > 0:
        # Abrir a janela de diálogo para escolher onde salvar o arquivo
        filepath = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if filepath:  # Verificar se um caminho foi selecionado
        # Abrir o arquivo no caminho escolhido em modo de escrita
            with open(filepath, 'w') as arquivo:
            # Iterar por cada item na lista Lcodico
                for item in Lcodico.get(0, 'end'):
                # Escrever o item no arquivo seguido de uma nova linha
                    arquivo.write(f"{item}\n")
        messagebox.showinfo("CODIGO","Codigo guardado com sucesso!")  # Confirmação no terminal
    else:
        messagebox.showinfo("Lista Vazia", "Não há dados para salvar.")
        
def copiar_codico():
    # Verificar se há códigos na lista
    if Lcodico.size() > 0:
        # Inicializar uma string vazia para armazenar o conteúdo da lista
        conteudo_para_copiar = ""
        # Obter todos os itens da lista Lcodico e adicionar à string
        for item in Lcodico.get(0, 'end'):
            conteudo_para_copiar += f"{item}\n"
        # Usar pyperclip para copiar o conteúdo para a área de transferência
        pyperclip.copy(conteudo_para_copiar)
        messagebox.showinfo("Copiar", "Conteúdo copiado para a área de transferência!")
    else:
        messagebox.showinfo("Lista Vazia", "Não há códigos para copiar.")

# Definir as cores a usar no projeto
co0 = '#ffffff'  # cor Branco
co1 = '#000000'  # cor preto
co2 = '#f1f3f5'  # cor Cinza
Co3 = '#f9f5fa'  # cor rosa Claro

# Configurar a janela
janela = customtkinter.CTk()
janela.geometry('800x470+100+100')
janela.title('SelectorV1 Dev Joel PT 2024 © ')
janela.resizable(False, False)
janela.config(bg=co0)  # Cor de fundo da janela
janela.iconbitmap('C:\\Users\\HP\\Desktop\\Python customtkinter\\Selector de Cores v1\\icon.ico')

# Ajuste para o CTkCanvas------------------------------------------------------------------------------------------------------------------------------------
PCor = customtkinter.CTkCanvas(janela, width=300, height=330)
PCor.place(x=10, y=10)
PCor.config(bg=co1, width=380)
#------------------------------------------------------------------------------------------------------------------------------------------------------------
# Labels e Sliders para Vermelho, Verde, Azul----------------------------------------------------------------------------------------------------------------
LVermelho = customtkinter.CTkLabel(janela, text='Vermelho:0', font=('arial', 15, 'bold'), bg_color=co0)
LVermelho.place(x=320, y=10)
SVermelho = customtkinter.CTkSlider(janela, bg_color=co0,to=0, from_=255, width=465,command=atualizar_cor)
SVermelho.place(x=320, y=40)
LVerde = customtkinter.CTkLabel(janela, text='Verde: 0', font=('arial', 15, 'bold'), bg_color=co0)
LVerde.place(x=320, y=70)
SVerde = customtkinter.CTkSlider(janela, bg_color=co0, width=465, to=0, from_=255, command=atualizar_cor)
SVerde.place(x=320, y=100)
LAzul = customtkinter.CTkLabel(janela, text='Azul: 0', font=('arial', 15, 'bold'), bg_color=co0)
LAzul.place(x=320, y=130)
SAzul = customtkinter.CTkSlider(janela, bg_color=co0, width=465, to=0, from_=255, command=atualizar_cor)
SAzul.place(x=320, y=160)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
# Entradas para Nome, Código Hexadecimal--------------------------------------------------------------------------------------------------------------------
Enome = customtkinter.CTkEntry(janela, placeholder_text='Referência Ex Co1', bg_color=co0, width=120)
Enome.place(x=320, y=190)
EHexa = customtkinter.CTkEntry(janela, placeholder_text='Código hexadecimal', bg_color=co0, width=130)
EHexa.place(x=450, y=190)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
# Entradas para Nome, Código RGB---------------------------------------------------------------------------------------------------------------------------- 
EnomeRGB = customtkinter.CTkEntry(janela, placeholder_text='Referência Ex Co1', bg_color=co0, width=120)
EnomeRGB.place(x=320, y=230)
ERGB = customtkinter.CTkEntry(janela, placeholder_text='Código RGB', bg_color=co0, width=130)
ERGB.place(x=450, y=230)
#----------------------------------------------------------------------------------------------------------------------------------------------------------
# criar Os botões -----------------------------------------------------------------------------------------------------------------------------------------
BcarregarRGB = customtkinter.CTkButton(janela, text='Carregar RGB', bg_color=co0, fg_color=co2,text_color=co1,font=('arial',12,'bold'),command=carregar_rgb)  # Corrigido nome do botão para evitar duplicidade
BcarregarRGB.place(x=590, y=230)
BLimpar = customtkinter.CTkButton(janela, text='Limpar', bg_color=co0, fg_color=co2,text_color=co1,font=('arial',12,'bold'),command=limpar)
BLimpar.place(x=10, y=290)
BGuardar = customtkinter.CTkButton(janela, text='Guardar', fg_color=co2,text_color=co1,font=('arial',12,'bold'),bg_color=co0, command=guardar_codico)
BGuardar.place(x=165, y=290)
BCopiar = customtkinter.CTkButton(janela, text='Copiar', bg_color=co0, fg_color=co2,text_color=co1,font=('arial',12,'bold'),command=copiar_codico)
BCopiar.place(x=310, y=290)
BcarregarHexa = customtkinter.CTkButton(janela, text='Carregar Hexadecimal', bg_color=co0, fg_color=co2,text_color=co1,font=('arial',12,'bold'),command=carregar_Hexa)
BcarregarHexa.place(x=590, y=190)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
# Listbox com Scrollbar-------------------------------------------------------------------------------------------------------------------------------------
frame_codico = customtkinter.CTkFrame(janela, width=240, height=70, bg_color=Co3)  # Ajustado para bg_color
frame_codico.place(x=10, y=330)
Lcodico = Listbox(frame_codico, width=87, height=6, bg=Co3, font=('arial 14'))
Lcodico.pack(side="left", fill="y")
scrollbar = Scrollbar(frame_codico, orient="vertical")
scrollbar.config(command=Lcodico.yview)
scrollbar.pack(side="right", fill="y")
Lcodico.config(yscrollcommand=scrollbar.set)
#--------------------------------------------------------------------------------------------------------------
# Iniciar a janela --------------------------------------------------------------------------------------------
janela.mainloop()
#---------------------------------------------------------------------------------------------------------------
