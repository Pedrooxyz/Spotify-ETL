CREATE TABLE PlaylistArtistTable (
    ID_Artista VARCHAR(50) PRIMARY KEY,
    Nome_Artista VARCHAR(500) NULL,
    Generos_Musicais VARCHAR(500) NULL, 
    Popularidade_Artista INT NULL,
    Seguidores BIGINT NULL

    ID_Musica VARCHAR(50) PRIMARY KEY, 
    Nome_Musica VARCHAR(255) NOT NULL,
    Nome_Album VARCHAR(255) NULL,
    Duracao_Min NVARCHAR(10) NULL,
    Popularidade_Musica INT NULL,
    Data_do_Album DATE NULL,          
    Adicionado_a TIMESTAMP NULL,      
    Cantores VARCHAR(500) NULL  
);