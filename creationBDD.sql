CREATE DATABASE ROC CHARACTER SET "utf8mb4";
USE ROC;
CREATE TABLE USER (
	user_id integer,
    user_name varchar(40),
    user_email varchar(40),
    user_pwd varchar(40),
    PRIMARY KEY (user_id)
);
CREATE TABLE GOLF (
    golf_id integer,
    golf_name integer,
    golf_installday datetime,
    golf_watersaved float,
    PRIMARY KEY (golf_id)
);
CREATE TABLE WATER (
    water_id integer,
    water_day varchar(40),
    water_start float,
    golf_end float,
    PRIMARY KEY (water_id)
);
CREATE TABLE ARDUINO (
    arduino_id integer,
    arduino_ref varchar(40),
    arduino_latitude float,
    arduino_longitude float,
    arduino_battery float,
    PRIMARY KEY (arduino_id)
);
CREATE TABLE INFO (
	info_id integer AUTO_INCREMENT,
    info_type integer,
    info_arduino integer,
    info_value float,
    info_date datetime,
    PRIMARY KEY (info_id),
    CONSTRAINT fk_id_arduino FOREIGN KEY (info_arduino) REFERENCES ARDUINO(arduino_id)
);