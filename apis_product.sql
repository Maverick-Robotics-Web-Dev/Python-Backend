/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

CREATE TABLE `apis_product` (
  `status` tinyint(1) NOT NULL,
  `status_description` varchar(256) NOT NULL,
  `create_at` datetime(6) NOT NULL,
  `update_at` datetime(6) DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  `barcode` varchar(200) NOT NULL,
  `code` varchar(50) NOT NULL,
  `name` varchar(100) NOT NULL,
  `stock` bigint unsigned NOT NULL,
  `presentation` varchar(256) NOT NULL,
  `purchase_price` decimal(11,2) NOT NULL,
  `sale_price` decimal(11,2) NOT NULL,
  `number_sale` bigint unsigned NOT NULL,
  `img` varchar(256) NOT NULL,
  `due_date` date DEFAULT NULL,
  `description` varchar(256) NOT NULL,
  `fk_brand_id` int NOT NULL,
  `fk_category_id` int NOT NULL,
  `fk_supplier_id` int NOT NULL,
  `fk_user_employee_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `APIS_PRODUCT_fk_brand_id_4e02cce5_fk_APIS_BRAND_id` (`fk_brand_id`),
  KEY `APIS_PRODUCT_fk_category_id_16c11539_fk_APIS_CATEGORY_id` (`fk_category_id`),
  KEY `APIS_PRODUCT_fk_supplier_id_5db4fe95_fk_APIS_SUPPLIER_id` (`fk_supplier_id`),
  KEY `APIS_PRODUCT_fk_user_employee_id_50de0e1d_fk_APIS_USER` (`fk_user_employee_id`),
  CONSTRAINT `APIS_PRODUCT_fk_brand_id_4e02cce5_fk_APIS_BRAND_id` FOREIGN KEY (`fk_brand_id`) REFERENCES `apis_brand` (`id`),
  CONSTRAINT `APIS_PRODUCT_fk_category_id_16c11539_fk_APIS_CATEGORY_id` FOREIGN KEY (`fk_category_id`) REFERENCES `apis_category` (`id`),
  CONSTRAINT `APIS_PRODUCT_fk_supplier_id_5db4fe95_fk_APIS_SUPPLIER_id` FOREIGN KEY (`fk_supplier_id`) REFERENCES `apis_supplier` (`id`),
  CONSTRAINT `APIS_PRODUCT_fk_user_employee_id_50de0e1d_fk_APIS_USER` FOREIGN KEY (`fk_user_employee_id`) REFERENCES `apis_user_employee` (`id`),
  CONSTRAINT `apis_product_chk_1` CHECK ((`stock` >= 0)),
  CONSTRAINT `apis_product_chk_2` CHECK ((`number_sale` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `apis_product` (`status`, `status_description`, `create_at`, `update_at`, `id`, `barcode`, `code`, `name`, `stock`, `presentation`, `purchase_price`, `sale_price`, `number_sale`, `img`, `due_date`, `description`, `fk_brand_id`, `fk_category_id`, `fk_supplier_id`, `fk_user_employee_id`) VALUES
(1, 'No existe descripción', '2024-04-08 22:03:17.910435', NULL, 1, 'No posee codigo', 'GNA', 'GINA', 10, 'UNIDAD', '4.02', '4.50', 0, 'C:/Users/CHRISCHAV-PC/Downloads/1169341.jpg', NULL, 'Ninguna', 1, 1, 1, 1);
INSERT INTO `apis_product` (`status`, `status_description`, `create_at`, `update_at`, `id`, `barcode`, `code`, `name`, `stock`, `presentation`, `purchase_price`, `sale_price`, `number_sale`, `img`, `due_date`, `description`, `fk_brand_id`, `fk_category_id`, `fk_supplier_id`, `fk_user_employee_id`) VALUES
(1, 'No existe descripción', '2024-04-08 22:18:57.998386', NULL, 2, 'No posee codigo', 'RTA', 'RITA', 10, 'UNIDAD', '3.40', '3.80', 0, 'C:/Users/CHRISCHAV-PC/Downloads/1169297.jpg', NULL, 'Ninguna', 1, 1, 1, 1);
INSERT INTO `apis_product` (`status`, `status_description`, `create_at`, `update_at`, `id`, `barcode`, `code`, `name`, `stock`, `presentation`, `purchase_price`, `sale_price`, `number_sale`, `img`, `due_date`, `description`, `fk_brand_id`, `fk_category_id`, `fk_supplier_id`, `fk_user_employee_id`) VALUES
(1, 'No existe descripción', '2024-04-08 22:25:04.287428', NULL, 3, 'No posee codigo', 'XMNACV', 'XIMENA-C/V', 10, 'UNIDAD', '4.02', '4.50', 0, 'C:/Users/CHRISCHAV-PC/Downloads/7690.jpg', NULL, 'Ninguna', 1, 1, 1, 1);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;