create_table_linelist = ('CREATE TABLE IF NOT EXISTS linelist (`IP` varchar(500) DEFAULT NULL, \
  `State` varchar(500) DEFAULT NULL, \
  `SurgeCommand` varchar(500) DEFAULT NULL, \
  `LGA` varchar(500) DEFAULT NULL, \
  `FacilityName` varchar(500) DEFAULT NULL, \
  `Pepid_datim` varchar(500) PRIMARY KEY, \
  `patient_id` double DEFAULT NULL, \
  `Pepid` varchar(500) NOT NULL, \
  `HospitalNo` varchar(500) DEFAULT NULL, \
  `Sex` varchar(500) DEFAULT NULL, \
`KP_Type` varchar(500) DEFAULT NULL, \
  `Date_Enrolled` timestamp(6) NULL DEFAULT NULL, \
  `AgeAtStartofART` double DEFAULT NULL, \
  `AgeAtStart_InMonth` double DEFAULT NULL, \
`CurrentAge` double DEFAULT NULL, \
  `ARTStartDate` timestamp(6) NULL DEFAULT NULL, \
  `LastPickupDate` timestamp(6) NULL DEFAULT NULL, \
`NextAppmt` timestamp(6) NULL DEFAULT NULL, \
  `DaysOfARVRefill` double DEFAULT NULL, \
  `RegLineAtStart` varchar(500) DEFAULT NULL, \
  `ARTRegAtStart` varchar(500) DEFAULT NULL, \
  `CurrentRegLine` varchar(500) DEFAULT NULL, \
  `CurrentARTReg` varchar(500) DEFAULT NULL, \
  `PregStatus` varchar(500) DEFAULT NULL, \
  `CurrentVL` double DEFAULT NULL, \
  `DateOfCurrentVL` timestamp(6) NULL DEFAULT NULL, \
  `ViralLoadIndication` varchar(500) DEFAULT NULL, \
  `Date_Result_Received` timestamp(6) NULL DEFAULT NULL, \
  `Last_VL_Sample_Date` timestamp(6) NULL DEFAULT NULL, \
  `Initial_CD4_Date` timestamp(6) NULL DEFAULT NULL, \
  `initial_CD4` double DEFAULT NULL, \
  `Last_CD4_Date` timestamp(6) NULL DEFAULT NULL, \
  `Last_CD4` double DEFAULT NULL, \
  `CurrentARTStatus_28Days` varchar(500) DEFAULT NULL, \
  `DaysInterval` double DEFAULT NULL, \
  `TI` varchar(500) DEFAULT NULL, \
  `DOB` date DEFAULT NULL, \
  `Surname` varchar(500) DEFAULT NULL, \
  `FirstName` varchar(500) DEFAULT NULL, \
  `Phone_No` varchar(500) DEFAULT NULL, \
  `Address` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL, \
  `Pill_Balance` double DEFAULT NULL, \
  `Next_Pickup_Date` timestamp(6) NULL DEFAULT NULL, \
  `DATIMCode` varchar(500) DEFAULT NULL, \
  `MonthOnART` double DEFAULT NULL, \
  `Last_Weight` double DEFAULT NULL, \
  `Last_Weight_Date` timestamp(6) NULL DEFAULT NULL, \
  `Biometrics_Captured` timestamp(6) NULL DEFAULT NULL, \
  `Recapture_Count` double DEFAULT NULL, \
  `Date_Last_Recaptured` timestamp(6) NULL DEFAULT NULL, \
  `Eligible_For_IPT` varchar(500) DEFAULT NULL, \
  `Date_IPT_start` timestamp(6) NULL DEFAULT NULL, \
  `Outcome_of_IPT` varchar(500) DEFAULT NULL, \
  `Date_of_Outcome` timestamp(6) NULL DEFAULT NULL, \
  `Last_Clinic_Visit_Date` timestamp(6) NULL DEFAULT NULL, \
  `Systolic_BP` double DEFAULT NULL, \
  `Diastolic_BP` double DEFAULT NULL, \
  `Next_Clinical_Appt_Date` timestamp(6) NULL DEFAULT NULL, \
  `Last_TB_Screening_Date` timestamp(6) NULL DEFAULT NULL, \
  `Last_TB_Screening_Status` varchar(500) DEFAULT NULL, \
  `TB_Investigations` varchar(500) DEFAULT NULL, \
  `Investig_Result` varchar(500) DEFAULT NULL, \
  `Date_TB_Investig` timestamp(6) NULL DEFAULT NULL, \
  `Reason_for_Tracking` varchar(500) DEFAULT NULL, \
  `Tracking_Date` timestamp(6) NULL DEFAULT NULL, \
  `Reason_for_Defaulting1` varchar(500) DEFAULT NULL, \
  `Reason_for_Termination` varchar(500) DEFAULT NULL, \
  `Date_of_Termination` timestamp(6) NULL DEFAULT NULL, \
`Facility_Transferred_To` varchar(500) DEFAULT NULL, \
  `Last_EAC_Session_Date` timestamp(6) NULL DEFAULT NULL, \
  `EAC_Session_Type` varchar(500) DEFAULT NULL, \
  `EAC_ARV_Plan` varchar(500) DEFAULT NULL, \
  `Date_VL_Before_EAC` timestamp(6) NULL DEFAULT NULL, \
  `VL_Before_EAC` double DEFAULT NULL, \
  `Date_VL_After_EAC` timestamp(6) NULL DEFAULT NULL, \
  `VL_After_EAC` double DEFAULT NULL, \
  `List_Parameters` varchar(500) DEFAULT NULL, \
  `Date_List_Gen` timestamp(6) NULL DEFAULT NULL)')

create_ahd_linelist = ("CREATE TABLE IF NOT EXISTS `ahd_linelist` ( \
  `IP` varchar(255) DEFAULT NULL,\
  `State` varchar(255) DEFAULT NULL,\
  `SurgeCommand` varchar(255) DEFAULT NULL,\
  `LGA` varchar(255) DEFAULT NULL,\
  `FacilityName` varchar(255) DEFAULT NULL,\
  `Pepid_datim` varchar(255) DEFAULT NULL,\
  `Pepid` varchar(255) DEFAULT NULL,\
  `person_id` double DEFAULT NULL,\
  `Sex` varchar(255) DEFAULT NULL,\
  `Date_Enrolled` timestamp(6) NULL DEFAULT NULL,\
  `ARTStartDate` timestamp(6) NULL DEFAULT NULL,\
  `Indication_for_CD4` varchar(255) DEFAULT NULL,\
  `CD4_LFA_Result` varchar(255) DEFAULT NULL,\
  `Date_of_CD4_LFA_Result` timestamp(6) NULL DEFAULT NULL,\
  `CD4_Percent` varchar(255) DEFAULT NULL,\
  `CD4_Percent_Date` varchar(255) DEFAULT NULL,\
  `CD4_Count` varchar(255) DEFAULT NULL,\
  `CD4_Count_Date` varchar(255) DEFAULT NULL,\
  `TB_LF_LAM_Result` varchar(255) DEFAULT NULL,\
  `Date_TB_LF_LAM_Result_Received` timestamp(6) NULL DEFAULT NULL,\
  `Serology_For_CrAg_Result` varchar(255) DEFAULT NULL,\
  `Date_Serology_For_CrAg_Result_Received` timestamp(6) NULL DEFAULT NULL,\
  `CSF_For_CrAg_Result` varchar(255) DEFAULT NULL,\
  `Date_CSF_For_CrAg_Result_Received` varchar(255) DEFAULT NULL,\
  `ICE_WHO_Staging` double DEFAULT NULL,\
  `Cryptococcal_Screening_Status` varchar(255) DEFAULT NULL,\
  `List_Parameters` varchar(255) DEFAULT NULL)")

