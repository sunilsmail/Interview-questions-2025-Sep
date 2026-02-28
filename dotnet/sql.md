CREATE PROCEDURE dbo.BulkUpdateEmployees
    @Employees dbo.EmployeeType READONLY
AS
BEGIN
    MERGE Employees AS target
    USING @Employees AS source
    ON target.Id = source.Id

    WHEN MATCHED THEN
        UPDATE SET 
            target.Name = source.Name,
            target.Salary = source.Salary;
END