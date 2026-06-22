# 🚛 LogisTrack - Event-Driven AI Pipeline

Sistema de monitoramento logístico baseado em eventos que utiliza Node.js, Redis, Python e Inteligência Artificial para detectar anomalias operacionais e gerar ações corretivas em tempo real.

## 🎯 Objetivo

Receber dados de telemetria de caminhões via API, processar eventos de forma assíncrona e utilizar um agente de IA para analisar situações críticas, como:

* Temperatura elevada de cargas sensíveis;
* Atrasos de entrega;
* Problemas operacionais;
* Alertas logísticos.

## 🏗️ Arquitetura

```text
Cliente / Webhook
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

## 📂 Estrutura dos Arquivos

```text
logistrack/
│
├── node_modules/         # Dependências instaladas pelo NPM (Node.js)
├── .gitignore            # Evita subir dependências e segredos para o GitHub
├── docker-compose.yml    # Infraestrutura (Sobe o Redis via Docker)
├── index.html            # Dashboard (Interface visual em tempo real)
├── package.json          # Lista dependências e scripts do projeto Node
├── package-lock.json     # Garante versões exatas das dependências
├── README.md             # Documentação do projeto
├── requirements.txt      # Dependências necessárias para o Worker Python
├── server.js             # API Gateway (Node, Express, Socket.io)
└── worker.py             # Motor de Inteligência Artificial (Escuta o Redis)
```

## 🚀 Como Executar

### 1. Subir a Infraestrutura (Redis)

```bash
docker-compose up -d
```

### 2. Iniciar a API (Gateway)

```bash
npm install
npm start
```

Acesse o dashboard em:

```text
http://localhost:3000
```

### 3. Iniciar o Worker de IA (Python)

```bash
pip install -r requirements.txt
python worker.py
```

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

## 🔥 Componentes Principais

| Componente       | Ferramenta        | Papel na Arquitetura                     |
| ---------------- | ----------------- | ---------------------------------------- |
| API Gateway      | Node.js + Express | Recebe webhooks e gerencia conexões.     |
| Message Broker   | Redis             | Fila de mensageria assíncrona (Buffer).  |
| Processamento IA | Python            | Aplica regras de negócio e aciona o LLM. |
| Front-end / UI   | HTML + Socket.io  | Dashboard em tempo real via WebSockets.  |
| Infraestrutura   | Docker            | Padronização do ambiente.                |

## 📈 Conceitos Demonstrados

* Microsserviços
* Arquitetura Orientada a Eventos
* Mensageria Assíncrona e Desacoplamento (Redis Pub/Sub)
* APIs REST
* WebSockets (Tempo Real)

```
```
