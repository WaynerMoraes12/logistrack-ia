Markdown# 🚛 LogisTrack - Event-Driven AI Pipeline

Sistema de monitoramento logístico baseado em eventos que utiliza Node.js, Redis, Python e Inteligência Artificial para detectar anomalias operacionais e gerar ações corretivas em tempo real.

## 🎯 Objetivo

Receber dados de telemetria de caminhões via API, processar eventos de forma assíncrona e utilizar um agente de IA para analisar situações críticas, como:
* Temperatura elevada de cargas sensíveis;
* Atrasos de entrega;
* Problemas operacionais;
* Alertas logísticos.

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
📂 Estrutura dos ArquivosPlaintextlogistrack/
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
📦 node_modules/Contém todas as dependências instaladas pelo NPM.Função: Bibliotecas utilizadas pelo servidor Node.js.🚫 .gitignoreDefine quais arquivos não serão enviados para o GitHub.Função: Evitar subir dependências, arquivos temporários e segredos.🐳 docker-compose.ymlArquivo responsável por subir o Redis automaticamente usando Docker.Função: Infraestrutura do sistema.🌐 index.htmlDashboard simples exibido no navegador.Função: Interface visual para acompanhar os eventos e respostas da IA em tempo real.📦 package.json e package-lock.jsonArquivos principais do projeto Node.js.Função: Lista dependências, define scripts de execução e garante versões exatas das bibliotecas.📄 README.mdDocumentação do projeto.Função: Explicar arquitetura, instalação e funcionamento.🐍 requirements.txtLista das dependências Python.Função: Instalar bibliotecas necessárias para o Worker de IA.🚀 server.jsAPI Gateway do sistema.Função: Receber webhooks, expor endpoints REST, publicar eventos no Redis e enviar atualizações para o Dashboard via WebSocket.Tecnologias: Node.js, Express, Redis, Socket.io.🤖 worker.pyMotor de Inteligência Artificial.Função: Escutar eventos enviados pelo Redis, aplicar regras de negócio, detectar anomalias, acionar o agente de IA e gerar recomendações automáticas.Tecnologias: Python, Redis, LLM Pipeline.🚀 Como Executar1. Subir o RedisBashdocker-compose up -d
2. Iniciar a API (Gateway)Bashnpm install
npm start
Acesse o dashboard em: http://localhost:30003. Iniciar o Worker de IAAbra um novo terminal e execute:Bashpip install -r requirements.txt
python worker.py
🧪 Teste de TelemetriaOperação NormalBashcurl -X POST http://localhost:3000/api/webhook/telemetria \
-H "Content-Type: application/json" \
-d '{"truckId":"MNGT-001","cargo":"Tijolos","temperature":22.5,"status":"No Prazo"}'
Anomalia CríticaBashcurl -X POST http://localhost:3000/api/webhook/telemetria \
-H "Content-Type: application/json" \
-d '{"truckId":"MNGT-002","cargo":"Cimento Usinado","temperature":32.1,"status":"No Prazo"}'
🔥 Componentes PrincipaisArquivo/ComponentePapel no SistemaTecnologia Principalserver.jsAPI GatewayNode.jsworker.pyAgente de IAPythonRedisMessage BrokerRedisindex.htmlDashboardHTML/JSDockerInfraestruturaDocker📈 Conceitos DemonstradosMicrosserviçosArquitetura Orientada a EventosMensageria Assíncrona (Redis Pub/Sub)Integração com IA (LLM Pipelines)APIs REST e WebhooksWebSockets (Tempo Real)Docker
