
import requests
import base64
import time

def gerar_imagem(prompt):
    """Gera imagem usando Stable Horde API"""
    
    prompt_completo = f"beautiful anime girl Ayumi, 22 years old, long brown hair, {prompt}, high quality, detailed, anime style, NSFW"
    
    payload = {
        "prompt": prompt_completo,
        "params": {
            "width": 512,
            "height": 512,
            "sampler_name": "k_euler_a",
            "steps": 20,
            "cfg_scale": 7.5,
            "karras": True
        },
        "models": ["stable_diffusion"],
        "nsfw": True,
        "r2": True
    }
    
    try:
        print(f"Gerando imagem: {prompt_completo}")
        resposta = requests.post("https://stablehorde.net/api/v2/generate/async", json=payload, timeout=10)
        
        if resposta.status_code != 202:
            print(f"Erro na requisição: {resposta.text}")
            return "https://via.placeholder.com/512x512/FF69B4/FFFFFF?text=Ayumi+💋"
            
        req_id = resposta.json()['id']
        print(f"ID da requisição: {req_id}")
        
        # Espera a imagem ficar pronta
        timeout = 120
        start_time = time.time()
        
        while True:
            if time.time() - start_time > timeout:
                print("Timeout na geração de imagem")
                return "https://via.placeholder.com/512x512/FF69B4/FFFFFF?text=Ayumi+💋"
                
            check = requests.get(f"https://stablehorde.net/api/v2/generate/check/{req_id}", timeout=5)
            data = check.json()
            
            if data.get('done', False):
                if data.get('generations') and len(data['generations']) > 0:
                    img_base64 = data['generations'][0]['img']
                    
                    # Salva imagem temporariamente
                    img_bytes = base64.b64decode(img_base64)
                    with open('temp_image.jpg', 'wb') as f:
                        f.write(img_bytes)
                    
                    print("Imagem gerada com sucesso!")
                    return open('temp_image.jpg', 'rb')
                else:
                    print("Nenhuma imagem foi gerada")
                    return "https://via.placeholder.com/512x512/FF69B4/FFFFFF?text=Ayumi+💋"
                    
            time.sleep(5)
            
    except Exception as e:
        print(f"Erro na geração de imagem: {e}")
        return "https://via.placeholder.com/512x512/FF69B4/FFFFFF?text=Ayumi+💋"
