SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

DROP TABLE IF EXISTS PlantOwnership;
DROP TABLE IF EXISTS WaterEvent;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Plant;
DROP TABLE IF EXISTS Location;
DROP TABLE IF EXISTS PlantType;


/* Keeps track of each location on campus where a plant could be at */
CREATE TABLE Location(
	locationID int NOT NULL AUTO_INCREMENT,
	building text NOT NULL,
	area text NOT NULL, /*Should be a room number, a hallroom or etc. */
	PRIMARY KEY(locationID)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

/* The type of each plant in the datatype */
CREATE TABLE PlantType(
	ID int NOT NULL AUTO_INCREMENT,
	name text NOT NULL,
	thirst int, /* How many times a mounth a plant needs to be watered */
	PRIMARY KEY(ID)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Keeps track of each plant in the database */
CREATE TABLE Plant (
  plantID int NOT NULL AUTO_INCREMENT,
  plantType int NOT NULL,
  locationID int,
  plantName text,
  PRIMARY KEY(plantID),
  FOREIGN KEY(locationID) REFERENCES Location(locationID) ON DELETE CASCADE,
  FOREIGN KEY(plantType) REFERENCES PlantType(ID) ON DELETE CASCADE
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*The creditials of the user */
CREATE TABLE Users(
	userID int NOT NULL,
	name text NOT NULL,
	phoneNumber char(10) NOT NULL,
	role enum('User','Admin', 'Creator') default 'User',
	PRIMARY KEY(userID)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Tracks the time and date a user watered a plant */
CREATE TABLE WaterEvent(
	waterID int NOT NULL AUTO_INCREMENT,
	plantID int NOT NULL,
	userID int NOT NULL,
	timeWatered TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY(waterID, plantID),
	FOREIGN KEY(plantID) REFERENCES Plant(plantID) ON DELETE CASCADE,
	FOREIGN KEY(userID) REFERENCES Users(userID) ON DELETE CASCADE
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Relationship between a person and a plant */
CREATE TABLE PlantOwnership(
	userID int NOT NULL,
	plantID int NOT NULL,
	PRIMARY KEY(userID, plantID),
	FOREIGN KEY(userID) REFERENCES Users(userID) ON DELETE CASCADE,
	FOREIGN KEY(plantID) REFERENCES Plant(plantID) ON DELETE CASCADE
)ENGINE=InnoDB DEFAULT CHARSET=latin1;




INSERT INTO PlantType(name,thirst)
	VALUES("Fern",10);

INSERT INTO PlantType(name,thirst)
	VALUES("tree1",2);

INSERT INTO PlantType(name,thirst)
	VALUES("tree1",20);

/* Insert test values */
INSERT INTO Location(Building,Area)
	VALUES("Herak","Room 324");

INSERT INTO Location(Building,Area)
	VALUES("PACCAR","Hallway by Tadrous's office");

INSERT INTO Plant(locationID,plantName,plantType)
	VALUES(1,"Fern",2);
INSERT INTO Plant(locationID, plantName,plantType)
	VALUES(2, "Botany",3);

INSERT INTO Users VALUES
	(48755,"Maxwell Dulin","3605085170","User");

INSERT INTO WaterEvent(plantID,userID)
	VALUES(1,48755);

INSERT INTO PlantOwnership VALUES
	(48755,1);
