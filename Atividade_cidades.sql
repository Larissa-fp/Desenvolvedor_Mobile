CREATE TABLE cidade (
	id INTEGER,
	nome TEXT,
	uf TEXT
);

INSERT INTO cidade (id, nome, uf) VALUES(1, "Porto Alegre", "RS");
INSERT INTO cidade (id, nome, uf) VALUES(2,"Passo Fundo", "RS");
INSERT INTO cidade (id, nome, uf) VALUES(3,"Marau", "RS");
INSERT INTO cidade (id, nome, uf) VALUES(4,"Ernestina", "RS");
INSERT INTO cidade (id, nome, uf) VALUES(5,"Não me toque", "RS");

UPDATE cidade
SET nome = "Vacaria"
WHERE id = 4

DELETE FROM cidade
WHERE id = 5
