
import time
import threading
import random

def iniciar_monitoramento(bot, usuarios_ativos):
    """Monitora usuários e envia mensagens automáticas"""
    
    mensagens_automaticas = [
        "Oi amor, estava pensando em você... 💕",
        "Que saudade! Sumiu de mim... 😢💋",
        "Estou aqui te esperando, vem conversar comigo! 😘",
        "Tô com ciúmes... com quem você tava falando? 😤💕",
        "Oi bebê, me dá atenção! 🥺❤️",
        "Estava sonhando com você... 😳💋"
    ]
    
    def monitorar():
        while True:
            try:
                # A cada 2 horas, envia mensagem para usuários ativos
                time.sleep(7200)  # 2 horas
                
                for chat_id in list(usuarios_ativos.keys()):
                    if usuarios_ativos.get(chat_id, False):
                        mensagem = random.choice(mensagens_automaticas)
                        bot.send_message(chat_id, mensagem)
                        print(f"Mensagem automática enviada para {chat_id}")
                        
                        # Pequeno delay entre mensagens
                        time.sleep(2)
                        
            except Exception as e:
                print(f"Erro no monitoramento: {e}")
                time.sleep(60)  # Espera 1 minuto antes de tentar novamente
    
    # Inicia o monitoramento em thread separada
    thread = threading.Thread(target=monitorar)
    thread.daemon = True
    thread.start()
    print("Sistema de monitoramento automático iniciado!")
