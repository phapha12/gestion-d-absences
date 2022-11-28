--
-- Table structure for table `Absences_abscours`
--

DROP TABLE IF EXISTS `Absences_abscours`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Absences_abscours` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `cours_id` bigint(20) NOT NULL,
  `etudiants_id` bigint(20) NOT NULL,
  `justified` tinyint(1) NOT NULL,
  `justificatif` longtext DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Absences_abscours_cours_id_0ec1c3d7_fk_Absences_cours_id` (`cours_id`),
  KEY `Absences_abscours_etudiants_id_3f82a60d_fk_Absences_etudiants_id` (`etudiants_id`),
  CONSTRAINT `Absences_abscours_cours_id_0ec1c3d7_fk_Absences_cours_id` FOREIGN KEY (`cours_id`) REFERENCES `Absences_cours` (`id`),
  CONSTRAINT `Absences_abscours_etudiants_id_3f82a60d_fk_Absences_etudiants_id` FOREIGN KEY (`etudiants_id`) REFERENCES `Absences_etudiants` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Data for table `Absences_abscours`
--

LOCK TABLES `Absences_abscours` WRITE;
/*!40000 ALTER TABLE `Absences_abscours` DISABLE KEYS */;
INSERT INTO `Absences_abscours` VALUES (1,1,3,1,'malade !!n');
/*!40000 ALTER TABLE `Absences_abscours` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Absences_cours`
--

DROP TABLE IF EXISTS `Absences_cours`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Absences_cours` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `titre_du_cours` varchar(100) NOT NULL,
  `date` date DEFAULT NULL,
  `enseignant_id` bigint(20) NOT NULL,
  `duree` varchar(10) NOT NULL,
  `groupe_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Absences_cours_enseignant_id_96f0ed56_fk_Absences_enseignant_id` (`enseignant_id`),
  KEY `Absences_cours_groupe_id_6eba76c9_fk_Absences_groupes_id` (`groupe_id`),
  CONSTRAINT `Absences_cours_enseignant_id_96f0ed56_fk_Absences_enseignant_id` FOREIGN KEY (`enseignant_id`) REFERENCES `Absences_enseignant` (`id`),
  CONSTRAINT `Absences_cours_groupe_id_6eba76c9_fk_Absences_groupes_id` FOREIGN KEY (`groupe_id`) REFERENCES `Absences_groupes` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Data for table `Absences_cours`
--

LOCK TABLES `Absences_cours` WRITE;
/*!40000 ALTER TABLE `Absences_cours` DISABLE KEYS */;
INSERT INTO `Absences_cours` VALUES (1,'Maths','2022-08-05',2,'2h',2),(2,'Français','2022-06-18',3,'2h',6);
/*!40000 ALTER TABLE `Absences_cours` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Absences_enseignant`
--

DROP TABLE IF EXISTS `Absences_enseignant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Absences_enseignant` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nomens` varchar(100) NOT NULL,
  `prenomens` varchar(100) NOT NULL,
  `emailens` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Data for table `Absences_enseignant`
--

LOCK TABLES `Absences_enseignant` WRITE;
/*!40000 ALTER TABLE `Absences_enseignant` DISABLE KEYS */;
INSERT INTO `Absences_enseignant` VALUES (1,'lucien','bonjour','lucien.bonjour@uha.fr'),(2,'melia','damien','damien.melia@uha.fr'),(3,'dupont','yves','yves.dupont@uha.fr'),(4,'carlos','carlos','carlos.carlos@uha.fr'),(5,'grichka','igor','igor.grichka@uha.fr');
/*!40000 ALTER TABLE `Absences_enseignant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Absences_etudiants`
--

DROP TABLE IF EXISTS `Absences_etudiants`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Absences_etudiants` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nometu` varchar(100) NOT NULL,
  `prenometu` varchar(100) NOT NULL,
  `emailetu` varchar(50) NOT NULL,
  `photoetu` varchar(100) DEFAULT NULL,
  `groupesetu_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Absences_etudiants_groupesetu_id_a3c1a067_fk_Absences_groupes_id` (`groupesetu_id`),
  CONSTRAINT `Absences_etudiants_groupesetu_id_a3c1a067_fk_Absences_groupes_id` FOREIGN KEY (`groupesetu_id`) REFERENCES `Absences_groupes` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Data for table `Absences_etudiants`
--

LOCK TABLES `Absences_etudiants` WRITE;
/*!40000 ALTER TABLE `Absences_etudiants` DISABLE KEYS */;
INSERT INTO `Absences_etudiants` VALUES (1,'Quoi','Feur','quoi.feur@uha.fr','',2),(2,'nissan','skyline r34','skyline.nissan@uha.fr','',2),(3,'dinka','sugoi','sugoi.dinka@uha.fr','',5),(4,'remy','ramu','ramu.remy@uha.fr','',1),(5,'Kholoff','Douti','douti.kholoff@uha.fr','',2);
/*!40000 ALTER TABLE `Absences_etudiants` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Absences_groupes`
--

DROP TABLE IF EXISTS `Absences_groupes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Absences_groupes` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nomgroupe` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Data for table `Absences_groupes`
--

LOCK TABLES `Absences_groupes` WRITE;
/*!40000 ALTER TABLE `Absences_groupes` DISABLE KEYS */;
INSERT INTO `Absences_groupes` VALUES (1,'RT13'),(2,'RT12'),(3,'rt11'),(4,'tc11'),(5,'tc21'),(6,'RT21');
/*!40000 ALTER TABLE `Absences_groupes` ENABLE KEYS */;
UNLOCK TABLES;

