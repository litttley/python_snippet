/*
Navicat MySQL Data Transfer

Source Server         : 本地数据
Source Server Version : 50555
Source Host           : localhost:3306
Source Database       : itsf_nd

Target Server Type    : MYSQL
Target Server Version : 50555
File Encoding         : 65001

Date: 2018-06-23 16:27:11
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for comment
-- ----------------------------
DROP TABLE IF EXISTS `comment`;
CREATE TABLE `comment` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `COMMENT` varchar(600) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of comment
-- ----------------------------
