import redis
import json
import time

def chamar_agente_llm(truck_id, cargo, issue):
    """
    Este é o MOCK (Simulação) do Pipeline de IA.
    Na entrevista diga: "Aqui é onde eu bateria na API da OpenAI (LLM) 
    passando o contexto da anomalia para gerar um plano de ação automatizado."
    """
    print(f"🤖 [Agente IA] Gerando plano de ação via LLM para o incidente: {issue}...")
    time.sleep(2) # Simula o delay de 2 segundos que as APIs de IA costumam ter
    
    if "Temperatura" in issue:
        return f"AÇÃO RECOMENDADA PELO LLM: Bloquear descarga no galpão. O material '{cargo}' passou do limite térmico e pode comprometer a estrutura. Redirecionar para área de quarentena e acionar a seguradora."
    elif "Atraso" in issue:
        return f"AÇÃO RECOMENDADA PELO LLM: O atraso do '{cargo}' vai paralisar a concretagem. Recalcular cronograma do MS Project automaticamente e realocar a equipe de pedreiros para o setor Sul."
    
    return "AÇÃO RECOMENDADA: Monitorar."

def worker_automacao_operacional():
    print("🧠 [Worker Python] Ativado. Escutando barramento de dados e operando Pipeline de IA...")
    
    r = redis.Redis(host='localhost', port=6379, db=0)
    pubsub = r.pubsub()
    pubsub.subscribe('logistics_raw')
    
    for message in pubsub.listen():
        if message['type'] == 'message':
            try:
                data = json.loads(message['data'].decode('utf-8'))
                truck_id = data['truckId']
                cargo = data['cargo']
                temp = float(data['temperature'])
                status = data['status']
                
                alert_msg = None
                
                # Regras Operacionais (Trigger para a IA)
                if cargo == 'Cimento Usinado' and temp > 30.0:
                    alert_msg = f"Temperatura Crítica: {temp}°C."
                elif status == 'Atrasado':
                    alert_msg = f"Status Crítico: Atraso na Rota."
                
                # Se detectou anomalia, aciona o Agente de IA (Pipeline LLM)
                if alert_msg:
                    print(f"⚠️ Anomalia detectada no {truck_id}. Acionando LLM...")
                    
                    # Chamada ao nosso Agente IA
                    plano_acao_llm = chamar_agente_llm(truck_id, cargo, alert_msg)
                    
                    # Monta o payload final (Dados + Resposta da IA)
                    insight_payload = {
                        "truckId": truck_id,
                        "issue": alert_msg,
                        "ai_recommendation": plano_acao_llm
                    }
                    
                    # Devolve para o Node.js via Redis
                    r.publish('logistics_insights', json.dumps(insight_payload))
                    print(f"✅ Insight gerado e devolvido ao Gateway.")
                    
            except Exception as e:
                print(f"Erro no pipeline: {e}")

if __name__ == '__main__':
    worker_automacao_operacional()