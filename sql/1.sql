create table author (
	id int identity primary key,
  	fio nvarchar(100) not null,
  	bdate datetime
)

create table book (
	id int identity primary key,
  	bookName nvarchar(100) not null,
  	authorId int foreign key references author(id),
  	publicationYear datetime ,
  	isReturn bit default 0
)

create table reader (
	id int identity PRIMARY key,
  	fio nvarchar(100) not null,
  	bdate datetime not null,
  	phone nvarchar(20) not null,
  	address nvarchar(100) not null
)

create table orders (
	id int identity primary key,
  	bookId int foreign key references book(id),
  	readerId int foreign key references reader(id),
  	startDate datetime ,
  	endDate datetime,
  	isBlackList bit default 0
)


update book
set isreturn = 1
where id % 3 = 2


update orders
set isBlackList = 1
where id % 10 = 0


update orders
set endDate = dateadd(day, 30, startdate)



CREATE table students (
 id int identity primary key,
   fullname nvarchar(100) not null,
   bdate datetime not null
)
CREATE table groups (
 id int identity primary key,
   groupname nvarchar(100) not null
)
create table groupsstudents (
 id int identity primary key,
   groupsid int foreign key references groups(id),
   studentsid int foreign key references students(id)
)
         
create table Student (
  	id int identity primary key,
	FirstName VARCHAR(50),
	LastName VARCHAR(50),
	Email VARCHAR(50),
	BirthDate DATE
);
  


create table Achievements (
  	id int identity primary key,
  	Assesment int not null,
	StudentId INT FOREIGN key references Student(id)
);
               
create table section 
(
	id int identity primary key,
	name nvarchar(50) not null unique
)

create table class 
(
	id int identity primary key,
	name nvarchar(50) not null unique
)

create table instructor
(
	id int identity primary key,
	fio nvarchar(100) not null,
	nick nvarchar(15) not null,
	workExperience int not null,
	price int not null,
	sectionId int foreign key references section(id),
	classId int foreign key references class(id)
)

create table client 
(
	id int identity primary key,
	name nvarchar(50) not null unique,
	instructorId int foreign key references instructor(id)
)

-- 1
SELECT GroupName, DepartmentName 
FROM Groups 
JOIN Departments ON Groups.DepartmentID = Departments.ID 
WHERE Year > DATEADD(year, -5, GETDATE());

--2
SELECT TOP 1 Name 
FROM Teachers 
ORDER BY Salary DESC;

--3
SELECT TOP 1 FacultyName 
FROM Faculties 
ORDER BY Funding ASC;


--4
SELECT COUNT(*) 
FROM Groups 
WHERE Schedule LIKE '%Monday%';


--5
SELECT LectureRoom, TeacherName, Subject 
FROM Lectures 
JOIN Teachers ON Lectures.TeacherID = Teachers.ID 
WHERE Teachers.Salary > 10000;

-- 6
SELECT Year, COUNT(*) 
FROM Departments 
JOIN Faculties ON Departments.FacultyID = Faculties.ID 
WHERE Faculties.Name LIKE 'A%' 
GROUP BY Year;

-- 7
SELECT FacultyName, SUM(Funding) 
FROM Faculties 
GROUP BY FacultyName;

--8
SELECT TeacherName, GroupName 
FROM Teachers 
JOIN Groups ON Teachers.GroupID = Groups.ID 
WHERE GroupName LIKE '%[0-9]%';


--9
SELECT COUNT(*), TeacherName 
FROM Subjects 
JOIN Teachers ON Subjects.TeacherID = Teachers.ID 
GROUP BY TeacherName;

--10
SELECT FacultyName, DepartmentName 
FROM Faculties 
JOIN Departments ON Faculties.ID = Departments.FacultyID 
ORDER BY Faculties.Funding ASC, Departments.Funding ASC

---11
SELECT GroupName, LectureRoom 
FROM Lectures 
JOIN Groups ON Lectures.GroupID = Groups.ID 
WHERE DayOfWeek = 'Monday';


--12
SELECT Salary, TeacherName 
FROM Teachers 
JOIN Subjects ON Teachers.ID = Subjects.TeacherID 
WHERE Subjects.Name LIKE '%22%';
