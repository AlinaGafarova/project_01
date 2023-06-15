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