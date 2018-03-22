USE crdt_db;

DROP TABLE IF EXISTS `IMSITEST2`;
CREATE TABLE `IMSITEST2` (
	`timestamp` int(10) unsigned DEFAULT '0' NOT NULL,
	`amount` int(11) DEFAULT '0' NOT NULL,
	`user_imsi` varchar(16) NOT NULL,
	`user_id` varchar(16) NOT NULL,
	`bts_id` varchar(16) NOT NULL,
	`ack` bit(1) DEFAULT 0 NOT NULL,
	`sent` bit(1) DEFAULT 0 NOT NULL,
	PRIMARY KEY (`timestamp`, `amount`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

INSERT INTO `IMSITEST2` VALUES (1, 100, 'IMSI123451234512', 'matt9j', 2, 0, 0);