create_eid_linelist = ("CREATE TABLE IF NOT EXISTS `eid_linelist` (\
`IP` varchar(500) DEFAULT NULL,\
  `State` varchar(500) DEFAULT NULL,\
  `SurgeCommand` varchar(500) DEFAULT NULL,\
  `LGA` varchar(500) DEFAULT NULL,\
  `FacilityName` varchar(500) DEFAULT NULL,\
  `HEI_Number_datim` varchar(500) PRIMARY KEY,\
  `HEI_Number` varchar(500) NOT NULL,\
  `ChildRegistrationDate` varchar(500) DEFAULT NULL,\
  `Surname` varchar(500) DEFAULT NULL,\
  `FirstName` varchar(500) DEFAULT NULL,\
  `DOB` date DEFAULT NULL,\
  `Sex` varchar(500) DEFAULT NULL,\
  `CurrentAge` double DEFAULT NULL,\
  `PhoneNumber` varchar(500) DEFAULT NULL,\
  `WeightAtBirth` varchar(500) DEFAULT NULL,\
  `lengthAtBirth` varchar(500) DEFAULT NULL,\
  `HeadCircumferenceAtBirth` varchar(500) DEFAULT NULL,\
  `ChildMUACAtBirth` varchar(500) DEFAULT NULL,\
  `APGAR_ScoreAtBirth` varchar(500) DEFAULT NULL,\
  `ChildGivenHepatitisB_Immunoglobulin` varchar(500) DEFAULT NULL,\
  `HighRiskHIVExposedInfant` varchar(500) DEFAULT NULL,\
  `ARVProphylaxis` varchar(500) DEFAULT NULL,\
  `TimingOfARVProphylaxis` varchar(500) DEFAULT NULL,\
  `ImmunizationReceivedAtBirth` varchar(500) DEFAULT NULL,\
  `FollowUpDate` varchar(500) DEFAULT NULL,\
  `TimingOfMotherARTInitiation` varchar(500) DEFAULT NULL,\
  `WeightAtFollowUP` varchar(500) DEFAULT NULL,\
  `lengthAtFollowUp` varchar(500) DEFAULT NULL,\
  `HeadCircumferenceAtFollowUp` varchar(500) DEFAULT NULL,\
  `MID_UpperARM_CircumferenceAtFollowUp` varchar(500) DEFAULT NULL,\
  `ChildMUACAtFollowUp` varchar(500) DEFAULT NULL,\
  `BMI_MUACAtFollowUp` varchar(500) DEFAULT NULL,\
  `CTX_GivenToChild` varchar(500) DEFAULT NULL,\
  `InfantFeedingMethod` varchar(500) DEFAULT NULL,\
  `PCR_Type` varchar(500) DEFAULT NULL,\
  `SampleCollectionDate` timestamp(6) NULL DEFAULT NULL,\
  `DateSampleSent` timestamp(6) NULL DEFAULT NULL,\
  `DateResultReceivedAtFacility` timestamp(6) NULL DEFAULT NULL,\
  `DateCaregiverWasGivenPCRResult` timestamp(6) NULL DEFAULT NULL,\
  `PCR_Result` varchar(500) DEFAULT NULL,\
  `RapidTestType` varchar(500) DEFAULT NULL,\
  `RapidTestDate` varchar(500) DEFAULT NULL,\
  `RapidTestResult` varchar(500) DEFAULT NULL,\
  `Outcome_At_18Month` varchar(500) DEFAULT NULL,\
  `ARTStartDate_IfPositive` varchar(500) DEFAULT NULL)")

create_hts_linelist = ("CREATE TABLE IF NOT EXISTS `hts_linelist` (\
  `IP` varchar(255) DEFAULT NULL,\
  `State` varchar(255) DEFAULT NULL,\
  `SurgeCommand` varchar(255) DEFAULT NULL,\
  `LGA` varchar(255) DEFAULT NULL,\
  `City` varchar(255) DEFAULT NULL,\
  `Datim_Code` varchar(255) DEFAULT NULL,\
  `FacilityName` varchar(255) DEFAULT NULL,\
  `Datim_HTS_ClientCode` varchar(255) PRIMARY KEY,\
  `patient_id` double DEFAULT NULL,\
  `HTS_ClientCode` varchar(255) NOT NULL,\
  `PEPFAR_Number_IfOnART` varchar(255) DEFAULT NULL,\
  `birthdate` date DEFAULT NULL,\
  `Sex` varchar(255) DEFAULT NULL,\
  `CurrentAge` double DEFAULT NULL,\
  `given_name` varchar(255) DEFAULT NULL,\
  `family_name` varchar(255) DEFAULT NULL,\
  `PhoneNumber` varchar(255) DEFAULT NULL,\
  `VisitDate` varchar(255) DEFAULT NULL,\
  `Test_VisitDate_Validation` varchar(255) DEFAULT NULL,\
  `KindOfHTS` varchar(255) DEFAULT NULL,\
  `setting` varchar(255) DEFAULT NULL,\
  `FirstTimeVisit` varchar(255) DEFAULT NULL,\
  `TypeOfSession` varchar(255) DEFAULT NULL,\
  `ReferredFrom` varchar(255) DEFAULT NULL,\
  `MaritalStatus` varchar(255) DEFAULT NULL,\
  `FromIndex` varchar(255) DEFAULT NULL,\
  `IndexClientID_Validation` varchar(255) DEFAULT NULL,\
  `IndexClientID` varchar(255) DEFAULT NULL,\
  `IndexType` varchar(255) DEFAULT NULL,\
  `IndexClientName` varchar(255) DEFAULT NULL,\
  `HIVScreeningTest` varchar(255) DEFAULT NULL,\
  `HIVScreeningTestDate` date DEFAULT NULL,\
  `HIVConfirmatoryTest` varchar(255) DEFAULT NULL,\
  `HIVConfirmatoryTestDate` date DEFAULT NULL,\
  `HIV_FinalResult` varchar(255) DEFAULT NULL,\
  `Opt_Out_of_RTRI?` varchar(255) DEFAULT NULL,\
  `Opt_Out_of_RTRI_Validation` varchar(255) DEFAULT NULL,\
  `HIVRecencyTestName` varchar(255) DEFAULT NULL,\
  `VerifyRecencyNumber` varchar(255) DEFAULT NULL,\
  `ControlLine` varchar(255) DEFAULT NULL,\
  `VerificationLine` varchar(255) DEFAULT NULL,\
  `LongTermLine` varchar(255) DEFAULT NULL,\
  `HIVRecencyTestDate` date DEFAULT NULL,\
  `RecencyInterpretation` varchar(255) DEFAULT NULL,\
  `ViralLoadRequest` varchar(255) DEFAULT NULL,\
  `VLSampleCollectionDate` varchar(255) DEFAULT NULL,\
  `PCR_LabNo` varchar(255) DEFAULT NULL,\
  `SampleType` varchar(255) DEFAULT NULL,\
  `PCR_Laboratory` varchar(255) DEFAULT NULL,\
  `HIV_ViralLoad` varchar(255) DEFAULT NULL,\
  `FinalHIVRecencyResult` varchar(255) DEFAULT NULL,\
  `NoOfPatnerElicited` varchar(255) DEFAULT NULL,\
  `PartnerFullName_1` varchar(255) DEFAULT NULL,\
  `IndexRelation_Gender_1` varchar(255) DEFAULT NULL,\
  `IndexType_Partner1` varchar(255) DEFAULT NULL,\
  `PartnerFullName_2` varchar(255) DEFAULT NULL,\
  `IndexRelation_Gender_2` varchar(255) DEFAULT NULL,\
  `IndexType_Partner2` varchar(255) DEFAULT NULL,\
  `PartnerFullName_3` varchar(255) DEFAULT NULL,\
  `IndexRelation_Gender_3` varchar(255) DEFAULT NULL,\
  `IndexType_Partner3` varchar(255) DEFAULT NULL,\
  `PartnerFullName_4` varchar(255) DEFAULT NULL,\
  `IndexRelation_Gender_4` varchar(255) DEFAULT NULL,\
  `IndexType_Partner4` varchar(255) DEFAULT NULL,\
  `PartnerFullName_5` varchar(255) DEFAULT NULL,\
  `IndexRelation_Gender_5` varchar(255) DEFAULT NULL,\
  `IndexType_Partner5` varchar(255) DEFAULT NULL,\
  `PartnerFullName_6` varchar(255) DEFAULT NULL,\
  `IndexRelation_Gender_6` varchar(255) DEFAULT NULL,\
  `IndexType_Partner6` varchar(255) DEFAULT NULL)")

create_lims_emr_linelist = ("CREATE TABLE IF NOT EXISTS `lims_emr_daily_report` (\
  `IP` varchar(500) DEFAULT NULL,\
  `State` varchar(500) DEFAULT NULL,\
  `SurgeCommand` varchar(500) DEFAULT NULL,\
  `LGA` varchar(500) DEFAULT NULL,\
  `FacilityName` varchar(500) DEFAULT NULL,\
  `Manifest_id` varchar(500) DEFAULT NULL,\
  `Sample_Collected_Date` varchar(500) DEFAULT NULL,\
  `Date_Sample_sent` varchar(500) DEFAULT NULL,\
  `Sample_Status` varchar(500) DEFAULT NULL,\
  `sample_id` varchar(500) DEFAULT NULL,\
  `patient_id` varchar(500) DEFAULT NULL,\
  `PEPID` varchar(500) NOT NULL,\
  `Date_Sample_Receieved_at_PCRlab` varchar(500) DEFAULT NULL,\
  `Assay_Date` varchar(500) DEFAULT NULL,\
  `Date_Result_Dispatched` varchar(500) DEFAULT NULL)")

