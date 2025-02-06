Aqui está a documentação no formato Markdown completa, pronta para ser copiada:


# Atualizador de Scripts SQL e Executáveis

## 📌 Visão Geral
O **Atualizador de Scripts SQL e Executáveis** é uma aplicação em Python com Tkinter que facilita a execução de scripts SQL e a cópia de arquivos executáveis para um diretório de destino. Ele fornece uma interface gráfica simples e interativa para esses processos.

---

## 🚀 Funcionalidades

1. **Execução de Scripts SQL**
   - Permite selecionar múltiplos arquivos `.sql`.
   - Conecta-se ao banco de dados e executa os scripts em sequência.
   - Exibe logs de sucesso ou erro.

2. **Cópia de Arquivos Executáveis**
   - Permite selecionar múltiplos arquivos `.exe`.
   - Copia os arquivos selecionados para o diretório de destino.
   - Mantém os metadados dos arquivos.

3. **Interface Gráfica (GUI)**
   - Interface simples e intuitiva desenvolvida com Tkinter.
   - Logs detalhados na tela para acompanhar os processos.

---

## 🖥️ Uso

### 1️⃣ **Executar Scripts SQL**
- Informe o **servidor**, **banco de dados**, **usuário** e **senha**.
- Clique em **"Executar Scripts SQL"**.
- Escolha os arquivos `.sql` para rodar.
- O sistema executará os scripts e exibirá os logs.

### 2️⃣ **Atualizar Executáveis**
- Clique em **"Atualizar Executáveis"**.
- Escolha os arquivos `.exe` a serem copiados.
- Escolha o diretório de destino.
- Os arquivos serão copiados e registrados no log.

---

## 🛠️ Tecnologias Utilizadas
- **Python 3.x**
- **Tkinter** (Interface Gráfica)
- **Subprocess** (Execução de comandos SQL)
- **Shutil** (Cópia de arquivos)

---

## 📌 Possíveis Erros e Soluções

| **Erro**                     | **Causa Provável**               | **Solução**                                                   |
|------------------------------|----------------------------------|--------------------------------------------------------------|
| "Nenhum arquivo selecionado!" | O usuário não escolheu arquivos. | Selecionar ao menos um `.sql` ou `.exe`.                     |
| "Erro ao executar o script"   | Problema de conexão com o banco. | Verificar credenciais e conexão.                             |
| "Erro ao copiar arquivo"      | Arquivo em uso ou sem permissão. | Fechar o arquivo e executar como administrador.              |

---
