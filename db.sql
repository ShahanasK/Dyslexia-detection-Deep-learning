/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 5.6.12-log : Database - asw_22_vimal_elearning
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`asw_22_vimal_elearning` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `asw_22_vimal_elearning`;

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `parent_id` int(11) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `complaint` varchar(200) DEFAULT NULL,
  `reply` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`parent_id`,`date`,`complaint`,`reply`) values 
(1,2,'2024-03-17','ghchjgkj','ok'),
(2,2,'2024-03-17','UOJLDFN','Sure we will look for it.'),
(3,2,'2024-03-17','Very slow','Sure,We will Work on it.'),
(4,5,'2024-03-18','good but little slow','pending');

/*Table structure for table `familiar_person` */

DROP TABLE IF EXISTS `familiar_person`;

CREATE TABLE `familiar_person` (
  `person_id` int(11) NOT NULL AUTO_INCREMENT,
  `parent_id` int(11) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `relation` varchar(50) DEFAULT NULL,
  `image` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`person_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `familiar_person` */

insert  into `familiar_person`(`person_id`,`parent_id`,`name`,`relation`,`image`) values 
(3,5,'Shahanas K','Aunty','/static/person/20240318_105234.jpg'),
(4,2,'Stephy','cousin','/static/person/20240318_105525.jpg');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `user_type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`user_type`) values 
(1,'admin@gmail.com','admin','admin'),
(2,'admin@gmail.com','aaaaa','parent'),
(3,'admin@gmail.com','aaaaa','parent'),
(4,'admin@gmail.com','aaaaa','parent'),
(5,'safnarashid4@gmail.com','safna','parent'),
(6,'safnarashid4@gmail.com','3379','student'),
(7,'shahanask4801@gmail.com','liza','parent'),
(8,'shahanask4801@gmail.com','3354','student'),
(9,'shahanask4801@gmail.com','6183','student'),
(10,'shahanask4801@gmail.com','8736','student'),
(11,'shahanask4801@gmail.com','7495','student'),
(12,'shahanask4801@gmail.com','6873','student');

/*Table structure for table `object` */

DROP TABLE IF EXISTS `object`;

CREATE TABLE `object` (
  `object_id` int(11) NOT NULL AUTO_INCREMENT,
  `object_name` varchar(50) DEFAULT NULL,
  `image` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`object_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `object` */

insert  into `object`(`object_id`,`object_name`,`image`) values 
(2,'Apple','/static/objects/20240317_201045.jpg'),
(3,'Ball','/static/objects/20240317_201159.jpg');

/*Table structure for table `parent` */

DROP TABLE IF EXISTS `parent`;

CREATE TABLE `parent` (
  `parent_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `image` varchar(200) DEFAULT NULL,
  `house` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `state` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`parent_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `parent` */

insert  into `parent`(`parent_id`,`name`,`email`,`phone`,`image`,`house`,`place`,`city`,`state`) values 
(2,'abc','admin@gmail.com','8289896272','/static/parent/20240317_154328.jpg','house','ernakulam','kochi','kerala'),
(3,'abc','admin@gmail.com','8623961046','/static/parent/20240317_200147.jpg','home','wayanad','wayanad','kerala'),
(4,'rty','admin@gmail.com','6989','/static/parent/20240318_104521.jpg','fihmk','poiiut','gtftyj','oiuiytd'),
(5,'Safna','safnarashid4@gmail.com','7856348533','/static/parent/20240318_104932.jpg','Arackal','Italy','Italy','Kuttipuram'),
(7,'SHAHANAS K','shahanask4801@gmail.com','6238670401','/static/parent/20240401_120446.jpg','Kotheri','wayanad','Wayanad','India');

/*Table structure for table `puzzle` */

DROP TABLE IF EXISTS `puzzle`;

CREATE TABLE `puzzle` (
  `puzzle_id` int(11) NOT NULL AUTO_INCREMENT,
  `puzzle_name` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `image` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`puzzle_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `puzzle` */

insert  into `puzzle`(`puzzle_id`,`puzzle_name`,`date`,`image`) values 
(3,'Letter Puzzle','2024-03-17','/static/puzzle/20240317_201549.jpg'),
(4,'Number Puzzle','2024-03-17','/static/puzzle/20240317_201804.jpg');

/*Table structure for table `result` */

DROP TABLE IF EXISTS `result`;

CREATE TABLE `result` (
  `result_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(50) DEFAULT NULL,
  `student_id` int(11) DEFAULT NULL,
  `test_type` varchar(50) DEFAULT NULL,
  `correct` varchar(50) DEFAULT NULL,
  `attended` varchar(50) DEFAULT NULL,
  `prediction` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`result_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `result` */

insert  into `result`(`result_id`,`date`,`student_id`,`test_type`,`correct`,`attended`,`prediction`) values 
(1,'2024-04-01',6,'Alphabet Recognition','20','26','Normal'),
(2,'2024-04-01',6,'Object Recognition','19','26','Normal'),
(3,'2024-04-01',8,'Alphabet Recognition','21','26','Normal'),
(4,'2024-04-01',8,'Object Recognition','20','26','Normal'),
(5,'2024-04-05',6,'Rhyming Test','10','13','Normal'),
(6,'2024-04-06',6,'Rhyming Test','9','13','Normal'),
(7,'2024-04-06',6,'Handwriting',NULL,NULL,'Normal');

/*Table structure for table `student` */

DROP TABLE IF EXISTS `student`;

CREATE TABLE `student` (
  `student_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `age` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `parent_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `student` */

insert  into `student`(`student_id`,`name`,`email`,`age`,`gender`,`parent_id`) values 
(1,'shifna','shifnamongam@gmail.com','5','Female',2),
(2,'Shahanas','shahanask4801@gmail.com','7','Female',2),
(6,'Dua Zehna','safnarashid4@gmail.com','5','Female',5),
(8,'Liza Nyha','shahanask4801@gmail.com','7','Female',7),
(9,'sana','shahanask4801@gmail.com','5','Female',7),
(12,'Hiba','shahanask4801@gmail.com','4','Female',7);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