create_otz_linelist = ("CREATE TABLE IF NOT EXISTS `otz_linelist` (\
  `IP` varchar(255) DEFAULT NULL,\
  `State` varchar(255) DEFAULT NULL,\
  `SurgeCommand` varchar(255) DEFAULT NULL,\
  `LGA` varchar(255) DEFAULT NULL,\
  `FacilityName` varchar(255) DEFAULT NULL,\
  `Pepid_datim` varchar(255) DEFAULT NULL,\
  `patient_id` double DEFAULT NULL,\
  `Pepid` varchar(255) DEFAULT NULL,\
  `Date_Enrolled_Into_OTZ` timestamp(6) NULL DEFAULT NULL,\
  `OTZ_Disclosure_Status` varchar(255) DEFAULT NULL,\
  `OTZ_Date_of_Full_Disclosure` timestamp(6) NULL DEFAULT NULL,\
  `Enrolled_Into_OTZ_Plus` varchar(255) DEFAULT NULL,\
  `Date_Enrolled_Into_OTZ_Plus` varchar(255) DEFAULT NULL,\
  `Date_of_Commencement_of_OTZ_Module` timestamp(6) NULL DEFAULT NULL,\
  `Positive_Living` varchar(255) DEFAULT NULL,\
  `Positive_Living_Comp_Date` timestamp(6) NULL DEFAULT NULL,\
  `Treatment_Literacy` varchar(255) DEFAULT NULL,\
  `Treatment_Literacy_Comp_Date` timestamp(6) NULL DEFAULT NULL,\
  `Adolescents_Participation` varchar(255) DEFAULT NULL,\
  `Adolescents_Participation_Comp_Date` timestamp(6) NULL DEFAULT NULL,\
  `Leadership_Training` varchar(255) DEFAULT NULL,\
  `Leadership_Training_Comp_Date` timestamp(6) NULL DEFAULT NULL,\
  `Peer_to_Peer_Mentorship` varchar(255) DEFAULT NULL,\
  `Peer_to_Peer_Mentorship_Comp_Date` timestamp(6) NULL DEFAULT NULL,\
  `Role_of_OTZ_in_95_95_95` varchar(255) DEFAULT NULL,\
  `Role_of_OTZ_in_95_95_95_Comp_Date` timestamp(6) NULL DEFAULT NULL,\
  `OTZ_Champion_Orientation` varchar(255) DEFAULT NULL,\
  `OTZ_Champion_Orientation_Comp_Date` timestamp(6) NULL DEFAULT NULL,\
  `Number_of_OTZ_Modules_Completed` double DEFAULT NULL,\
  `Date_of_Final_Module_Completion` timestamp(6) NULL DEFAULT NULL,\
  `Transitioned_to_Adult_Clinic` varchar(255) DEFAULT NULL,\
  `Date_Transitioned_to_Adult_Clinic` varchar(255) DEFAULT NULL,\
  `OTZ_Program_Outcome` varchar(255) DEFAULT NULL,\
  `List_Parameters` varchar(255) DEFAULT NULL)")

create_pmtct_linelist = ("CREATE TABLE IF NOT EXISTS `pmtct_linelist` (\
  `IP` varchar(500) DEFAULT NULL,\
  `State` varchar(500) DEFAULT NULL,\
  `SurgeCommand` varchar(500) DEFAULT NULL,\
  `LGA` varchar(500) DEFAULT NULL,\
  `FacilityName` varchar(500) DEFAULT NULL,\
  `City` varchar(500) DEFAULT NULL,\
  `Datim_Code` varchar(500) DEFAULT NULL,\
  `ANC_Number_datim` varchar(500) PRIMARY KEY,\
  `ANC_Number` varchar(500) NOT NULL,\
  `PEPFAR_Number(IfOnART)` varchar(500) DEFAULT NULL,\
  `person_id` double DEFAULT NULL,\
  `birthdate` date DEFAULT NULL,\
  `Gender` varchar(500) DEFAULT NULL,\
  `CurrentAge` double DEFAULT NULL,\
  `given_name` varchar(500) DEFAULT NULL,\
  `family_name` varchar(500) DEFAULT NULL,\
  `PhoneNumber` varchar(500) DEFAULT NULL,\
  `Address` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,\
  `Client_LGA` varchar(500) DEFAULT NULL,\
  `LGA_Latitude` varchar(500) DEFAULT NULL,\
  `LGA_Longitude` varchar(500) DEFAULT NULL,\
  `GeneralANC_VisitDate` varchar(500) DEFAULT NULL,\
  `LMP_DATE` varchar(500) DEFAULT NULL,\
  `GA` double DEFAULT NULL,\
  `Gravida` double DEFAULT NULL,\
  `Parity` double DEFAULT NULL,\
  `Point_Of_Entry` varchar(500) DEFAULT NULL,\
  `EDD` varchar(500) DEFAULT NULL,\
  `PMTCT_HTS_Date` varchar(500) DEFAULT NULL,\
  `PMTCT_HTS_SettingRegister` varchar(500) DEFAULT NULL,\
  `PMTCT_HTS_Register_Date` varchar(500) DEFAULT NULL,\
  `Previously_Known_HIV_Status` varchar(500) DEFAULT NULL,\
  `Date_Previously_Tested_Positive` varchar(500) DEFAULT NULL,\
  `HIV_TestAccepted` varchar(500) DEFAULT NULL,\
  `HIV_ReTesting` varchar(500) DEFAULT NULL,\
  `ResultOfHIVTest` varchar(500) DEFAULT NULL,\
  `Received_HIV_Test_Result` varchar(500) DEFAULT NULL)")

create_full_pharmacy_complement = """
CREATE TABLE IF NOT EXIST `full_pharmacy_complement_for_ex` (
  `IP` varchar(255) DEFAULT NULL,
  `State` varchar(255) DEFAULT NULL,
  `SurgeCommand` varchar(255) DEFAULT NULL,
  `LGA` varchar(255) DEFAULT NULL,
  `FacilityName` varchar(255) DEFAULT NULL,
  `DATIMCode` varchar(255) DEFAULT NULL,
  `Pepid_datim` varchar(255) DEFAULT NULL,
  `PEPID` varchar(255) DEFAULT NULL,
  `patient_id` double DEFAULT NULL,
  `LastPickupDate` timestamp(6) NULL DEFAULT NULL,
  `encounter_id` double DEFAULT NULL,
  `RegLineAtStart` varchar(255) DEFAULT NULL,
  `ARTRegAtStart` varchar(255) DEFAULT NULL,
  `DaysOfARVRefill` double DEFAULT NULL,
  `CurrentARTStatus_28Days` varchar(255) DEFAULT NULL,
  `Pill_Balance` varchar(255) DEFAULT NULL,
  `Next_Pickup_Date` timestamp(6) NULL DEFAULT NULL,
  `CurrentARTReg` varchar(255) DEFAULT NULL,
  `CurrentRegLine` varchar(255) DEFAULT NULL,
  `ARV_Drug_Strength` varchar(255) DEFAULT NULL,
  `OI_Drug_CTX` varchar(255) DEFAULT NULL,
  `CTX_Strength` varchar(255) DEFAULT NULL,
  `OI_Drug_INH` varchar(255) DEFAULT NULL,
  `INH_Strength` varchar(255) DEFAULT NULL,
  `DSD_Model` varchar(255) DEFAULT NULL,
  `DDD_Fac_Disp` varchar(255) DEFAULT NULL,
  `Switch/Substitution` varchar(255) DEFAULT NULL,
  `PregStatus` varchar(255) DEFAULT NULL,
  `List_Parameters` varchar(255) DEFAULT NULL)
"""

create_last_5_pharmacy = ("CREATE TABLE IF NOT EXISTS `last_5_pharmacy` (\
  `IP` varchar(500) DEFAULT NULL,\
  `State` varchar(500) DEFAULT NULL,\
  `SurgeCommand` varchar(500) DEFAULT NULL,\
  `LGA` varchar(500) DEFAULT NULL,\
  `FacilityName` varchar(500) DEFAULT NULL,\
  `DatimCode` varchar(500) DEFAULT NULL,\
  `Pepid_Datim` varchar(500) PRIMARY KEY,\
  `patient_id` double DEFAULT NULL,\
  `PEPID` varchar(500) NOT NULL,\
  `1_LastPickupDate` timestamp(6) NULL DEFAULT NULL,\
  `1_DaysOfARVRefill` double DEFAULT NULL,\
  `1_NextAppmt` timestamp(6) NULL DEFAULT NULL,\
  `2_LastPickupDate` timestamp(6) NULL DEFAULT NULL,\
  `2_DaysOfARVRefill` double DEFAULT NULL,\
  `2_NextAppmt` timestamp(6) NULL DEFAULT NULL,\
  `3_LastPickupDate` timestamp(6) NULL DEFAULT NULL,\
  `3_DaysOfARVRefill` double DEFAULT NULL,\
  `3_NextAppmt` timestamp(6) NULL DEFAULT NULL,\
  `4_LastPickupDate` timestamp(6) NULL DEFAULT NULL,\
  `4_DaysOfARVRefill` double DEFAULT NULL,\
  `4_NextAppmt` timestamp(6) NULL DEFAULT NULL,\
  `5_LastPickupDate` timestamp(6) NULL DEFAULT NULL,\
  `5_DaysOfARVRefill` double DEFAULT NULL,\
  `5_NextAppmt` timestamp(6) NULL DEFAULT NULL)")

