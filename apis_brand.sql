/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

CREATE TABLE `apis_brand` (
  `status` tinyint(1) NOT NULL,
  `status_description` varchar(256) NOT NULL,
  `create_at` datetime(6) NOT NULL,
  `update_at` datetime(6) DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  `code` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `description` varchar(256) NOT NULL,
  `img` varchar(256) NOT NULL,
  `fk_user_employee_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `APIS_BRAND_fk_user_employee_id_327a1781_fk_APIS_USER_EMPLOYEE_id` (`fk_user_employee_id`),
  CONSTRAINT `APIS_BRAND_fk_user_employee_id_327a1781_fk_APIS_USER_EMPLOYEE_id` FOREIGN KEY (`fk_user_employee_id`) REFERENCES `apis_user_employee` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `apis_brand` (`status`, `status_description`, `create_at`, `update_at`, `id`, `code`, `name`, `description`, `img`, `fk_user_employee_id`) VALUES
(1, 'No existe descripción', '2024-04-08 21:29:22.484965', NULL, 1, 'TR', 'TERMOPLASTICO', 'Ninguna', 'C:/Users/CHRISCHAV-PC/Downloads/889061.jpg', 1);


/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;