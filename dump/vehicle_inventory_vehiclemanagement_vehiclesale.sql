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
-- Table structure for table `vehiclemanagement_vehiclesale`
--

DROP TABLE IF EXISTS `vehiclemanagement_vehiclesale`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vehiclemanagement_vehiclesale` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `sale_price` decimal(11,2) NOT NULL,
  `sale_date` date NOT NULL,
  `customer_id` int NOT NULL,
  `employee_id` int NOT NULL,
  `vehicle_id` varchar(17) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `vehiclemanagement_ve_customer_id_7255cd5c_fk_auth_user` (`customer_id`),
  KEY `vehiclemanagement_ve_employee_id_b6c983b9_fk_vehiclema` (`employee_id`),
  KEY `vehiclemanagement_ve_vehicle_id_966a0247_fk_vehiclema` (`vehicle_id`),
  KEY `vehiclemanagement_vehiclesale_sale_date_884fe914` (`sale_date`),
  CONSTRAINT `vehiclemanagement_ve_customer_id_7255cd5c_fk_auth_user` FOREIGN KEY (`customer_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `vehiclemanagement_ve_employee_id_b6c983b9_fk_vehiclema` FOREIGN KEY (`employee_id`) REFERENCES `vehiclemanagement_employee` (`user_id`),
  CONSTRAINT `vehiclemanagement_ve_vehicle_id_966a0247_fk_vehiclema` FOREIGN KEY (`vehicle_id`) REFERENCES `vehiclemanagement_vehicle` (`vin_number`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehiclemanagement_vehiclesale`
--

LOCK TABLES `vehiclemanagement_vehiclesale` WRITE;
/*!40000 ALTER TABLE `vehiclemanagement_vehiclesale` DISABLE KEYS */;
INSERT INTO `vehiclemanagement_vehiclesale` VALUES (1,14566.98,'2022-11-16',2,1,'1HGEM21292L047875');
/*!40000 ALTER TABLE `vehiclemanagement_vehiclesale` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-20 13:32:41