create_mobile_hts_tracker = ("CREATE TABLE IF NOT EXISTS `mobile_hts_tracker` (\
    `IP` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `State` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `SurgeCommand` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `LGA` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `patient_Id` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `pep_id` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `facility_name` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `datim_code` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `patient_date_created` DATETIME DEFAULT NULL,\
    `baseline_date` DATETIME DEFAULT NULL,\
    `recapture_date` DATETIME DEFAULT NULL,\
    `encounter_date` DATETIME DEFAULT NULL,\
    `encounter_date_created` DATETIME DEFAULT NULL,\
    `current_status_90days` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `latitude` double DEFAULT NULL,\
    `longitude` double DEFAULT NULL,\
    `entry_source` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `baseline_source` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `recapture_source` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL)")


create_ncd_linelist = ("CREATE TABLE IF NOT EXISTS `ncd_linelist` (\
  `IP` varchar(500) DEFAULT NULL,\
  `State` varchar(500) DEFAULT NULL,\
  `SurgeCommand` varchar(500) DEFAULT NULL,\
  `LGA` varchar(500) DEFAULT NULL,\
  `FacilityName` varchar(500) DEFAULT NULL,\
  `PATIENT ID` double DEFAULT NULL,\
  `PATIENT IDENTIFIER` varchar(500) DEFAULT NULL,\
  `GENDER` varchar(500) DEFAULT NULL,\
  `PHONE NUMBER` varchar(500) DEFAULT NULL,\
  `PATIENT NAME` varchar(500) DEFAULT NULL,\
  `FAMILY NAME` varchar(500) DEFAULT NULL,\
  `AGE` double DEFAULT NULL,\
  `ADDRESS` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,\
  `STATE_Res` varchar(500) DEFAULT NULL,\
  `LGA_Res` varchar(500) DEFAULT NULL,\
  `SITE` varchar(500) DEFAULT NULL,\
  `SERVICE AREA NAME` varchar(500) DEFAULT NULL,\
  `RISK ASSESSMENT SCORE` double DEFAULT NULL,\
  `HYPERTENSIVE` varchar(500) DEFAULT NULL,\
  `MEDICATION FOR HTN` varchar(500) DEFAULT NULL,\
  `LATEST BP UPPER` double DEFAULT NULL,\
  `LATEST BP LOWER` double DEFAULT NULL,\
  `DIABETIC` varchar(500) DEFAULT NULL,\
  `MEDICATION FOR DM` varchar(500) DEFAULT NULL,\
  `LATEST RBS` double DEFAULT NULL,\
  `BMI WEIGHT` double DEFAULT NULL,\
  `BMI HEIGHT` double DEFAULT NULL,\
  `BMI` double DEFAULT NULL,\
  `BMI RANGE` varchar(500) DEFAULT NULL,\
  `NCD SCREENING SCORE` double DEFAULT NULL,\
  `HIV STATUS` varchar(500) DEFAULT NULL,\
  `ART STATUS` varchar(500) DEFAULT NULL,\
  `HIV OUTCOME` varchar(500) DEFAULT NULL,\
  `NCD OUTCOME` varchar(500) DEFAULT NULL,\
  `ENCOUNTER DATE` timestamp(6) NULL DEFAULT NULL,\
  `DATE CREATED` timestamp(6) NULL DEFAULT NULL)")

create_pbs_linelist = ("CREATE TABLE IF NOT EXISTS `pbs_linelist` (\
  `IP` varchar(500) DEFAULT NULL,\
  `State` varchar(500) DEFAULT NULL,\
  `SurgeCommand` varchar(500) DEFAULT NULL,\
  `LGA` varchar(500) DEFAULT NULL,\
  `FacilityName` varchar(500) DEFAULT NULL,\
  `DATIM_Code` varchar(500) DEFAULT NULL,\
  `Pepid_datim` varchar(500) PRIMARY KEY,\
  `patient_Id` double DEFAULT NULL,\
  `PEPID` varchar(500) NOT NULL,\
  `Initial_Date_Captured` timestamp(6) NULL DEFAULT NULL,\
  `No_Initial_Finger_Captured` double DEFAULT NULL,\
  `Date_Recapture` timestamp(6) NULL DEFAULT NULL,\
  `No_Recaptured_Finger` double DEFAULT NULL,\
  `Recapture_Count` double DEFAULT NULL,\
  `Last_Visit_Date` timestamp(6) NULL DEFAULT NULL,\
  `Last_Encounter` varchar(500) DEFAULT NULL,\
  `Total_%_PBS_Quality` double DEFAULT NULL,\
  `L_Thumb_Quality(%)` double DEFAULT NULL,\
  `L_Index_Quality(%)` double DEFAULT NULL,\
  `L_Middle_Quality(%)` double DEFAULT NULL,\
  `L_Wedding_Quality(%)` double DEFAULT NULL,\
  `L_Small_Quality(%)` double DEFAULT NULL,\
  `R_Thumb_Quality(%)` double DEFAULT NULL,\
  `R_Index_Quality(%)` double DEFAULT NULL,\
  `R_Middle_Quality(%)` double DEFAULT NULL,\
  `R_Wedding_Quality(%)` double DEFAULT NULL,\
  `R_Small_Quality(%)` double DEFAULT NULL,\
  `Initial_LeftThumb` double DEFAULT NULL, \
  `Initial_LeftIndex` double DEFAULT NULL,\
  `Initial_LeftMiddle` double DEFAULT NULL,\
  `Initial_LeftWedding` double DEFAULT NULL,\
  `Initial_LeftSmall` double DEFAULT NULL,\
  `Initial_RightThumb` double DEFAULT NULL,\
  `Initial_RightIndex` double DEFAULT NULL,\
  `Initial_RightMiddle` double DEFAULT NULL,\
  `Initial_RightWedding` double DEFAULT NULL,\
  `Initial_RightSmall` double DEFAULT NULL,\
  `LeftThumb` double DEFAULT NULL,\
  `LeftIndex` double DEFAULT NULL,\
  `LeftMiddle` double DEFAULT NULL,\
  `LeftWedding` double DEFAULT NULL,\
  `LeftSmall` double DEFAULT NULL,\
  `RightThumb` double DEFAULT NULL,\
  `RightIndex` double DEFAULT NULL,\
  `RightMiddle` double DEFAULT NULL,\
  `RightWedding` double DEFAULT NULL,\
  `RightSmall` double DEFAULT NULL)")


create_client_tracking_and_discontinuation = ("CREATE TABLE IF NOT EXISTS `client_tracking_and_discontinuation` (\
  `IP` varchar(255) DEFAULT NULL,\
  `State` varchar(255) DEFAULT NULL,\
  `SurgeCommand` varchar(255) DEFAULT NULL,\
  `LGA` varchar(255) DEFAULT NULL,\
  `FacilityName` varchar(255) DEFAULT NULL,\
`Pepid_datim` varchar(500) PRIMARY KEY,\
`PEPID` varchar(500) NOT NULL,\
  `person_id` double DEFAULT NULL,\
  `encounter_id` double DEFAULT NULL,\
  `encounter_datetime` timestamp(6) NULL DEFAULT NULL,\
  `Tracking_Date` timestamp(6) NULL DEFAULT NULL,\
  `Reason_For_Tracking` varchar(255) DEFAULT NULL,\
  `Partner_Full_Name` varchar(255) DEFAULT NULL,\
  `Address_of_Tx_Supporter` varchar(255) DEFAULT NULL,\
  `Contact_Phone_No` varchar(255) DEFAULT NULL,\
  `Date_of_Last_Actual` timestamp(6) NULL DEFAULT NULL,\
  `Date_Missed_Scheduled_App` timestamp(6) NULL DEFAULT NULL,\
  `ContAttempt_Date1` timestamp(6) NULL DEFAULT NULL,\
  `Who_Attempted_Contact1` varchar(255) DEFAULT NULL,\
  `Mode_of_Communication1` varchar(255) DEFAULT NULL,\
  `Person_Contacted1` varchar(255) DEFAULT NULL,\
  `Reason_for_Defaulting1` varchar(255) DEFAULT NULL,\
  `Reason_for_Discontinuation` varchar(255) DEFAULT NULL,\
  `Date_of_Discontinuation` timestamp(6) NULL DEFAULT NULL,\
  `Previous_ARV_exposure` varchar(255) DEFAULT NULL,\
  `Referred_for` varchar(255) DEFAULT NULL,\
  `Date_Returned` timestamp(6) NULL DEFAULT NULL,\
  `Returned_to_Treatment_Status` varchar(255) DEFAULT NULL,\
  `Date_LTFU` varchar(255) DEFAULT NULL,\
  `Reason_LTFU` varchar(255) DEFAULT NULL,\
  `LTFU` varchar(255) DEFAULT NULL,\
  `Name_of_Tracker` varchar(255) DEFAULT NULL,\
  `Tracker_Sig_Date` timestamp(6) NULL DEFAULT NULL,\
  `Facility_Transferred_To` varchar(255) DEFAULT NULL\
`List_Parameters` varchar(255) DEFAULT NULL)")


