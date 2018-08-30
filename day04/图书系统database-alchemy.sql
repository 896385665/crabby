/*
Navicat MySQL Data Transfer

Source Server         : user
Source Server Version : 80011
Source Host           : localhost:3306
Source Database       : alchemy

Target Server Type    : MYSQL
Target Server Version : 80011
File Encoding         : 65001

Date: 2018-08-21 19:57:26
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `author`
-- ----------------------------
DROP TABLE IF EXISTS `author`;
CREATE TABLE `author` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of author
-- ----------------------------
INSERT INTO `author` VALUES ('7', 'ww');
INSERT INTO `author` VALUES ('2', '老刘');
INSERT INTO `author` VALUES ('3', '老尹');
INSERT INTO `author` VALUES ('1', '老王');

-- ----------------------------
-- Table structure for `books`
-- ----------------------------
DROP TABLE IF EXISTS `books`;
CREATE TABLE `books` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `author_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `author_id` (`author_id`),
  CONSTRAINT `books_ibfk_1` FOREIGN KEY (`author_id`) REFERENCES `author` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of books
-- ----------------------------
INSERT INTO `books` VALUES ('1', '老王回忆录', '1');
INSERT INTO `books` VALUES ('2', '我读书少，你别骗我', '1');
INSERT INTO `books` VALUES ('3', '如何才能让自己更骚', '2');
INSERT INTO `books` VALUES ('4', '怎样征服美丽少女', '3');
INSERT INTO `books` VALUES ('5', '如何征服英俊少男', '3');
INSERT INTO `books` VALUES ('13', '4554', '7');
INSERT INTO `books` VALUES ('15', '2', '7');
INSERT INTO `books` VALUES ('16', '444', '7');
INSERT INTO `books` VALUES ('17', '4447', '7');

-- ----------------------------
-- Table structure for `roles`
-- ----------------------------
DROP TABLE IF EXISTS `roles`;
CREATE TABLE `roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of roles
-- ----------------------------
INSERT INTO `roles` VALUES ('1', 'admin');
INSERT INTO `roles` VALUES ('2', 'user');

-- ----------------------------
-- Table structure for `users`
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `email` varchar(128) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `password` varchar(128) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `email` (`email`),
  KEY `role_id` (`role_id`),
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES ('1', 'wang', 'wang@163.com', '123456', '1');
INSERT INTO `users` VALUES ('2', 'zhang', 'zhang@189.com', '201512', '2');
INSERT INTO `users` VALUES ('3', 'chen', 'chen@126.com', '987654', '2');
INSERT INTO `users` VALUES ('4', 'zhou', 'zhou@163.com', '456789', '1');
INSERT INTO `users` VALUES ('5', 'tang', 'tang@itheima.com', '158104', '2');
INSERT INTO `users` VALUES ('6', 'wu', 'wu@gmail.com', '5623514', '2');
INSERT INTO `users` VALUES ('7', 'qian', 'qian@gmail.com', '1543567', '1');
INSERT INTO `users` VALUES ('8', 'liu', 'liu@itheima.com', '867322', '1');
INSERT INTO `users` VALUES ('9', 'li', 'li@163.com', '4526342', '2');
INSERT INTO `users` VALUES ('10', 'sun', 'sun@163.com', '235523', '2');
