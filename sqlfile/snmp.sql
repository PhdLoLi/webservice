-- MySQL dump 10.13  Distrib 5.1.69, for redhat-linux-gnu (x86_64)
--
-- Host: localhost    Database: snmp
-- ------------------------------------------------------
-- Server version	5.1.69

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `agentCurrentCPUUtilization`
--

DROP TABLE IF EXISTS `agentCurrentCPUUtilization`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `agentCurrentCPUUtilization` (
  `time` bigint(20) DEFAULT NULL,
  `oid` varchar(100) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `value` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `agentFreeMemory`
--

DROP TABLE IF EXISTS `agentFreeMemory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `agentFreeMemory` (
  `time` bigint(20) DEFAULT NULL,
  `oid` varchar(100) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `value` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `agentTotalMemory`
--

DROP TABLE IF EXISTS `agentTotalMemory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `agentTotalMemory` (
  `time` bigint(20) DEFAULT NULL,
  `oid` varchar(100) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `value` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `bsnAPDot3MacAddress`
--

DROP TABLE IF EXISTS `bsnAPDot3MacAddress`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bsnAPDot3MacAddress` (
  `time` bigint(20) DEFAULT NULL,
  `oid` varchar(100) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `value` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `bsnAPIfDBNoisePower`
--

DROP TABLE IF EXISTS `bsnAPIfDBNoisePower`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bsnAPIfDBNoisePower` (
  `time` bigint(20) DEFAULT NULL,
  `oid` varchar(100) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `value` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `bsnAPIfDot11ACKFailureCount`
--

DROP TABLE IF EXISTS `bsnAPIfDot11ACKFailureCount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bsnAPIfDot11ACKFailureCount` (
  `time` bigint(20) DEFAULT NULL,
  `oid` varchar(100) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `value` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `bsnAPIfDot11FCSErrorCount`
--

DROP TABLE IF EXISTS `bsnAPIfDot11FCSErrorCount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bsnAPIfDot11FCSErrorCount` (
  `time` bigint(20) DEFAULT NULL,
  `oid` varchar(100) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `value` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `bsnAPIfDot11FailedCount`
--

DROP TABLE IF EXISTS `bsnAPIfDot11FailedCount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bsnAPIfDot11FailedCount` (
  `time` bigint(20) DEFAULT NULL,
  `oid` varchar(100) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `value` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `bsnAPIfDot11MulticastTransmittedFrameCount`
--

DROP TABLE IF EXISTS `bsnAPIfDot11MulticastTransmittedFrameCount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bsnAPIfDot11MulticastTransmittedFrameCount` (
  `time` bigint(20) DEFAULT NULL,
  `oid` varchar(100) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `value` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `bsnAPIfDot11MultipleRetryCount`
--

DROP TABLE IF EXISTS `bsnAPIfDot11MultipleRetryCount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bsnAPIfDot11MultipleRetryCount` (
  `time` bigint(20) DEFAULT NULL,
  `oid` varchar(100) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `value` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `bsnAPIfDot11RTSFailureCount`
--

DROP TABLE IF EXISTS `bsnAPIfDot11RTSFailureCount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bsnAPIfDot11RTSFailureCount` (
  `time` bigint(20) DEFAULT NULL,
  `oid` varchar(100) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `value` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `bsnAPIfDot11RTSSuccessCount`
--

DROP TABLE IF EXISTS `bsnAPIfDot11RTSSuccessCount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bsnAPIfDot11RTSSuccessCount` (
  `time` bigint(20) DEFAULT NULL,
  `oid` varchar(100) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `value` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `bsnAPIfDot11RetryCount`
--

DROP TABLE IF EXISTS `bsnAPIfDot11RetryCount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bsnAPIfDot11RetryCount` (
  `time` bigint(20) DEFAULT NULL,
  `oid` varchar(100) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `value` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `bsnAPIfDot11TransmittedFragmentCount`
--

DROP TABLE IF EXISTS `bsnAPIfDot11TransmittedFragmentCount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bsnAPIfDot11TransmittedFragmentCount` (
  `time` bigint(20) DEFAULT NULL,
  `oid` varchar(100) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `value` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `bsnAPIfDot11TransmittedFrameCount`
--

DROP TABLE IF EXISTS `bsnAPIfDot11TransmittedFrameCount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bsnAPIfDot11TransmittedFrameCount` (
  `time` bigint(20) DEFAULT NULL,
  `oid` varchar(100) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `value` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `bsnAPIfInterferencePower`
--

DROP TABLE IF EXISTS `bsnAPIfInterferencePower`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bsnAPIfInterferencePower` (
  `time` bigint(20) DEFAULT NULL,
  `oid` varchar(100) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `value` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `bsnAPIfInterferenceUtilization`
--

DROP TABLE IF EXISTS `bsnAPIfInterferenceUtilization`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bsnAPIfInterferenceUtilization` (
  `time` bigint(20) DEFAULT NULL,
  `oid` varchar(100) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `value` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `bsnAPIfLoadChannelUtilization`
--

DROP TABLE IF EXISTS `bsnAPIfLoadChannelUtilization`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bsnAPIfLoadChannelUtilization` (
  `time` bigint(20) DEFAULT NULL,
  `oid` varchar(100) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `value` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `bsnAPIfLoadRxUtilization`
--

DROP TABLE IF EXISTS `bsnAPIfLoadRxUtilization`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bsnAPIfLoadRxUtilization` (
  `time` bigint(20) DEFAULT NULL,
  `oid` varchar(100) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `value` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `bsnAPIfLoadTxUtilization`
--

DROP TABLE IF EXISTS `bsnAPIfLoadTxUtilization`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bsnAPIfLoadTxUtilization` (
  `time` bigint(20) DEFAULT NULL,
  `oid` varchar(100) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `value` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `bsnAPIfPoorSNRClients`
--

DROP TABLE IF EXISTS `bsnAPIfPoorSNRClients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bsnAPIfPoorSNRClients` (
  `time` bigint(20) DEFAULT NULL,
  `oid` varchar(100) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `value` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `bsnAPLocation`
--

DROP TABLE IF EXISTS `bsnAPLocation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bsnAPLocation` (
  `time` bigint(20) DEFAULT NULL,
  `oid` varchar(100) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `value` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `bsnAPModel`
--

DROP TABLE IF EXISTS `bsnAPModel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bsnAPModel` (
  `time` bigint(20) DEFAULT NULL,
  `oid` varchar(100) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `value` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `bsnAPName`
--

DROP TABLE IF EXISTS `bsnAPName`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bsnAPName` (
  `time` bigint(20) DEFAULT NULL,
  `oid` varchar(100) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `value` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `bsnAPNumOfSlots`
--

DROP TABLE IF EXISTS `bsnAPNumOfSlots`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bsnAPNumOfSlots` (
  `time` bigint(20) DEFAULT NULL,
  `oid` varchar(100) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `value` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `bsnApIfNoOfUsers`
--

DROP TABLE IF EXISTS `bsnApIfNoOfUsers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bsnApIfNoOfUsers` (
  `time` bigint(20) DEFAULT NULL,
  `oid` varchar(100) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `value` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `bsnMobileStationBytesReceived`
--

DROP TABLE IF EXISTS `bsnMobileStationBytesReceived`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bsnMobileStationBytesReceived` (
  `time` bigint(20) DEFAULT NULL,
  `oid` varchar(100) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `value` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `bsnMobileStationBytesSent`
--

DROP TABLE IF EXISTS `bsnMobileStationBytesSent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bsnMobileStationBytesSent` (
  `time` bigint(20) DEFAULT NULL,
  `oid` varchar(100) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `value` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `bsnMobileStationPacketsReceived`
--

DROP TABLE IF EXISTS `bsnMobileStationPacketsReceived`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bsnMobileStationPacketsReceived` (
  `time` bigint(20) DEFAULT NULL,
  `oid` varchar(100) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `value` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `bsnMobileStationPacketsSent`
--

DROP TABLE IF EXISTS `bsnMobileStationPacketsSent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bsnMobileStationPacketsSent` (
  `time` bigint(20) DEFAULT NULL,
  `oid` varchar(100) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `value` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `bsnMobileStationRSSI`
--

DROP TABLE IF EXISTS `bsnMobileStationRSSI`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bsnMobileStationRSSI` (
  `time` bigint(20) DEFAULT NULL,
  `oid` varchar(100) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `value` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `bsnMobileStationRssiData`
--

DROP TABLE IF EXISTS `bsnMobileStationRssiData`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bsnMobileStationRssiData` (
  `time` bigint(20) DEFAULT NULL,
  `oid` varchar(100) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `value` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `bsnMobileStationSnr`
--

DROP TABLE IF EXISTS `bsnMobileStationSnr`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bsnMobileStationSnr` (
  `time` bigint(20) DEFAULT NULL,
  `oid` varchar(100) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `value` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `bsnRogueAPAirespaceAPRSSI`
--

DROP TABLE IF EXISTS `bsnRogueAPAirespaceAPRSSI`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bsnRogueAPAirespaceAPRSSI` (
  `time` bigint(20) DEFAULT NULL,
  `oid` varchar(100) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `value` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `bsnRogueAPAirespaceAPSNR`
--

DROP TABLE IF EXISTS `bsnRogueAPAirespaceAPSNR`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bsnRogueAPAirespaceAPSNR` (
  `time` bigint(20) DEFAULT NULL,
  `oid` varchar(100) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `value` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `bsnRogueClientAirespaceAPRSSI`
--

DROP TABLE IF EXISTS `bsnRogueClientAirespaceAPRSSI`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bsnRogueClientAirespaceAPRSSI` (
  `time` bigint(20) DEFAULT NULL,
  `oid` varchar(100) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `value` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `bsnRogueClientAirespaceAPSNR`
--

DROP TABLE IF EXISTS `bsnRogueClientAirespaceAPSNR`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bsnRogueClientAirespaceAPSNR` (
  `time` bigint(20) DEFAULT NULL,
  `oid` varchar(100) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `value` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `bsnSensorTemperature`
--

DROP TABLE IF EXISTS `bsnSensorTemperature`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bsnSensorTemperature` (
  `time` bigint(20) DEFAULT NULL,
  `oid` varchar(100) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `value` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `countavg`
--

DROP TABLE IF EXISTS `countavg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `countavg` (
  `name` char(100) DEFAULT NULL,
  `allnum` bigint(20) DEFAULT NULL,
  `allstorage` bigint(20) DEFAULT NULL,
  `avgnum` bigint(20) DEFAULT NULL,
  `avgstorage` bigint(20) DEFAULT NULL,
  `period` char(100) DEFAULT NULL,
  `last_time` datetime DEFAULT NULL,
  `actual_timediff` time DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `record_time`
--

DROP TABLE IF EXISTS `record_time`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `record_time` (
  `name` char(50) DEFAULT NULL,
  `start_time` bigint(20) DEFAULT NULL,
  `last_time` datetime DEFAULT NULL,
  `numbers` bigint(20) DEFAULT NULL,
  `start_time_read` datetime DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `snmptraps`
--

DROP TABLE IF EXISTS `snmptraps`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `snmptraps` (
  `time` bigint(20) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `id` varchar(100) DEFAULT NULL,
  `oids` text
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `yongqian`
--

DROP TABLE IF EXISTS `yongqian`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `yongqian` (
  `router` varchar(100) DEFAULT NULL,
  `port` int(11) DEFAULT NULL,
  `time` bigint(20) DEFAULT NULL,
  `octs_in` bigint(20) DEFAULT NULL,
  `pits_in` int(11) DEFAULT NULL,
  `octs_out` bigint(20) DEFAULT NULL,
  `pits_out` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-03-03 13:47:17
