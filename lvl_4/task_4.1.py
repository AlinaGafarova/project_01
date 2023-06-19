import sqlite3


def get_connection():
    connection = sqlite3.connect('sqlite.db')
    return connection


def close_connection(connection):
    if connection:
        connection.close()


def get_student(student_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sqlquery = "SELECT Students.Student_Id, Students.Student_Name, School.School_Id, School.School_Name " \
                   "FROM Students JOIN School on Students.school_id = School.School_Id " \
                   "WHERE Student_Id = ?"
        cursor.execute(sqlquery, (student_id,))
        records = cursor.fetchall()
        print("Данные по студенту:")
        for row in records:
            print("Student_Id:", row[0], "\nStudent_Name:", row[1], "\nSchool_Id:", row[2], "\nSchool_Name:", row[3])
    except (Exception, sqlite3.Error) as error:
        print("Ошибка", error)
    close_connection(connection)

id = int(input("Введите ID студента: "))
get_student(id)
