SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

CREATE TABLE `这里写群号`  (
  `QQ` int(20) NOT NULL,
  `QQname` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `GroupNum` int(20) NULL DEFAULT NULL,
  `GroupName` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `Message` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `InsertTime` datetime NULL DEFAULT NULL,
  `self` int(20) NULL DEFAULT NULL,
  `InsertTimestamp` bigint(20) NOT NULL,
  PRIMARY KEY (`InsertTimestamp`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;

SET FOREIGN_KEY_CHECKS = 1;
