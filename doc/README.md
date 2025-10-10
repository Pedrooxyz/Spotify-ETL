# Spotify ETL - Integração de Sistemas de Informação

Este projeto tem como objetivo demonstrar um processo completo de ETL (Extract, Transform, Load) utilizando dados do Spotify. O trabalho foi desenvolvido no âmbito da disciplina **Integração de Sistemas de Informação (ISI)**.

## Objetivo
- Extrair dados de APIs do Spotify sobre músicas, artistas e playlists.
- Transformar os dados para limpeza, normalização e agregação.
- Carregar os dados num formato estruturado, pronto para análise ou visualização.
- Explorar conceitos de integração de sistemas e boas práticas de ETL.

---

## Ferramentas Utilizadas
- **[Knime](https://www.knime.com/)** - para desenvolvimento do workflow ETL.
- **[Spotify Web API](https://developer.spotify.com/documentation/web-api/)** - para extração de dados.

## Estrutura do Repositório
tp01-12345/
├── README.md
├── doc/
├── dataint/
│   └── Spotify-ETL/
├── data/
│   ├── input/
│   └── output/
└── src/

---

## Como Executar

Para garantir o sucesso da extração de dados da API do Spotify, siga os seguintes passos de configuração e autenticação:

### Passo 1: Obter as Credenciais da API

O *workflow* utiliza a autenticação **Client Credentials Flow**. Para tal, é essencial obter as credenciais:

1.  Crie uma conta no **[Spotify for Developers](https://developer.spotify.com/)**.
2.  Crie uma nova aplicação para obter o seu **Client ID** e o **Client Secret**.

### Passo 2: Configurar o Ficheiro `credentials.txt`

O *workflow* lê a chave de autenticação a partir do ficheiro **`data/input/credentials.txt`**. Existem duas formas de inserir as credenciais necessárias:

#### Opção A: Executar o Script de Auxílio (Recomendado)

Esta opção é a forma mais simples, pois o *script* faz a codificação Base64 e escreve no ficheiro automaticamente.

1.  Abra a consola (CMD/Terminal) na pasta `[O seu workspace]\tp01-27960\src\`.
2.  Execute o ficheiro **`spotify_auth_encoder.py`**, passando o seu Client ID e Client Secret como argumentos:

    ```bash
    python spotify_auth_encoder.py <Client ID> <Client Secret>
    ```

    O *script* irá gerar a *string* **Base64** e **automaticamente escrever a chave** no ficheiro `credentials.txt`.

#### Opção B: Inserção Manual

Se preferir inserir manualmente, edite o ficheiro **`data/input/credentials.txt`** e substitua os *placeholders*.

1.  Codifique a *string* `Client ID:Client Secret` em Base64 externamente.
2.  Edite o ficheiro e insira a chave de autorização e o URL da playlist:

    ```txt
    AUTHORIZATION_HEADER=Basic [SUA_CHAVE_BASE64]
    PLAYLIST_URL=[LINK_COMPLETO_DA_PLAYLIST_A_PROCESSAR]
    ```

### Passo 3: Definir a Playlist Alvo (Ficheiro `playlist_link.txt`)

Para que o ETL saiba qual playlist extrair, o URL deve ser inserido no ficheiro `playlist_link.txt`.

1.  Edite o ficheiro **`data/input/playlist_link.txt`**.
2.  Insira apenas o **URL completo** da playlist que deseja processar.

    > **NOTA IMPORTANTE:** O *workflow* requer playlists com um criador utilizador. **Não utilize playlists automáticas** geradas pelo Spotify (ex: "Daily Mix", "Radar de Novidades").

### Passo 4: Executar o Workflow

1.  Abra o *workflow* no **KNIME**.
2.  Execute o *workflow* para iniciar o processo ETL.

---

## Autor
Pedro – Aluno de Engenharia de Sistemas Informáticos, Disciplina ISI

## Referências
- [Knime Documentation](https://docs.knime.com/)
- [Spotify Web API](https://developer.spotify.com/documentation/web-api/)
