-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 24, 2020 at 06:28 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.2.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sbtdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `attendance_dailyattendancestatus`
--

CREATE TABLE `attendance_dailyattendancestatus` (
  `status_id` int(11) NOT NULL,
  `is_present` tinyint(1) NOT NULL,
  `on_leave` tinyint(1) NOT NULL,
  `employee_id_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `attendance_dailyattendancestatus`
--

INSERT INTO `attendance_dailyattendancestatus` (`status_id`, `is_present`, `on_leave`, `employee_id_id`) VALUES
(1, 0, 1, NULL),
(2, 0, 1, NULL),
(3, 1, 0, 1),
(4, 0, 1, 2),
(5, 0, 1, 2),
(6, 1, 0, 2);

-- --------------------------------------------------------

--
-- Table structure for table `attendance_employee`
--

CREATE TABLE `attendance_employee` (
  `employee_id` int(11) NOT NULL,
  `vendor_id` bigint(20) NOT NULL,
  `employee_name` varchar(20) NOT NULL,
  `employee_salary` bigint(20) NOT NULL,
  `employee_mobile_no` varchar(128) NOT NULL,
  `employee_email` varchar(254) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `attendance_employee`
--

INSERT INTO `attendance_employee` (`employee_id`, `vendor_id`, `employee_name`, `employee_salary`, `employee_mobile_no`, `employee_email`) VALUES
(1, 123, 'ravi', 14254240, '+918010920174', 'ronniloreo@gmail.com'),
(2, 123, 'ravibeniwal', 14254, '+918010920174', 'ronniloreo@gmail.com'),
(3, 123, 'ravi', 45545, '+918010920174', 'ronniloreo@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(1, 'Employee');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_group_permissions`
--

INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES
(2, 1, 117),
(1, 1, 120);

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add add testimonial', 7, 'add_addtestimonial'),
(26, 'Can change add testimonial', 7, 'change_addtestimonial'),
(27, 'Can delete add testimonial', 7, 'delete_addtestimonial'),
(28, 'Can view add testimonial', 7, 'view_addtestimonial'),
(29, 'Can add categories', 8, 'add_categories'),
(30, 'Can change categories', 8, 'change_categories'),
(31, 'Can delete categories', 8, 'delete_categories'),
(32, 'Can view categories', 8, 'view_categories'),
(33, 'Can add faq', 9, 'add_faq'),
(34, 'Can change faq', 9, 'change_faq'),
(35, 'Can delete faq', 9, 'delete_faq'),
(36, 'Can view faq', 9, 'view_faq'),
(37, 'Can add feedback', 10, 'add_feedback'),
(38, 'Can change feedback', 10, 'change_feedback'),
(39, 'Can delete feedback', 10, 'delete_feedback'),
(40, 'Can view feedback', 10, 'view_feedback'),
(41, 'Can add free listing', 11, 'add_freelisting'),
(42, 'Can change free listing', 11, 'change_freelisting'),
(43, 'Can delete free listing', 11, 'delete_freelisting'),
(44, 'Can view free listing', 11, 'view_freelisting'),
(45, 'Can add frenchise contact', 12, 'add_frenchisecontact'),
(46, 'Can change frenchise contact', 12, 'change_frenchisecontact'),
(47, 'Can delete frenchise contact', 12, 'delete_frenchisecontact'),
(48, 'Can view frenchise contact', 12, 'view_frenchisecontact'),
(49, 'Can add job', 13, 'add_job'),
(50, 'Can change job', 13, 'change_job'),
(51, 'Can delete job', 13, 'delete_job'),
(52, 'Can view job', 13, 'view_job'),
(53, 'Can add order', 14, 'add_order'),
(54, 'Can change order', 14, 'change_order'),
(55, 'Can delete order', 14, 'delete_order'),
(56, 'Can view order', 14, 'view_order'),
(57, 'Can add plan', 15, 'add_plan'),
(58, 'Can change plan', 15, 'change_plan'),
(59, 'Can delete plan', 15, 'delete_plan'),
(60, 'Can view plan', 15, 'view_plan'),
(61, 'Can add pricing', 16, 'add_pricing'),
(62, 'Can change pricing', 16, 'change_pricing'),
(63, 'Can delete pricing', 16, 'delete_pricing'),
(64, 'Can view pricing', 16, 'view_pricing'),
(65, 'Can add query contact', 17, 'add_querycontact'),
(66, 'Can change query contact', 17, 'change_querycontact'),
(67, 'Can delete query contact', 17, 'delete_querycontact'),
(68, 'Can view query contact', 17, 'view_querycontact'),
(69, 'Can add service contact', 18, 'add_servicecontact'),
(70, 'Can change service contact', 18, 'change_servicecontact'),
(71, 'Can delete service contact', 18, 'delete_servicecontact'),
(72, 'Can view service contact', 18, 'view_servicecontact'),
(73, 'Can add trading', 19, 'add_trading'),
(74, 'Can change trading', 19, 'change_trading'),
(75, 'Can delete trading', 19, 'delete_trading'),
(76, 'Can view trading', 19, 'view_trading'),
(77, 'Can add upload_resume', 20, 'add_upload_resume'),
(78, 'Can change upload_resume', 20, 'change_upload_resume'),
(79, 'Can delete upload_resume', 20, 'delete_upload_resume'),
(80, 'Can view upload_resume', 20, 'view_upload_resume'),
(81, 'Can add vendor', 21, 'add_vendor'),
(82, 'Can change vendor', 21, 'change_vendor'),
(83, 'Can delete vendor', 21, 'delete_vendor'),
(84, 'Can view vendor', 21, 'view_vendor'),
(85, 'Can add top', 22, 'add_top'),
(86, 'Can change top', 22, 'change_top'),
(87, 'Can delete top', 22, 'delete_top'),
(88, 'Can view top', 22, 'view_top'),
(89, 'Can add subcategory', 23, 'add_subcategory'),
(90, 'Can change subcategory', 23, 'change_subcategory'),
(91, 'Can delete subcategory', 23, 'delete_subcategory'),
(92, 'Can view subcategory', 23, 'view_subcategory'),
(93, 'Can add sub_sub_category', 24, 'add_sub_sub_category'),
(94, 'Can change sub_sub_category', 24, 'change_sub_sub_category'),
(95, 'Can delete sub_sub_category', 24, 'delete_sub_sub_category'),
(96, 'Can view sub_sub_category', 24, 'view_sub_sub_category'),
(97, 'Can add service', 25, 'add_service'),
(98, 'Can change service', 25, 'change_service'),
(99, 'Can delete service', 25, 'delete_service'),
(100, 'Can view service', 25, 'view_service'),
(101, 'Can add profile', 26, 'add_profile'),
(102, 'Can change profile', 26, 'change_profile'),
(103, 'Can delete profile', 26, 'delete_profile'),
(104, 'Can view profile', 26, 'view_profile'),
(105, 'Can add order_ payment', 27, 'add_order_payment'),
(106, 'Can change order_ payment', 27, 'change_order_payment'),
(107, 'Can delete order_ payment', 27, 'delete_order_payment'),
(108, 'Can view order_ payment', 27, 'view_order_payment'),
(109, 'Can add contactviacategory', 28, 'add_contactviacategory'),
(110, 'Can change contactviacategory', 28, 'change_contactviacategory'),
(111, 'Can delete contactviacategory', 28, 'delete_contactviacategory'),
(112, 'Can view contactviacategory', 28, 'view_contactviacategory'),
(113, 'Can add employee', 29, 'add_employee'),
(114, 'Can change employee', 29, 'change_employee'),
(115, 'Can delete employee', 29, 'delete_employee'),
(116, 'Can view employee', 29, 'view_employee'),
(117, 'Can add daily attendance status', 30, 'add_dailyattendancestatus'),
(118, 'Can change daily attendance status', 30, 'change_dailyattendancestatus'),
(119, 'Can delete daily attendance status', 30, 'delete_dailyattendancestatus'),
(120, 'Can view daily attendance status', 30, 'view_dailyattendancestatus');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$216000$C0FlJCwVQtbO$k36EYutt9GyhZ3IlxvmTmmk9sIbSkuUe7ju0AlWIqLI=', '2020-09-14 10:57:48.911791', 1, 'root', '', '', 'ronniloreo@gmail.com', 1, 1, '2020-09-10 17:27:20.209786'),
(2, 'pbkdf2_sha256$216000$xKv2Y42kSz1V$/NQEmnC2EzoauPX7qg9s+WTqzjloYaadKlx4SS4+Eyk=', '2020-09-23 06:05:41.803642', 1, 'ap', '', '', '', 1, 1, '2020-09-10 12:49:27.573693'),
(3, 'pbkdf2_sha256$216000$urJuO94XxZFF$SGLRnf67Mz/9YCx446ysLkOuqec5SNv1DX887dKGkmc=', '2020-09-23 05:41:03.097855', 0, 'user', '', '', 'test@gmail.com', 0, 1, '2020-09-12 09:12:04.342477');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2020-09-10 17:28:10.643612', '1', 'Ravi Beniwal', 1, '[{\"added\": {}}]', 7, 1),
(2, '2020-09-10 17:28:45.513218', '2', 'Ronnil', 1, '[{\"added\": {}}]', 7, 1),
(3, '2020-09-10 17:30:00.903570', '1', 'IT  & Computer services', 1, '[{\"added\": {}}]', 8, 1),
(4, '2020-09-10 17:30:44.281003', '1', 'Android development', 1, '[{\"added\": {}}]', 23, 1),
(5, '2020-09-10 17:44:27.853101', '1', 'App design', 1, '[{\"added\": {}}]', 24, 1),
(6, '2020-09-10 17:46:14.607557', '1', 'test', 1, '[{\"added\": {}}]', 9, 1),
(7, '2020-09-10 17:56:14.287704', '1', 'SBT Market Card', 1, '[{\"added\": {}}]', 15, 1),
(8, '2020-09-10 18:05:20.853278', '1', 'Stack Softwares', 1, '[{\"added\": {}}]', 22, 1),
(9, '2020-09-12 07:06:06.250451', 'None', 'IT & Computer Service', 1, '[{\"added\": {}}]', 8, 1),
(10, '2020-09-12 07:06:25.682571', 'None', 'IT & Computer Service', 1, '[{\"added\": {}}]', 8, 1),
(11, '2020-09-12 07:30:02.342039', 'None', 'IT & Computer Service', 1, '[{\"added\": {}}]', 8, 1),
(12, '2020-09-12 07:30:12.117302', 'None', 'IT & Computer Service', 1, '[{\"added\": {}}]', 8, 1),
(13, '2020-09-12 07:33:03.044427', 'None', 'IT & Computer Service', 1, '[{\"added\": {}}]', 8, 1),
(14, '2020-09-12 07:33:12.043011', 'None', 'IT & Computer Service', 1, '[{\"added\": {}}]', 8, 1),
(15, '2020-09-12 07:36:14.633521', '2', 'IT & Computer Service', 1, '[{\"added\": {}}]', 8, 1),
(16, '2020-09-12 07:44:59.943543', '2', 'IT & Computer Service', 3, '', 8, 1),
(17, '2020-09-12 07:46:27.106513', '3', 'flower', 1, '[{\"added\": {}}]', 8, 1),
(18, '2020-09-12 07:46:34.256589', '4', 'IT & Computer Service', 1, '[{\"added\": {}}]', 8, 1),
(19, '2020-09-12 07:46:44.560870', '5', 'IT & Computer services', 1, '[{\"added\": {}}]', 8, 1),
(20, '2020-09-12 07:47:04.885656', '5', 'IT & Computer services', 3, '', 8, 1),
(21, '2020-09-12 07:47:04.886660', '4', 'IT & Computer Service', 3, '', 8, 1),
(22, '2020-09-12 07:47:04.897655', '3', 'flower', 3, '', 8, 1),
(23, '2020-09-12 07:53:37.524657', '6', 'Phones', 1, '[{\"added\": {}}]', 8, 1),
(24, '2020-09-12 07:53:44.391151', '7', 'IT & Computer services', 1, '[{\"added\": {}}]', 8, 1),
(25, '2020-09-12 07:54:27.694492', '7', 'IT & Computer services', 3, '', 8, 1),
(26, '2020-09-12 08:06:02.631422', '8', 'ravi', 1, '[{\"added\": {}}]', 8, 1),
(27, '2020-09-12 08:06:08.365197', '9', 'IT & Computer services', 1, '[{\"added\": {}}]', 8, 1),
(28, '2020-09-12 08:06:13.747367', '9', 'IT & Computer services', 3, '', 8, 1),
(29, '2020-09-12 08:22:10.008402', '10', 'IT & Computer services', 1, '[{\"added\": {}}]', 8, 1),
(30, '2020-09-12 08:23:37.334740', 'None', 'IT & Computer services', 1, '[{\"added\": {}}]', 8, 1),
(31, '2020-09-12 08:23:48.689283', '10', 'IT & Computer services', 3, '', 8, 1),
(32, '2020-09-12 08:23:53.959934', '11', 'IT & Computer services', 1, '[{\"added\": {}}]', 8, 1),
(33, '2020-09-12 08:24:02.247465', 'None', 'Phones', 1, '[{\"added\": {}}]', 8, 1),
(34, '2020-09-14 11:21:14.807922', '1', '1', 1, '[{\"added\": {}}]', 30, 1),
(35, '2020-09-14 11:21:17.718248', '2', '2', 1, '[{\"added\": {}}]', 30, 1),
(36, '2020-09-15 04:56:38.801293', '1', 'Employee', 1, '[{\"added\": {}}]', 3, 1),
(37, '2020-09-23 09:19:24.853392', '2', 'SBT Distributor Card', 1, '[{\"added\": {}}]', 15, 2),
(38, '2020-09-23 09:20:05.268099', '3', 'SBT Ultimate Super Card', 1, '[{\"added\": {}}]', 15, 2);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(30, 'attendance', 'dailyattendancestatus'),
(29, 'attendance', 'employee'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'website', 'addtestimonial'),
(8, 'website', 'categories'),
(28, 'website', 'contactviacategory'),
(9, 'website', 'faq'),
(10, 'website', 'feedback'),
(11, 'website', 'freelisting'),
(12, 'website', 'frenchisecontact'),
(13, 'website', 'job'),
(14, 'website', 'order'),
(27, 'website', 'order_payment'),
(15, 'website', 'plan'),
(16, 'website', 'pricing'),
(26, 'website', 'profile'),
(17, 'website', 'querycontact'),
(25, 'website', 'service'),
(18, 'website', 'servicecontact'),
(23, 'website', 'subcategory'),
(24, 'website', 'sub_sub_category'),
(22, 'website', 'top'),
(19, 'website', 'trading'),
(20, 'website', 'upload_resume'),
(21, 'website', 'vendor');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2020-09-10 17:23:07.175193'),
(2, 'auth', '0001_initial', '2020-09-10 17:23:12.715638'),
(3, 'admin', '0001_initial', '2020-09-10 17:24:02.189904'),
(4, 'admin', '0002_logentry_remove_auto_add', '2020-09-10 17:24:11.871427'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2020-09-10 17:24:12.011564'),
(6, 'contenttypes', '0002_remove_content_type_name', '2020-09-10 17:24:16.153119'),
(7, 'auth', '0002_alter_permission_name_max_length', '2020-09-10 17:24:21.436971'),
(8, 'auth', '0003_alter_user_email_max_length', '2020-09-10 17:24:21.861693'),
(9, 'auth', '0004_alter_user_username_opts', '2020-09-10 17:24:21.957514'),
(10, 'auth', '0005_alter_user_last_login_null', '2020-09-10 17:24:31.449091'),
(11, 'auth', '0006_require_contenttypes_0002', '2020-09-10 17:24:31.980942'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2020-09-10 17:24:32.145321'),
(13, 'auth', '0008_alter_user_username_max_length', '2020-09-10 17:24:32.384295'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2020-09-10 17:24:32.782810'),
(15, 'auth', '0010_alter_group_name_max_length', '2020-09-10 17:24:33.901141'),
(16, 'auth', '0011_update_proxy_permissions', '2020-09-10 17:24:34.286921'),
(17, 'sessions', '0001_initial', '2020-09-10 17:24:37.007318'),
(18, 'website', '0001_initial', '2020-09-10 17:25:19.597405'),
(19, 'website', '0002_order_payment_order_completed', '2020-09-10 12:11:40.709384'),
(20, 'website', '0003_auto_20200910_1743', '2020-09-10 12:13:52.362921'),
(21, 'website', '0004_auto_20200910_2016', '2020-09-10 14:47:18.021410'),
(22, 'auth', '0012_alter_user_first_name_max_length', '2020-09-10 17:23:41.999676'),
(23, 'website', '0005_auto_20200912_1135', '2020-09-12 06:05:48.541231'),
(24, 'website', '0006_auto_20200912_1742', '2020-09-12 12:12:49.494548'),
(25, 'attendance', '0001_initial', '2020-09-14 10:53:55.163566'),
(26, 'attendance', '0002_auto_20200914_1703', '2020-09-14 11:33:39.083673'),
(27, 'attendance', '0003_auto_20200914_1704', '2020-09-14 11:35:00.276655'),
(28, 'attendance', '0004_auto_20200914_1739', '2020-09-14 12:09:36.259925'),
(29, 'attendance', '0005_auto_20200914_1742', '2020-09-14 12:12:49.830677'),
(30, 'website', '0006_auto_20200919_1048', '2020-09-19 05:18:11.922385'),
(31, 'website', '0007_auto_20200919_1318', '2020-09-19 07:48:12.429383'),
(32, 'website', '0008_auto_20200923_1411', '2020-09-23 09:17:41.133189');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0m5xbf0xkmm37zrsrxwdkph1hx37uouy', 'OGQ2NTFmZTJlM2FmOWY0MmYyMzFiOTk4ZWZjNjAzYjBiMTliMWVkOTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkZmY2YzEzODM5NTViYzZlMDU2MDhjMjFiMWRhYjM1OTMyY2Y5OTdmIn0=', '2020-09-24 12:49:53.608576'),
('30j6j1btgygf1ftdisw80jgp82g9g7uv', 'e30:1kKcTL:WFq0mCpzc-6DImX5FLVlVOX-HIBRzEiuAWsJ-7beabY', '2020-10-06 07:12:19.326468'),
('3anpp8mwigndpyb241pasgtvce4iemti', 'e30:1kKc2U:WJEx8rywwdtD-6ZtnGWVdBvWe4kcBCFjKADe4pUS4xA', '2020-10-06 06:44:34.116270'),
('3grnaru1ip6rwbz4okyggn34u0w5b2jo', 'e30:1kKcLq:e6Ao-Su_I3wgRiGywWLdkizuvRc8G9o2ls9-3IsKUZ4', '2020-10-06 07:04:34.784692'),
('5a3x46p2md0pop2jop86m8manjmjwilh', 'e30:1kKcVJ:zbx8bxqwlODdBdPSJXdJ3m6EcBBHDQw4nCaNuH8CKLA', '2020-10-06 07:14:21.961902'),
('5jlaty4bd6fsomdtxwc0xsohlaaleocs', 'e30:1kKcNa:JlGe8yIqRiDjn_XdezNSIBdfYJ6sP53o9ezMWZRTJJU', '2020-10-06 07:06:22.085150'),
('6uw5g94g056lgbshf2vj6u11jo5zskak', 'e30:1kKcI0:6fevSR30kwkgHMrzGzZGurb3cmR4BaOKxIHqnPtD278', '2020-10-06 07:00:36.642563'),
('74h6qcl8c3hjh572242eu5z59qccyddv', 'e30:1kKc3f:oUmE75e_D0WfVj70X4L91tRslInj-pIsqsOwmdAD3is', '2020-10-06 06:45:47.669462'),
('77ra4n3elegzwwxl9p7eun84s7hm0cnn', 'ODBiY2UwZTk5OTZiZjdkZjRhOTVjMzhlNjYzMThjMDcwN2U5ZmFjNzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiZDY5Zjg3YmMwZGMyNGIxZDczZTFmZWZjZjVhMmEyYjVmZGQwZDY3In0=', '2020-09-24 17:27:36.753726'),
('8710kjjccnrfjic9bemfdutd1n757xzp', 'e30:1kKcQR:WGBOpnP13yj5yvEznh1VsukPi6VYtYlPTB43bk_4pTk', '2020-10-06 07:09:19.778673'),
('90aj69mdnatezzmak58709a71ne8z7da', 'e30:1kKcRZ:jFZdI7ppW_-J__c8gu4EVchHMNMRjEh_bhlih6wxH-c', '2020-10-06 07:10:29.726728'),
('919o8uararuxvssdf8piykgu2uhy1k95', 'e30:1kKcLh:B8Q3oSPff6PatJuXjjEKS1d3258nTSVop4bi3DqOvJc', '2020-10-06 07:04:25.435409'),
('b57popk131p904ynucr46sxbyhjv97ej', 'e30:1kKcP7:DIqZNMGsxyK9mAOK9Fy5Kwbj8r8Zlm0mEpVL_KLjOgA', '2020-10-06 07:07:57.322300'),
('d9qk9j41bt4qx3ey5ow753jgw5ixigmw', 'e30:1kKcST:AOBgN9x81aS282F21cIx8akzNr0lIFbO3B40wfh6kyE', '2020-10-06 07:11:25.631004'),
('ix4hmcell59u6gtw6iaigej81tts75p0', 'e30:1kKcPR:vCZUtRiFREPbI4ZufKGWN-uWcncEdxVyEGvG8L8Jk4o', '2020-10-06 07:08:17.774017'),
('ogseyb867w4xc9mu4g6v6riqetuir20l', 'e30:1kKcO0:ESMGrfUi6DwxSg6IqfDJp7YzdDLEKmwruutTzYAHTG8', '2020-10-06 07:06:48.584019'),
('p8x2wqnn1xswg862kc61v1lcg6z0f8kv', '.eJxVjEEOwiAQRe_C2hAGKDAu3fcMZIBRqoYmpV0Z765NutDtf-_9l4i0rTVunZc4FXEWIE6_W6L84LaDcqd2m2We27pMSe6KPGiX41z4eTncv4NKvX5rBzl45XIeUKUAlpjM4A05VBhAswdEA1ZnsC6xt9qyLT6lq8GChEW8P7i1NyA:1kHmBA:nCl68n2dEGdBUH1PRBg1PYBHdVLuXARdeozORN25AbE', '2020-09-28 10:57:48.915783'),
('pg8xphjebg3s1e92k7zmeix32ywdt88g', '.eJxVjMEOwiAQRP-FsyFQCnQ9eu83kF0WpGpoUtqT8d9tkx70Npn3Zt4i4LaWsLW0hInFVRhx-e0I4zPVA_AD632Wca7rMpE8FHnSJseZ0-t2un8HBVvZ17pLSVsi8s577AfNoIGsTtGZbBQMvCdrCFhFyNlpx71lxs4rZ5BAfL7mtDgN:1kH1a0:F0vWFMLJxscVip5ELWHY-NOJk35R4qXoVQzoOQUl4HA', '2020-09-26 09:12:20.809907'),
('t0dnsqnkoz2hu7pi5gd0yash28128qsq', 'e30:1kKc3I:AiVut5WLXxVBvqxoWQii5EX4HvH2KTWcqjDUixjmFNM', '2020-10-06 06:45:24.829589'),
('t1sp9p0w3ol9meefpbfv0ucz2nx0dwpd', '.eJxVjDEOAiEURO9CbQjwIYClvWcg8OHLqoFk2a2Md1eSLbSaZN6bebEQ962GfZQ1LJmdmWKn3y5FfJQ2Qb7Hdusce9vWJfGp8IMOfu25PC-H-3dQ46jftSWjiQxkg-D8TFfQGy0oIWrtXfYlEigkiQA6SnBJSQtGkbA-C_b-AOp7N7Q:1kKCTL:uuUfNEAnGqOPDalR2jawXvZKmRsdjlGGRtiZiZXOi4Y', '2020-10-05 03:26:36.000306'),
('tedvfpdwhbdmu8zqrit5ndekqq9k9k6x', 'e30:1kKcEh:-_iLpqq0htgCKxQLJ8ZsnKy5WaVloFFtMPgbo2soRfY', '2020-10-06 06:57:11.752446'),
('ush98hqjphevu29ftpwoovlr3swvviuh', 'e30:1kKcqJ:tH_tLly2ocvoHo7e8N3K1tH-E3L3fqCvohAgYcWOqY0', '2020-10-06 07:36:03.327694'),
('v42iu313k6lxvxn2ectvgzviequubtzs', 'e30:1kKcPo:z_0sKe4mdOj5hKXfqcCAq94y-TBVrCf3nmC51YUl0Kw', '2020-10-06 07:08:40.426413'),
('wnyhg3632m7jjwzpva8ko9uzn1eejvu0', 'e30:1kKb7I:Hl1zbVrO8v1GXQqYoYvbdkCSs63p_Rqwd639o-cVdGM', '2020-10-06 05:45:28.784581'),
('x1agytqyoosv3w7ch3ov5myyte3fhttf', 'OGQ2NTFmZTJlM2FmOWY0MmYyMzFiOTk4ZWZjNjAzYjBiMTliMWVkOTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkZmY2YzEzODM5NTViYzZlMDU2MDhjMjFiMWRhYjM1OTMyY2Y5OTdmIn0=', '2020-09-24 13:00:47.687208'),
('zhoo2p5w5v5pciz13o1bkizuwalu8gr0', 'e30:1kKcWC:oiQfjdk2ULsKlO7JwcW2ulw8iSiVnR_CwR58VWXhNqU', '2020-10-06 07:15:16.820517'),
('ztowg185ly2gyje99m2khq78c52rth7q', '.eJxVjDEOAiEURO9CbQjwIYClvWcg8OHLqoFk2a2Md1eSLbSaZN6bebEQ962GfZQ1LJmdmWKn3y5FfJQ2Qb7Hdusce9vWJfGp8IMOfu25PC-H-3dQ46jftSWjiQxkg-D8TFfQGy0oIWrtXfYlEigkiQA6SnBJSQtGkbA-C_b-AOp7N7Q:1kKxuP:JhFRKYIXt5CqCYViJ1IrSz2Z6AYv0iQNihpRsyor6kA', '2020-10-07 06:05:41.806636');

-- --------------------------------------------------------

--
-- Table structure for table `website_addtestimonial`
--

CREATE TABLE `website_addtestimonial` (
  `id` int(11) NOT NULL,
  `customer_name` varchar(50) NOT NULL,
  `quote` longtext NOT NULL,
  `submit_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `website_addtestimonial`
--

INSERT INTO `website_addtestimonial` (`id`, `customer_name`, `quote`, `submit_date`) VALUES
(1, 'Ravi Beniwal', 'Very Impressive customer care service.', '2020-09-10 17:28:10.642796'),
(2, 'Ronnil', 'Good experience', '2020-09-10 17:28:45.512010');

-- --------------------------------------------------------

--
-- Table structure for table `website_categories`
--

CREATE TABLE `website_categories` (
  `category_id` int(11) NOT NULL,
  `category_name` varchar(50) NOT NULL,
  `Image` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `website_categories`
--

INSERT INTO `website_categories` (`category_id`, `category_name`, `Image`) VALUES
(1, 'IT  & Computer services', 'work-from-home.svg'),
(6, 'Phones', ''),
(8, 'ravi', ''),
(11, 'IT & Computer services', '');

-- --------------------------------------------------------

--
-- Table structure for table `website_contactviacategory`
--

CREATE TABLE `website_contactviacategory` (
  `registrant_id` int(11) NOT NULL,
  `registrant_name` varchar(50) NOT NULL,
  `registrant_mobile_no` varchar(128) NOT NULL,
  `calling_time` varchar(50) NOT NULL,
  `submit_date` datetime(6) NOT NULL,
  `service_name_id` int(11) DEFAULT NULL,
  `sub_service_name_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `website_contactviacategory`
--

INSERT INTO `website_contactviacategory` (`registrant_id`, `registrant_name`, `registrant_mobile_no`, `calling_time`, `submit_date`, `service_name_id`, `sub_service_name_id`) VALUES
(1, 'test', '8010920174', '3PM - 6PM', '2020-09-10 17:31:05.947667', 1, NULL),
(2, 'test', '8010920174', '3PM - 6PM', '2020-09-10 17:34:35.007147', 1, NULL),
(3, 'test', '8010920174', '3PM - 6PM', '2020-09-10 17:36:28.101761', 1, NULL),
(4, 'test', '8010920174', '3PM - 6PM', '2020-09-10 17:38:38.911306', 1, NULL),
(5, 'test', '8010920174', '3PM - 6PM', '2020-09-10 17:38:59.196435', 1, NULL),
(6, 'test', '8010920174', '3PM - 6PM', '2020-09-10 17:42:01.436361', 1, NULL),
(7, 'test', '8010920174', '3PM - 6PM', '2020-09-10 17:43:22.568853', 1, NULL),
(8, 'test2', '8419826535112', '6PM - 9PM', '2020-09-10 17:44:49.751097', 1, 1),
(9, 'test', '34', 'Any Time', '2020-09-19 05:47:12.162596', 1, 1),
(10, 'test', '34', 'Any Time', '2020-09-19 05:47:13.493074', 1, 1),
(11, 'test', '34', 'Any Time', '2020-09-19 05:50:33.864697', 1, 1),
(12, 'adsfasdf', '234523532', 'Any Time', '2020-09-19 05:50:50.604240', 1, 1),
(13, 'sdfgsdf', '54235', 'Any Time', '2020-09-19 05:51:01.418916', 1, 1),
(14, 'sdfgsdf', '54235', 'Any Time', '2020-09-19 05:51:17.891127', 1, 1),
(15, '3245', '345', 'Any Time', '2020-09-19 05:51:26.858486', 1, 1),
(16, 'sdfgsdf', '54235', 'Any Time', '2020-09-19 05:52:18.376929', 1, 1),
(17, '23453', '23423', '3PM - 6PM', '2020-09-19 05:52:45.006042', 1, 1),
(18, '23453', '23423', '3PM - 6PM', '2020-09-19 06:07:23.616158', 1, 1),
(19, '23453', '23423', '3PM - 6PM', '2020-09-19 06:09:23.733726', 1, 1),
(20, '23453', '23423', '3PM - 6PM', '2020-09-19 06:10:14.416857', 1, 1),
(21, 'adsfas', 'dasf', 'Any Time', '2020-09-19 06:10:23.025468', 1, 1),
(22, 'danucd', 'asdfghjklq', 'Any Time', '2020-09-19 06:13:40.547591', 1, 1),
(23, 'ads', 'asdfghjklq', '3PM - 6PM', '2020-09-19 06:14:57.417435', 1, 1),
(24, 'ads', 'asdfghjklq', '6PM - 9PM', '2020-09-19 06:15:20.943258', 1, 1),
(25, 'sdfsf', 'sdfd', '6PM - 9PM', '2020-09-19 06:17:24.240987', 1, 1),
(26, 'sdfsf', 'sdfd', '6PM - 9PM', '2020-09-19 06:19:15.495196', 1, 1),
(27, 'asfasd', 'asdfghjklq', '6PM - 9PM', '2020-09-19 06:19:33.640329', 1, 1),
(28, 'asfasd', 'asdfghjklq', '6PM - 9PM', '2020-09-19 06:24:36.492881', 1, 1),
(29, 'sdfsf', 'sdfd', '6PM - 9PM', '2020-09-19 06:26:51.879947', 1, 1),
(30, 'asdff', 'asdfghjklq', 'Any Time', '2020-09-19 06:27:32.150849', 1, 1),
(31, 'akarsh', '8708046736', '3PM - 6PM', '2020-09-19 06:29:27.578167', 1, 1),
(32, 'lalu', '1123456789', '6PM - 9PM', '2020-09-19 06:31:38.841045', 1, 1),
(33, 'spiderman', '8708046736', '6PM - 9PM', '2020-09-19 06:32:46.044538', 1, 1),
(34, 'asd', '8708046736', '6PM - 9PM', '2020-09-19 06:34:14.865775', 1, 1),
(35, 'dsfasf', '435345', '3PM - 6PM', '2020-09-19 06:35:51.073825', 1, 1),
(36, 'asd', '8708046736', '6PM - 9PM', '2020-09-19 06:37:05.400383', 1, 1),
(37, 'sdf', '435345', 'Any Time', '2020-09-19 06:37:18.342640', 1, 1),
(38, 'sdf', '435345', 'Any Time', '2020-09-19 06:40:22.037556', 1, 1),
(39, 'addfg', '56345636', '6PM - 9PM', '2020-09-19 06:41:21.977251', 1, 1),
(40, 'akarsh', '9416733262', '6PM - 9PM', '2020-09-19 06:43:09.750743', 1, 1),
(41, 'akarsh', '44444', '6PM - 9PM', '2020-09-19 06:45:48.410940', 1, 1),
(42, 'test', '34343434', '6PM - 9PM', '2020-09-19 06:46:38.685044', 1, 1),
(43, 'test', '34343434', '6PM - 9PM', '2020-09-19 06:47:47.454434', 1, 1),
(44, 'akarsh', '44444', '6PM - 9PM', '2020-09-19 06:49:31.149938', 1, 1),
(45, 'akarsh', '44444', '6PM - 9PM', '2020-09-19 06:49:50.534482', 1, 1),
(46, 'akarsh', '44444', '6PM - 9PM', '2020-09-19 06:50:20.614579', 1, 1),
(47, 'bhaisaveghoja', '45454545', '3PM - 6PM', '2020-09-19 06:50:54.364359', 1, 1),
(48, 'bunny', '3432', '6PM - 9PM', '2020-09-19 06:56:27.470848', 1, 1),
(49, 'bunny', '3432', '6PM - 9PM', '2020-09-19 07:10:45.024228', 1, 1),
(50, 'akarsh', '666666', '6PM - 9PM', '2020-09-19 07:11:00.908386', 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `website_faq`
--

CREATE TABLE `website_faq` (
  `question_id` int(11) NOT NULL,
  `question_category` varchar(100) NOT NULL,
  `market_executive_name` varchar(50) NOT NULL,
  `submit_date` datetime(6) NOT NULL,
  `question` longtext NOT NULL,
  `answer` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `website_faq`
--

INSERT INTO `website_faq` (`question_id`, `question_category`, `market_executive_name`, `submit_date`, `question`, `answer`) VALUES
(1, 'test', 'test', '2020-09-10 17:46:14.606673', '<p>testing</p>', '<p>test</p>');

-- --------------------------------------------------------

--
-- Table structure for table `website_feedback`
--

CREATE TABLE `website_feedback` (
  `customer_id` int(11) NOT NULL,
  `feed_back` varchar(50) NOT NULL,
  `submit_date` datetime(6) NOT NULL,
  `Comments` longtext NOT NULL,
  `customer_name` varchar(50) NOT NULL,
  `email` varchar(254) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `website_feedback`
--

INSERT INTO `website_feedback` (`customer_id`, `feed_back`, `submit_date`, `Comments`, `customer_name`, `email`) VALUES
(1, 'Average', '2020-09-10 17:49:04.771957', 'asa', 'test', 'test@gmail.com'),
(2, 'Average', '2020-09-10 17:50:40.325893', 'asa', 'test', 'test@gmail.com'),
(3, 'Very Good', '2020-09-22 05:19:26.756831', 'sd', 'Suraj Auto Works', 'test@test.com'),
(4, 'Very Good', '2020-09-22 05:20:15.974806', 'sd', 'Suraj Auto Works', 'test@test.com');

-- --------------------------------------------------------

--
-- Table structure for table `website_freelisting`
--

CREATE TABLE `website_freelisting` (
  `vendor_id` int(11) NOT NULL,
  `Company_name` varchar(50) NOT NULL,
  `location` varchar(50) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL,
  `zip_code` int(11) NOT NULL,
  `mobile` bigint(20) NOT NULL,
  `submit_date` datetime(6) NOT NULL,
  `email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `website_freelisting`
--

INSERT INTO `website_freelisting` (`vendor_id`, `Company_name`, `location`, `first_name`, `last_name`, `city`, `state`, `zip_code`, `mobile`, `submit_date`, `email`) VALUES
(1, 'testjisjd', 'test', 'test', 'test', 'test', 'test', 121005, 8010920174, '2020-09-10 17:51:57.356735', 'test@gmail.com'),
(2, 'dance studio', 'mumbai', 'oreo', 'ddff', 'dfdsf', 'fdfd', 121005, 8010920174, '2020-09-22 05:13:19.828728', 'test@test.com'),
(3, 'dance studio', 'mumbai', 'oreo', 'ddff', 'dfdsf', 'fdfd', 121005, 8010920174, '2020-09-22 05:14:39.719035', 'test@test.com'),
(4, 'dance studio', 'mumbai', 'Arsh', 'Cosmetics', 'Taraori', 'Haryana', 132116, 9050342348, '2020-09-22 05:15:23.218371', 'test@test.com'),
(5, 'dance studio', 'mumbai', 'Shiv', 'Dairy', 'Karnal', 'Haryana', 132001, 8816020231, '2020-09-22 05:15:58.469454', 'test@test.com'),
(6, 'dance studio', 'mumbai', 'Golden', 'Gym', 'Karnal', 'Haryana', 132001, 8053433932, '2020-09-22 05:16:31.771040', 'test@test.com'),
(7, 'dance studio', 'mumbai', 'Sisodiya', 'Works', 'Karnal', 'Haryana', 132001, 9671144609, '2020-09-22 05:17:48.293681', 'test@test.com');

-- --------------------------------------------------------

--
-- Table structure for table `website_frenchisecontact`
--

CREATE TABLE `website_frenchisecontact` (
  `customer_id` int(11) NOT NULL,
  `customer_name` varchar(50) NOT NULL,
  `email` varchar(254) NOT NULL,
  `mobile_no` varchar(128) NOT NULL,
  `address` varchar(200) NOT NULL,
  `frenchise_option` varchar(50) NOT NULL,
  `submit_time` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `website_frenchisecontact`
--

INSERT INTO `website_frenchisecontact` (`customer_id`, `customer_name`, `email`, `mobile_no`, `address`, `frenchise_option`, `submit_time`) VALUES
(1, 'test', 'test@gmail.com', '8010920174', 'test address', 'Tehsil ( ₹ 25,000 to  ₹ 50,000)', '2020-09-10 17:52:52.694870');

-- --------------------------------------------------------

--
-- Table structure for table `website_job`
--

CREATE TABLE `website_job` (
  `seeker_id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `mobile` bigint(20) NOT NULL,
  `submit_date` datetime(6) NOT NULL,
  `education` varchar(200) NOT NULL,
  `experience` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `website_job`
--

INSERT INTO `website_job` (`seeker_id`, `name`, `mobile`, `submit_date`, `education`, `experience`) VALUES
(1, 'ravi', 8010920174, '2020-09-10 17:53:41.036797', 'empundnsndsldjskajdkls', 'nothing man just a fresher'),
(2, 'ravi', 8010920174, '2020-09-10 17:54:21.713036', 'empundnsndsldjskajdkls', 'nothing man just a fresher');

-- --------------------------------------------------------

--
-- Table structure for table `website_order`
--

CREATE TABLE `website_order` (
  `id` int(11) NOT NULL,
  `order_id` int(11) NOT NULL,
  `email_id` varchar(45) NOT NULL,
  `name` varchar(20) NOT NULL,
  `phone` varchar(128) NOT NULL,
  `address` varchar(111) NOT NULL,
  `state` varchar(111) NOT NULL,
  `city` varchar(111) NOT NULL,
  `order_date` datetime(6) NOT NULL,
  `zip_code` varchar(8) NOT NULL,
  `amount` int(11) NOT NULL,
  `plan_id_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `order_completed` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `website_order`
--

INSERT INTO `website_order` (`id`, `order_id`, `email_id`, `name`, `phone`, `address`, `state`, `city`, `order_date`, `zip_code`, `amount`, `plan_id_id`, `user_id`, `order_completed`) VALUES
(1, 3286, 'paliwalap7@gmail.com', 'Akarsh', '144', ' Asd', 'Asd', 'Asd', '2020-09-10 12:55:00.299812', 'Asd', 100, 1, 2, 0),
(2, 7387, 'test@test.com', 'Akarsh', '2342', ' asds', 'asds', 'asds', '2020-09-10 13:05:57.172297', '232', 2300, 1, 2, 0),
(3, 7047, 'test@test.com', 'Akarsh', 'sdfa', ' asdd', 'asd', 'asd', '2020-09-10 14:07:46.888090', '22112', 1200, 1, 2, 0),
(4, 5409, 'test@test.com', 'test', '321', ' ads', 'ads', 'ads', '2020-09-10 14:35:27.035532', '321', 100, 1, 2, 0),
(5, 7639, 'bunny@test.com', 'Bunny', '34224', ' ads', 'ads', 'ads', '2020-09-10 14:45:04.874671', '2321', 100, 1, 2, 0),
(6, 6979, 'test@test.com', 'test', 'ads', ' ads', 'ads', 'das', '2020-09-19 05:10:17.005180', 'ads', 500, 1, 3, 0),
(7, 6905, 'test@test.com', 'test', 'ads', ' ads', 'ads', 'das', '2020-09-19 05:18:31.741688', 'ads', 100, 1, 3, 0),
(8, 3128, 'test@test.com', 'tedst', 'asdfasdfasdf', ' ads', 'ads', 'ads', '2020-09-19 05:18:57.177454', 'da', 300, 1, 3, 0),
(9, 451, 'test@tet.con', 'test', 'ets', ' test', 'test', 'etst', '2020-09-19 05:28:30.692869', 'etst', 2300, 1, 3, 0),
(10, 6262, 'test@tet.con', 'test', 'ets', ' test', 'test', 'etst', '2020-09-19 05:31:02.043633', 'etst', 100, 1, 3, 0),
(11, 1013, 'test@test.com', 'test', 'asd', ' ads', 'dasd', 'ads', '2020-09-19 11:48:36.855834', 'ds', 100, 1, 2, 0),
(12, 2618, 'test@test.com', 'test', 'asd', ' ads', 'dasd', 'ads', '2020-09-19 11:49:21.918670', 'ds', 100, 1, 2, 0),
(13, 9398, 'test@test.com', 'test', 'asd', ' ads', 'dasd', 'ads', '2020-09-19 11:59:31.811729', '34', 100, 1, 2, 0),
(14, 6353, 'test@test.com', 'test', 'asd', ' ads', 'dasd', 'ads', '2020-09-19 12:00:51.447468', '34', 100, 1, 2, 0),
(15, 5054, 'test@test.com', 'test', 'asd', ' ads', 'dasd', 'ads', '2020-09-19 12:02:17.786105', '12', 100, 1, 2, 0),
(16, 3829, 'test@test.com', 'Akarsh', 'df', ' da', 'asdf', 'asd', '2020-09-19 12:04:09.990401', '123', 100, 1, 2, 0),
(17, 3798, 'test@test.com', 'Akarsh', 'df', ' da', 'asdf', 'asd', '2020-09-19 12:04:50.818233', 'sfsdf', 100, 1, 2, 0),
(18, 9050, 'test@test.com', 'Akarsh', '2345234545455', ' da', 'asdf', 'asd', '2020-09-19 12:06:31.442816', '3453', 100, 1, 2, 0),
(19, 2503, 'test@test.com', 'Akarsh', '2345234545', ' da', 'asdf', 'asd', '2020-09-19 12:07:12.659038', '3453', 100, 1, 2, 0),
(20, 7921, 'test@test.com', 'Manjeet Arts', '9812008100', ' Near Guru Nanak Girls School , Bus Stand', 'Haryana', 'Karnal', '2020-09-22 05:11:08.072238', '1212', 1000, 1, 3, 0),
(21, 7618, 'test@test.com', 'test', '1234567890', ' ads', 'ads', 'ads', '2020-09-23 04:53:54.771138', '2324', 100, 1, 2, 0),
(22, 2274, 'RAY@TECH.COM', 'rAY', '9416172154', ' Basant Vihar', 'Haryana', 'Karnal', '2020-09-23 05:05:35.480488', '132001', 1200, 1, 2, 0),
(23, 3405, 'name@test.com', 'name', '9812008100', ' Near Guru Nanak Girls School , Bus Stand', 'Haryana', 'Karnal', '2020-09-23 05:18:02.438746', '1212', 100, 1, 2, 0),
(24, 6117, 'name2@test.com', 'name2', '9812008100', ' Near Guru Nanak Girls School , Bus Stand', 'Haryana', 'Karnal', '2020-09-23 05:35:47.727112', '1212', 100, 1, 2, 0),
(25, 312, 'nummy@test.com', 'name3', '8053433932', ' Committee Chowk', 'Haryana', 'Karnal', '2020-09-23 06:07:07.150773', '132001', 100, 1, 2, 0);

-- --------------------------------------------------------

--
-- Table structure for table `website_order_payment`
--

CREATE TABLE `website_order_payment` (
  `id` int(11) NOT NULL,
  `currency` varchar(8) NOT NULL,
  `gateway_name` varchar(25) NOT NULL,
  `response_message` longtext NOT NULL,
  `bank_name` varchar(25) NOT NULL,
  `Payment_mode` varchar(25) NOT NULL,
  `response_code` varchar(3) NOT NULL,
  `txn_id` longtext NOT NULL,
  `txn_amount` varchar(9) NOT NULL,
  `order_id` int(11) NOT NULL,
  `status` varchar(12) NOT NULL,
  `bank_txn_id` varchar(12) NOT NULL,
  `txn_date` varchar(23) NOT NULL,
  `refund_amount` int(11) NOT NULL,
  `order_summary_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `website_order_payment`
--

INSERT INTO `website_order_payment` (`id`, `currency`, `gateway_name`, `response_message`, `bank_name`, `Payment_mode`, `response_code`, `txn_id`, `txn_amount`, `order_id`, `status`, `bank_txn_id`, `txn_date`, `refund_amount`, `order_summary_id`) VALUES
(1, 'INR', 'AXIS', 'Txn Success', '', 'NB', '01', '20200910111212800110168843001874677', '1200.00', 7047, 'PENDING', '15690470654', '2020-09-10 19:37:56.0', 0, 3),
(2, 'INR', 'ICICI', 'Your payment has been declined by your bank. Please try again or use a different method to complete the payment.', '', 'NB', '227', '20200910111212800110168479101893280', '100.00', 7639, 'PENDING', '12860362154', '2020-09-10 20:15:03.0', 0, 5),
(3, 'INR', 'HDFC', 'Your payment has been declined by your bank. Please try again or use a different method to complete the payment.', '', 'NB', '227', '20200923111212800110168103301906161', '100.00', 7618, 'PENDING', '19507849858', '2020-09-23 10:23:57.0', 0, 21),
(4, 'INR', 'HDFC', 'Txn Success', 'HDFC', 'NB', '01', '20200923111212800110168272801919595', '1200.00', 2274, 'TXN_SUCCESS', '10804304956', '2020-09-23 10:35:38.0', 0, 22),
(5, 'INR', 'HDFC', 'Txn Success', '', 'NB', '01', '20200923111212800110168301402032582', '100.00', 3405, 'PENDING', '19957532343', '2020-09-23 10:48:05.0', 0, 23),
(6, 'INR', 'ICICI', 'Your payment has been declined by your bank. Please try again or use a different method to complete the payment.', '', 'NB', '227', '20200923111212800110168070901932289', '100.00', 6117, 'PENDING', '17382177707', '2020-09-23 11:05:50.0', 0, 24);

-- --------------------------------------------------------

--
-- Table structure for table `website_plan`
--

CREATE TABLE `website_plan` (
  `plan_id` int(11) NOT NULL,
  `plan_name` varchar(25) NOT NULL,
  `plan_amount` int(11) NOT NULL,
  `description_1` varchar(50) DEFAULT NULL,
  `description_2` varchar(50) DEFAULT NULL,
  `description_3` varchar(50) DEFAULT NULL,
  `description_4` varchar(50) DEFAULT NULL,
  `maximum_discount` int(11) NOT NULL,
  `minimum_discount` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `website_plan`
--

INSERT INTO `website_plan` (`plan_id`, `plan_name`, `plan_amount`, `description_1`, `description_2`, `description_3`, `description_4`, `maximum_discount`, `minimum_discount`) VALUES
(1, 'SBT Market Card', 30, 'Discount from 1% upto 30% based on Market card.', 'Training your team', 'Discount on mobile recharges,Flights,etc', '24/7 Customer service', 30, 0),
(2, 'SBT Distributor Card', 200, 'Test', 'Test', 'Test', 'Test', 60, 30),
(3, 'SBT Ultimate Super Card', 300, 'Test', 'Test', 'Test', 'Test', 100, 60);

-- --------------------------------------------------------

--
-- Table structure for table `website_pricing`
--

CREATE TABLE `website_pricing` (
  `id` int(11) NOT NULL,
  `name` varchar(27) NOT NULL,
  `description` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `website_profile`
--

CREATE TABLE `website_profile` (
  `id` int(11) NOT NULL,
  `Fathers_name` varchar(50) NOT NULL,
  `Mobile_No` varchar(128) NOT NULL,
  `Mobile_No_2` varchar(128) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `City` varchar(100) NOT NULL,
  `State` varchar(100) NOT NULL,
  `PinCode` int(11) NOT NULL,
  `Gross_Salary` int(11) NOT NULL,
  `Gender` varchar(100) NOT NULL,
  `Date_of_Birth` date DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `website_querycontact`
--

CREATE TABLE `website_querycontact` (
  `query_id` int(11) NOT NULL,
  `customer_name` varchar(50) NOT NULL,
  `mobile` varchar(128) NOT NULL,
  `submit_date` datetime(6) NOT NULL,
  `message` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `website_querycontact`
--

INSERT INTO `website_querycontact` (`query_id`, `customer_name`, `mobile`, `submit_date`, `message`) VALUES
(1, 'ravi', '4461515120425', '2020-09-10 17:47:54.010103', 'nothing');

-- --------------------------------------------------------

--
-- Table structure for table `website_service`
--

CREATE TABLE `website_service` (
  `service_id` int(11) NOT NULL,
  `service_name` varchar(50) NOT NULL,
  `category_title` varchar(150) NOT NULL,
  `price` int(11) NOT NULL,
  `service_desc` longtext NOT NULL,
  `publish_date` datetime(6) NOT NULL,
  `Image` varchar(100) NOT NULL,
  `category_id` int(11) NOT NULL,
  `subcategory_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `website_servicecontact`
--

CREATE TABLE `website_servicecontact` (
  `registrant_id` int(11) NOT NULL,
  `registrant_name` varchar(50) NOT NULL,
  `registrant_mobile_no` varchar(128) NOT NULL,
  `submit_date` datetime(6) NOT NULL,
  `registrant_interest` varchar(50) NOT NULL,
  `registrant_query` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `website_subcategory`
--

CREATE TABLE `website_subcategory` (
  `subcategory_id` int(11) NOT NULL,
  `sub_category_name` varchar(50) NOT NULL,
  `category_name_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `website_subcategory`
--

INSERT INTO `website_subcategory` (`subcategory_id`, `sub_category_name`, `category_name_id`) VALUES
(1, 'Android development', 1);

-- --------------------------------------------------------

--
-- Table structure for table `website_sub_sub_category`
--

CREATE TABLE `website_sub_sub_category` (
  `subcategory_id` int(11) NOT NULL,
  `sub_sub_category_name` varchar(50) NOT NULL,
  `sub_category_name_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `website_sub_sub_category`
--

INSERT INTO `website_sub_sub_category` (`subcategory_id`, `sub_sub_category_name`, `sub_category_name_id`) VALUES
(1, 'App design', 1);

-- --------------------------------------------------------

--
-- Table structure for table `website_top`
--

CREATE TABLE `website_top` (
  `vendor_id` int(11) NOT NULL,
  `vendor_name` varchar(50) NOT NULL,
  `vendor_work_desc` longtext NOT NULL,
  `address` varchar(100) NOT NULL,
  `state` varchar(100) NOT NULL,
  `city` varchar(100) NOT NULL,
  `vendor_mobile_no` varchar(128) NOT NULL,
  `vendor_email` varchar(254) DEFAULT NULL,
  `Image` varchar(100) NOT NULL,
  `Busniess_Type_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `website_top`
--

INSERT INTO `website_top` (`vendor_id`, `vendor_name`, `vendor_work_desc`, `address`, `state`, `city`, `vendor_mobile_no`, `vendor_email`, `Image`, `Busniess_Type_id`) VALUES
(1, 'Stack Softwares', '<p>testing</p>', 'test address', 'haryana', 'karnal', '+918010920174', NULL, 'website/images/TOPvendors/eleni-afiontzi-gLU8GZpHtRA-unsplash.jpg', 1);

-- --------------------------------------------------------

--
-- Table structure for table `website_trading`
--

CREATE TABLE `website_trading` (
  `customer_id` int(11) NOT NULL,
  `customer_name` varchar(50) NOT NULL,
  `product_name` varchar(50) NOT NULL,
  `address_from` varchar(50) NOT NULL,
  `address_to` varchar(50) NOT NULL,
  `submit_date` datetime(6) NOT NULL,
  `zip_code` int(11) NOT NULL,
  `mobile` varchar(128) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `website_upload_resume`
--

CREATE TABLE `website_upload_resume` (
  `resume_id` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `filling_date` datetime(6) NOT NULL,
  `Resume` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `website_upload_resume`
--

INSERT INTO `website_upload_resume` (`resume_id`, `name`, `filling_date`, `Resume`) VALUES
(1, 'ravi', '2020-09-10 17:55:00.239993', 'Mr.Ravi_InternshalaResume.pdf'),
(2, 'ravi', '2020-09-12 06:08:06.755010', 'website/resumes/dummy.pdf'),
(3, 'ravi', '2020-09-12 06:13:06.430372', 'website/JobResumes/dummy.pdf'),
(4, 'ravi', '2020-09-12 06:17:31.724494', 'website/JobResumes/dummy_4NwMJgi.pdf'),
(5, 'fdfd', '2020-09-22 05:21:31.847989', 'website/JobResumes/Doc_Sep_20_2020.pdf'),
(6, 'fdfd', '2020-09-22 05:23:06.246502', 'website/JobResumes/Doc_Sep_20_2020_w4P4MdS.pdf');

-- --------------------------------------------------------

--
-- Table structure for table `website_vendor`
--

CREATE TABLE `website_vendor` (
  `vendor_id` int(11) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Company_Name` varchar(100) NOT NULL,
  `Service_decsription` longtext NOT NULL,
  `Mobile_No` varchar(128) NOT NULL,
  `Mobile_No_2` varchar(128) NOT NULL,
  `Address1` varchar(100) NOT NULL,
  `Address2` varchar(100) DEFAULT NULL,
  `city` varchar(100) NOT NULL,
  `state` varchar(100) NOT NULL,
  `PinCode` int(11) NOT NULL,
  `Contact_Person` varchar(100) DEFAULT NULL,
  `EmailID` varchar(254) DEFAULT NULL,
  `Landline` varchar(128) DEFAULT NULL,
  `GST_No` int(11) DEFAULT NULL,
  `Pan_No` int(11) DEFAULT NULL,
  `TIN_No` int(11) DEFAULT NULL,
  `Registered_Trade_Name` varchar(100) DEFAULT NULL,
  `Facebook_URL` varchar(200) DEFAULT NULL,
  `Twitter_URL` varchar(200) DEFAULT NULL,
  `website_URL` varchar(200) DEFAULT NULL,
  `Status` varchar(20) NOT NULL,
  `Other_Info` varchar(200) DEFAULT NULL,
  `Discount_Percentage` int(11) DEFAULT NULL,
  `Longitude` double DEFAULT NULL,
  `Latitude` double DEFAULT NULL,
  `submit_date` datetime(6) NOT NULL,
  `Image` varchar(100) NOT NULL,
  `Busniess_Type_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `attendance_dailyattendancestatus`
--
ALTER TABLE `attendance_dailyattendancestatus`
  ADD PRIMARY KEY (`status_id`),
  ADD KEY `attendance_dailyatte_employee_id_id_9e7be119_fk_attendanc` (`employee_id_id`);

--
-- Indexes for table `attendance_employee`
--
ALTER TABLE `attendance_employee`
  ADD PRIMARY KEY (`employee_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `website_addtestimonial`
--
ALTER TABLE `website_addtestimonial`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `website_categories`
--
ALTER TABLE `website_categories`
  ADD PRIMARY KEY (`category_id`);

--
-- Indexes for table `website_contactviacategory`
--
ALTER TABLE `website_contactviacategory`
  ADD PRIMARY KEY (`registrant_id`),
  ADD KEY `website_contactviaca_service_name_id_83a40c2b_fk_website_s` (`service_name_id`),
  ADD KEY `website_contactviaca_sub_service_name_id_dd22ba6f_fk_website_s` (`sub_service_name_id`);

--
-- Indexes for table `website_faq`
--
ALTER TABLE `website_faq`
  ADD PRIMARY KEY (`question_id`);

--
-- Indexes for table `website_feedback`
--
ALTER TABLE `website_feedback`
  ADD PRIMARY KEY (`customer_id`);

--
-- Indexes for table `website_freelisting`
--
ALTER TABLE `website_freelisting`
  ADD PRIMARY KEY (`vendor_id`);

--
-- Indexes for table `website_frenchisecontact`
--
ALTER TABLE `website_frenchisecontact`
  ADD PRIMARY KEY (`customer_id`);

--
-- Indexes for table `website_job`
--
ALTER TABLE `website_job`
  ADD PRIMARY KEY (`seeker_id`);

--
-- Indexes for table `website_order`
--
ALTER TABLE `website_order`
  ADD PRIMARY KEY (`id`),
  ADD KEY `website_order_plan_id_id_1aebf333_fk_website_plan_plan_id` (`plan_id_id`),
  ADD KEY `website_order_user_id_13a763ad_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `website_order_payment`
--
ALTER TABLE `website_order_payment`
  ADD PRIMARY KEY (`id`),
  ADD KEY `website_order_paymen_order_summary_id_3b905a9d_fk_website_o` (`order_summary_id`);

--
-- Indexes for table `website_plan`
--
ALTER TABLE `website_plan`
  ADD PRIMARY KEY (`plan_id`);

--
-- Indexes for table `website_pricing`
--
ALTER TABLE `website_pricing`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `website_profile`
--
ALTER TABLE `website_profile`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `website_querycontact`
--
ALTER TABLE `website_querycontact`
  ADD PRIMARY KEY (`query_id`);

--
-- Indexes for table `website_service`
--
ALTER TABLE `website_service`
  ADD PRIMARY KEY (`service_id`),
  ADD KEY `website_service_category_id_6f210761_fk_website_c` (`category_id`),
  ADD KEY `website_service_subcategory_id_f1989863_fk_website_s` (`subcategory_id`);

--
-- Indexes for table `website_servicecontact`
--
ALTER TABLE `website_servicecontact`
  ADD PRIMARY KEY (`registrant_id`);

--
-- Indexes for table `website_subcategory`
--
ALTER TABLE `website_subcategory`
  ADD PRIMARY KEY (`subcategory_id`),
  ADD KEY `website_subcategory_category_name_id_d95bf90d_fk_website_c` (`category_name_id`);

--
-- Indexes for table `website_sub_sub_category`
--
ALTER TABLE `website_sub_sub_category`
  ADD PRIMARY KEY (`subcategory_id`),
  ADD KEY `website_sub_sub_cate_sub_category_name_id_994270b1_fk_website_s` (`sub_category_name_id`);

--
-- Indexes for table `website_top`
--
ALTER TABLE `website_top`
  ADD PRIMARY KEY (`vendor_id`),
  ADD KEY `website_top_Busniess_Type_id_840a1280_fk_website_c` (`Busniess_Type_id`);

--
-- Indexes for table `website_trading`
--
ALTER TABLE `website_trading`
  ADD PRIMARY KEY (`customer_id`);

--
-- Indexes for table `website_upload_resume`
--
ALTER TABLE `website_upload_resume`
  ADD PRIMARY KEY (`resume_id`);

--
-- Indexes for table `website_vendor`
--
ALTER TABLE `website_vendor`
  ADD PRIMARY KEY (`vendor_id`),
  ADD KEY `website_vendor_Busniess_Type_id_fd71f8a7_fk_website_c` (`Busniess_Type_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `attendance_dailyattendancestatus`
--
ALTER TABLE `attendance_dailyattendancestatus`
  MODIFY `status_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `attendance_employee`
--
ALTER TABLE `attendance_employee`
  MODIFY `employee_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=121;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `website_addtestimonial`
--
ALTER TABLE `website_addtestimonial`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `website_categories`
--
ALTER TABLE `website_categories`
  MODIFY `category_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `website_contactviacategory`
--
ALTER TABLE `website_contactviacategory`
  MODIFY `registrant_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- AUTO_INCREMENT for table `website_faq`
--
ALTER TABLE `website_faq`
  MODIFY `question_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `website_feedback`
--
ALTER TABLE `website_feedback`
  MODIFY `customer_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `website_freelisting`
--
ALTER TABLE `website_freelisting`
  MODIFY `vendor_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `website_frenchisecontact`
--
ALTER TABLE `website_frenchisecontact`
  MODIFY `customer_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `website_job`
--
ALTER TABLE `website_job`
  MODIFY `seeker_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `website_order`
--
ALTER TABLE `website_order`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `website_order_payment`
--
ALTER TABLE `website_order_payment`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `website_plan`
--
ALTER TABLE `website_plan`
  MODIFY `plan_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `website_pricing`
--
ALTER TABLE `website_pricing`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `website_profile`
--
ALTER TABLE `website_profile`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `website_querycontact`
--
ALTER TABLE `website_querycontact`
  MODIFY `query_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `website_service`
--
ALTER TABLE `website_service`
  MODIFY `service_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `website_servicecontact`
--
ALTER TABLE `website_servicecontact`
  MODIFY `registrant_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `website_subcategory`
--
ALTER TABLE `website_subcategory`
  MODIFY `subcategory_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `website_sub_sub_category`
--
ALTER TABLE `website_sub_sub_category`
  MODIFY `subcategory_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `website_top`
--
ALTER TABLE `website_top`
  MODIFY `vendor_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `website_trading`
--
ALTER TABLE `website_trading`
  MODIFY `customer_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `website_upload_resume`
--
ALTER TABLE `website_upload_resume`
  MODIFY `resume_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `website_vendor`
--
ALTER TABLE `website_vendor`
  MODIFY `vendor_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `attendance_dailyattendancestatus`
--
ALTER TABLE `attendance_dailyattendancestatus`
  ADD CONSTRAINT `attendance_dailyatte_employee_id_id_9e7be119_fk_attendanc` FOREIGN KEY (`employee_id_id`) REFERENCES `attendance_employee` (`employee_id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `website_contactviacategory`
--
ALTER TABLE `website_contactviacategory`
  ADD CONSTRAINT `website_contactviaca_service_name_id_83a40c2b_fk_website_s` FOREIGN KEY (`service_name_id`) REFERENCES `website_subcategory` (`subcategory_id`),
  ADD CONSTRAINT `website_contactviaca_sub_service_name_id_dd22ba6f_fk_website_s` FOREIGN KEY (`sub_service_name_id`) REFERENCES `website_sub_sub_category` (`subcategory_id`);

--
-- Constraints for table `website_order`
--
ALTER TABLE `website_order`
  ADD CONSTRAINT `website_order_plan_id_id_1aebf333_fk_website_plan_plan_id` FOREIGN KEY (`plan_id_id`) REFERENCES `website_plan` (`plan_id`),
  ADD CONSTRAINT `website_order_user_id_13a763ad_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `website_order_payment`
--
ALTER TABLE `website_order_payment`
  ADD CONSTRAINT `website_order_paymen_order_summary_id_3b905a9d_fk_website_o` FOREIGN KEY (`order_summary_id`) REFERENCES `website_order` (`id`);

--
-- Constraints for table `website_profile`
--
ALTER TABLE `website_profile`
  ADD CONSTRAINT `website_profile_user_id_87886a5c_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `website_service`
--
ALTER TABLE `website_service`
  ADD CONSTRAINT `website_service_category_id_6f210761_fk_website_c` FOREIGN KEY (`category_id`) REFERENCES `website_categories` (`category_id`),
  ADD CONSTRAINT `website_service_subcategory_id_f1989863_fk_website_s` FOREIGN KEY (`subcategory_id`) REFERENCES `website_subcategory` (`subcategory_id`);

--
-- Constraints for table `website_subcategory`
--
ALTER TABLE `website_subcategory`
  ADD CONSTRAINT `website_subcategory_category_name_id_d95bf90d_fk_website_c` FOREIGN KEY (`category_name_id`) REFERENCES `website_categories` (`category_id`);

--
-- Constraints for table `website_sub_sub_category`
--
ALTER TABLE `website_sub_sub_category`
  ADD CONSTRAINT `website_sub_sub_cate_sub_category_name_id_994270b1_fk_website_s` FOREIGN KEY (`sub_category_name_id`) REFERENCES `website_subcategory` (`subcategory_id`);

--
-- Constraints for table `website_top`
--
ALTER TABLE `website_top`
  ADD CONSTRAINT `website_top_Busniess_Type_id_840a1280_fk_website_c` FOREIGN KEY (`Busniess_Type_id`) REFERENCES `website_categories` (`category_id`);

--
-- Constraints for table `website_vendor`
--
ALTER TABLE `website_vendor`
  ADD CONSTRAINT `website_vendor_Busniess_Type_id_fd71f8a7_fk_website_c` FOREIGN KEY (`Busniess_Type_id`) REFERENCES `website_categories` (`category_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