create_recency_standalone = ("CREATE TABLE IF NOT EXISTS `recency_standalone` (\
    `IP` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `State` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `SurgeCommand` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `LGA` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `City_of_Residence` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `DATIMCode` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `FacilityName` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `patient_id` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `Datim_HTS_ClientCode` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `HTS_ClientCode` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `PEPFAR_Number_IfOnART` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `Birthdate` DATETIME DEFAULT NULL,\
    `Sex` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `Age <= 15 (at Test)?` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `given_name` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `family_name` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `PhoneNumber` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `VisitDate` DATETIME DEFAULT NULL,\
    `Test_VisitDate_Validation` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `KindOfHTS` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `Setting` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `HIVScreeningTestDate` DATETIME DEFAULT NULL,\
    `Opt_Out_of_RTRI?` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `HIVRecencyTestName` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `Recency Number` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `ControlLine` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `VerificationLine` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `LongTermLine` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `HIVRecencyTestDate` DATETIME DEFAULT NULL,\
    `RecencyInterpretation` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `ViralLoadRequest` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `VLSampleCollectionDate` DATETIME DEFAULT NULL,\
    `PCR_LabNo` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `SampleType` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `PCR_Laboratory` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `HIV_ViralLoad` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `FinalHIVRecencyResult` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL)")

create_Nutritional_Status = ("CREATE TABLE IF NOT EXISTS `Nutritional_Status` (\
    `IP` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `State` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `SurgeCommand` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `LGA` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `FacilityName` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `DATIMCode` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `patient_id` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `PEPID` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `Birthdate` DATETIME DEFAULT NULL,\
    `SEX` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `Educational level` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `Occupation` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `Next_of_kin` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `NOK_Phone_no` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `LGA of residence` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `State of Residence` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `Date of enrolment into care` DATETIME DEFAULT NULL,\
    `Date of ART initiation` DATETIME DEFAULT NULL,\
    `Q1_Visit_Date(W)` DATETIME DEFAULT NULL,\
    `Q1_Weight(kg)` double DEFAULT NULL,\
    `Q1_Visit_Date(H)` DATETIME DEFAULT NULL,\
    `Q1_Height(cm)` double DEFAULT NULL,\
    `Q1_BMI` double DEFAULT NULL,\
    `Q2_Visit_Date(W)` DATETIME DEFAULT NULL,\
    `Q2_Weight(kg)` double DEFAULT NULL,\
    `Q2_Visit_Date(H)` DATETIME DEFAULT NULL,\
    `Q2_Height(cm)` double DEFAULT NULL,\
    `Q2_BMI` double DEFAULT NULL,\
    `Q3_Visit_Date(W)` DATETIME DEFAULT NULL,\
    `Q3_Weight(kg)` double DEFAULT NULL,\
    `Q3_Visit_Date(H)` double DEFAULT NULL,\
    `Q3_Height(cm)` double DEFAULT NULL,\
    `Q3_BMI` double DEFAULT NULL,\
    `Q4_Visit_Date(W)` DATETIME DEFAULT NULL,\
    `Q4_Weight(kg)` double DEFAULT NULL,\
    `Q4_Visit_Date(H)` DATETIME DEFAULT NULL,\
    `Q4_Height(cm)` double DEFAULT NULL,\
    `Q4_BMI` double DEFAULT NULL,\
    `Marital status` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `Surname` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `FirstName` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
    `Phone_No` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL)")


create_Last_6_Viral_Load_Sample_Result = ("CREATE TABLE  IF NOT EXISTS `Last_6_Viral_Load_Sample_Result` (\
    `IP` longtext CHARACTER SET utf8 DEFAULT NULL,\
  `State` longtext CHARACTER SET utf8 DEFAULT NULL,\
  `SurgeCommand` longtext CHARACTER SET utf8 DEFAULT NULL,\
  `LGA` longtext CHARACTER SET utf8 DEFAULT NULL,\
  `FacilityName` mediumtext CHARACTER SET utf8 DEFAULT NULL,\
  `DatimCode` mediumtext CHARACTER SET utf8 DEFAULT NULL,\
  `Pepid_Datim` longtext CHARACTER SET utf8 DEFAULT NULL,\
  `Patient_id` int(11) NOT NULL DEFAULT '0',\
  `Pepid` varchar(50) CHARACTER SET utf8 DEFAULT '',\
  `CurrentAge` bigint(21) DEFAULT NULL,\
  `1st_Last_Sample_Collection` datetime,\
  `1st_Last_ViralLoadIndication` text,\
  `1st_Last_VLDate` datetime,\
  `1st_Last_VL` double DEFAULT NULL,\
  `1st_Last_Date_Result_Received` datetime DEFAULT NULL,\
  `2nd_Last_Sample_Collection` datetime,\
  `2nd_Last_ViralLoadIndication` text,\
  `2nd_Last_VLDate` datetime,\
  `2nd_Last_VL` double DEFAULT NULL,\
  `2nd_Last_Date_Result_Received` datetime DEFAULT NULL,\
  `3rd_Last_Sample_Collection` datetime,\
  `3rd_Last_ViralLoadIndication` text,\
  `3rd_Last_VLDate` datetime,\
  `3rd_Last_VL` double DEFAULT NULL,\
  `3rd__Last_Date_Result_Received` datetime DEFAULT NULL,\
  `4th_Last_Sample_Collection` datetime,\
  `4th_Last_ViralLoadIndication` text,\
  `4th_Last_VLDate` datetime,\
  `4th_Last_VL` double DEFAULT NULL,\
  `4th_Last_Date_Result_Received` datetime DEFAULT NULL,\
  `5th_Last_Sample_Collection` datetime,\
  `5th_Last_ViralLoadIndication` text,\
  `5th_Last_VLDate` datetime,\
  `5th_Last_VL` double DEFAULT NULL,\
  `5th_Last_Date_Result_Received` datetime DEFAULT NULL,\
  `6th_Last_Sample_Collection` datetime,\
  `6th_Last_ViralLoadIndication` text,\
  `6th_Last_VLDate` datetime,\
  `6th_Last_VL` double DEFAULT NULL,\
  `6th_Last_Date_Result_Received` datetime DEFAULT NULL)")



create_Service_Integrator_Log_SIMO = ("CREATE TABLE  IF NOT EXISTS `Service_Integrator_Log_SIMO` (\
    `IP` varchar(255) CHARACTER SET utf8 DEFAULT NULL,\
  `State` varchar(255) CHARACTER SET utf8 DEFAULT NULL,\
  `SurgeCommand` varchar(255) CHARACTER SET utf8 DEFAULT NULL,\
  `LGA` varchar(255) CHARACTER SET utf8 DEFAULT NULL,\
  `Datim_code` varchar(255) CHARACTER SET utf8 DEFAULT NULL,\
  `Facilityname` varchar(255) CHARACTER SET utf8 DEFAULT NULL,\
  `Pepid_Datim_code` varchar(255) CHARACTER SET utf8 DEFAULT NULL,\
  `Patient_Id` varchar(255) CHARACTER SET utf8 DEFAULT NULL,\
  `Pepid` varchar(255) CHARACTER SET utf8 DEFAULT NULL,\
  `Client_Bio` varchar(255) CHARACTER SET utf8 DEFAULT NULL,\
  `Last_Pickup_Date` varchar(255) CHARACTER SET utf8 DEFAULT NULL,\
  `Duration_Last_Pickup` varchar(255) CHARACTER SET utf8 DEFAULT NULL,\
  `Pill_Balance` varchar(255) CHARACTER SET utf8 DEFAULT NULL,\
  `Last_VL_Date` varchar(255) CHARACTER SET utf8 DEFAULT NULL,\
  `Last_VL_Result` varchar(255) CHARACTER SET utf8 DEFAULT NULL,\
  `Bleeding_Alert` varchar(255) CHARACTER SET utf8 DEFAULT NULL,\
  `Suggested_Next_Appt_Date` varchar(255) CHARACTER SET utf8 DEFAULT NULL,\
  `Suggested_Next_Appt_Day` varchar(255) CHARACTER SET utf8 DEFAULT NULL,\
  `Actual_Suggested_Next_Appt_Date` varchar(255) CHARACTER SET utf8 DEFAULT NULL,\
  `Actual_Suggested_Next_Appt_Day` varchar(255) CHARACTER SET utf8 DEFAULT NULL,\
  `Key_Note` longtext CHARACTER SET utf8,\
  `Search_Timestamp` timestamp NULL DEFAULT CURRENT_TIMESTAMP)")

