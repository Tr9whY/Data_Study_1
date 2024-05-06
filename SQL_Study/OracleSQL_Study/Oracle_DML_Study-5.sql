CREATE TABLE employees (
employee_id NUMBER PRIMARY KEY,
last_name VARCHAR2(50),
department_id NUMBER
);
-- Departments 테이블 생성
CREATE TABLE departments (
department_id NUMBER PRIMARY KEY,
department_name VARCHAR2(50)
);
-- Employees 데이터 삽입
INSERT INTO employees (employee_id, last_name, department_id) VALUES (1, 'Smith', 10);
INSERT INTO employees (employee_id, last_name, department_id) VALUES (2, 'Johnson', 20);
INSERT INTO employees (employee_id, last_name, department_id) VALUES (3, 'Williams', 10);
INSERT INTO employees (employee_id, last_name, department_id) VALUES (4, 'Jones', 30);
INSERT INTO employees (employee_id, last_name, department_id) VALUES (5, 'Brown', 30);
-- Departments 데이터 삽입
INSERT INTO departments (department_id, department_name) VALUES (10, 'Accounting');
INSERT INTO departments (department_id, department_name) VALUES (20, 'Marketing');
INSERT INTO departments (department_id, department_name) VALUES (30, 'Engineering');
-- 쿼리 실행
SELECT * FROM employees;
SELECT * FROM departments;

SELECT * FROM employees;
SELECT * FROM departments;

-- equi join query

select 사원.employee_id, 사원.last_name, 사원.department_id, 부서.department_name
from employees 사원, departments 부서
where 사원.department_id = 부서.department_id;

-- -----------------------------------------------------------------------------------
CREATE TABLE nation (
nation_id NUMBER PRIMARY KEY,
country_name VARCHAR2(100),
population NUMBER
);
CREATE TABLE participant (
participant_id NUMBER PRIMARY KEY,
first_name VARCHAR2(100),
gender CHAR(1), -- 'M' for Male, 'F' for Female
nation_id NUMBER,
CONSTRAINT fk_nation
FOREIGN KEY (nation_id)
REFERENCES nation (nation_id)
);
-- 데이터 생성
INSERT INTO nation (nation_id, country_name, population) VALUES (1, 'USA', 330000000);
INSERT INTO nation (nation_id, country_name, population) VALUES (2, 'Canada', 38000000);
INSERT INTO nation (nation_id, country_name, population) VALUES (3, 'South Korea', 51200000);
INSERT INTO participant (participant_id, first_name, gender, nation_id) VALUES (1, 'John', 'M', 1);
INSERT INTO participant (participant_id, first_name, gender, nation_id) VALUES (2, 'Emma', 'F', 1);
INSERT INTO participant (participant_id, first_name, gender, nation_id) VALUES (3, 'Chris', 'M', 2);
INSERT INTO participant (participant_id, first_name, gender, nation_id) VALUES (4, 'Olivia', 'F', 3);

select p.first_name , p.gender, n.country_name, n.population
from participant p, nation n
where p.nation_id = n.nation_id;

select * from participant;

-- -------------------------------------------------------------------------
CREATE TABLE employees (
employee_id NUMBER PRIMARY KEY,
last_name VARCHAR2(50),
department_id NUMBER
);
-- Departments 테이블 생성
CREATE TABLE departments (
department_id NUMBER PRIMARY KEY,
department_name VARCHAR2(50)
);
-- Employees 데이터 삽입
INSERT INTO employees (employee_id, last_name, department_id) VALUES (1, 'Smith', 10);
INSERT INTO employees (employee_id, last_name, department_id) VALUES (2, 'Johnson', 20);
INSERT INTO employees (employee_id, last_name, department_id) VALUES (3, 'Williams', 10);
INSERT INTO employees (employee_id, last_name, department_id) VALUES (4, 'Jones', 30);
INSERT INTO employees (employee_id, last_name, department_id) VALUES (5, 'Brown', 30);
-- Departments 데이터 삽입
INSERT INTO departments (department_id, department_name) VALUES (10, 'Accounting');
INSERT INTO departments (department_id, department_name) VALUES (20, 'Marketing');
INSERT INTO departments (department_id, department_name) VALUES (30, 'Engineering');

