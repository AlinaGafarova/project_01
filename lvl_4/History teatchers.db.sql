--- 12-06-2023 02:06:41
--- teatchers.db
SELECT * FROM Teatcher;

--- 12-06-2023 02:07:50
--- teatchers.db
-- SELECT * FROM Teatcher;
CREATE TABLE Students (
  Student_Id Integer , 
  Student_Name Text, 
  School_Id Integer);

--- 12-06-2023 02:10:34
--- teatchers.db
-- SELECT * FROM Teatcher;
-- CREATE TABLE Students (
  -- Student_Id Integer , 
  -- Student_Name Text, 
  -- School_Id Integer);
INSERT INTO Students (student_id, student_name, school_id)
VALUES
 (205, 'Иван', 1),
 (202, 'Петр', 2),
 (203, 'Анастасия', 3),
 (204, 'Игорь', 4);

--- 12-06-2023 02:11:26
--- teatchers.db
-- SELECT * FROM Teatcher;
-- CREATE TABLE Students (
  -- Student_Id Integer , 
  -- Student_Name Text, 
  -- School_Id Integer);
-- INSERT INTO Students (student_id, student_name, school_id)
-- VALUES
-- (205, 'Иван', 1),
-- (202, 'Петр', 2),
-- (203, 'Анастасия', 3),
-- (204, 'Игорь', 4);
SELECT * FROM Students;

--- 12-06-2023 02:57:31
--- teatchers.db
-- SELECT * FROM Teatcher;
-- CREATE TABLE Students (
  -- Student_Id Integer , 
  -- Student_Name Text, 
  -- School_Id Integer);
-- INSERT INTO Students (student_id, student_name, school_id)
-- VALUES
-- (205, 'Иван', 1),
-- (202, 'Петр', 2),
-- (203, 'Анастасия', 3),
-- (204, 'Игорь', 4);
-- SELECT * FROM Students;
SELECT Students.Student_Id, Students.Student_Name, School.School_Id, School.School_Name
FROM Students
JOIN School on Students.school_id = School.School_Id;

