/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

CREATE TABLE `apis_client` (
  `document_type` varchar(20) NOT NULL,
  `document_number` int unsigned NOT NULL,
  `lastname` varchar(500) NOT NULL,
  `country` varchar(200) NOT NULL,
  `state_province` varchar(200) NOT NULL,
  `city` varchar(200) NOT NULL,
  `address` varchar(200) NOT NULL,
  `postal_code` varchar(200) NOT NULL,
  `phone_number` varchar(50) NOT NULL,
  `cellphone_number` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `img` varchar(100) DEFAULT NULL,
  `status` tinyint(1) NOT NULL,
  `status_description` varchar(256) NOT NULL,
  `create_at` datetime(6) NOT NULL,
  `update_at` datetime(6) DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  `code` varchar(50) NOT NULL,
  `name` varchar(500) NOT NULL,
  `trade_name` varchar(500) DEFAULT NULL,
  `branch_office_address_one` varchar(200) NOT NULL,
  `branch_office_address_two` varchar(200) NOT NULL,
  `branch_office_address_three` varchar(200) NOT NULL,
  `branch_office_address_four` varchar(200) NOT NULL,
  `phone_number_one` varchar(50) NOT NULL,
  `phone_number_two` varchar(50) NOT NULL,
  `phone_number_three` varchar(50) NOT NULL,
  `phone_number_four` varchar(50) NOT NULL,
  `fk_user_employee_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `APIS_CLIENT_fk_user_employee_id_19358f18_fk_APIS_USER` (`fk_user_employee_id`),
  CONSTRAINT `APIS_CLIENT_fk_user_employee_id_19358f18_fk_APIS_USER` FOREIGN KEY (`fk_user_employee_id`) REFERENCES `apis_user_employee` (`id`),
  CONSTRAINT `apis_client_chk_1` CHECK ((`document_number` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `apis_client` (`document_type`, `document_number`, `lastname`, `country`, `state_province`, `city`, `address`, `postal_code`, `phone_number`, `cellphone_number`, `email`, `img`, `status`, `status_description`, `create_at`, `update_at`, `id`, `code`, `name`, `trade_name`, `branch_office_address_one`, `branch_office_address_two`, `branch_office_address_three`, `branch_office_address_four`, `phone_number_one`, `phone_number_two`, `phone_number_three`, `phone_number_four`, `fk_user_employee_id`) VALUES
('Cedula', 1803628419, 'Chavez', 'ECUADOR', 'TUNGURAHUA', 'AMBATO', 'fEBRES CORDERO Y JAVIER ASCAZUBI', 'S/N', 'Sin Telefono Convencional', '0981498842', 'No Posee email', '', 1, 'No existe descripción', '2024-04-08 20:42:22.542427', NULL, 1, 'CH-001', 'Christian', NULL, 'Sin Sucursal', 'Sin Sucursal', 'Sin Sucursal', 'Sin Sucursal', 'No posee numero telefonico', 'No posee numero telefonico', 'No posee numero telefonico', 'No posee numero telefonico', 1);


/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;