create_Extended_Treatment_Linelist = ("CREATE TABLE  IF NOT EXISTS `extended_treatment_linelist` (\
  `IP` varchar(255) DEFAULT NULL,\
  `State` varchar(255) DEFAULT NULL,\
  `SurgeCommand` varchar(255) DEFAULT NULL,\
  `LGA` varchar(255) DEFAULT NULL,\
  `FacilityName` varchar(255) DEFAULT NULL,\
  `DATIMCode` varchar(255) DEFAULT NULL,\
  `Pepid_datim` varchar(255) DEFAULT NULL,\
  `patient_id` varchar(255) DEFAULT NULL,\
  `Pepid` varchar(255) DEFAULT NULL,\
  `HospitalNo` varchar(255) DEFAULT NULL,\
  `Sex` varchar(255) DEFAULT NULL,\
  `Date_of_PregStatus` timestamp(6) NULL DEFAULT NULL,\
  `PregStatus` varchar(255) DEFAULT NULL,\
  `Date_Enrolled` timestamp(6) NULL DEFAULT NULL,\
  `DOB` timestamp(6) NULL DEFAULT NULL,\
  `AgeAtStartofART` double DEFAULT NULL,\
  `CurrentAge` double DEFAULT NULL,\
  `ARTStartDate` timestamp(6) NULL DEFAULT NULL,\
  `RegLineAtStart` varchar(255) DEFAULT NULL,\
  `ARTRegAtStart` varchar(255) DEFAULT NULL,\
  `TI_Date` varchar(255) DEFAULT NULL,\
  `LastPickupDate` timestamp(6) NULL DEFAULT NULL,\
  `NextAppmt` timestamp(6) NULL DEFAULT NULL,\
  `DaysOfARVRefill` double DEFAULT NULL,\
  `CurrentARTStatus_28Days` varchar(255) DEFAULT NULL,\
  `CurrentRegLine` varchar(255) DEFAULT NULL,\
  `CurrentARTReg` varchar(255) DEFAULT NULL,\
  `Switch_Substitution` varchar(255) DEFAULT NULL,\
  `Date_AtStart_of_Current_ARTregimen` varchar(255) DEFAULT NULL,\
  `CurrentVL` double DEFAULT NULL,\
  `DateOfCurrentVL` timestamp(6) NULL DEFAULT NULL,\
  `ViralLoadIndication` varchar(255) DEFAULT NULL,\
  `Date_Result_Received` timestamp(6) NULL DEFAULT NULL,\
  `Last_VL_Sample_Collection_Date` timestamp(6) NULL DEFAULT NULL,\
  `Indication_for_CD4` varchar(255) DEFAULT NULL,\
  `CD4_LFA_Result` varchar(255) DEFAULT NULL,\
  `Date_CD4_LFA` varchar(255) DEFAULT NULL,\
  `CD4_Percentage` varchar(255) DEFAULT NULL,\
  `Date_of_CD4_Percentage` varchar(255) DEFAULT NULL,\
  `CD4_cell_count` varchar(255) DEFAULT NULL,\
  `Date_of_CD4_Cell_count` varchar(255) DEFAULT NULL,\
  `TB_LF_LAM_Result` varchar(255) DEFAULT NULL,\
  `Date_TB_LF_LAM_Result_Received` varchar(255) DEFAULT NULL,\
  `Serology_For_CrAg_Result` varchar(255) DEFAULT NULL,\
  `Date_Serology_For_CrAg_Result_Received` varchar(255) DEFAULT NULL,\
  `CSF_For_CrAg_Result` varchar(255) DEFAULT NULL,\
  `Date_CSF_For_CrAg_Result_Received` varchar(255) DEFAULT NULL,\
  `Cryptococcal_Screening_Status` varchar(255) DEFAULT NULL,\
  `ICE_WHO_Staging` varchar(255) DEFAULT NULL,\
  `RTT` varchar(255) DEFAULT NULL,\
  `RTT_Date` varchar(255) DEFAULT NULL,\
  `RTT_after_IIT_Lessthan_12months` varchar(255) DEFAULT NULL,\
  `RTT_Outcome` varchar(255) DEFAULT NULL,\
  `ART_Status_Previous_quarter` varchar(255) DEFAULT NULL,\
  `Last_Weight` double DEFAULT NULL,\
  `Last_Weight_Date` timestamp(6) NULL DEFAULT NULL,\
  `Eligible_For_IPT` varchar(255) DEFAULT NULL,\
  `Last_TB_Screening_Date` timestamp(6) NULL DEFAULT NULL,\
  `Last_TB_Screening_Status` varchar(255) DEFAULT NULL,\
  `TB_Investigations` varchar(255) DEFAULT NULL,\
  `Investig_Result` varchar(255) DEFAULT NULL,\
  `Date_TB_Investig` timestamp(6) NULL DEFAULT NULL,\
  `Date_IPT_start` timestamp(6) NULL DEFAULT NULL,\
  `Outcome_of_IPT` varchar(255) DEFAULT NULL,\
  `Date_of_Outcome` varchar(255) DEFAULT NULL,\
  `Last_Clinic_Visit_Date` timestamp(6) NULL DEFAULT NULL,\
  `Systolic_BP` double DEFAULT NULL,\
  `Diastolic_BP` double DEFAULT NULL,\
  `Tracking_Date` timestamp(6) NULL DEFAULT NULL,\
  `Reason_for_tracking` varchar(255) DEFAULT NULL,\
  `Tracking_Outcome` varchar(255) DEFAULT NULL,\
  `Date_of_Tracking_Outcome` varchar(255) DEFAULT NULL,\
  `Reason_for_Discontinuation` varchar(255) DEFAULT NULL,\
  `Date_of_Discontinuation` timestamp(6) NULL DEFAULT NULL,\
  `Facility_Transferred_To` timestamp(6) NULL DEFAULT NULL,\
  `VL_result__before_EAC` timestamp(6) NULL DEFAULT NULL,\
  `Date_of_VL_before_EAC_was_received` timestamp(6) NULL DEFAULT NULL,\
  `EAC_start_Date` timestamp(6) NULL DEFAULT NULL,\
  `EAC_Adherence_Outcome` timestamp(6) NULL DEFAULT NULL,\
  `Date_of_2nd_EAC` timestamp(6) NULL DEFAULT NULL,\
  `2nd_EAC_Adherence_Outcome` timestamp(6) NULL DEFAULT NULL,\
  `Date_of_3rd_EAC` timestamp(6) NULL DEFAULT NULL,\
  `3rd_EAC_Adherence_Outcome` timestamp(6) NULL DEFAULT NULL,\
  `Date_of_Additional_EAC` timestamp(6) NULL DEFAULT NULL,\
  `Date_of_Post_EAC_VL_sample_collection` timestamp(6) NULL DEFAULT NULL,\
  `Post_EAC_VL_result` timestamp(6) NULL DEFAULT NULL,\
  `Date_of_Post_EAC_VL_result_Received` timestamp(6) NULL DEFAULT NULL,\
  `DSD_Status` varchar(255) DEFAULT NULL,\
  `Date_of_devolvement_to_DSD_model` varchar(255) DEFAULT NULL,\
  `DSD_Model` varchar(255) DEFAULT NULL,\
  `DSD_Model_Type` varchar(255) DEFAULT NULL,\
  `Date_Enrolled_into_OTZ` varchar(255) DEFAULT NULL,\
  `OTZ_Disclosure_status` varchar(255) DEFAULT NULL,\
  `OTZ_Date_of_Full_Dsiclosure` varchar(255) DEFAULT NULL,\
  `Date_of_commencement_of_OTZ_Modules` varchar(255) DEFAULT NULL,\
  `Number_of_OTZ_modules_completed` varchar(255) DEFAULT NULL,\
  `Date_of_Completion_of_Final_Module` varchar(255) DEFAULT NULL,\
  `OTZ_Program_Outcome` varchar(255) DEFAULT NULL,\
  `Date_transitioned_into_Adult_care` varchar(255) DEFAULT NULL,\
  `Biometrics_Captured` timestamp(6) NULL DEFAULT NULL,\
  `Recapture_Count` double DEFAULT NULL,\
  `Date_Last_Recaptured` timestamp(6) NULL DEFAULT NULL,\
  `List_Parameters` varchar(255) DEFAULT NULL,\
  `Date_List_Gen` timestamp(6) NULL DEFAULT NULL)")


