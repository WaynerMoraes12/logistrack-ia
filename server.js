const express = require('express');
const { createClient } = require('redis');
const http = require('http');
const { Server } = require('socket.io');
const path = require('path');

const app = express();
const server = http.createServer(app);
const io = new Server(server);

// Middleware para aceitar Webhooks em JSON
app.use(express.json());

const publisher = createClient({ url: 'redis://localhost:6379' });
const subscriber = createClient({ url: 'redis://localhost:6379' });

// Painel Visual
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

// API REST / Webhook: Recebe dados operacionais
app.post('/api/webhook/telemetria', async (req, res) => {
    const { truckId, cargo, temperature, status } = req.body;

    if (!truckId || !cargo || temperature === undefined) {
        return res.status(400).json({ error: 'Payload do webhook inválido.' });
    }

    const payload = JSON.stringify({ truckId, cargo, temperature, status, timestamp: new Date() });

    try {
        // Envia para o Redis de forma assíncrona
        await publisher.publish('logistics_raw', payload);
        io.emit('truck_update', JSON.parse(payload));
        
        return res.status(202).json({ message: 'Webhook recebido. Na fila para análise da IA.' });
    } catch (err) {
        console.error('Erro de I/O no Redis:', err);
        return res.status(500).json({ error: 'Falha no Broker.' });
    }
});

async function startGateway() {
    await publisher.connect();
    await subscriber.connect();
    console.log('🚧 [Gateway Node.js] Online e conectado ao Broker Redis.');

    // Escuta as respostas do Pipeline de IA (Python)
    await subscriber.subscribe('logistics_insights', (message) => {
        const aiData = JSON.parse(message);
        console.log(`🤖 [INSIGHT DA IA RECEBIDO]:`, aiData.truckId);
        // Emite para a tela em tempo real
        io.emit('ai_insight', aiData);
    });

    server.listen(3000, () => {
        console.log(`🚚 LogisTrack rodando na porta http://localhost:3000`);
    });
}

startGateway().catch(console.error);