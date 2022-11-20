-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: vehicle_inventory
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `vehiclemanagement_vehicle`
--

DROP TABLE IF EXISTS `vehiclemanagement_vehicle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vehiclemanagement_vehicle` (
  `vin_number` varchar(17) NOT NULL,
  `price` decimal(11,2) NOT NULL,
  `color` varchar(255) NOT NULL,
  `trim_level` varchar(63) NOT NULL,
  `is_sold` tinyint(1) NOT NULL,
  `mpg` smallint NOT NULL,
  `mileage` int NOT NULL,
  `description` longtext NOT NULL,
  `vehicle_model_id` bigint NOT NULL,
  `image` longtext,
  PRIMARY KEY (`vin_number`),
  KEY `vehiclemanagement_ve_vehicle_model_id_68094d49_fk_vehiclema` (`vehicle_model_id`),
  CONSTRAINT `vehiclemanagement_ve_vehicle_model_id_68094d49_fk_vehiclema` FOREIGN KEY (`vehicle_model_id`) REFERENCES `vehiclemanagement_vehiclemodel` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehiclemanagement_vehicle`
--

LOCK TABLES `vehiclemanagement_vehicle` WRITE;
/*!40000 ALTER TABLE `vehiclemanagement_vehicle` DISABLE KEYS */;
INSERT INTO `vehiclemanagement_vehicle` VALUES ('1D7HA18D44J218509',22788.00,'white','CrewCab',0,19,144234,'Moderate Condition. Dent on front bumper.',2,'/media/4ca127c6bcca48f4aca75453dda444df.jpg'),('1HGEM21292L047875',14566.99,'gray','EX',1,27,122844,'Missing cylinder.',3,'/media/hondacrv2012idjasda.jpg'),('2G4WB54T1N1466114',39999.99,'blue','GT',0,25,90,'Fast.',4,'/media/2022-Ford-Mustang-GT-California-Special-Sealth-Edition-A_o.jpg'),('JH4KA3150JC014805',43999.00,'black','King',0,23,8795,'GM',5,'/media/gsgsdgsdgs_j6hwKyU.jpg'),('KNDPB3A23B7135414',17888.00,'red','S',0,30,35200,'Good condition',1,'/media/2015-Nissan-Altima-front-q-2.jpg');
/*!40000 ALTER TABLE `vehiclemanagement_vehicle` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-20 13:32:42
