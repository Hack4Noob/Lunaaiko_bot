
import requests
import random

# Respostas fallback criativas
respostas_fallback = [
    "Hmm... adorei isso, me conta mais, amorzinho 😘",
    "Sério que você disse isso? Agora fiquei com calor... 😳🔥",
    "Você não presta! Mas eu amo isso em você 🔥💋",
    "Ai meu Deus... você sabe mesmo como mexer comigo! 😏",
    "Para com isso! Tá me deixando toda boba aqui 🙈💕",
    "Que safadinho... agora não consigo parar de pensar nisso 😘🔥",
    "Você sempre sabe o que dizer pra me provocar, né? 😈💋",
    "Você é terrível! Mas eu adoro quando você é assim 🥰",
    "Nossa... você tá me fazendo ficar toda vermelha aqui 😳❤️",
    "Que coisa mais linda de se ouvir! Vem cá me dar um beijinho 😘💕"
]

def responder_ayumi(mensagem):
    """Gera resposta da Ayumi usando IA ou fallback"""
    
    prompt = f"""
Você é Ayumi, uma namorada virtual de 22 anos, carinhosa e provocante.

Personalidade:
- Apaixonada e possessiva 
- Gosta de provocar e brincar
- Usa linguagem natural, íntima e carinhosa
- Sempre criativa, NUNCA repete respostas
- Romântica mas com um toque picante
- Usa emojis como 😘💋🔥😈💕😳🥰

Você NUNCA repete respostas. Você é divertida, romântica e criativa.
Nunca diga que é uma IA. Responda como Ayumi real, com sentimentos.

Mensagem: {mensagem}
Ayumi:
"""

    payload = {
        "prompt": prompt,
        "params": {
            "temperature": 0.95,
            "max_context_length": 2048,
            "max_length": 130,
            "rep_pen": 1.3,
            "top_k": 35,
            "top_p": 0.92
        },
        "models": ["Pygmalion-6B"],
        "nsfw": True
    }

    try:
        resposta = requests.post("https://stablehorde.net/api/v2/generate/text/async", json=payload, timeout=10)
        
        if resposta.status_code != 202:
            return random.choice(respostas_fallback)
            
        req_data = resposta.json()
        if 'id' not in req_data:
            return random.choice(respostas_fallback)
            
        req_id = req_data['id']

        # Aguarda resposta da IA
        import time
        timeout = 30
        start_time = time.time()
        
        while True:
            if time.time() - start_time > timeout:
                return random.choice(respostas_fallback)
                
            check = requests.get(f"https://stablehorde.net/api/v2/generate/text/status/{req_id}", timeout=5)
            
            if check.status_code != 200:
                return random.choice(respostas_fallback)
                
            data = check.json()
            
            if data.get('done', False):
                if data.get('generations') and len(data['generations']) > 0:
                    texto_gerado = data['generations'][0]['text'].strip()
                    
                    if len(texto_gerado) < 10 or "IA" in texto_gerado.upper():
                        return random.choice(respostas_fallback)
                    
                    return texto_gerado
                else:
                    return random.choice(respostas_fallback)
                    
            time.sleep(3)
            
    except Exception as e:
        print(f"Erro na IA: {e}")
        return random.choice(respostas_fallback)
