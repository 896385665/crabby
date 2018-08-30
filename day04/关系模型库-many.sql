/*
Navicat MySQL Data Transfer

Source Server         : user
Source Server Version : 80011
Source Host           : localhost:3306
Source Database       : many

Target Server Type    : MYSQL
Target Server Version : 80011
File Encoding         : 65001

Date: 2018-08-21 19:57:57
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `courses`
-- ----------------------------
DROP TABLE IF EXISTS `courses`;
CREATE TABLE `courses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of courses
-- ----------------------------
INSERT INTO `courses` VALUES ('2', '化学');
INSERT INTO `courses` VALUES ('1', '物理');
INSERT INTO `courses` VALUES ('3', '生物');

-- ----------------------------
-- Table structure for `students`
-- ----------------------------
DROP TABLE IF EXISTS `students`;
CREATE TABLE `students` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of students
-- ----------------------------
INSERT INTO `students` VALUES ('1', '王五');
INSERT INTO `students` VALUES ('2', '张三');
INSERT INTO `students` VALUES ('3', '李四');

-- ----------------------------
-- Table structure for `tb_student_course`
-- ----------------------------
DROP TABLE IF EXISTS `tb_student_course`;
CREATE TABLE `tb_student_course` (
  `student_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  PRIMARY KEY (`student_id`,`course_id`),
  KEY `course_id` (`course_id`),
  CONSTRAINT `tb_student_course_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `students` (`id`),
  CONSTRAINT `tb_student_course_ibfk_2` FOREIGN KEY (`course_id`) REFERENCES `courses` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of tb_student_course
-- ----------------------------
INSERT INTO `tb_student_course` VALUES ('1', '1');
INSERT INTO `tb_student_course` VALUES ('1', '2');
INSERT INTO `tb_student_course` VALUES ('2', '2');
INSERT INTO `tb_student_course` VALUES ('3', '2');
INSERT INTO `tb_student_course` VALUES ('1', '3');
INSERT INTO `tb_student_course` VALUES ('2', '3');