select * from employees;
select * from departments;

select e.last_name, e.employee_id, d.department_name
from employees e, departments d
where e.department_id = d.department_id
order by e. last_name;

-- 여성 참가자들의 이름과 국적 및 인구 수를 이름 내림차순으로 조회하는 SQL문을 작성해 보세요.

CREATE TABLE nation (
nation_id NUMBER PRIMARY KEY,
country_name VARCHAR2(100),
population NUMBER
);
CREATE TABLE participant (
participant_id NUMBER PRIMARY KEY,
first_name VARCHAR2(100),
gender CHAR(1), -- 'M' for Male, 'F' for Female
nation_id NUMBER,
CONSTRAINT fk_nation
FOREIGN KEY (nation_id)
REFERENCES nation (nation_id)
);
-- 데이터 삽입
INSERT INTO nation (nation_id, country_name, population) VALUES (1, 'USA', 330000000);
INSERT INTO nation (nation_id, country_name, population) VALUES (2, 'Canada', 38000000);
INSERT INTO nation (nation_id, country_name, population) VALUES (3, 'South Korea', 51200000);
INSERT INTO participant (participant_id, first_name, gender, nation_id) VALUES (1, 'John', 'M', 1);
INSERT INTO participant (participant_id, first_name, gender, nation_id) VALUES (2, 'Emma', 'F', 1);
INSERT INTO participant (participant_id, first_name, gender, nation_id) VALUES (3, 'Chris', 'M', 2);
INSERT INTO participant (participant_id, first_name, gender, nation_id) VALUES (4, 'Olivia', 'F', 3);
INSERT INTO participant (participant_id, first_name, gender, nation_id) VALUES (5, 'Sophia', 'F', 2);
INSERT INTO participant (participant_id, first_name, gender, nation_id) VALUES (6, 'Isabella', 'F', 1);


-- 여성 참가자들의 이름과 국적 및 인구 수를 이름 내림차순으로 조회하는 SQL문을 작성해 보세요.

select * from nation;
select * from participant;

select 
    n.country_name, p.first_name, n.population
from 
    nation n, participant p
where n.nation_id = p.nation_id and p.gender = 'F'
order by p.first_name DESC;

-- ------------------------------------------------------------------------
CREATE TABLE nation (
    nation_id NUMBER PRIMARY KEY,
    country_name VARCHAR2(100)
);
CREATE TABLE sport (
    sport_id NUMBER PRIMARY KEY,
    sport_name VARCHAR2(100)
);
CREATE TABLE participant (
    participant_id NUMBER PRIMARY KEY,
    first_name VARCHAR2(100),
    nation_id NUMBER,
    main_sport_id NUMBER,
    CONSTRAINT fk_nation
        FOREIGN KEY (nation_id)
        REFERENCES nation (nation_id),
    CONSTRAINT fk_sport
        FOREIGN KEY (main_sport_id)
        REFERENCES sport (sport_id)
);
-- 데이터 생성
INSERT INTO nation (nation_id, country_name) VALUES (1, 'USA');
INSERT INTO nation (nation_id, country_name) VALUES (2, 'Canada');
INSERT INTO nation (nation_id, country_name) VALUES (3, 'South Korea');
INSERT INTO sport (sport_id, sport_name) VALUES (1, 'Basketball');
INSERT INTO sport (sport_id, sport_name) VALUES (2, 'Hockey');
INSERT INTO sport (sport_id, sport_name) VALUES (3, 'Archery');
INSERT INTO participant (participant_id, first_name, nation_id, main_sport_id) VALUES (1, 'John', 1, 1);
INSERT INTO participant (participant_id, first_name, nation_id, main_sport_id) VALUES (2, 'Emma', 1, 3);
INSERT INTO participant (participant_id, first_name, nation_id, main_sport_id) VALUES (3, 'Chris', 2, 2);
INSERT INTO participant (participant_id, first_name, nation_id, main_sport_id) VALUES (4, 'Olivia', 3, 3);
INSERT INTO participant (participant_id, first_name, nation_id, main_sport_id) VALUES (5, 'Sophia', 2, 1);
INSERT INTO participant (participant_id, first_name, nation_id, main_sport_id) VALUES (6, 'Liam', 3, 2);


