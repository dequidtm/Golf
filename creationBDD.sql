﻿CREATE DATABASE GOLF CHARACTER SET "utf8mb4";
USE GOLF;
CREATE TABLE CAPTEUR (
	ID_CAPTEUR VARCHAR(40),
    LOC_CAPTEUR VARCHAR(40),
    PRIMARY KEY (ID_CAPTEUR)
);
CREATE TABLE MESURE (
	DATE_MESURE DATETIME NOT NULL,
    ID_CAPTEUR VARCHAR(40),
    TEMPERATURE FLOAT,
    HUMIDITE_AIR FLOAT,
    HUMIDITE_SOL FLOAT,
    ARROSAGE VARCHAR(5),
    PRIMARY KEY (DATE_MESURE),
    CONSTRAINT fk_id_capteur FOREIGN KEY (ID_CAPTEUR) REFERENCES CAPTEUR(ID_CAPTEUR)
);