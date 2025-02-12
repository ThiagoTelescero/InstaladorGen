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

## 🆕 Patch de Atualização - Versão 0.0.5

### 🔄 Melhorias Implementadas

Esta atualização traz diversas melhorias para tornar o Atualizador de Scripts e Executáveis mais eficiente e intuitivo.

## 📌 Novidades e Melhorias

✅ 1. **Barra de Progresso Percentual** -Agora, a barra de progresso exibe o percentual real do processo, avançando proporcionalmente ao número de scripts SQL ou executáveis processados.

✅ 2. **Captura de Erros SQL no Log** -Os erros do SQL não são mais genéricos. O programa agora exibe detalhes completos do erro gerado pelo sqlcmd, tornando a depuração muito mais rápida e eficaz.

✅ 3. **Interface Responsiva e Scroll Automático no Log** -O log agora inclui uma barra de rolagem, permitindo visualizar erros e mensagens anteriores sem precisar redimensionar a janela. Além disso, o scroll é automático, sempre exibindo a última linha do log conforme novos registros são adicionados.

✅ 4. **Execução Assíncrona Melhorada** -As operações rodam em threads separadas, evitando travamentos e garantindo que a interface continue responsiva mesmo durante processos longos.
