import os
from tqdm import tqdm

def buscar_arquivos_por_tags(diretorio_base, tags_procuradas):
    arquivos_encontrados = []

    # Converter todas as tags para minúsculas para busca insensível a maiúsculas
    tags_procuradas = [tag.lower().strip() for tag in tags_procuradas]
    
    # Prefixo da tag que você está procurando (#TAG:)
    prefixo_tag = "#tag:"

    total_arquivos = sum(len(files) for _, _, files in os.walk(diretorio_base))
    with tqdm(total=total_arquivos, desc="Procurando arquivos", unit="arquivo") as barra:
        for root, dirs, files in os.walk(diretorio_base):
            for file in files:
                if file.endswith(".py"):
                    caminho_completo = os.path.join(root, file)

                    try:
                        with open(caminho_completo, 'r', encoding='utf-8') as f:
                            for line in f:
                                conteudo = line.lower()  # Verifica linha a linha, insensível a maiúsculas
                                # Verificar se a linha contém o prefixo e qualquer uma das tags procuradas
                                if prefixo_tag in conteudo:
                                    for tag in tags_procuradas:
                                        if f"{prefixo_tag} {tag}" in conteudo:
                                            arquivos_encontrados.append(caminho_completo)
                                            break  # Evita adicionar o mesmo arquivo várias vezes
                    except Exception as e:
                        print(f"Erro ao ler o arquivo {caminho_completo}: {e}")
                barra.update(1)  # Atualiza a barra de progresso

    return arquivos_encontrados

# Interação com o usuário
diretorio = input("Digite o caminho do diretório onde estão seus arquivos Python: ").strip()
tags_input = input("Digite as tags que deseja procurar, separadas por vírgulas: ").strip()
tags = [tag.strip() for tag in tags_input.split(",")]  # Separa e remove espaços desnecessários

resultados = buscar_arquivos_por_tags(diretorio, tags)

# Exibição dos resultados
if resultados:
    print(f"\nArquivos encontrados com as tags: {', '.join(tags)}")
    for arquivo in resultados:
        print(arquivo)
else:
    print(f"\nNenhum arquivo encontrado com as tags: {', '.join(tags)}.")
