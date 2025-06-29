
from gtts import gTTS
import io
import os

def gerar_audio(texto):
    """Gera áudio usando Google TTS"""
    try:
        # Remove emojis para o TTS funcionar melhor
        texto_limpo = ''.join(char for char in texto if ord(char) < 128)
        
        if not texto_limpo.strip():
            texto_limpo = "Oi meu amor, te amo muito!"
        
        tts = gTTS(text=texto_limpo, lang='pt', slow=False)
        
        # Salva temporariamente
        audio_path = 'temp_audio.mp3'
        tts.save(audio_path)
        
        print(f"Áudio gerado: {texto_limpo}")
        return audio_path
        
    except Exception as e:
        print(f"Erro no TTS: {e}")
        
        # Cria arquivo de áudio vazio em caso de erro
        with open('temp_audio.mp3', 'w') as f:
            f.write('')
        return 'temp_audio.mp3'
