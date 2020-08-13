CREATE DATABASE `Exp` 

USE `Exp`;


DROP TABLE IF EXISTS `activity`;
CREATE TABLE `activity` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `INorOUT` varchar(50) NOT NULL,
  `cost` varchar(50) NOT NULL,
  `causale` varchar(50) NOT NULL,
  `data` date NOT NULL,
  `categoria` varchar(50) NOT NULL,
  `FK_userId` int(11) NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `FK_userId` (`FK_userId`),
  CONSTRAINT `FK_userId` FOREIGN KEY (`FK_userId`) REFERENCES `user` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS `fuel`;
CREATE TABLE `fuel` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `CostLit` varchar(50) NOT NULL,
  `cash` varchar(50) NOT NULL,
  `totKm` varchar(50) NOT NULL,
  `data` date NOT NULL,
  `FK_userId` int(11) NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `FK-userId` (`FK_userId`),
  CONSTRAINT `FK-userId` FOREIGN KEY (`FK_userId`) REFERENCES `user` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL,
  `cognome` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `psw` varchar(50) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

