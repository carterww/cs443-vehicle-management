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
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2022-11-10 21:30:31.399013'),(2,'auth','0001_initial','2022-11-10 21:30:31.672013'),(3,'admin','0001_initial','2022-11-10 21:30:31.740014'),(4,'admin','0002_logentry_remove_auto_add','2022-11-10 21:30:31.746015'),(5,'admin','0003_logentry_add_action_flag_choices','2022-11-10 21:30:31.752016'),(6,'contenttypes','0002_remove_content_type_name','2022-11-10 21:30:31.789014'),(7,'auth','0002_alter_permission_name_max_length','2022-11-10 21:30:31.816013'),(8,'auth','0003_alter_user_email_max_length','2022-11-10 21:30:31.831014'),(9,'auth','0004_alter_user_username_opts','2022-11-10 21:30:31.837013'),(10,'auth','0005_alter_user_last_login_null','2022-11-10 21:30:31.867013'),(11,'auth','0006_require_contenttypes_0002','2022-11-10 21:30:31.870015'),(12,'auth','0007_alter_validators_add_error_messages','2022-11-10 21:30:31.877015'),(13,'auth','0008_alter_user_username_max_length','2022-11-10 21:30:31.915014'),(14,'auth','0009_alter_user_last_name_max_length','2022-11-10 21:30:31.971014'),(15,'auth','0010_alter_group_name_max_length','2022-11-10 21:30:31.986015'),(16,'auth','0011_update_proxy_permissions','2022-11-10 21:30:31.993015'),(17,'auth','0012_alter_user_first_name_max_length','2022-11-10 21:30:32.034015'),(18,'sessions','0001_initial','2022-11-10 21:30:32.065015'),(19,'vehiclemanagement','0001_initial','2022-11-10 22:03:47.188691'),(20,'vehiclemanagement','0002_department_vehicle_vehiclemodel_car_truck_and_more','2022-11-10 22:48:00.914691'),(21,'vehiclemanagement','0003_alter_employee_user','2022-11-14 21:58:14.614514'),(22,'vehiclemanagement','0004_vehicle_image_alter_employee_phone_number','2022-11-15 00:58:02.532025'),(23,'vehiclemanagement','0005_alter_vehicle_image','2022-11-15 01:13:55.775668'),(24,'vehiclemanagement','0006_rename_vehilce_type_vehiclemodel_vehicle_type','2022-11-15 01:24:38.731903'),(25,'vehiclemanagement','0007_remove_car_trunk_area_remove_truck_number_of_axles_and_more','2022-11-16 05:10:14.969930'),(26,'vehiclemanagement','0008_alter_vehiclesale_sale_date','2022-11-17 20:28:56.222501');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
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
