import tkinter as tk
from tkinter import filedialog, messagebox
import os
import subprocess

def executar_sql():
    server = server_entry.get()
    database = db_entry.get()
    user = user_entry.get()
    password = password_entry.get()
    scripts_files = filedialog.askopenfilenames(title="Selecione os scripts SQL", filetypes=[("Arquivos SQL", "*.sql")])

    if not scripts_files:
        messagebox.showerror("Erro", "Nenhum arquivo SQL selecionado!")
        return

    for script_path in scripts_files:
        cmd = f"sqlcmd -S {server} -d {database} -U {user} -P {password} -i \"{script_path}\""
        try:
            subprocess.run(cmd, check=True, shell=True)
            log_text.insert(tk.END, f"Executado com sucesso: {os.path.basename(script_path)}\n")
        except subprocess.CalledProcessError as e:
            log_text.insert(tk.END, f"Erro no script: {os.path.basename(script_path)}\n")
            messagebox.showerror("Erro", f"Falha ao executar: {os.path.basename(script_path)}")

def atualizar_executaveis():
    executaveis_files = filedialog.askopenfilenames(title="Selecione os novos executáveis", filetypes=[("Arquivos Executáveis", "*.exe"),("Todos os arquivos", "*.*")])
    target_dir = filedialog.askdirectory(title="Selecione o diretório de destino")

    if not executaveis_files or not target_dir:
        messagebox.showerror("Erro", "Arquivos ou diretório de destino não selecionados!")
        return

    for file_path in executaveis_files:
        file_name = os.path.basename(file_path)
        dst_path = os.path.join(target_dir, file_name)
        try:
            # Copia os arquivos sem mover
            with open(file_path, "rb") as src, open(dst_path, "wb") as dst:
                dst.write(src.read())
            log_text.insert(tk.END, f"Atualizado: {file_name}\n")
        except Exception as e:
            log_text.insert(tk.END, f"Erro ao atualizar: {file_name}\n")

root = tk.Tk()
root.title("Atualizador de Scripts e Executáveis")
##root.iconbitmap(os.path.join(os.path.dirname(__file__), "meu_icone.ico"))  # Adiciona o ícone
root.configure(bg="#0b2447")  # Define o fundo como azul escuro

# Configurações do Servidor
tk.Label(root, text="Servidor:", bg="#0b2447", fg="white", anchor="w").grid(row=0, column=0, sticky="w", padx=10, pady=5)
server_entry = tk.Entry(root)
server_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Banco de Dados:", bg="#0b2447", fg="white", anchor="w").grid(row=1, column=0, sticky="w", padx=10, pady=5)
db_entry = tk.Entry(root)
db_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Usuário:", bg="#0b2447", fg="white", anchor="w").grid(row=2, column=0, sticky="w", padx=10, pady=5)
user_entry = tk.Entry(root)
user_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Senha:", bg="#0b2447", fg="white", anchor="w").grid(row=3, column=0, sticky="w", padx=10, pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=3, column=1, padx=10, pady=5)

# Botões de Ação
tk.Button(root, text="Executar Scripts SQL", command=executar_sql, bg="#001233", fg="white", relief="raised").grid(row=4, column=0, padx=10, pady=10)
tk.Button(root, text="Atualizar Executáveis", command=atualizar_executaveis, bg="#001233", fg="white", relief="raised").grid(row=4, column=1, padx=10, pady=10)

# Log
log_text = tk.Text(root, height=15, width=60, bg="#0b2447", fg="white", relief="solid")
log_text.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()