select * from participant;
select * from participant, sport, nation;

select
    p.first_name, n.country_name, s.sport_name
from participant p, nation n, sport s
where (p.nation_id = n.nation_id) and (p.main_sport_id = s.sport_id)
order by s.sport_name;

-- --------------------------------------------------------
CREATE TABLE VolunteerActivity (
    activity_id NUMBER PRIMARY KEY,
    juice_type VARCHAR2(20),
    quantity_sold NUMBER
);
INSERT INTO VolunteerActivity VALUES (1, 'Orange Juice', 100);
INSERT INTO VolunteerActivity VALUES (2, 'Apple Juice', 80);
INSERT INTO VolunteerActivity VALUES (3, 'Grape Juice', 640);
INSERT INTO VolunteerActivity VALUES (4, 'Pineapple Juice', 300);
INSERT INTO VolunteerActivity VALUES (5, 'Lemonade Juice', 110);
CREATE TABLE Unit (
    unit_id NUMBER PRIMARY KEY,
    unit_name VARCHAR2(20),
    activity_id NUMBER,
    FOREIGN KEY (activity_id) REFERENCES VolunteerActivity(activity_id)
);
INSERT INTO Unit VALUES (101, 'Alpha Unit', 1);
INSERT INTO Unit VALUES (102, 'Bravo Unit', 2);
INSERT INTO Unit VALUES (103, 'Charlie Unit', 3);
INSERT INTO Unit VALUES (104, 'Delta Unit', 4);
INSERT INTO Unit VALUES (105, 'Echo Unit', 5);
CREATE TABLE Soldier (
    soldier_id NUMBER PRIMARY KEY,
    first_name VARCHAR2(20),
    last_name VARCHAR2(20),
    rank VARCHAR2(20),
    unit_id NUMBER,
    activity_id NUMBER,
    FOREIGN KEY (unit_id) REFERENCES Unit(unit_id),
    FOREIGN KEY (activity_id) REFERENCES VolunteerActivity(activity_id)
);
INSERT INTO Soldier VALUES (3028, 'John', 'Doe', 'Sergeant', 101, 1);
INSERT INTO Soldier VALUES (2734, 'Jane', 'Smith', 'Private', 102, 2);
INSERT INTO Soldier VALUES (3103, 'Michael', 'Johnson', 'Private', 103, 3);
INSERT INTO Soldier VALUES (4865, 'Emily', 'Davis', 'Private', 104, 4);
INSERT INTO Soldier VALUES (5371, 'Chris', 'Brown', 'Sergeant', 105, 5);

select * from Soldier;
select * from Unit;
select * from VolunteerActivity;

# 부대 이름과 봉사활동 시 판매했던 과일명을 출력해 보세요.
SELECT u.unit_name, v.juice_type
FROM unit u JOIN volunteerActivity v
  ON u.activity_id = v.activity_id;
  
# 군인 이름, 부대 이름, 계급을 Soldier, Unit 테이블의 NATURAL JOIN을 이용하여 출력해보세요
select first_name, unit_name, rank
from soldier natural join unit;

# Soldier와 Unit 테이블을 USING절을 이용하여 부대 ID, 군인이름, 부대이름, 계급을 출력해보세요.
SELECT unit_id, s.first_name, u.unit_name
FROM soldier s join unit u
using (unit_id);

# 부대 이름이 Alpha Unit인 군인의 이름과 성(last_name), 계급 그리고 봉사활동 id를 출력해보세요.
select s.first_name, s.last_name, s.rank, u.activity_id
from soldier s 
join Unit u
on s.activity_id = u.activity_id
where u.unit_name = 'Alpha Unit';

