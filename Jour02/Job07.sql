CREATE DATABASE entreprise;

USE entreprise

CREATE TABLE employe (
id INT AUTO_INCREMENT PRIMARY KEY,
nom VARCHAR(255),
prenom VARCHAR(255),
salaire DECIMAL(10, 2),
id_service INT
);

INSERT INTO employe (nom, prenom, salaire, id_service)
VALUES
('Dupuis', 'Jean' , 3500, 1),
('Deschamps', 'Didier' , 2000, 2),
('Elfie', 'Eva', 7000, 1),
('Ferrara', 'Manuel', 1200, 3),
('Clara' , 'Morgane', 4000, 2);

SELECT * FROM employe
WHERE salaire > 3000;


CREATE TABLE service (
id INT AUTO_INCREMENT PRIMARY KEY,
nom VARCHAR(255)
);


INSERT INTO service (nom)
VALUES
('Comptabilité'),
('Marketing'),
('Communication');