insert_Available_Linelist = """
SELECT CONCAT(list_name, ' - ', parsed_date) AS sweedy FROM (SELECT * FROM (
    SELECT 
      'Treatment Line List              ' AS list_name,
      DATE(CONCAT(LEFT(CURRENT_DATE, 2), 
                  RIGHT(SUBSTRING_INDEX(List_Parameters, '-', 1), 2), '-', 
                  RIGHT(SUBSTRING_INDEX(List_Parameters, '-', 2), 2), '-', 
                  RIGHT(List_Parameters, 2))) AS parsed_date
    FROM validation_linelist.full_linelist_for_quick_list_update
    LIMIT 1
) AS t1

UNION ALL 

SELECT * FROM (
    SELECT 
      'OTZ Line List                        ',
      DATE(CONCAT(LEFT(CURRENT_DATE, 2), 
                  RIGHT(SUBSTRING_INDEX(List_Parameters, '-', 1), 2), '-', 
                  RIGHT(SUBSTRING_INDEX(List_Parameters, '-', 2), 2), '-',
                  RIGHT(List_Parameters, 2)))
    FROM validation_linelist.otz_linelist_for_ex
    LIMIT 1
) AS t2

UNION ALL

SELECT * FROM (
    SELECT 
      'AHD Line List                        ',
      DATE(CONCAT(LEFT(CURRENT_DATE, 2), 
                  RIGHT(SUBSTRING_INDEX(List_Parameters, '-', 1), 2), '-', 
                  RIGHT(SUBSTRING_INDEX(List_Parameters, '-', 2), 2), '-', 
                  RIGHT(List_Parameters, 2)))
    FROM validation_linelist.ahd_linelist_for_ex
    LIMIT 1
) AS t3

UNION ALL

SELECT * FROM (
    SELECT 
      'Client Tracking and Discon.',
      DATE(CONCAT(LEFT(CURRENT_DATE, 2), 
                  RIGHT(SUBSTRING_INDEX(List_Parameters, '-', 1), 2), '-', 
                  RIGHT(SUBSTRING_INDEX(List_Parameters, '-', 2), 2), '-', 
                  RIGHT(List_Parameters, 2)))
    FROM validation_linelist.ctd_linelist_for_ex
    LIMIT 1
) AS t4

UNION ALL

SELECT * FROM (
    SELECT 
      'Full Pharmacy Complement ',
      DATE(CONCAT(LEFT(CURRENT_DATE, 2), 
                  RIGHT(SUBSTRING_INDEX(List_Parameters, '-', 1), 2), '-', 
                  RIGHT(SUBSTRING_INDEX(List_Parameters, '-', 2), 2), '-', 
                  RIGHT(List_Parameters, 2)))
    FROM validation_linelist.`full_pharmacy_complement_for_ex`
    LIMIT 1
) AS t5

UNION ALL

SELECT * FROM (
    SELECT 
      'EAC Cascade List                 ',
      DATE(CONCAT(LEFT(CURRENT_DATE, 2), 
                  RIGHT(SUBSTRING_INDEX(List_Parameters, '-', 1), 2), '-', 
                  RIGHT(SUBSTRING_INDEX(List_Parameters, '-', 2), 2), '-', 
                  RIGHT(List_Parameters, 2)))
    FROM validation_linelist.`eac_linelist_for_ex`
    LIMIT 1
) AS t6
ORDER BY parsed_date DESC) a;
"""



tx_Linelist_List_Para = ("SELECT DATE(CONCAT(LEFT(CURRENT_DATE, 2), \
RIGHT(SUBSTRING_INDEX(List_Parameters, '-', 1 ), 2), '-', \
RIGHT(SUBSTRING_INDEX(List_Parameters, '-', 2 ), 2),'-', RIGHT(List_Parameters, 2))) \
FROM `full_linelist_for_quick_list_update` LIMIT 1;")


create_otz_linelist_for_ex = ("CREATE TABLE IF NOT EXISTS `otz_linelist_for_ex` (\
  `IP` varchar(255) DEFAULT NULL,\
  `State` varchar(255) DEFAULT NULL,\
  `SurgeCommand` varchar(255) DEFAULT NULL,\
  `LGA` varchar(255) DEFAULT NULL,\
  `FacilityName` varchar(255) DEFAULT NULL,\
  `Pepid_datim` varchar(255) DEFAULT NULL,\
  `patient_id` double DEFAULT NULL,\
  `Pepid` varchar(255) DEFAULT NULL,\
  `Date_Enrolled_Into_OTZ` timestamp(6) NULL DEFAULT NULL,\
  `OTZ_Disclosure_Status` varchar(255) DEFAULT NULL,\
  `OTZ_Date_of_Full_Disclosure` timestamp(6) NULL DEFAULT NULL,\
  `Enrolled_Into_OTZ_Plus` varchar(255) DEFAULT NULL,\
  `Date_Enrolled_Into_OTZ_Plus` varchar(255) DEFAULT NULL,\
  `Date_of_Commencement_of_OTZ_Module` timestamp(6) NULL DEFAULT NULL,\
  `Positive_Living` varchar(255) DEFAULT NULL,\
  `Positive_Living_Comp_Date` timestamp(6) NULL DEFAULT NULL,\
  `Treatment_Literacy` varchar(255) DEFAULT NULL,\
  `Treatment_Literacy_Comp_Date` timestamp(6) NULL DEFAULT NULL,\
  `Adolescents_Participation` varchar(255) DEFAULT NULL,\
  `Adolescents_Participation_Comp_Date` timestamp(6) NULL DEFAULT NULL,\
  `Leadership_Training` varchar(255) DEFAULT NULL,\
  `Leadership_Training_Comp_Date` timestamp(6) NULL DEFAULT NULL,\
  `Peer_to_Peer_Mentorship` varchar(255) DEFAULT NULL,\
  `Peer_to_Peer_Mentorship_Comp_Date` timestamp(6) NULL DEFAULT NULL,\
  `Role_of_OTZ_in_95_95_95` varchar(255) DEFAULT NULL,\
  `Role_of_OTZ_in_95_95_95_Comp_Date` timestamp(6) NULL DEFAULT NULL,\
  `OTZ_Champion_Orientation` varchar(255) DEFAULT NULL,\
  `OTZ_Champion_Orientation_Comp_Date` timestamp(6) NULL DEFAULT NULL,\
  `Number_of_OTZ_Modules_Completed` double DEFAULT NULL,\
  `Date_of_Final_Module_Completion` timestamp(6) NULL DEFAULT NULL,\
  `Transitioned_to_Adult_Clinic` varchar(255) DEFAULT NULL,\
  `Date_Transitioned_to_Adult_Clinic` varchar(255) DEFAULT NULL,\
  `OTZ_Program_Outcome` varchar(255) DEFAULT NULL,\
  `List_Parameters` varchar(255) DEFAULT NULL)")