# 주스 판매량이 110 이상인 부대의 이름과 판매량을 출력해 보세요.
select u.unit_name, v.quantity_sold
from VolunteerActivity v join unit u
	on (v.activity_id = u.activity_id) and v.quantity_sold >= 110;
# where 사용 권장
select u.unit_name, v.quantity_sold
from VolunteerActivity v join unit u
	on (v.activity_id = u.activity_id)
where v.quantity_sold >= 110;

# 군인의 이름과 부대명을 출력해보세요.
select first_name, unit_name
from soldier s join unit u
on s.unit_id = u.unit_id
order by unit_name;

-- ----------------------------------------------------
-- dept_temp 데이터
CREATE TABLE dept_temp (
deptno NUMBER PRIMARY KEY,
dname VARCHAR2(30),
loc VARCHAR2(30)
);
INSERT INTO dept_temp VALUES (10, 'Administration', 'New York');
INSERT INTO dept_temp VALUES (20, 'Marketing', 'Los Angeles');
INSERT INTO dept_temp VALUES (30, 'Purchasing', 'San Francisco');
INSERT INTO dept_temp VALUES (40, 'Human Resources', 'Chicago');
select * from dept_temp;
-- Departments 테이블 생성
CREATE TABLE departments (
department_id NUMBER PRIMARY KEY,
department_name VARCHAR2(50)
);
INSERT INTO departments (department_id, department_name) VALUES (10, 'Accounting');
INSERT INTO departments (department_id, department_name) VALUES (20, 'Marketing');
INSERT INTO departments (department_id, department_name) VALUES (30, 'Engineering');
select * from departments;
CREATE TABLE employees (
employee_id NUMBER PRIMARY KEY,
last_name VARCHAR2(50),
department_id NUMBER
);
INSERT INTO employees (employee_id, last_name, department_id) VALUES (1, 'Smith', 10);
INSERT INTO employees (employee_id, last_name, department_id) VALUES (2, 'Johnson', 20);
INSERT INTO employees (employee_id, last_name, department_id) VALUES (3, 'Williams', 10);
INSERT INTO employees (employee_id, last_name, department_id) VALUES (4, 'Jones', 30);
INSERT INTO employees (employee_id, last_name, department_id) VALUES (5, 'Brown', 30);

select * from employees;

-- 사원과 dept 테이블의 소속 부서명, dept_temp 테이블의 바뀐 부서명 정보를 출력
SELECT e.employee_id, d.department_id, d.department_name, t.dname AS new_dname
FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN dept_temp t ON e.department_id = t.deptno

-- -----------------------------------------------------------------
CREATE TABLE VolunteerActivity (
    activity_id NUMBER PRIMARY KEY,
    juice_type VARCHAR2(20),
    quantity_sold NUMBER
);
INSERT INTO VolunteerActivity VALUES (1, 'Orange Juice', 100);
INSERT INTO VolunteerActivity VALUES (2, 'Apple Juice', 80);
INSERT INTO VolunteerActivity VALUES (3, 'Grape Juice', 640);
INSERT INTO VolunteerActivity VALUES (4, 'Pineapple Juice', 300);
INSERT INTO VolunteerActivity VALUES (5, 'Lemonade Juice', 110);
CREATE TABLE Unit (
    unit_id NUMBER PRIMARY KEY,
    unit_name VARCHAR2(20),
    activity_id NUMBER,
    FOREIGN KEY (activity_id) REFERENCES VolunteerActivity(activity_id)
);
INSERT INTO Unit VALUES (101, 'Alpha Unit', 1);
INSERT INTO Unit VALUES (102, 'Bravo Unit', 2);
INSERT INTO Unit VALUES (103, 'Charlie Unit', 3);
INSERT INTO Unit VALUES (104, 'Delta Unit', 4);
INSERT INTO Unit VALUES (105, 'Echo Unit', 5);
CREATE TABLE Soldier (
    soldier_id NUMBER PRIMARY KEY,
    first_name VARCHAR2(20),
    last_name VARCHAR2(20),
    rank VARCHAR2(20),
    unit_id NUMBER,
    activity_id NUMBER,
    FOREIGN KEY (unit_id) REFERENCES Unit(unit_id),
    FOREIGN KEY (activity_id) REFERENCES VolunteerActivity(activity_id)
);
INSERT INTO Soldier VALUES (3028, 'John', 'Doe', 'Sergeant', 101, 1);
INSERT INTO Soldier VALUES (2734, 'Jane', 'Smith', 'Private', 102, 2);
INSERT INTO Soldier VALUES (3103, 'Michael', 'Johnson', 'Private', 103, 3);
INSERT INTO Soldier VALUES (4865, 'Emily', 'Davis', 'Private', 104, 4);
INSERT INTO Soldier VALUES (5371, 'Chris', 'Brown', 'Sergeant', 105, 5);

