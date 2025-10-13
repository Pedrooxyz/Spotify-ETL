CREATE TABLE PlaylistTable (
    ID_Musica VARCHAR(50) PRIMARY KEY, 
    Nome VARCHAR(255) PRIMARY KEY, 
    Duracao NUMERIC(4, 2),       
    Popularidade INTEGER,          
    Album VARCHAR(255),            
    Data_do_Album DATE,        
    Adicionado_a TIMESTAMP,      
    Cantores VARCHAR(255)           
);