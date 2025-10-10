# Spotify ETL - Integração de Sistemas de Informação

Este projeto tem como objetivo demonstrar um processo completo de ETL (Extract, Transform, Load) utilizando dados do Spotify. O trabalho foi desenvolvido no âmbito da disciplina **Integração de Sistemas de Informação (ISI)**.

## Objetivo
- Extrair dados de APIs do Spotify sobre músicas, artistas e playlists.
- Transformar os dados para limpeza, normalização e agregação.
- Carregar os dados num formato estruturado, pronto para análise ou visualização.
- Explorar conceitos de integração de sistemas e boas práticas de ETL.

## Ferramentas Utilizadas
- [Knime](https://www.knime.com/) - para desenvolvimento do workflow ETL.
- [Spotify Web API](https://developer.spotify.com/documentation/web-api/) - para extração de dados.

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

## Funcionalidades
- Extração de dados de playlists, artistas e faixas do Spotify.
- Transformações com limpeza, normalização, merges e validações.
- Exportação dos dados em formatos estruturados (CSV, JSON, etc.).
- Logging e monitorização do workflow.
- Possível integração com dashboards para visualização.

## Requisitos e Configuração do Ambiente

Este workflow do KNIME tem dependências externas para funcionar corretamente, incluindo extensões KNIME e um caminho de ficheiro específico para os dados. Siga os passos abaixo antes de executar o workflow principal.

### 1. Instalação das Extensões KNIME (Obrigatório)

O workflow utiliza um nó de scripting para a autenticação Base64 (Autorização **Basic**), o que requer as seguintes extensões:

* **KNIME Python Integration** (Versão 5.7.0 ou superior).
* **KNIME Conda Integration** (Versão 5.6.0 ou superior).

**Como Instalar:**

1.  No KNIME Analytics Platform, vá a **Menu** > **Install Extensions...**.
2.  Procure por **"python"**.
3.  **Selecione** os dois itens acima.
4.  Prossiga com a instalação e **reinicie** o KNIME.



## Autor
Pedro – Aluno de Engenharia de Sistemas Informáticos, Disciplina ISI

## Referências
- [Knime Documentation](https://docs.knime.com/)
- [Spotify Web API](https://developer.spotify.com/documentation/web-api/)