# 주스 판매량이 100에서 600사이인 부대의 이름과 판매량, 주스이름, 해당 부대에 소속된 군인 이름, 계급을 출력해 보세요.
select * from volunteeractivity;
select * from unit;
select * from soldier;

SELECT u.unit_name,v.juice_type,v.quantity_sold,s.first_name, s.rank
FROM volunteeractivity v 
JOIN unit u 
    ON v.activity_id = u.activity_id  
JOIN soldier s 
    ON u.unit_id = s.unit_id
WHERE v.quantity_sold BETWEEN 100 and 600;


# 부대 테이블과 봉사활동 테이블을 CROSS JOIN을 활용하여 부대 이름, 주스 종류, 판매수량을 판매수량 내림차순으로 하여 출력해 보세요.
SELECT unit_name, juice_type, quantity_sold
FROM Unit 
CROSS JOIN VolunteerActivity
ORDER BY quantity_sold DESC;

-- 부서 테이블 DEPT_EX 생성
CREATE TABLE DEPT_EX (
    DEPT_NO VARCHAR(10),
    DEPT_NM VARCHAR(50),
    PRIMARY KEY (DEPT_NO)
);
-- 직원 테이블 EMP_EX 생성
CREATE TABLE EMP_EX (
    EMP_NO VARCHAR(10),
    EMP_NM VARCHAR(50),
    DEPT_NO VARCHAR(10),
    FOREIGN KEY (DEPT_NO) REFERENCES DEPT_EX(DEPT_NO)
);
-- 부서 데이터 입력
INSERT INTO DEPT_EX (DEPT_NO, DEPT_NM) VALUES ('D01', '인사팀');
INSERT INTO DEPT_EX (DEPT_NO, DEPT_NM) VALUES ('D02', '개발팀');
INSERT INTO DEPT_EX (DEPT_NO, DEPT_NM) VALUES ('D03', '영업팀');
-- 직원 데이터 입력
INSERT INTO EMP_EX (EMP_NO, EMP_NM, DEPT_NO) VALUES ('E01', '홍길동', 'D02');
INSERT INTO EMP_EX (EMP_NO, EMP_NM, DEPT_NO) VALUES ('E02', '김철수', 'D01');
INSERT INTO EMP_EX (EMP_NO, EMP_NM, DEPT_NO) VALUES ('E03', '이영희', 'D02');
-- 개발팀에 속하지 않는 직원 추가
INSERT INTO EMP_EX (EMP_NO, EMP_NM, DEPT_NO) VALUES ('E04', '박보검', 'D03');


select * from EMP_EX, DEPT_EX;

select
    a.dept_no, a.dept_nm
    ,nvl(b.emp_no, 'null') as emp_no
    ,nvl(b.emp_nm, 'null') as emp_nm
from dept_ex a left outer join emp_ex b
  on (a.dept_no = b.dept_no) and (a.dept_nm = '개발팀')
where a.dept_no is not null;



