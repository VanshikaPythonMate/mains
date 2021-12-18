-- MySQL dump 10.19  Distrib 10.3.31-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: mainsias1
-- ------------------------------------------------------
-- Server version	10.3.31-MariaDB-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_api_user`
--

DROP TABLE IF EXISTS `auth_api_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_api_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `isAdmin` tinyint(1) NOT NULL,
  `isManager` tinyint(1) NOT NULL,
  `isStudent` tinyint(1) NOT NULL,
  `isTeacher` tinyint(1) NOT NULL,
  `isVerified` tinyint(1) NOT NULL,
  `defaultExam` varchar(30) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `email` varchar(254) NOT NULL,
  `created_by_id` int(11) DEFAULT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `can_create_subscription` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `auth_api_user_created_by_id_0a108862_fk_auth_api_user_id` (`created_by_id`),
  CONSTRAINT `auth_api_user_created_by_id_0a108862_fk_auth_api_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_api_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_api_user`
--

LOCK TABLES `auth_api_user` WRITE;
/*!40000 ALTER TABLE `auth_api_user` DISABLE KEYS */;
INSERT INTO `auth_api_user` VALUES (1,'pbkdf2_sha256$216000$5EZkbKQkupCe$+c1nZn/lpQ4kbH52FO0VgGkZSQC7ZdGts1Et06N9hSQ=',NULL,1,'admin','user',1,1,'2021-11-07 11:01:11.000000',1,0,0,0,1,'None','images/profile/Screenshot_2021-11-08_at_1.48.16_AM.png','234234234','admin@mainsias.com',1,'Male',1),(2,'pbkdf2_sha256$216000$NITiGX5Nt6m5$eMWlAPljrG676P2iDTA84jBoCujdaiW4YDQXLkVnahs=','2021-11-07 11:04:00.863973',1,'','',1,1,'2021-11-07 11:01:45.316375',0,0,0,0,1,NULL,'',NULL,'mohit@worksnet.in',NULL,NULL,0),(9,'pbkdf2_sha256$216000$3eKAsSVAE01S$kpcxfMxciXpmIx+U1FbftPBPWHVFjpIZ15aODD6IFqI=',NULL,0,'Domey','User',0,1,'2021-11-07 20:10:15.684917',0,0,1,0,1,NULL,'',NULL,'domeyuser@gmail.com',NULL,NULL,0),(10,'pbkdf2_sha256$216000$JdGPThXNBlEz$y+YYC5M7xUfDKkmI6X8XEgE/01k08ihcNcUs+HVZqUQ=',NULL,0,'Test','Manager',0,1,'2021-11-08 06:04:26.583737',0,1,0,0,1,'True','','23423423423','manager@hello.com',NULL,NULL,1);
/*!40000 ALTER TABLE `auth_api_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_api_user_groups`
--

DROP TABLE IF EXISTS `auth_api_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_api_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_api_user_groups_user_id_group_id_367034cc_uniq` (`user_id`,`group_id`),
  KEY `auth_api_user_groups_group_id_f3134bb3_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_api_user_groups_group_id_f3134bb3_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_api_user_groups_user_id_09902e42_fk_auth_api_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_api_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_api_user_groups`
--

LOCK TABLES `auth_api_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_api_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_api_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_api_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_api_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_api_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_api_user_user_permi_user_id_permission_id_d9204bb8_uniq` (`user_id`,`permission_id`),
  KEY `auth_api_user_user_p_permission_id_fddfd460_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_api_user_user_p_permission_id_fddfd460_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_api_user_user_p_user_id_ad33a4f7_fk_auth_api_` FOREIGN KEY (`user_id`) REFERENCES `auth_api_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_api_user_user_permissions`
--

LOCK TABLES `auth_api_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_api_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_api_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_api_verificationotp`
--

DROP TABLE IF EXISTS `auth_api_verificationotp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_api_verificationotp` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `otp` longtext DEFAULT NULL,
  `reason` varchar(256) DEFAULT NULL,
  `date_time` datetime(6) NOT NULL,
  `date_time_expiry` datetime(6) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `auth_api_verificationotp_user_id_fffb768e_fk_auth_api_user_id` (`user_id`),
  CONSTRAINT `auth_api_verificationotp_user_id_fffb768e_fk_auth_api_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_api_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_api_verificationotp`
--

LOCK TABLES `auth_api_verificationotp` WRITE;
/*!40000 ALTER TABLE `auth_api_verificationotp` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_api_verificationotp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=109 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add notice board',1,'add_noticeboard'),(2,'Can change notice board',1,'change_noticeboard'),(3,'Can delete notice board',1,'delete_noticeboard'),(4,'Can view notice board',1,'view_noticeboard'),(5,'Can add termsn conditions',2,'add_termsnconditions'),(6,'Can change termsn conditions',2,'change_termsnconditions'),(7,'Can delete termsn conditions',2,'delete_termsnconditions'),(8,'Can view termsn conditions',2,'view_termsnconditions'),(9,'Can add exam',3,'add_exam'),(10,'Can change exam',3,'change_exam'),(11,'Can delete exam',3,'delete_exam'),(12,'Can view exam',3,'view_exam'),(13,'Can add exam manager relation',4,'add_exammanagerrelation'),(14,'Can change exam manager relation',4,'change_exammanagerrelation'),(15,'Can delete exam manager relation',4,'delete_exammanagerrelation'),(16,'Can view exam manager relation',4,'view_exammanagerrelation'),(17,'Can add student subscription record',5,'add_studentsubscriptionrecord'),(18,'Can change student subscription record',5,'change_studentsubscriptionrecord'),(19,'Can delete student subscription record',5,'delete_studentsubscriptionrecord'),(20,'Can view student subscription record',5,'view_studentsubscriptionrecord'),(21,'Can add student subscriptions questions record',6,'add_studentsubscriptionsquestionsrecord'),(22,'Can change student subscriptions questions record',6,'change_studentsubscriptionsquestionsrecord'),(23,'Can delete student subscriptions questions record',6,'delete_studentsubscriptionsquestionsrecord'),(24,'Can view student subscriptions questions record',6,'view_studentsubscriptionsquestionsrecord'),(25,'Can add evaluator payment details',7,'add_evaluatorpaymentdetails'),(26,'Can change evaluator payment details',7,'change_evaluatorpaymentdetails'),(27,'Can delete evaluator payment details',7,'delete_evaluatorpaymentdetails'),(28,'Can view evaluator payment details',7,'view_evaluatorpaymentdetails'),(29,'Can add evaluator glance',8,'add_evaluatorglance'),(30,'Can change evaluator glance',8,'change_evaluatorglance'),(31,'Can delete evaluator glance',8,'delete_evaluatorglance'),(32,'Can view evaluator glance',8,'view_evaluatorglance'),(33,'Can add glance evaluations record',9,'add_glanceevaluationsrecord'),(34,'Can change glance evaluations record',9,'change_glanceevaluationsrecord'),(35,'Can delete glance evaluations record',9,'delete_glanceevaluationsrecord'),(36,'Can view glance evaluations record',9,'view_glanceevaluationsrecord'),(37,'Can add evaluator rating',10,'add_evaluatorrating'),(38,'Can change evaluator rating',10,'change_evaluatorrating'),(39,'Can delete evaluator rating',10,'delete_evaluatorrating'),(40,'Can view evaluator rating',10,'view_evaluatorrating'),(41,'Can add evaluator category pricing',11,'add_evaluatorcategorypricing'),(42,'Can change evaluator category pricing',11,'change_evaluatorcategorypricing'),(43,'Can delete evaluator category pricing',11,'delete_evaluatorcategorypricing'),(44,'Can view evaluator category pricing',11,'view_evaluatorcategorypricing'),(45,'Can add about manager',12,'add_aboutmanager'),(46,'Can change about manager',12,'change_aboutmanager'),(47,'Can delete about manager',12,'delete_aboutmanager'),(48,'Can view about manager',12,'view_aboutmanager'),(49,'Can add user',13,'add_user'),(50,'Can change user',13,'change_user'),(51,'Can delete user',13,'delete_user'),(52,'Can view user',13,'view_user'),(53,'Can add verification otp',14,'add_verificationotp'),(54,'Can change verification otp',14,'change_verificationotp'),(55,'Can delete verification otp',14,'delete_verificationotp'),(56,'Can view verification otp',14,'view_verificationotp'),(57,'Can add evaluation',15,'add_evaluation'),(58,'Can change evaluation',15,'change_evaluation'),(59,'Can delete evaluation',15,'delete_evaluation'),(60,'Can view evaluation',15,'view_evaluation'),(61,'Can add subscription',16,'add_subscription'),(62,'Can change subscription',16,'change_subscription'),(63,'Can delete subscription',16,'delete_subscription'),(64,'Can view subscription',16,'view_subscription'),(65,'Can add subscription question allowence',17,'add_subscriptionquestionallowence'),(66,'Can change subscription question allowence',17,'change_subscriptionquestionallowence'),(67,'Can delete subscription question allowence',17,'delete_subscriptionquestionallowence'),(68,'Can view subscription question allowence',17,'view_subscriptionquestionallowence'),(69,'Can add subscription question category',18,'add_subscriptionquestioncategory'),(70,'Can change subscription question category',18,'change_subscriptionquestioncategory'),(71,'Can delete subscription question category',18,'delete_subscriptionquestioncategory'),(72,'Can view subscription question category',18,'view_subscriptionquestioncategory'),(73,'Can add manager edits',19,'add_manageredits'),(74,'Can change manager edits',19,'change_manageredits'),(75,'Can delete manager edits',19,'delete_manageredits'),(76,'Can view manager edits',19,'view_manageredits'),(77,'Can add subscription payment details',20,'add_subscriptionpaymentdetails'),(78,'Can change subscription payment details',20,'change_subscriptionpaymentdetails'),(79,'Can delete subscription payment details',20,'delete_subscriptionpaymentdetails'),(80,'Can view subscription payment details',20,'view_subscriptionpaymentdetails'),(81,'Can add Token',21,'add_token'),(82,'Can change Token',21,'change_token'),(83,'Can delete Token',21,'delete_token'),(84,'Can view Token',21,'view_token'),(85,'Can add token',22,'add_tokenproxy'),(86,'Can change token',22,'change_tokenproxy'),(87,'Can delete token',22,'delete_tokenproxy'),(88,'Can view token',22,'view_tokenproxy'),(89,'Can add log entry',23,'add_logentry'),(90,'Can change log entry',23,'change_logentry'),(91,'Can delete log entry',23,'delete_logentry'),(92,'Can view log entry',23,'view_logentry'),(93,'Can add permission',24,'add_permission'),(94,'Can change permission',24,'change_permission'),(95,'Can delete permission',24,'delete_permission'),(96,'Can view permission',24,'view_permission'),(97,'Can add group',25,'add_group'),(98,'Can change group',25,'change_group'),(99,'Can delete group',25,'delete_group'),(100,'Can view group',25,'view_group'),(101,'Can add content type',26,'add_contenttype'),(102,'Can change content type',26,'change_contenttype'),(103,'Can delete content type',26,'delete_contenttype'),(104,'Can view content type',26,'view_contenttype'),(105,'Can add session',27,'add_session'),(106,'Can change session',27,'change_session'),(107,'Can delete session',27,'delete_session'),(108,'Can view session',27,'view_session');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authtoken_token`
--

DROP TABLE IF EXISTS `authtoken_token`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `authtoken_token_user_id_35299eff_fk_auth_api_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_api_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authtoken_token`
--

LOCK TABLES `authtoken_token` WRITE;
/*!40000 ALTER TABLE `authtoken_token` DISABLE KEYS */;
INSERT INTO `authtoken_token` VALUES ('7903cd556b16f7db5b7a27407471db8ad5c2ba9d','2021-11-08 06:04:52.713115',10),('c2a13e4e50967182f22a817ecbf118a95df9077a','2021-11-07 11:05:52.841220',2),('d1c0d2cd9b9b67f0fe0d33564b83a946b9962d66','2021-11-07 20:10:19.004964',9),('da07458345ab710b88da895c0872ceecbddd47b0','2021-11-07 11:27:50.776775',1);
/*!40000 ALTER TABLE `authtoken_token` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_api_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_api_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_api_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2021-11-07 11:20:14.281242','1','1 english 0.0',1,'[{\"added\": {}}]',18,2),(2,'2021-11-07 20:07:25.685758','8','8, Student, domeyser@gmail.comldd, Domey',3,'',13,2),(3,'2021-11-07 20:07:25.691028','7','7, Student, domeyser@gmail.comld, Domey',3,'',13,2),(4,'2021-11-07 20:07:25.692280','6','6, Student, domeyser@gmail.coml, Domey',3,'',13,2),(5,'2021-11-07 20:07:25.694738','5','5, Student, domeyser@gmail.com, Domey',3,'',13,2),(6,'2021-11-07 20:07:25.695871','4','4, Student, domeyuser@gmail.com, Domey',3,'',13,2),(7,'2021-11-07 20:07:25.698556','3','3, Student, mohitbansalias@rediffmail.com, Mohit',3,'',13,2),(8,'2021-11-07 20:20:00.427497','1','admin@mainsias.com',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"DefaultExam\", \"Image\", \"Gender\", \"Phone\", \"Created by\"]}}]',13,2),(9,'2021-11-07 20:21:05.018231','1','1, Admin, admin@mainsias.com, admin',2,'[{\"changed\": {\"fields\": [\"IsAdmin\"]}}]',13,2),(10,'2021-11-07 20:39:00.768849','2','2 BONUSNOFFERS',2,'[{\"changed\": {\"fields\": [\"Active\", \"Created by\", \"Image\"]}}]',3,2),(11,'2021-11-08 05:55:50.246639','1','1, Admin, admin@mainsias.com, admin',2,'[{\"changed\": {\"fields\": [\"Can create subscription\"]}}]',13,2);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (23,'admin','logentry'),(25,'auth','group'),(24,'auth','permission'),(21,'authtoken','token'),(22,'authtoken','tokenproxy'),(13,'auth_api','user'),(14,'auth_api','verificationotp'),(26,'contenttypes','contenttype'),(1,'door','noticeboard'),(2,'door','termsnconditions'),(15,'evaluation','evaluation'),(3,'exam','exam'),(4,'exam','exammanagerrelation'),(12,'manager','aboutmanager'),(27,'sessions','session'),(5,'student','studentsubscriptionrecord'),(6,'student','studentsubscriptionsquestionsrecord'),(19,'subscription','manageredits'),(16,'subscription','subscription'),(20,'subscription','subscriptionpaymentdetails'),(17,'subscription','subscriptionquestionallowence'),(18,'subscription','subscriptionquestioncategory'),(11,'teacher','evaluatorcategorypricing'),(8,'teacher','evaluatorglance'),(7,'teacher','evaluatorpaymentdetails'),(10,'teacher','evaluatorrating'),(9,'teacher','glanceevaluationsrecord');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=98 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-11-07 11:00:03.111208'),(2,'contenttypes','0002_remove_content_type_name','2021-11-07 11:00:03.172851'),(3,'auth','0001_initial','2021-11-07 11:00:03.226546'),(4,'auth','0002_alter_permission_name_max_length','2021-11-07 11:00:03.391425'),(5,'auth','0003_alter_user_email_max_length','2021-11-07 11:00:03.400372'),(6,'auth','0004_alter_user_username_opts','2021-11-07 11:00:03.409265'),(7,'auth','0005_alter_user_last_login_null','2021-11-07 11:00:03.425306'),(8,'auth','0006_require_contenttypes_0002','2021-11-07 11:00:03.430043'),(9,'auth','0007_alter_validators_add_error_messages','2021-11-07 11:00:03.443179'),(10,'auth','0008_alter_user_username_max_length','2021-11-07 11:00:03.451519'),(11,'auth','0009_alter_user_last_name_max_length','2021-11-07 11:00:03.459499'),(12,'auth_api','0001_initial','2021-11-07 11:00:03.555005'),(13,'admin','0001_initial','2021-11-07 11:00:03.788407'),(14,'admin','0002_logentry_remove_auto_add','2021-11-07 11:00:03.870833'),(15,'admin','0003_logentry_add_action_flag_choices','2021-11-07 11:00:03.882194'),(16,'auth','0010_alter_group_name_max_length','2021-11-07 11:00:03.907038'),(17,'auth','0011_update_proxy_permissions','2021-11-07 11:00:03.920016'),(18,'auth','0012_alter_user_first_name_max_length','2021-11-07 11:00:03.932387'),(19,'auth_api','0002_auto_20210308_2215','2021-11-07 11:00:03.944169'),(20,'auth_api','0003_auto_20210308_2216','2021-11-07 11:00:03.963283'),(21,'auth_api','0004_auto_20210308_2217','2021-11-07 11:00:03.977736'),(22,'auth_api','0005_auto_20210309_0256','2021-11-07 11:00:03.989463'),(23,'auth_api','0006_auto_20210320_1527','2021-11-07 11:00:04.005963'),(24,'auth_api','0007_auto_20210404_0024','2021-11-07 11:00:04.019549'),(25,'auth_api','0008_auto_20210406_0010','2021-11-07 11:00:04.032652'),(26,'auth_api','0009_auto_20210406_0012','2021-11-07 11:00:04.044624'),(27,'auth_api','0010_auto_20210410_2222','2021-11-07 11:00:04.058612'),(28,'auth_api','0011_auto_20210417_2326','2021-11-07 11:00:04.106849'),(29,'auth_api','0012_user_gender','2021-11-07 11:00:04.122197'),(30,'auth_api','0013_user_can_create_subscription','2021-11-07 11:00:04.137795'),(31,'auth_api','0014_auto_20210425_1403','2021-11-07 11:00:04.171590'),(32,'authtoken','0001_initial','2021-11-07 11:00:04.202687'),(33,'authtoken','0002_auto_20160226_1747','2021-11-07 11:00:04.331142'),(34,'authtoken','0003_tokenproxy','2021-11-07 11:00:04.335119'),(35,'door','0001_initial','2021-11-07 11:00:04.353262'),(36,'door','0002_auto_20210309_0257','2021-11-07 11:00:04.358376'),(37,'door','0003_siteglance_thingname','2021-11-07 11:00:04.369832'),(38,'door','0004_auto_20210320_1527','2021-11-07 11:00:04.385037'),(39,'door','0005_noticeboard','2021-11-07 11:00:04.407009'),(40,'door','0006_auto_20210521_2336','2021-11-07 11:00:04.439160'),(41,'exam','0001_initial','2021-11-07 11:00:04.502162'),(42,'subscription','0001_initial','2021-11-07 11:00:04.745240'),(43,'subscription','0002_auto_20210308_2234','2021-11-07 11:00:05.093210'),(44,'subscription','0003_auto_20210308_2357','2021-11-07 11:00:05.136165'),(45,'subscription','0004_auto_20210309_0009','2021-11-07 11:00:05.191971'),(46,'subscription','0005_auto_20210320_1527','2021-11-07 11:00:05.370920'),(47,'subscription','0006_auto_20210324_2331','2021-11-07 11:00:05.467086'),(48,'subscription','0007_auto_20210326_2333','2021-11-07 11:00:05.587911'),(49,'subscription','0008_subscriptionquestionallowence_frequency','2021-11-07 11:00:05.606562'),(50,'subscription','0009_auto_20210405_2325','2021-11-07 11:00:05.622216'),(51,'subscription','0010_auto_20210410_2222','2021-11-07 11:00:05.695612'),(52,'subscription','0011_manageredits','2021-11-07 11:00:05.727174'),(53,'subscription','0012_manageredits_content_bkp','2021-11-07 11:00:05.785713'),(54,'subscription','0013_auto_20210427_0119','2021-11-07 11:00:05.816823'),(55,'subscription','0014_auto_20210427_0134','2021-11-07 11:00:05.878626'),(56,'subscription','0015_subscriptionpaymentdetails','2021-11-07 11:00:05.916829'),(57,'subscription','0016_subscriptionpaymentdetails_signature','2021-11-07 11:00:06.005255'),(58,'subscription','0017_delete_subscriptionextras','2021-11-07 11:00:06.016746'),(59,'exam','0002_exammanagerrelation_can_create_subscription','2021-11-07 11:00:06.038436'),(60,'student','0001_initial','2021-11-07 11:00:06.139024'),(61,'evaluation','0001_initial','2021-11-07 11:00:06.294530'),(62,'evaluation','0002_evaluation_subject','2021-11-07 11:00:06.525287'),(63,'evaluation','0003_auto_20210328_2047','2021-11-07 11:00:06.608493'),(64,'evaluation','0004_auto_20210404_0024','2021-11-07 11:00:06.630097'),(65,'evaluation','0005_auto_20210405_2325','2021-11-07 11:00:06.678079'),(66,'evaluation','0006_auto_20210406_0010','2021-11-07 11:00:06.697289'),(67,'evaluation','0007_auto_20210410_2222','2021-11-07 11:00:07.107476'),(68,'evaluation','0008_auto_20210417_2317','2021-11-07 11:00:07.232812'),(69,'evaluation','0009_auto_20210502_0153','2021-11-07 11:00:07.267477'),(70,'evaluation','0010_auto_20210515_0640','2021-11-07 11:00:07.286997'),(71,'evaluation','0011_auto_20210515_1527','2021-11-07 11:00:07.385284'),(72,'evaluation','0012_auto_20210518_1624','2021-11-07 11:00:07.406444'),(73,'exam','0003_auto_20210404_0024','2021-11-07 11:00:07.431385'),(74,'exam','0004_auto_20210405_2325','2021-11-07 11:00:07.452971'),(75,'exam','0005_remove_exammanagerrelation_can_create_subscription','2021-11-07 11:00:07.500325'),(76,'exam','0006_exam_image','2021-11-07 11:00:07.522756'),(77,'exam','0007_auto_20210521_2333','2021-11-07 11:00:07.639861'),(78,'manager','0001_initial','2021-11-07 11:00:07.675104'),(79,'sessions','0001_initial','2021-11-07 11:00:07.737605'),(80,'student','0002_studentsubscriptionrecord_one_limit','2021-11-07 11:00:07.775005'),(81,'student','0003_auto_20210331_2242','2021-11-07 11:00:07.836844'),(82,'student','0004_auto_20210405_2325','2021-11-07 11:00:07.856941'),(83,'student','0005_auto_20210410_2222','2021-11-07 11:00:07.932900'),(84,'student','0006_auto_20210417_2317','2021-11-07 11:00:08.004554'),(85,'student','0007_auto_20210429_2351','2021-11-07 11:00:08.119211'),(86,'student','0008_auto_20210518_1624','2021-11-07 11:00:08.167306'),(87,'student','0009_auto_20210523_1904','2021-11-07 11:00:08.216214'),(88,'subscription','0018_auto_20210515_1620','2021-11-07 11:00:08.289490'),(89,'subscription','0019_auto_20210516_1014','2021-11-07 11:00:08.436632'),(90,'teacher','0001_initial','2021-11-07 11:00:08.481141'),(91,'teacher','0002_auto_20210425_1355','2021-11-07 11:00:08.537821'),(92,'teacher','0003_evaluatorglance_glanceevaluationsrecord','2021-11-07 11:00:08.667629'),(93,'teacher','0004_auto_20210429_2355','2021-11-07 11:00:08.940547'),(94,'teacher','0005_auto_20210430_0229','2021-11-07 11:00:09.063103'),(95,'teacher','0006_evaluatorrating','2021-11-07 11:00:09.107477'),(96,'teacher','0007_evaluatorcategorypricing','2021-11-07 11:00:09.195183'),(97,'auth_api','0015_auto_20211108_0135','2021-11-07 20:06:09.245034');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('tjc3rdvrwg8e4dzhdj2gjjjlr5ri3y2o','.eJxVjDsOwjAQBe_iGlnG8ZeSPmewdr0bHEC2FCcV4u4QKQW0b2beSyTY1pK2zkuaSVyEFqffDSE_uO6A7lBvTeZW12VGuSvyoF2Ojfh5Pdy_gwK9fGsOBrxSCgd07LVj4yFECugVk0ZGF8GSUYPVYJzLEzDYbG2YooZwZvH-AOfEODU:1mjfxw:eKDQQ6kt_9bvv2R6-3yFrUcD9nd18AE9rd3GnK6C-_w','2021-11-21 11:04:00.868430');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `door_noticeboard`
--

DROP TABLE IF EXISTS `door_noticeboard`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `door_noticeboard` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `notice` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `door_noticeboard`
--

LOCK TABLES `door_noticeboard` WRITE;
/*!40000 ALTER TABLE `door_noticeboard` DISABLE KEYS */;
/*!40000 ALTER TABLE `door_noticeboard` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `door_termsnconditions`
--

DROP TABLE IF EXISTS `door_termsnconditions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `door_termsnconditions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `note` longtext NOT NULL,
  `is_heading` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `door_termsnconditions`
--

LOCK TABLES `door_termsnconditions` WRITE;
/*!40000 ALTER TABLE `door_termsnconditions` DISABLE KEYS */;
/*!40000 ALTER TABLE `door_termsnconditions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `evaluation_evaluation`
--

DROP TABLE IF EXISTS `evaluation_evaluation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `evaluation_evaluation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `answer_file` varchar(100) DEFAULT NULL,
  `answers_count` int(11) NOT NULL,
  `student_message` longtext DEFAULT NULL,
  `evaluator_message` longtext DEFAULT NULL,
  `rating_to_evaluator` double DEFAULT NULL,
  `tags` longtext DEFAULT NULL,
  `status` varchar(50) NOT NULL,
  `date` date NOT NULL,
  `time` time(6) NOT NULL,
  `date_time_recent` datetime(6) NOT NULL,
  `date_time_evaluated` datetime(6) DEFAULT NULL,
  `evaluator_id` int(11) DEFAULT NULL,
  `exam_id` int(11) DEFAULT NULL,
  `student_id` int(11) NOT NULL,
  `subscribed_subscription_id` int(11) DEFAULT NULL,
  `subject_id` int(11) DEFAULT NULL,
  `evaluated_file` varchar(100) DEFAULT NULL,
  `marks` varchar(20) NOT NULL,
  `feedback_to_evaluator` longtext DEFAULT NULL,
  `category_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `evaluation_evaluation_student_id_5a8123de_fk_auth_api_user_id` (`student_id`),
  KEY `evaluation_evaluation_evaluator_id_d0cbf08f_fk_auth_api_user_id` (`evaluator_id`),
  KEY `evaluation_evaluation_exam_id_3173259e_fk_exam_exam_id` (`exam_id`),
  KEY `evaluation_evaluatio_subject_id_e14e33ef_fk_student_s` (`subject_id`),
  KEY `evaluation_evaluatio_subscribed_subscript_47ff807d_fk_student_s` (`subscribed_subscription_id`),
  KEY `evaluation_evaluatio_category_id_a8b37d3d_fk_subscript` (`category_id`),
  CONSTRAINT `evaluation_evaluatio_category_id_a8b37d3d_fk_subscript` FOREIGN KEY (`category_id`) REFERENCES `subscription_subscriptionquestioncategory` (`id`),
  CONSTRAINT `evaluation_evaluatio_subject_id_e14e33ef_fk_student_s` FOREIGN KEY (`subject_id`) REFERENCES `student_studentsubscriptionsquestionsrecord` (`id`),
  CONSTRAINT `evaluation_evaluatio_subscribed_subscript_47ff807d_fk_student_s` FOREIGN KEY (`subscribed_subscription_id`) REFERENCES `student_studentsubscriptionrecord` (`id`),
  CONSTRAINT `evaluation_evaluation_evaluator_id_d0cbf08f_fk_auth_api_user_id` FOREIGN KEY (`evaluator_id`) REFERENCES `auth_api_user` (`id`),
  CONSTRAINT `evaluation_evaluation_exam_id_3173259e_fk_exam_exam_id` FOREIGN KEY (`exam_id`) REFERENCES `exam_exam` (`id`),
  CONSTRAINT `evaluation_evaluation_student_id_5a8123de_fk_auth_api_user_id` FOREIGN KEY (`student_id`) REFERENCES `auth_api_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `evaluation_evaluation`
--

LOCK TABLES `evaluation_evaluation` WRITE;
/*!40000 ALTER TABLE `evaluation_evaluation` DISABLE KEYS */;
/*!40000 ALTER TABLE `evaluation_evaluation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exam_exam`
--

DROP TABLE IF EXISTS `exam_exam`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `exam_exam` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `short_name` varchar(20) NOT NULL,
  `full_name` varchar(150) DEFAULT NULL,
  `content1` longtext DEFAULT NULL,
  `content2` longtext DEFAULT NULL,
  `content3` longtext DEFAULT NULL,
  `content4` longtext DEFAULT NULL,
  `date_time_created` datetime(6) NOT NULL,
  `active` tinyint(1) NOT NULL,
  `created_by_id` int(11) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `short_name` (`short_name`),
  KEY `exam_exam_created_by_id_32831130_fk_auth_api_user_id` (`created_by_id`),
  CONSTRAINT `exam_exam_created_by_id_32831130_fk_auth_api_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_api_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exam_exam`
--

LOCK TABLES `exam_exam` WRITE;
/*!40000 ALTER TABLE `exam_exam` DISABLE KEYS */;
INSERT INTO `exam_exam` VALUES (1,'UPSC',NULL,'Put Your contents here.','Put Your contents here.','Put Your contents here.','Put Your contents here.','2021-11-07 11:15:37.797828',1,NULL,''),(2,'BONUSNOFFERS','Bonusnoffers','Put Your contents here.','Put Your contents here.','Put Your contents here.','Put Your contents here.','2021-11-07 20:23:41.223308',0,1,'exam_images/Screenshot_2021-11-08_at_1.48.16_AM.png');
/*!40000 ALTER TABLE `exam_exam` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exam_exammanagerrelation`
--

DROP TABLE IF EXISTS `exam_exammanagerrelation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `exam_exammanagerrelation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date_time_created` datetime(6) NOT NULL,
  `active` tinyint(1) NOT NULL,
  `exam_id` int(11) NOT NULL,
  `manager_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `exam_exammanagerrelation_exam_id_1dc9b29c_fk_exam_exam_id` (`exam_id`),
  KEY `exam_exammanagerrelation_manager_id_64690f33_fk_auth_api_user_id` (`manager_id`),
  CONSTRAINT `exam_exammanagerrelation_exam_id_1dc9b29c_fk_exam_exam_id` FOREIGN KEY (`exam_id`) REFERENCES `exam_exam` (`id`),
  CONSTRAINT `exam_exammanagerrelation_manager_id_64690f33_fk_auth_api_user_id` FOREIGN KEY (`manager_id`) REFERENCES `auth_api_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exam_exammanagerrelation`
--

LOCK TABLES `exam_exammanagerrelation` WRITE;
/*!40000 ALTER TABLE `exam_exammanagerrelation` DISABLE KEYS */;
INSERT INTO `exam_exammanagerrelation` VALUES (1,'2021-11-08 06:04:26.589975',1,1,10);
/*!40000 ALTER TABLE `exam_exammanagerrelation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manager_aboutmanager`
--

DROP TABLE IF EXISTS `manager_aboutmanager`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `manager_aboutmanager` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `exams_handling` int(11) NOT NULL,
  `can_create_subscriptions` tinyint(1) NOT NULL,
  `manager_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `manager_aboutmanager_manager_id_7a45ae58_fk_auth_api_user_id` (`manager_id`),
  CONSTRAINT `manager_aboutmanager_manager_id_7a45ae58_fk_auth_api_user_id` FOREIGN KEY (`manager_id`) REFERENCES `auth_api_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manager_aboutmanager`
--

LOCK TABLES `manager_aboutmanager` WRITE;
/*!40000 ALTER TABLE `manager_aboutmanager` DISABLE KEYS */;
/*!40000 ALTER TABLE `manager_aboutmanager` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_studentsubscriptionrecord`
--

DROP TABLE IF EXISTS `student_studentsubscriptionrecord`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student_studentsubscriptionrecord` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `subscription_name` varchar(200) NOT NULL,
  `paid` bigint(20) NOT NULL,
  `selling_points` longtext DEFAULT NULL,
  `purchase_time` datetime(6) NOT NULL,
  `expiry_date` date DEFAULT NULL,
  `exam_id` int(11) DEFAULT NULL,
  `student_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `student_studentsubsc_student_id_f1125778_fk_auth_api_` (`student_id`),
  KEY `student_studentsubsc_exam_id_04958107_fk_exam_exam` (`exam_id`),
  CONSTRAINT `student_studentsubsc_exam_id_04958107_fk_exam_exam` FOREIGN KEY (`exam_id`) REFERENCES `exam_exam` (`id`),
  CONSTRAINT `student_studentsubsc_student_id_f1125778_fk_auth_api_` FOREIGN KEY (`student_id`) REFERENCES `auth_api_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_studentsubscriptionrecord`
--

LOCK TABLES `student_studentsubscriptionrecord` WRITE;
/*!40000 ALTER TABLE `student_studentsubscriptionrecord` DISABLE KEYS */;
INSERT INTO `student_studentsubscriptionrecord` VALUES (1,'Test',55,'[{\"id\":0.01661601104606114,\"sellingPoints\":\"test\"}]','2021-11-08 06:18:57.542994','2021-11-12',1,9);
/*!40000 ALTER TABLE `student_studentsubscriptionrecord` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_studentsubscriptionsquestionsrecord`
--

DROP TABLE IF EXISTS `student_studentsubscriptionsquestionsrecord`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student_studentsubscriptionsquestionsrecord` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `subject_name` varchar(100) NOT NULL,
  `question_number` int(11) NOT NULL,
  `subscription_id` int(11) NOT NULL,
  `frequency` int(11) NOT NULL,
  `category_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `student_studentsubsc_subscription_id_07e3a3ce_fk_student_s` (`subscription_id`),
  KEY `student_studentsubsc_category_id_39d839b2_fk_subscript` (`category_id`),
  CONSTRAINT `student_studentsubsc_category_id_39d839b2_fk_subscript` FOREIGN KEY (`category_id`) REFERENCES `subscription_subscriptionquestioncategory` (`id`),
  CONSTRAINT `student_studentsubsc_subscription_id_07e3a3ce_fk_student_s` FOREIGN KEY (`subscription_id`) REFERENCES `student_studentsubscriptionrecord` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_studentsubscriptionsquestionsrecord`
--

LOCK TABLES `student_studentsubscriptionsquestionsrecord` WRITE;
/*!40000 ALTER TABLE `student_studentsubscriptionsquestionsrecord` DISABLE KEYS */;
INSERT INTO `student_studentsubscriptionsquestionsrecord` VALUES (1,'test',5,1,5,1);
/*!40000 ALTER TABLE `student_studentsubscriptionsquestionsrecord` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subscription_manageredits`
--

DROP TABLE IF EXISTS `subscription_manageredits`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `subscription_manageredits` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `_type` varchar(30) NOT NULL,
  `note` longtext DEFAULT NULL,
  `content` longtext NOT NULL,
  `date_time_created` datetime(6) NOT NULL,
  `created_by_id` int(11) NOT NULL,
  `content_bkp` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `subscription_manager_created_by_id_3031d6da_fk_auth_api_` (`created_by_id`),
  CONSTRAINT `subscription_manager_created_by_id_3031d6da_fk_auth_api_` FOREIGN KEY (`created_by_id`) REFERENCES `auth_api_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subscription_manageredits`
--

LOCK TABLES `subscription_manageredits` WRITE;
/*!40000 ALTER TABLE `subscription_manageredits` DISABLE KEYS */;
INSERT INTO `subscription_manageredits` VALUES (2,'Active-toggle','Active button toggled to False','{\"subscription\": {\"id\": 1, \"date_time_created\": \"08-Nov-2021 11:27\", \"created_by\": {\"id\": 1, \"first_name\": \"admin\", \"last_name\": \"user\", \"email\": \"admin@mainsias.com\", \"phone\": \"234234234\"}, \"exam\": {\"short_name\": \"UPSC\", \"full_name\": null, \"id\": 1}, \"name\": \"Test\", \"days\": null, \"till_date\": \"2021-11-12\", \"price\": 55, \"active\": true, \"featured\": false, \"selling_points\": \"[{\\\"id\\\":0.01661601104606114,\\\"sellingPoints\\\":\\\"test\\\"}]\", \"description\": null, \"limited_time_to\": null}, \"active\": false, \"question_number_allowence\": [{\"id\": 2, \"category\": {\"id\": 1, \"name\": \"english\"}, \"secondary_id\": 0.8526214860239933, \"subject_name\": \"test\", \"question_number\": 5, \"frequency\": 5, \"subscription\": 1}], \"sid\": 1}','2021-11-08 06:08:01.849380',10,'');
/*!40000 ALTER TABLE `subscription_manageredits` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subscription_subscription`
--

DROP TABLE IF EXISTS `subscription_subscription`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `subscription_subscription` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `days` int(11) DEFAULT NULL,
  `price` bigint(20) NOT NULL,
  `active` tinyint(1) NOT NULL,
  `selling_points` longtext DEFAULT NULL,
  `date_time_created` datetime(6) NOT NULL,
  `limited_time_to` date DEFAULT NULL,
  `created_by_id` int(11) NOT NULL,
  `exam_id` int(11) NOT NULL,
  `description` longtext DEFAULT NULL,
  `till_date` date DEFAULT NULL,
  `featured` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `subscription_subscri_created_by_id_60f46705_fk_auth_api_` (`created_by_id`),
  KEY `subscription_subscription_exam_id_e416e5ec_fk_exam_exam_id` (`exam_id`),
  CONSTRAINT `subscription_subscri_created_by_id_60f46705_fk_auth_api_` FOREIGN KEY (`created_by_id`) REFERENCES `auth_api_user` (`id`),
  CONSTRAINT `subscription_subscription_exam_id_e416e5ec_fk_exam_exam_id` FOREIGN KEY (`exam_id`) REFERENCES `exam_exam` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subscription_subscription`
--

LOCK TABLES `subscription_subscription` WRITE;
/*!40000 ALTER TABLE `subscription_subscription` DISABLE KEYS */;
INSERT INTO `subscription_subscription` VALUES (1,'Test',NULL,55,0,'[{\"id\":0.01661601104606114,\"sellingPoints\":\"test\"}]','2021-11-08 05:57:41.469191',NULL,1,1,NULL,'2021-11-12',0);
/*!40000 ALTER TABLE `subscription_subscription` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subscription_subscriptionpaymentdetails`
--

DROP TABLE IF EXISTS `subscription_subscriptionpaymentdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `subscription_subscriptionpaymentdetails` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order_id` longtext DEFAULT NULL,
  `order_obj` longtext DEFAULT NULL,
  `receipt_id` longtext DEFAULT NULL,
  `payment_id` longtext DEFAULT NULL,
  `is_paid` tinyint(1) NOT NULL,
  `last_saved` datetime(6) NOT NULL,
  `student_id` int(11) NOT NULL,
  `subscription_id` int(11) DEFAULT NULL,
  `signature` longtext DEFAULT NULL,
  `subscription_subscribed_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `subscription_subscri_student_id_b5068622_fk_auth_api_` (`student_id`),
  KEY `subscription_subscri_subscription_subscri_18071d0c_fk_student_s` (`subscription_subscribed_id`),
  KEY `subscription_subscri_subscription_id_53b5ddab_fk_subscript` (`subscription_id`),
  CONSTRAINT `subscription_subscri_student_id_b5068622_fk_auth_api_` FOREIGN KEY (`student_id`) REFERENCES `auth_api_user` (`id`),
  CONSTRAINT `subscription_subscri_subscription_id_53b5ddab_fk_subscript` FOREIGN KEY (`subscription_id`) REFERENCES `subscription_subscription` (`id`),
  CONSTRAINT `subscription_subscri_subscription_subscri_18071d0c_fk_student_s` FOREIGN KEY (`subscription_subscribed_id`) REFERENCES `student_studentsubscriptionrecord` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subscription_subscriptionpaymentdetails`
--

LOCK TABLES `subscription_subscriptionpaymentdetails` WRITE;
/*!40000 ALTER TABLE `subscription_subscriptionpaymentdetails` DISABLE KEYS */;
INSERT INTO `subscription_subscriptionpaymentdetails` VALUES (1,'order_IJ0V3Nw3JgwPkz','{\"id\": \"order_IJ0V3Nw3JgwPkz\", \"entity\": \"order\", \"amount\": 5500, \"amount_paid\": 0, \"amount_due\": 5500, \"currency\": \"INR\", \"receipt\": \"receipt_20211108114623-PaymentInit\", \"offer_id\": null, \"status\": \"created\", \"attempts\": 0, \"notes\": [], \"created_at\": 1636352183}','receipt_20211108114623-PaymentInit',NULL,0,'2021-11-08 06:16:23.822099',9,1,NULL,NULL),(2,'order_IJ0WKnn2XCWieD','{\"id\": \"order_IJ0WKnn2XCWieD\", \"entity\": \"order\", \"amount\": 5500, \"amount_paid\": 0, \"amount_due\": 5500, \"currency\": \"INR\", \"receipt\": \"receipt_20211108114736-PaymentInit\", \"offer_id\": null, \"status\": \"created\", \"attempts\": 0, \"notes\": [], \"created_at\": 1636352256}','receipt_20211108114736-PaymentInit','pay_IJ0XdQKMcSobdh',1,'2021-11-08 06:18:57.545816',9,1,'96b43b26c1506be768b8f2e773497da0e5cd104cd47cc8786ee9cf5aa18f8bff',1);
/*!40000 ALTER TABLE `subscription_subscriptionpaymentdetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subscription_subscriptionquestionallowence`
--

DROP TABLE IF EXISTS `subscription_subscriptionquestionallowence`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `subscription_subscriptionquestionallowence` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `subject_name` varchar(100) NOT NULL,
  `question_number` int(11) NOT NULL,
  `subscription_id` int(11) NOT NULL,
  `secondary_id` double DEFAULT NULL,
  `frequency` int(11) NOT NULL,
  `category_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `subscription_subscri_subscription_id_34e09702_fk_subscript` (`subscription_id`),
  KEY `subscription_subscri_category_id_04fd583e_fk_subscript` (`category_id`),
  CONSTRAINT `subscription_subscri_category_id_04fd583e_fk_subscript` FOREIGN KEY (`category_id`) REFERENCES `subscription_subscriptionquestioncategory` (`id`),
  CONSTRAINT `subscription_subscri_subscription_id_34e09702_fk_subscript` FOREIGN KEY (`subscription_id`) REFERENCES `subscription_subscription` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subscription_subscriptionquestionallowence`
--

LOCK TABLES `subscription_subscriptionquestionallowence` WRITE;
/*!40000 ALTER TABLE `subscription_subscriptionquestionallowence` DISABLE KEYS */;
INSERT INTO `subscription_subscriptionquestionallowence` VALUES (2,'test',5,1,0.8526214860239933,5,1);
/*!40000 ALTER TABLE `subscription_subscriptionquestionallowence` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subscription_subscriptionquestioncategory`
--

DROP TABLE IF EXISTS `subscription_subscriptionquestioncategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `subscription_subscriptionquestioncategory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `evaluation_cost` double NOT NULL,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subscription_subscriptionquestioncategory`
--

LOCK TABLES `subscription_subscriptionquestioncategory` WRITE;
/*!40000 ALTER TABLE `subscription_subscriptionquestioncategory` DISABLE KEYS */;
INSERT INTO `subscription_subscriptionquestioncategory` VALUES (1,0,'english');
/*!40000 ALTER TABLE `subscription_subscriptionquestioncategory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teacher_evaluatorcategorypricing`
--

DROP TABLE IF EXISTS `teacher_evaluatorcategorypricing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `teacher_evaluatorcategorypricing` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cost` double NOT NULL,
  `category_id` int(11) DEFAULT NULL,
  `evaluator_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `evaluator_id` (`evaluator_id`),
  UNIQUE KEY `teacher_evaluatorcategor_evaluator_id_category_id_ec311781_uniq` (`evaluator_id`,`category_id`),
  KEY `teacher_evaluatorcat_category_id_ba45d21d_fk_subscript` (`category_id`),
  CONSTRAINT `teacher_evaluatorcat_category_id_ba45d21d_fk_subscript` FOREIGN KEY (`category_id`) REFERENCES `subscription_subscriptionquestioncategory` (`id`),
  CONSTRAINT `teacher_evaluatorcat_evaluator_id_9e9cc383_fk_auth_api_` FOREIGN KEY (`evaluator_id`) REFERENCES `auth_api_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher_evaluatorcategorypricing`
--

LOCK TABLES `teacher_evaluatorcategorypricing` WRITE;
/*!40000 ALTER TABLE `teacher_evaluatorcategorypricing` DISABLE KEYS */;
/*!40000 ALTER TABLE `teacher_evaluatorcategorypricing` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teacher_evaluatorglance`
--

DROP TABLE IF EXISTS `teacher_evaluatorglance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `teacher_evaluatorglance` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status` varchar(50) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `last_updated` datetime(6) NOT NULL,
  `closed_at` datetime(6) DEFAULT NULL,
  `evaluator_id` int(11) NOT NULL,
  `closed_details` longtext DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `teacher_evaluatorgla_evaluator_id_ec0ca059_fk_auth_api_` (`evaluator_id`),
  CONSTRAINT `teacher_evaluatorgla_evaluator_id_ec0ca059_fk_auth_api_` FOREIGN KEY (`evaluator_id`) REFERENCES `auth_api_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher_evaluatorglance`
--

LOCK TABLES `teacher_evaluatorglance` WRITE;
/*!40000 ALTER TABLE `teacher_evaluatorglance` DISABLE KEYS */;
/*!40000 ALTER TABLE `teacher_evaluatorglance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teacher_evaluatorpaymentdetails`
--

DROP TABLE IF EXISTS `teacher_evaluatorpaymentdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `teacher_evaluatorpaymentdetails` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `details` longtext DEFAULT NULL,
  `evaluator_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `evaluator_id` (`evaluator_id`),
  CONSTRAINT `teacher_evaluatorpay_evaluator_id_5666a221_fk_auth_api_` FOREIGN KEY (`evaluator_id`) REFERENCES `auth_api_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher_evaluatorpaymentdetails`
--

LOCK TABLES `teacher_evaluatorpaymentdetails` WRITE;
/*!40000 ALTER TABLE `teacher_evaluatorpaymentdetails` DISABLE KEYS */;
/*!40000 ALTER TABLE `teacher_evaluatorpaymentdetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teacher_evaluatorrating`
--

DROP TABLE IF EXISTS `teacher_evaluatorrating`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `teacher_evaluatorrating` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ratings_total` double NOT NULL,
  `ratings_count` int(11) NOT NULL,
  `evaluator_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `evaluator_id` (`evaluator_id`),
  CONSTRAINT `teacher_evaluatorrat_evaluator_id_fb809de8_fk_auth_api_` FOREIGN KEY (`evaluator_id`) REFERENCES `auth_api_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher_evaluatorrating`
--

LOCK TABLES `teacher_evaluatorrating` WRITE;
/*!40000 ALTER TABLE `teacher_evaluatorrating` DISABLE KEYS */;
/*!40000 ALTER TABLE `teacher_evaluatorrating` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teacher_glanceevaluationsrecord`
--

DROP TABLE IF EXISTS `teacher_glanceevaluationsrecord`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `teacher_glanceevaluationsrecord` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `category_id` int(11) NOT NULL,
  `evaluation_id` int(11) NOT NULL,
  `glance_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `teacher_glanceevaluationsrecord_evaluation_id_5f8491b1_uniq` (`evaluation_id`),
  UNIQUE KEY `teacher_glanceevaluation_glance_id_evaluation_id_4f0be8af_uniq` (`glance_id`,`evaluation_id`),
  KEY `teacher_glanceevalua_category_id_e2b5ab03_fk_subscript` (`category_id`),
  CONSTRAINT `teacher_glanceevalua_category_id_e2b5ab03_fk_subscript` FOREIGN KEY (`category_id`) REFERENCES `subscription_subscriptionquestioncategory` (`id`),
  CONSTRAINT `teacher_glanceevalua_evaluation_id_5f8491b1_fk_evaluatio` FOREIGN KEY (`evaluation_id`) REFERENCES `evaluation_evaluation` (`id`),
  CONSTRAINT `teacher_glanceevalua_glance_id_59894f00_fk_teacher_e` FOREIGN KEY (`glance_id`) REFERENCES `teacher_evaluatorglance` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher_glanceevaluationsrecord`
--

LOCK TABLES `teacher_glanceevaluationsrecord` WRITE;
/*!40000 ALTER TABLE `teacher_glanceevaluationsrecord` DISABLE KEYS */;
/*!40000 ALTER TABLE `teacher_glanceevaluationsrecord` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-08 11:55:29