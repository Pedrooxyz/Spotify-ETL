CREATE TABLE ArtistTable (
    ID_Artista VARCHAR(50) PRIMARY KEY, 
    Nome_Artista VARCHAR(255) NOT NULL,
    Generos_Musicais VARCHAR(500) NULL, 
    Popularidade_Artista INT NULL,
    Seguidores BIGINT NULL 
);