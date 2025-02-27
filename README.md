## 🔍 Monitoramento de Computadores - Tarefa Bimestral  

🚀 **Um sistema cliente-servidor para recuperar e exibir informações de hardware dos computadores em rede.**  
📚 **Trabalho para a disciplina de Redes de Computadores no IFRN**

### 📌 Funcionalidades  

✅ Quantidade de processadores  
✅ Memória RAM livre  
✅ Espaço em disco livre  
✅ **BÔNUS**: Temperatura do processador  
✅ Cálculo da média simples dos dados  
✅ Listagem e detalhamento de um computador específico  

### 📡 Arquitetura  

O sistema segue o modelo **cliente/servidor**, garantindo que os clientes sejam **localizados automaticamente** e a comunicação seja feita utilizando **sockets puros** e **criptografia**.  

### 🛠️ Tecnologias  

🔹 **Linguagem:** Python  
🔹 **Paradigma:** Programação Orientada a Objetos  
🔹 **Bibliotecas Utilizadas:** `socket`, `psutil`, `cryptography`

### 📥 Instalação  

1. Clone o repositório:  
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```  
2. Instale as dependências necessárias:  
   ```bash
   pip install -r requirements.txt
   ```  

### 🔒 Segurança  

A comunicação entre cliente e servidor é criptografada para garantir a segurança dos dados transmitidos.  
