CREATE DATABASE crdt_db;
USE crdt_db;

DROP TABLE IF EXISTS `IMSITEST`;
CREATE TABLE `IMSITEST` (
	`timestamp` int(10) unsigned DEFAULT '0' NOT NULL,
	`amount` int(11) DEFAULT '0' NOT NULL,
	`user_imsi` varchar(16) NOT NULL,
	`user_id` varchar(16) NOT NULL,
	`bts_id` varchar(16) NOT NULL,
	`ack` bit(1) DEFAULT '0' NOT NULL,
	PRIMARY KEY (`timestamp`, `amount`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

INSERT INTO `IMSITEST` VALUES (1, 100, 'IMSI123451234512', 'matt9j', 2, 0);