create_ahd_linelist_for_ex = ("CREATE TABLE IF NOT EXISTS `ahd_linelist_for_ex` (\
  `IP` varchar(255) DEFAULT NULL,\
  `State` varchar(255) DEFAULT NULL,\
  `SurgeCommand` varchar(255) DEFAULT NULL,\
  `LGA` varchar(255) DEFAULT NULL,\
  `FacilityName` varchar(255) DEFAULT NULL,\
  `Pepid_datim` varchar(255) DEFAULT NULL,\
  `Pepid` varchar(255) DEFAULT NULL,\
  `person_id` double DEFAULT NULL,\
  `Sex` varchar(255) DEFAULT NULL,\
  `Date_Enrolled` timestamp(6) NULL DEFAULT NULL,\
  `ARTStartDate` timestamp(6) NULL DEFAULT NULL,\
  `Indication_for_CD4` varchar(255) DEFAULT NULL,\
  `CD4_LFA_Result` varchar(255) DEFAULT NULL,\
  `Date_of_CD4_LFA_Result` timestamp(6) NULL DEFAULT NULL,\
  `CD4_Percent` varchar(255) DEFAULT NULL,\
  `CD4_Percent_Date` varchar(255) DEFAULT NULL,\
  `CD4_Count` varchar(255) DEFAULT NULL,\
  `CD4_Count_Date` varchar(255) DEFAULT NULL,\
  `TB_LF_LAM_Result` varchar(255) DEFAULT NULL,\
  `Date_TB_LF_LAM_Result_Received` timestamp(6) NULL DEFAULT NULL,\
  `Serology_For_CrAg_Result` varchar(255) DEFAULT NULL,\
  `Date_Serology_For_CrAg_Result_Received` timestamp(6) NULL DEFAULT NULL,\
  `CSF_For_CrAg_Result` varchar(255) DEFAULT NULL,\
  `Date_CSF_For_CrAg_Result_Received` varchar(255) DEFAULT NULL,\
  `ICE_WHO_Staging` double DEFAULT NULL,\
  `Cryptococcal_Screening_Status` varchar(255) DEFAULT NULL,\
  `List_Parameters` varchar(255) DEFAULT NULL)")


create_ctd_linelist_for_ex = ("CREATE TABLE IF NOT EXISTS `ctd_linelist_for_ex` (\
  `IP` varchar(255) DEFAULT NULL,\
  `State` varchar(255) DEFAULT NULL,\
  `SurgeCommand` varchar(255) DEFAULT NULL,\
  `LGA` varchar(255) DEFAULT NULL,\
  `FacilityName` varchar(255) DEFAULT NULL,\
  `person_id` double DEFAULT NULL,\
  `encounter_id` double DEFAULT NULL,\
  `encounter_datetime` timestamp(6) NULL DEFAULT NULL,\
  `Tracking_Date` timestamp(6) NULL DEFAULT NULL,\
  `Reason_For_Tracking` varchar(255) DEFAULT NULL,\
  `Partner_Full_Name` varchar(255) DEFAULT NULL,\
  `Address_of_Tx_Supporter` varchar(255) DEFAULT NULL,\
  `Contact_Phone_No` varchar(255) DEFAULT NULL,\
  `Date_of_Last_Actual` timestamp(6) NULL DEFAULT NULL,\
  `Date_Missed_Scheduled_App` timestamp(6) NULL DEFAULT NULL,\
  `ContAttempt_Date1` timestamp(6) NULL DEFAULT NULL,\
  `Who_Attempted_Contact1` varchar(255) DEFAULT NULL,\
  `Mode_of_Communication1` varchar(255) DEFAULT NULL,\
  `Person_Contacted1` varchar(255) DEFAULT NULL,\
  `Reason_for_Defaulting1` varchar(255) DEFAULT NULL,\
  `Reason_for_Discontinuation` varchar(255) DEFAULT NULL,\
  `Date_of_Discontinuation` timestamp(6) NULL DEFAULT NULL,\
  `Previous_ARV_exposure` varchar(255) DEFAULT NULL,\
  `Referred_for` varchar(255) DEFAULT NULL,\
  `Date_Returned` timestamp(6) NULL DEFAULT NULL,\
  `Returned_to_Treatment_Status` varchar(255) DEFAULT NULL,\
  `Date_LTFU` varchar(255) DEFAULT NULL,\
  `Reason_LTFU` varchar(255) DEFAULT NULL,\
  `LTFU` varchar(255) DEFAULT NULL,\
  `Name_of_Tracker` varchar(255) DEFAULT NULL,\
  `Tracker_Sig_Date` timestamp(6) NULL DEFAULT NULL,\
  `Facility_Transferred_To` varchar(255) DEFAULT NULL)")


create_client_tracking_and_discontinuation = ("CREATE TABLE IF NOT EXISTS `client_tracking_and_discontinuation` (\
  `IP` varchar(255) DEFAULT NULL,\
  `State` varchar(255) DEFAULT NULL,\
  `SurgeCommand` varchar(255) DEFAULT NULL,\
  `LGA` varchar(255) DEFAULT NULL,\
  `FacilityName` varchar(255) DEFAULT NULL,\
  `person_id` double DEFAULT NULL,\
  `encounter_id` double DEFAULT NULL,\
  `encounter_datetime` timestamp(6) NULL DEFAULT NULL,\
  `Tracking_Date` timestamp(6) NULL DEFAULT NULL,\
  `Reason_For_Tracking` varchar(255) DEFAULT NULL,\
  `Partner_Full_Name` varchar(255) DEFAULT NULL,\
  `Address_of_Tx_Supporter` varchar(255) DEFAULT NULL,\
  `Contact_Phone_No` varchar(255) DEFAULT NULL,\
  `Date_of_Last_Actual` timestamp(6) NULL DEFAULT NULL,\
  `Date_Missed_Scheduled_App` timestamp(6) NULL DEFAULT NULL,\
  `ContAttempt_Date1` timestamp(6) NULL DEFAULT NULL,\
  `Who_Attempted_Contact1` varchar(255) DEFAULT NULL,\
  `Mode_of_Communication1` varchar(255) DEFAULT NULL,\
  `Person_Contacted1` varchar(255) DEFAULT NULL,\
  `Reason_for_Defaulting1` varchar(255) DEFAULT NULL,\
  `Reason_for_Discontinuation` varchar(255) DEFAULT NULL,\
  `Date_of_Discontinuation` timestamp(6) NULL DEFAULT NULL,\
  `Previous_ARV_exposure` varchar(255) DEFAULT NULL,\
  `Referred_for` varchar(255) DEFAULT NULL,\
  `Date_Returned` timestamp(6) NULL DEFAULT NULL,\
  `Returned_to_Treatment_Status` varchar(255) DEFAULT NULL,\
  `Date_LTFU` varchar(255) DEFAULT NULL,\
  `Reason_LTFU` varchar(255) DEFAULT NULL,\
  `LTFU` varchar(255) DEFAULT NULL,\
  `Name_of_Tracker` varchar(255) DEFAULT NULL,\
  `Tracker_Sig_Date` timestamp(6) NULL DEFAULT NULL,\
  `Facility_Transferred_To` varchar(255) DEFAULT NULL)")


create_eac_linelist = """
CREATE TABLE IF NOT EXISTS `eac_linelist` 
  `IP` varchar(4) CHARACTER SET utf8 NOT NULL DEFAULT '',
  `State` longtext CHARACTER SET utf8,
  `SurgeCommand` longtext CHARACTER SET utf8,
  `LGA` longtext CHARACTER SET utf8,
  `FacilityName` longtext CHARACTER SET utf8,
  `Pepid_datim` longtext CHARACTER SET utf8,
  `Pepid` varchar(50) CHARACTER SET utf8 DEFAULT '',
  `patient_id` int(11) NOT NULL DEFAULT '0',
  `ARTStartDate` datetime DEFAULT NULL,
  `Current_Age` bigint(21) DEFAULT NULL,
  `Indication_For_VL` varchar(61) CHARACTER SET utf8 DEFAULT NULL,
  `VL_Result_Before_EAC` double DEFAULT NULL,
  `Date_of_VL_Result_Before_EAC` datetime,
  `First_EAC_Session` varchar(15) CHARACTER SET utf8 DEFAULT NULL,
  `Date_of_First_EAC_Session` datetime DEFAULT NULL,
  `ARV_Adherence_First_Session` varchar(4) CHARACTER SET utf8 DEFAULT NULL,
  `Second_EAC_Session` varchar(15) CHARACTER SET utf8 DEFAULT NULL,
  `Date_of_Second_EAC_Session` datetime DEFAULT NULL,
  `ARV_Adherence_Second_Session` varchar(4) CHARACTER SET utf8 DEFAULT NULL,
  `Third_EAC_Session` varchar(15) CHARACTER SET utf8 DEFAULT NULL,
  `Date_of_Third_EAC_Session` datetime DEFAULT NULL,
  `ARV_Adherence_Third_Session` varchar(4) CHARACTER SET utf8 DEFAULT NULL,
  `Additional_EAC_Session` varchar(17) CHARACTER SET utf8 DEFAULT NULL,
  `Date_of_Additional_EAC_Session` datetime DEFAULT NULL,
  `ARV_Adherence_Additional_Session` varchar(4) CHARACTER SET utf8 DEFAULT NULL,
  `Sample_Collection_Date_After_EAC` datetime DEFAULT NULL,
  `VL_Result_After_EAC` double DEFAULT NULL,
  `Date_of_VL_Result_After_EAC` datetime DEFAULT NULL,
  `List_Parameters` varchar(20) CHARACTER SET utf8 DEFAULT NULL)
  """

