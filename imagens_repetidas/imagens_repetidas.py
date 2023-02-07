import os
from PIL import Image
from collections import defaultdict
import imagehash

def deletar_imagens_repetidas(caminho_pasta):
    
    todas_imagens = [os.path.join(caminho_pasta, imagem) for imagem in os.listdir(caminho_pasta) if imagem.endswith('.jpg') or imagem.endswith('.jpeg') or imagem.endswith('.png')]
    
    hashes_imagens = defaultdict(list)
    for caminho_imagem in todas_imagens:
        imagem = Image.open(caminho_imagem)
        hash = str(imagehash.phash(imagem))
        hashes_imagens[hash].append(caminho_imagem)
    
    imagens_repetidas = [imagens for imagens in hashes_imagens.values() if len(imagens) > 1]
    
    for imagens in imagens_repetidas:
        print(f'Imagem "{imagens[0]}" repetida {len(imagens)} vezes')
   
    if imagens_repetidas:
        resposta = input("Deseja deletar as imagens repetidas? (s/n) ")
        if resposta.lower() == 's':
            for imagens in imagens_repetidas:
                for imagem in imagens[1:]:
                    os.remove(imagem)
                    print(f'Imagem "{imagem}" deletada com sucesso.')
    else:
        print("Não possui imagens repetidas :)")

caminho_pasta = ''
deletar_imagens_repetidas(caminho_pasta)
