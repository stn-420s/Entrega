-- Active: 1693094085421@@127.0.0.1@3306@impo

drop table if exists r1;

CREATE TABLE r1 AS SELECT es.EmployeeID, es.EnvironmentSatisfaction, es.JobSatisfaction, es.WorkLifeBalance, 
gd.Age, gd.BusinessTravel, gd.Department, gd.DistanceFromHome, gd.Education, gd.EducationField, gd.EmployeeCount, gd.Gender, gd.JobLevel, gd.JobRole, gd.MaritalStatus, gd.MonthlyIncome, gd.NumCompaniesWorked, gd.Over18, gd.PercentSalaryHike, gd.StandardHours, gd.StockOptionLevel, gd.TotalWorkingYears, gd.TrainingTimesLastYear, gd.YearsAtCompany, gd.YearsSinceLastPromotion, gd.YearsWithCurrManager 
FROM impo.es AS es 
LEFT JOIN impo.gd AS gd ON es.EmployeeID = gd.EmployeeID;

SELECT COUNT(*) AS cantidad_filas
FROM r1;

drop table if exists r2;

CREATE TABLE r2 AS SELECT r1.EmployeeID, r1.EnvironmentSatisfaction, r1.JobSatisfaction, r1.WorkLifeBalance, r1.Age, r1.BusinessTravel, r1.Department, r1.DistanceFromHome, r1.Education, r1.EducationField, r1.EmployeeCount, r1.Gender, r1.JobLevel, r1.JobRole, r1.MaritalStatus, r1.MonthlyIncome, r1.NumCompaniesWorked, r1.Over18, r1.PercentSalaryHike, r1.StandardHours, r1.StockOptionLevel, r1.TotalWorkingYears, r1.TrainingTimesLastYear, r1.YearsAtCompany, r1.YearsSinceLastPromotion, r1.YearsWithCurrManager,  
ms.JobInvolvement, ms.PerformanceRating
FROM r1  
LEFT JOIN impo.ms AS ms ON r1.EmployeeID = ms.EmployeeID;

drop table if exists r3;

CREATE TABLE r3 AS SELECT
r2.EmployeeID, r2.EnvironmentSatisfaction, r2.JobSatisfaction, r2.WorkLifeBalance, r2.Age, r2.BusinessTravel, r2.Department, r2.DistanceFromHome, r2.Education, r2.EducationField, r2.EmployeeCount, r2.Gender, r2.JobLevel, r2.JobRole, r2.MaritalStatus, r2.MonthlyIncome, r2.NumCompaniesWorked, r2.Over18, r2.PercentSalaryHike, r2.StandardHours, r2.StockOptionLevel, r2.TotalWorkingYears, r2.TrainingTimesLastYear, r2.YearsAtCompany, r2.YearsSinceLastPromotion, r2.YearsWithCurrManager, r2.JobInvolvement, r2.PerformanceRating,
ri.Attrition, ri.retirementDate, ri.retirementType, ri.resignationReason
FROM r2  
LEFT JOIN impo.ri AS ri ON r2.EmployeeID = ri.EmployeeID;

select * from r3;
SELECT COUNT(*) AS cantidad_filas
FROM r3;

SELECT COUNT(*) AS cantidad_columnas
FROM information_schema.columns
WHERE table_schema = 'impo'
AND table_name = 'r3';

-- Los archivos fueron importados y exportados a través de MySQL.