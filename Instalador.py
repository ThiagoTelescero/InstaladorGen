import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import subprocess
import threading

def executar_sql():
    server = server_entry.get()
    database = db_entry.get()
    user = user_entry.get()
    password = password_entry.get()
    scripts_files = filedialog.askopenfilenames(title="Selecione os scripts SQL", filetypes=[("Arquivos SQL", "*.sql")])

    if not scripts_files:
        messagebox.showerror("Erro", "Nenhum arquivo SQL selecionado!")
        return

    total_scripts = len(scripts_files)
    progress_bar["maximum"] = total_scripts
    progress_bar["value"] = 0

    def run_scripts():
        for index, script_path in enumerate(scripts_files, start=1):
            cmd = f"sqlcmd -S {server} -d {database} -U {user} -P {password} -i \"{script_path}\""
            try:
                result = subprocess.run(cmd, check=True, shell=True, capture_output=True, text=True)
                log_text.insert(tk.END, f"✅ Executado com sucesso: {os.path.basename(script_path)}\n")
                if result.stdout:
                    log_text.insert(tk.END, f"📜 Log SQL: {result.stdout}\n")
            except subprocess.CalledProcessError as e:
                log_text.insert(tk.END, f"❌ Erro no script: {os.path.basename(script_path)}\n")
                log_text.insert(tk.END, f"🔴 Detalhes do erro: {e.stderr}\n")
                messagebox.showerror("Erro", f"Falha ao executar: {os.path.basename(script_path)}\n\n{e.stderr}")

            progress_bar["value"] = index
            progress_label.config(text=f"Progresso: {int((index/total_scripts) * 100)}%")
            log_text.yview_moveto(1)  # Mantém o scroll sempre no final
            root.update_idletasks()

        messagebox.showinfo("Concluído", "Todos os scripts SQL foram executados!")

    threading.Thread(target=run_scripts).start()

def atualizar_executaveis():
    executaveis_files = filedialog.askopenfilenames(title="Selecione os novos executáveis", filetypes=[("Arquivos Executáveis", "*.exe"), ("Todos os arquivos", "*.*")])
    target_dir = filedialog.askdirectory(title="Selecione o diretório de destino")

    if not executaveis_files or not target_dir:
        messagebox.showerror("Erro", "Arquivos ou diretório de destino não selecionados!")
        return

    total_files = len(executaveis_files)
    progress_bar["maximum"] = total_files
    progress_bar["value"] = 0

    def update_files():
        for index, file_path in enumerate(executaveis_files, start=1):
            file_name = os.path.basename(file_path)
            dst_path = os.path.join(target_dir, file_name)
            try:
                with open(file_path, "rb") as src, open(dst_path, "wb") as dst:
                    dst.write(src.read())
                log_text.insert(tk.END, f"✅ Atualizado: {file_name}\n")
            except Exception as e:
                log_text.insert(tk.END, f"❌ Erro ao atualizar: {file_name}\n🔴 Detalhes: {str(e)}\n")

            progress_bar["value"] = index
            progress_label.config(text=f"Progresso: {int((index/total_files) * 100)}%")
            log_text.yview_moveto(1)  # Mantém o scroll sempre no final
            root.update_idletasks()

        messagebox.showinfo("Concluído", "Todos os executáveis foram atualizados!")

    threading.Thread(target=update_files).start()

# Configuração da Janela Principal
root = tk.Tk()
root.title("Atualizador de Scripts e Executáveis")
root.configure(bg="#0b2447")

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

# Barra de Progresso
progress_bar = ttk.Progressbar(root, mode="determinate", length=300)
progress_bar.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Label para exibir a porcentagem
progress_label = tk.Label(root, text="Progresso: 0%", bg="#0b2447", fg="white")
progress_label.grid(row=6, column=0, columnspan=2)

# Frame para Log + Barra de Rolagem
log_frame = tk.Frame(root)
log_frame.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

scrollbar = tk.Scrollbar(log_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

log_text = tk.Text(log_frame, height=15, width=60, bg="#0b2447", fg="white", relief="solid", yscrollcommand=scrollbar.set)
log_text.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar.config(command=log_text.yview)  # Conecta a barra de rolagem ao log

root.mainloop()