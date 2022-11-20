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
-- Table structure for table `vehiclemanagement_employee`
--

DROP TABLE IF EXISTS `vehiclemanagement_employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vehiclemanagement_employee` (
  `user_id` int NOT NULL,
  `SSN` int NOT NULL,
  `birthday` date NOT NULL,
  `phone_number` bigint NOT NULL,
  `sex` varchar(1) NOT NULL,
  `salary` decimal(11,2) NOT NULL,
  `total_commissions` decimal(11,2) NOT NULL,
  `manager_id` int DEFAULT NULL,
  `employee_department_id` bigint DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `SSN` (`SSN`),
  UNIQUE KEY `phone_number` (`phone_number`),
  KEY `vehiclemanagement_em_manager_id_6c70c49f_fk_vehiclema` (`manager_id`),
  KEY `vehiclemanagement_em_employee_department__0514c416_fk_vehiclema` (`employee_department_id`),
  CONSTRAINT `vehiclemanagement_em_employee_department__0514c416_fk_vehiclema` FOREIGN KEY (`employee_department_id`) REFERENCES `vehiclemanagement_department` (`id`),
  CONSTRAINT `vehiclemanagement_em_manager_id_6c70c49f_fk_vehiclema` FOREIGN KEY (`manager_id`) REFERENCES `vehiclemanagement_employee` (`user_id`),
  CONSTRAINT `vehiclemanagement_employee_user_id_a872532a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehiclemanagement_employee`
--

LOCK TABLES `vehiclemanagement_employee` WRITE;
/*!40000 ALTER TABLE `vehiclemanagement_employee` DISABLE KEYS */;
INSERT INTO `vehiclemanagement_employee` VALUES (1,0,'2001-07-18',0,'M',135675.00,0.00,NULL,1),(3,5,'2022-11-14',5,'F',50000.00,0.00,1,1);
/*!40000 ALTER TABLE `vehiclemanagement_employee` ENABLE KEYS */;
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
