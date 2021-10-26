-- MySQL dump 10.13  Distrib 8.0.26, for Linux (x86_64)
--
-- Host: localhost    Database: bbke
-- ------------------------------------------------------
-- Server version	8.0.26-0ubuntu0.21.04.3

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `avail_service_at`
--

DROP TABLE IF EXISTS `avail_service_at`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `avail_service_at` (
  `customer_id` int DEFAULT NULL,
  `product_code` int DEFAULT NULL,
  `building_id` int DEFAULT NULL,
  `service_id` int DEFAULT NULL,
  `under_warranty` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `avail_service_at`
--

LOCK TABLES `avail_service_at` WRITE;
/*!40000 ALTER TABLE `avail_service_at` DISABLE KEYS */;
/*!40000 ALTER TABLE `avail_service_at` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `brands`
--

DROP TABLE IF EXISTS `brands`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `brands` (
  `brand_name` varchar(50) DEFAULT NULL,
  `founder` varchar(50) DEFAULT NULL,
  `ceo` varchar(50) DEFAULT NULL,
  `founding_date` date DEFAULT NULL,
  `yoy_growth` double DEFAULT NULL,
  `qoq_growth` double DEFAULT NULL,
  `market_share` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `brands`
--

LOCK TABLES `brands` WRITE;
/*!40000 ALTER TABLE `brands` DISABLE KEYS */;
INSERT INTO `brands` VALUES ('oneplus','Carl Pei','ABC','2011-09-09',4.5,6.5,3.5),('oppo','ABCD','ABCDE','2007-09-09',3,2.5,2.1),('vivo','no idea','also no idea','2008-03-06',2.5,4.5,1.4);
/*!40000 ALTER TABLE `brands` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `buildings`
--

DROP TABLE IF EXISTS `buildings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `buildings` (
  `id` int NOT NULL,
  `address` varchar(200) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `state` varchar(50) DEFAULT NULL,
  `country` varchar(50) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `buildings`
--

LOCK TABLES `buildings` WRITE;
/*!40000 ALTER TABLE `buildings` DISABLE KEYS */;
INSERT INTO `buildings` VALUES (123,'somewhere','city1','state1','country1','warehouse'),(124,'somewhere_else','city2','state1','country1','retail_store');
/*!40000 ALTER TABLE `buildings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `premium_customer` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `state` varchar(50) DEFAULT NULL,
  `country` varchar(50) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `age` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES (1,'Rohit','Sharma','Yes','Male','Mumbai','Maha','In','0000-00-00',32),(2,'Virat','Kohli','Yes','Male','Bangalore','Karnataka','In','0000-00-00',32),(3,'Mugun','Kottu','yes','Male','Chennai','Tamil Nadu','India','2002-08-22',19),(4,'Harry','Potter','yes','male','London','idk lol','England','1980-07-31',41),(5,'RJ','Lupin','yes','male','London','somewhere','england','1960-02-14',61),(6,'Remus','Lupin','n','male','dhwfh','akfhw','fwkgfuw','1945-12-10',75);
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `earphone`
--

DROP TABLE IF EXISTS `earphone`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `earphone` (
  `product_code` int NOT NULL,
  `buds_battery` int DEFAULT NULL,
  `case_battery` int DEFAULT NULL,
  `weight` int DEFAULT NULL,
  `driver_size` int DEFAULT NULL,
  `ip_rating` char(2) DEFAULT NULL,
  `total_battery` int DEFAULT NULL,
  `charging_time` int DEFAULT NULL,
  PRIMARY KEY (`product_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `earphone`
--

LOCK TABLES `earphone` WRITE;
/*!40000 ALTER TABLE `earphone` DISABLE KEYS */;
INSERT INTO `earphone` VALUES (8,4,16,40,6,'53',20,100);
/*!40000 ALTER TABLE `earphone` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employees` (
  `id` int NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `role` varchar(50) DEFAULT NULL,
  `team` varchar(50) DEFAULT NULL,
  `experience` int DEFAULT NULL,
  `salary` int DEFAULT NULL,
  `no_of_leaves_used` int DEFAULT NULL,
  `hours_spent_a_month` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` VALUES (123,'John','manager','r&d',10,100000,6,180),(124,'ABC','salesman','marketing',5,10000,6,180),(125,'XYZ','engineer','display',2,1000000,7,200),(4234,'harry','djwfbiw','fbcjh',4,345,0,0);
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `has_inventory`
--

DROP TABLE IF EXISTS `has_inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `has_inventory` (
  `building_id` int DEFAULT NULL,
  `product_id` int DEFAULT NULL,
  `part_id` int DEFAULT NULL,
  `inventory_count` int DEFAULT NULL,
  `inventory_type` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `has_inventory`
--

LOCK TABLES `has_inventory` WRITE;
/*!40000 ALTER TABLE `has_inventory` DISABLE KEYS */;
/*!40000 ALTER TABLE `has_inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `head_of`
--

DROP TABLE IF EXISTS `head_of`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `head_of` (
  `head_employee_id` int DEFAULT NULL,
  `sub_employee_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `head_of`
--

LOCK TABLES `head_of` WRITE;
/*!40000 ALTER TABLE `head_of` DISABLE KEYS */;
/*!40000 ALTER TABLE `head_of` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `headed_creation_of`
--

DROP TABLE IF EXISTS `headed_creation_of`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `headed_creation_of` (
  `employee_id` int DEFAULT NULL,
  `product_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `headed_creation_of`
--

LOCK TABLES `headed_creation_of` WRITE;
/*!40000 ALTER TABLE `headed_creation_of` DISABLE KEYS */;
/*!40000 ALTER TABLE `headed_creation_of` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `owns_a`
--

DROP TABLE IF EXISTS `owns_a`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `owns_a` (
  `customer_id` int DEFAULT NULL,
  `product_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `owns_a`
--

LOCK TABLES `owns_a` WRITE;
/*!40000 ALTER TABLE `owns_a` DISABLE KEYS */;
INSERT INTO `owns_a` VALUES (3,1);
/*!40000 ALTER TABLE `owns_a` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `parts`
--

DROP TABLE IF EXISTS `parts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `parts` (
  `id` int NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  `price` double DEFAULT NULL,
  `manufacturer` varchar(50) DEFAULT NULL,
  `year_of_release` varchar(50) DEFAULT NULL,
  `weekly_production` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parts`
--

LOCK TABLES `parts` WRITE;
/*!40000 ALTER TABLE `parts` DISABLE KEYS */;
/*!40000 ALTER TABLE `parts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `powerbank`
--

DROP TABLE IF EXISTS `powerbank`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `powerbank` (
  `product_code` int NOT NULL,
  `weight` int DEFAULT NULL,
  `ip_rating` char(2) DEFAULT NULL,
  `battery_size` int DEFAULT NULL,
  `charging_time` int DEFAULT NULL,
  `no_of_ports` int DEFAULT NULL,
  PRIMARY KEY (`product_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `powerbank`
--

LOCK TABLES `powerbank` WRITE;
/*!40000 ALTER TABLE `powerbank` DISABLE KEYS */;
INSERT INTO `powerbank` VALUES (9,300,NULL,10000,150,2);
/*!40000 ALTER TABLE `powerbank` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_of`
--

DROP TABLE IF EXISTS `product_of`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_of` (
  `product_id` int DEFAULT NULL,
  `brand_name` varchar(50) DEFAULT NULL,
  `sub_brand_name` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_of`
--

LOCK TABLES `product_of` WRITE;
/*!40000 ALTER TABLE `product_of` DISABLE KEYS */;
/*!40000 ALTER TABLE `product_of` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `code` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `cost` int DEFAULT NULL,
  `sales` int DEFAULT NULL,
  `profit` int DEFAULT NULL,
  `launch_date` date DEFAULT NULL,
  `weekly_production` int DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  `brand` varchar(50) DEFAULT NULL,
  `sub_brand` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,'Nord 2 5G',30000,1000000,5000,'2021-05-05',50000,'smartphone','oneplus','nord'),(2,'IQOO 7 5G',32000,1500000,3000,'2021-03-05',30000,'smartphone','vivo','iqoo'),(3,'Realme GT ME',28000,500000,3000,'2021-07-05',20000,'smartphone','oppo','realme'),(4,'X70 Pro',50000,100000,7000,'2021-09-05',10000,'smartphone','vivo',NULL),(5,'F19',20000,1000000,3000,'2021-01-05',20000,'smartphone','oppo',NULL),(6,'9R',40000,800000,6000,'2021-02-05',30000,'smartphone','oneplus',NULL),(7,'Dumb speaker',5000,100000,1000,'2021-06-06',5000,'speaker','oppo',NULL),(8,'Buds Air ANC',4500,300000,500,'2021-08-03',10000,'earphone','oppo','realme'),(9,'Powerbank 2',1200,200000,200,'2021-07-03',7000,'powerbank','oppo','realme');
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `retail_store`
--

DROP TABLE IF EXISTS `retail_store`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `retail_store` (
  `building_id` int NOT NULL,
  `avg_customers` int DEFAULT NULL,
  `avg_profit` int DEFAULT NULL,
  PRIMARY KEY (`building_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `retail_store`
--

LOCK TABLES `retail_store` WRITE;
/*!40000 ALTER TABLE `retail_store` DISABLE KEYS */;
/*!40000 ALTER TABLE `retail_store` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `review`
--

DROP TABLE IF EXISTS `review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `review` (
  `customer_id` int DEFAULT NULL,
  `product_id` int DEFAULT NULL,
  `review_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `review`
--

LOCK TABLES `review` WRITE;
/*!40000 ALTER TABLE `review` DISABLE KEYS */;
INSERT INTO `review` VALUES (3,1,4),(3,1,5);
/*!40000 ALTER TABLE `review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviews`
--

DROP TABLE IF EXISTS `reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reviews` (
  `id` int NOT NULL AUTO_INCREMENT,
  `stars` int DEFAULT NULL,
  `review` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviews`
--

LOCK TABLES `reviews` WRITE;
/*!40000 ALTER TABLE `reviews` DISABLE KEYS */;
INSERT INTO `reviews` VALUES (4,1,'fds fds'),(5,5,'Best Phone ever of 1990');
/*!40000 ALTER TABLE `reviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `services`
--

DROP TABLE IF EXISTS `services`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `services` (
  `id` int NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `price` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `services`
--

LOCK TABLES `services` WRITE;
/*!40000 ALTER TABLE `services` DISABLE KEYS */;
INSERT INTO `services` VALUES (123,'idklol',500);
/*!40000 ALTER TABLE `services` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `smartphone`
--

DROP TABLE IF EXISTS `smartphone`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `smartphone` (
  `code` int NOT NULL,
  `battery` int DEFAULT NULL,
  `main_cam_res` int DEFAULT NULL,
  `charger_wattage` int DEFAULT NULL,
  `weight` int DEFAULT NULL,
  `frame_material` varchar(50) DEFAULT NULL,
  `glass_spec` varchar(50) DEFAULT NULL,
  `soc` varchar(50) DEFAULT NULL,
  `ip_rating` char(2) DEFAULT NULL,
  `display` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `smartphone`
--

LOCK TABLES `smartphone` WRITE;
/*!40000 ALTER TABLE `smartphone` DISABLE KEYS */;
INSERT INTO `smartphone` VALUES (1,4500,50,65,196,'plastic','GorillaGlass6','Dimensity1200',NULL,'90hz 6.7 OLED'),(2,4500,50,66,190,'plastic','GorillaGlass5','SD 870',NULL,'120hz 6.7 OLED'),(3,4400,64,65,175,'plastic','GorillaGlass5','SD 778G',NULL,'120hz 6.4 OLED'),(4,4000,108,65,205,'aluminium','GorillaGlassVictus','SD 870','68','120hz 6.6 OLED'),(5,4200,64,30,160,'aluminium','GorillaGlass3','Dimensity800U',NULL,'60hz 6.3 OLED'),(6,4300,48,65,160,'aluminium','GorillaGlass6','SD 870',NULL,'120hz 6.6 OLED');
/*!40000 ALTER TABLE `smartphone` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `speaker`
--

DROP TABLE IF EXISTS `speaker`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `speaker` (
  `product_code` int NOT NULL,
  `battery_life` int DEFAULT NULL,
  `weight` int DEFAULT NULL,
  `ip_rating` char(2) DEFAULT NULL,
  `battery_size` int DEFAULT NULL,
  `output_power` int DEFAULT NULL,
  `driver_size` float DEFAULT NULL,
  PRIMARY KEY (`product_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `speaker`
--

LOCK TABLES `speaker` WRITE;
/*!40000 ALTER TABLE `speaker` DISABLE KEYS */;
INSERT INTO `speaker` VALUES (7,12,1600,'56',7000,10,4);
/*!40000 ALTER TABLE `speaker` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stock_of`
--

DROP TABLE IF EXISTS `stock_of`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stock_of` (
  `brand_name` varchar(50) NOT NULL,
  `yoy_growth` double DEFAULT NULL,
  `qoq_growth` double DEFAULT NULL,
  `stock_price` double DEFAULT NULL,
  PRIMARY KEY (`brand_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stock_of`
--

LOCK TABLES `stock_of` WRITE;
/*!40000 ALTER TABLE `stock_of` DISABLE KEYS */;
/*!40000 ALTER TABLE `stock_of` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sub_brands`
--

DROP TABLE IF EXISTS `sub_brands`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sub_brands` (
  `brand_name` varchar(50) DEFAULT NULL,
  `sub_brand_name` varchar(50) NOT NULL,
  `market_share` double DEFAULT NULL,
  `yoy_growth` double DEFAULT NULL,
  `qoq_growth` double DEFAULT NULL,
  `product_type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`sub_brand_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sub_brands`
--

LOCK TABLES `sub_brands` WRITE;
/*!40000 ALTER TABLE `sub_brands` DISABLE KEYS */;
INSERT INTO `sub_brands` VALUES ('Vivo','IQOO',5.6,2.3,3.4,'smartphones'),('Oppo','Realme',5.6,2.3,3.4,'ecosystem');
/*!40000 ALTER TABLE `sub_brands` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tv`
--

DROP TABLE IF EXISTS `tv`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tv` (
  `product_code` int NOT NULL,
  `dimensions` int DEFAULT NULL,
  `frame` varchar(50) DEFAULT NULL,
  `display` varchar(50) DEFAULT NULL,
  `soc` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`product_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tv`
--

LOCK TABLES `tv` WRITE;
/*!40000 ALTER TABLE `tv` DISABLE KEYS */;
/*!40000 ALTER TABLE `tv` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `uses_parts`
--

DROP TABLE IF EXISTS `uses_parts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `uses_parts` (
  `product_id` int DEFAULT NULL,
  `part_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `uses_parts`
--

LOCK TABLES `uses_parts` WRITE;
/*!40000 ALTER TABLE `uses_parts` DISABLE KEYS */;
/*!40000 ALTER TABLE `uses_parts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `warehouse`
--

DROP TABLE IF EXISTS `warehouse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `warehouse` (
  `building_id` int NOT NULL,
  `size` int DEFAULT NULL,
  `operational_costs` int DEFAULT NULL,
  `unused_space` int DEFAULT NULL,
  PRIMARY KEY (`building_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `warehouse`
--

LOCK TABLES `warehouse` WRITE;
/*!40000 ALTER TABLE `warehouse` DISABLE KEYS */;
/*!40000 ALTER TABLE `warehouse` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `works_on`
--

DROP TABLE IF EXISTS `works_on`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `works_on` (
  `employee_id` int DEFAULT NULL,
  `product_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `works_on`
--

LOCK TABLES `works_on` WRITE;
/*!40000 ALTER TABLE `works_on` DISABLE KEYS */;
/*!40000 ALTER TABLE `works_on` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `works_under`
--

DROP TABLE IF EXISTS `works_under`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `works_under` (
  `employee_id` int DEFAULT NULL,
  `brand_name` varchar(50) DEFAULT NULL,
  `sub_brand_name` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `works_under`
--

LOCK TABLES `works_under` WRITE;
/*!40000 ALTER TABLE `works_under` DISABLE KEYS */;
/*!40000 ALTER TABLE `works_under` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-26 12:23:46