CREATE TABLE Unit (
unit_id INT,
unit_name VARCHAR(50),
PRIMARY KEY (unit_id)
);
-- 병사 테이블 Soldier 생성
CREATE TABLE Soldier (
soldier_id INT,
first_name VARCHAR(50),
unit_id INT,
FOREIGN KEY (unit_id) REFERENCES Unit(unit_id)
);
-- 부대 데이터 입력
INSERT INTO Unit (unit_id, unit_name) VALUES (1, 'Alpha');
INSERT INTO Unit (unit_id, unit_name) VALUES (2, 'Bravo');
INSERT INTO Unit (unit_id, unit_name) VALUES (3, 'Charlie');
-- 병사 데이터 입력
INSERT INTO Soldier (soldier_id, first_name, unit_id) VALUES (101, 'John', 1);
INSERT INTO Soldier (soldier_id, first_name, unit_id) VALUES (102, 'Mike', 1);
INSERT INTO Soldier (soldier_id, first_name, unit_id) VALUES (103, 'Alex', 2);
-- 부대에 소속되지 않은 병사 추가
INSERT INTO Soldier (soldier_id, first_name, unit_id) VALUES (104, 'Liam', NULL);


/*부대를 기준으로 해당 부대에 속하는 군인의 정보를 나타내보세요.
해당 부대에 속한 군인이 없다면 빈 값으로 나타내세요*/

select * from unit, soldier;

select u.unit_id, u.unit_name, s.first_name
from unit u
left outer join soldier s
on (u.unit_id = s.unit_id)
order by 1;

CREATE TABLE Unit (
unit_id INT,
unit_name VARCHAR(50),
PRIMARY KEY (unit_id)
);
-- 병사 테이블 Soldier 생성
CREATE TABLE Soldier (
soldier_id INT,
first_name VARCHAR(50),
unit_id INT,
FOREIGN KEY (unit_id) REFERENCES Unit(unit_id)
);
-- 부대 데이터 입력
INSERT INTO Unit (unit_id, unit_name) VALUES (1, 'Alpha');
INSERT INTO Unit (unit_id, unit_name) VALUES (2, 'Bravo');
INSERT INTO Unit (unit_id, unit_name) VALUES (3, 'Charlie');
-- 병사 데이터 입력
INSERT INTO Soldier (soldier_id, first_name, unit_id) VALUES (101, 'John', 1);
INSERT INTO Soldier (soldier_id, first_name, unit_id) VALUES (102, 'Mike', 1);
INSERT INTO Soldier (soldier_id, first_name, unit_id) VALUES (103, 'Alex', 2);
-- 부대에 소속되지 않은 병사 추가
INSERT INTO Soldier (soldier_id, first_name, unit_id) VALUES (104, 'Liam', NULL);

-- 각 군인들은 어떤 부대에 속해있는지 RIGHT JOIN을 활용하여 나타내보세요.

SELECT s.first_name, u.unit_name
FROM unit u
RIGHT JOIN soldier s
ON (u.unit_id = s.unit_id)
order by u.unit_name;

-- -------------------------------------------------------------

-- 부서 테이블 dept 생성
CREATE TABLE dept_origin (
    deptno INT,
    dname VARCHAR(50),
    PRIMARY KEY (deptno)
);
-- 임시 부서 테이블 dept_temp 생성
CREATE TABLE dept_temp (
    deptno INT,
    dname VARCHAR(50),
    PRIMARY KEY (deptno)
);
-- 부서 테이블 dept에 데이터 입력
INSERT INTO dept_origin (deptno, dname) VALUES (10, 'Accounting');
INSERT INTO dept_origin (deptno, dname) VALUES (20, 'Research');
INSERT INTO dept_origin (deptno, dname) VALUES (30, 'Sales');
-- 임시 부서 테이블 dept_temp에 데이터 입력
INSERT INTO dept_temp (deptno, dname) VALUES (20, 'Research');
INSERT INTO dept_temp (deptno, dname) VALUES (30, 'Sales');
INSERT INTO dept_temp (deptno, dname) VALUES (40, 'Operations');

-- 부서가 하나의 테이블에만 존재하는 경우 포함
SELECT *
FROM dept_origin 
FULL OUTER JOIN dept_temp
ON dept_origin.deptno = dept_temp.deptno;

