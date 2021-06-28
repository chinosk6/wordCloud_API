SET NAMES utf8mb4;

CREATE TABLE IF NOT EXISTS `这里写群号`  (
  `QQ` bigint(20) NOT NULL,
  `QQname` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `GroupNum` bigint(20) NULL DEFAULT NULL,
  `GroupName` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `Message` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `InsertTime` datetime NULL DEFAULT NULL,
  `self` bigint(20) NULL DEFAULT NULL,
  `InsertTimestamp` bigint(20) NOT NULL,
  PRIMARY KEY (`InsertTimestamp`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;

