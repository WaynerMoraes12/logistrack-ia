# 🚛 LogisTrack - Event-Driven AI Pipeline

Sistema de monitoramento logístico baseado em eventos que utiliza **Node.js**, **Redis**, **Python** e **Inteligência Artificial** para detectar anomalias operacionais e gerar ações corretivas em tempo real.

---

## 🎯 Objetivo

Receber dados de telemetria de caminhões via API, processar eventos de forma assíncrona e utilizar um agente de IA para analisar situações críticas, como:

* Temperatura elevada de cargas sensíveis;
* Atrasos de entrega;
* Problemas operacionais;
* Alertas logísticos.

---

## 🏗️ Arquitetura

```text
Cliente/Webhook
       │
       ▼
 API Gateway (Node.js)
       │
       ▼
   Redis Pub/Sub
       │
       ▼
 AI Worker (Python)
       │
       ▼
 Dashboard (Socket.io)
```

---

## 📂 Estrutura dos Arquivos

```text
logistrack/
│
├── node_modules/
├── .gitignore
├── docker-compose.yml
├── index.html
├── package.json
├── package-lock.json
├── README.md
├── requirements.txt
├── server.js
└── worker.py
```

### 📦 node_modules/

Contém todas as dependências instaladas pelo NPM.

**Função:** Bibliotecas utilizadas pelo servidor Node.js.

---

### 🚫 .gitignore

Define quais arquivos não serão enviados para o GitHub.

**Função:** Evitar subir dependências, arquivos temporários e segredos.

---

### 🐳 docker-compose.yml

Arquivo responsável por subir o Redis automaticamente usando Docker.

**Função:** Infraestrutura do sistema.

---

### 🌐 index.html

Dashboard simples exibido no navegador.

**Função:** Interface visual para acompanhar os eventos e respostas da IA em tempo real.

---

### 📦 package.json

Arquivo principal do projeto Node.js.

**Função:**

* Lista dependências;
* Define scripts de execução;
* Configura o projeto.

---

### 🔒 package-lock.json

Gerado automaticamente pelo NPM.

**Função:** Garantir versões exatas das dependências.

---

### 📄 README.md

Documentação do projeto.

**Função:** Explicar arquitetura, instalação e funcionamento.

---

### 🐍 requirements.txt

Lista das dependências Python.

**Função:** Instalar bibliotecas necessárias para o Worker de IA.

Exemplo:

```bash
pip install -r requirements.txt
```

---

### 🚀 server.js

API Gateway do sistema.

**Função:**

* Receber webhooks;
* Expor endpoints REST;
* Publicar eventos no Redis;
* Enviar atualizações para o Dashboard via WebSocket.

**Tecnologias:**

* Node.js
* Express
* Redis
* Socket.io

---

### 🤖 worker.py

Motor de Inteligência Artificial.

**Função:**

* Escutar eventos enviados pelo Redis;
* Aplicar regras de negócio;
* Detectar anomalias;
* Acionar o agente de IA;
* Gerar recomendações automáticas.

**Tecnologias:**

* Python
* Redis
* LLM Pipeline

---

## 🚀 Como Executar

### 1. Subir o Redis

```bash
docker-compose up -d
```

### 2. Iniciar a API

```bash
npm install
npm start
```

Acesse:

```text
http://localhost:3000
```

### 3. Iniciar o Worker de IA

```bash
pip install -r requirements.txt
python worker.py
```

---

## 🧪 Teste de Telemetria

### Operação Normal

```bash
curl -X POST http://localhost:3000/api/webhook/telemetria \
-H "Content-Type: application/json" \
-d '{"truckId":"MNGT-001","cargo":"Tijolos","temperature":22.5,"status":"No Prazo"}'
```

### Anomalia Crítica

```bash
curl -X POST http://localhost:3000/api/webhook/telemetria \
-H "Content-Type: application/json" \
-d '{"truckId":"MNGT-002","cargo":"Cimento Usinado","temperature":32.1,"status":"No Prazo"}'
```

---

## 🔥 Componentes Principais

| Arquivo    | Papel                     |
| ---------- | ------------------------- |
| server.js  | API Gateway               |
| worker.py  | Agente de IA              |
| Redis      | Message Broker            |
| index.html | Dashboard                 |
| Docker     | Infraestrutura            |
| Node.js    | Backend                   |
| Python     | Processamento Inteligente |

---

## 📈 Conceitos Demonstrados

* Microsserviços
* Arquitetura Orientada a Eventos
* Mensageria Assíncrona
* Redis Pub/Sub
* Integração com IA
* APIs REST
* WebSockets
* Docker
