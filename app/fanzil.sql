-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 01, 2023 at 02:43 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `fanzil`
--

-- --------------------------------------------------------

--
-- Table structure for table `curso`
--

CREATE TABLE `curso` (
  `n_curso` int(11) NOT NULL,
  `descripcion` varchar(250) NOT NULL,
  `fecha_inicial` date NOT NULL,
  `fecha_final` date NOT NULL,
  `n_instructor` int(11) NOT NULL,
  `n_documento` int(11) NOT NULL,
  `n_modulo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `modulos`
--

CREATE TABLE `modulos` (
  `n_modulo` int(11) NOT NULL,
  `descripcion` varchar(500) NOT NULL,
  `horas` time NOT NULL,
  `nombres` varchar(40) NOT NULL,
  `n_instructor` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `roles`
--

CREATE TABLE `roles` (
  `rol` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `uso_vehiculo`
--

CREATE TABLE `uso_vehiculo` (
  `n_registro` int(11) NOT NULL,
  `fecha_inicio` date NOT NULL,
  `fecha_expiracion` date NOT NULL,
  `n_documento` int(20) NOT NULL,
  `matricula` varchar(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `usuario`
--

CREATE TABLE `usuario` (
  `n_documento` int(20) NOT NULL,
  `nombres` varchar(50) NOT NULL,
  `apellidos` varchar(50) NOT NULL,
  `password` varchar(40) NOT NULL,
  `n_instructor` int(11) NOT NULL,
  `n_curso` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `vehiculo`
--

CREATE TABLE `vehiculo` (
  `matricula` varchar(6) NOT NULL,
  `marca` varchar(20) NOT NULL,
  `referencia` varchar(30) NOT NULL,
  `tipo_vehiculo` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `curso`
--
ALTER TABLE `curso`
  ADD PRIMARY KEY (`n_curso`),
  ADD KEY `n_documento` (`n_documento`),
  ADD KEY `n_modulo` (`n_modulo`);

--
-- Indexes for table `modulos`
--
ALTER TABLE `modulos`
  ADD PRIMARY KEY (`n_modulo`);

--
-- Indexes for table `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`rol`);

--
-- Indexes for table `uso_vehiculo`
--
ALTER TABLE `uso_vehiculo`
  ADD PRIMARY KEY (`n_registro`),
  ADD KEY `n_documento` (`n_documento`),
  ADD KEY `matricula` (`matricula`);

--
-- Indexes for table `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`n_documento`),
  ADD KEY `n_curso` (`n_curso`);

--
-- Indexes for table `vehiculo`
--
ALTER TABLE `vehiculo`
  ADD PRIMARY KEY (`matricula`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `curso`
--
ALTER TABLE `curso`
  ADD CONSTRAINT `curso_ibfk_1` FOREIGN KEY (`n_documento`) REFERENCES `usuario` (`n_documento`),
  ADD CONSTRAINT `curso_ibfk_2` FOREIGN KEY (`n_modulo`) REFERENCES `modulos` (`n_modulo`);

--
-- Constraints for table `uso_vehiculo`
--
ALTER TABLE `uso_vehiculo`
  ADD CONSTRAINT `uso_vehiculo_ibfk_1` FOREIGN KEY (`n_documento`) REFERENCES `usuario` (`n_documento`),
  ADD CONSTRAINT `uso_vehiculo_ibfk_2` FOREIGN KEY (`matricula`) REFERENCES `vehiculo` (`matricula`);

--
-- Constraints for table `usuario`
--
ALTER TABLE `usuario`
  ADD CONSTRAINT `usuario_ibfk_1` FOREIGN KEY (`n_curso`) REFERENCES `curso` (`n_curso`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
