import sys
import base64
import os

# Define o caminho de destino do ficheiro de credenciais
# Este é o caminho fornecido pelo utilizador: C:\Users\Pedro M Ribeiro\knime-workspace\tp01-27960\data\input\credentials.txt
CREDENTIALS_FILE_PATH = "..\\data\\input\\credentials.txt"

def encode_and_save_credentials():
    """
    Recebe o Client ID e Client Secret da linha de comando, 
    codifica-os em Base64 e escreve o header completo no ficheiro de credenciais.
    """
    
    if len(sys.argv) < 3:
        print("Uso correto: python spotify_auth_encoder.py <Client ID> <Client Secret>", file=sys.stderr)
        sys.exit(1)

    client_id = sys.argv[1]
    client_secret = sys.argv[2]
    
    credentials = f"{client_id}:{client_secret}"
    
    base64_bytes = base64.b64encode(credentials.encode('utf-8'))
    base64_string = base64_bytes.decode('utf-8')
    
    auth_header_value = f"{base64_string}"
    
    try:
        with open(CREDENTIALS_FILE_PATH, 'w', encoding='utf-8') as f:
            f.write(f"{auth_header_value}")
            print(f"Sucesso: O header de autenticação foi guardado em '{CREDENTIALS_FILE_PATH}'")
            
    except Exception as e:
        print(f"ERRO: Não foi possível escrever no ficheiro. Verifique o caminho ou permissões.\nDetalhe: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    encode_and_save_credentials()