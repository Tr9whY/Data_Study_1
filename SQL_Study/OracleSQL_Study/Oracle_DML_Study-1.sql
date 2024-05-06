CREATE TABLE employees (
                         employee_id NUMBER,
                         first_name VARCHAR2(50),
                         last_name VARCHAR2(50),
                         salary NUMBER );

INSERT INTO employees VALUES (1, 'John', 'Doe', 5000);
INSERT INTO employees VALUES (2, 'Jane', 'Smith', 6000 );
INSERT INTO employees VALUES (3, 'Michael', 'Johnson', 7500 );
INSERT INTO employees VALUES (4, 'Michael', 'Johnson', 103 );

SELECT * FROM employees;
SELECT first_name, last_name, salary*12 as annual_salary FROM employees;

SELECT Distinct first_name FROM employees;

SELECT Distinct first_name, last_name FROM employees;


create table pokemon(
    pm_id int primary key not null,
    name varchar(20) not null,
    attr varchar(20) DEFAULT'normal'
);

insert into pokemon values(1,'Bulbasaur','grass');
insert into pokemon values(2,'lvysaur','grass');
insert into pokemon values(3,'Venusaur','grass');
insert into pokemon values(4,'Charmander','Fire');
insert into pokemon values(5,'charmeleon','Fire');
insert into pokemon values(25,'Pikachu','Electric');

SELECT pm_id as 번호, name as 이름, attr as 속성 FROM pokemon;
SELECT * FROM pokemon;
SELECT DISTINCT attr FROM pokemon;
-- ----------------------------- ----------------------------- ----------------------------- -----------------------------

SELECT 10+5 as addition, 15-7 as subtraction,6*3 as multiplication, 20/4 as division, mod(17,5) as modulo FROM DUAL;


CREATE TABLE pokemon (
pm_id INT PRIMARY KEY NOT NULL,
name VARCHAR(20) NOT NULL,
attr VARCHAR(20) DEFAULT 'normal',
weight INT
);
INSERT INTO pokemon VALUES (1, 'Bulbasaur', 'grass', 30);
INSERT INTO pokemon VALUES (2, 'Ivysaur', 'grass', 50);
INSERT INTO pokemon VALUES (3, 'Venusaur', 'grass', 150);
INSERT INTO pokemon VALUES (4, 'Charmander', 'Fire', 80);
INSERT INTO pokemon VALUES (5, 'Charmeleon', 'Fire', 200);
INSERT INTO pokemon VALUES (25, 'Pikachu', 'Electric', 15);

/*
pockemon 테이블에서 Pikachu의 몸무게는 현재 kg 단위로 저장이 되어 있음.
SELECT를 이용하여 kg 기준이 아닌 파운드 단위(lbs) 기준으로 변환된 값을조회해보세요. (1kg = 2.2 lbs)
*/

SELECT concat(weight*2.2, ' Ibs') as pound FROM pokemon;

SELECT player_name||'선수' from pokemon;
SELECT * FROM pokemon;

CREATE TABLE pokemon (
pm_id NUMBER PRIMARY KEY NOT NULL,
name VARCHAR2(20) NOT NULL,
attr VARCHAR2(20) DEFAULT 'normal',
height NUMBER
);
INSERT INTO pokemon VALUES (1, 'Bulbasaur', 'grass', 50);
INSERT INTO pokemon VALUES (2, 'Ivysaur', 'grass', 90);
INSERT INTO pokemon VALUES (3, 'Venusaur', 'grass', 250);
INSERT INTO pokemon VALUES (4, 'Charmander', 'Fire', 80);
INSERT INTO pokemon VALUES (5, 'Charmeleon', 'Fire', 120);
INSERT INTO pokemon VALUES (25, 'Pikachu', 'Electric', 55);

SELECT
'포켓몬번호: ' || pm_id 번호,
'이름: ' || name 이름,
'속성: ' || attr 속성,
'키: ' || height 키
FROM pokemon;

SELECT LOWER('SQL Expert') FROM DUAL;

SELECT UPPER('SQL Expert') FROM DUAL;

SELECT CONCAT('RDBMS', ' SQL') FROM DUAL;

SELECT CONCAT(UPPER('sqld'),lower('completed!')) FROM DUAL;

SELECT ASCII('A') FROM DUAL;

SELECT ASCII('S')+ASCII('Q')+ASCII('L')+ASCII('D') FROM DUAL;

SELECT
CHR(70) ||
CHR(105) ||
CHR(71) ||
CHR(104) ||
CHR(84) ||
CHR(105) ||
CHR(78) ||
CHR(103) ||
'!'
FROM DUAL;

SELECT SUBSTR('SQL Expert',5,3) from dual;

SELECT substr('SQL is a standard language for accessing and manipulating databases.',19,8) FROM DUAL;
SELECT substr('SQL is a standard language for accessing and manipulating databases.',19) FROM DUAL;

SELECT LENGTH('SQL Expert') FROM DUAL;

SELECT LENGTH('SQL is a standard language for accessing and manipulating databases.') as len_1 FROM DUAL;

-- -----------------------------------------------------------------------------
-- 양쪽 제거
SELECT TRIM('x' FROM 'xxYYZZxYZxx') FROM DUAL;

-- 왼쪽 제거
SELECT LTRIM('xxxYYZZxYZ', 'x') FROM DUAL;

-- 오른쪽 제거
SELECT RTRIM('XXYYzzXYzz', 'z') FROM DUAL;

SELECT TRIM('-' FROM '----SQL Tutorial----') FROM DUAL;

-- 'ABC' 에서 전체를 8개의 자리로 만든 후, 'Z'를 왼쪽에 대줘.
SELECT LPAD('ABC',8,'Z') FROM DUAL;

SELECT LPAD('TY',10,'P') FROM DUAL;

-- 'ABC' 에서 전체를 8개의 자리로 만든 후, 오른쪽 공백
SELECT RPAD('ABC',8) FROM DUAL;

/*
다음 문자열을 8자리만큼만 늘리고, 오른쪽 빈 공간을 15로 채워서 리턴
'SQL' 사용
*/
SELECT RPAD('SQL',8,15) FROM DUAL;

/*
숫자의 부호를 판단하는 함수.
숫자가 양수이면 1을 리턴, 0이면 0을 리턴, 음수면 -1을 리턴
숫자가 양수인지, 음수인지, 0인지를 구별하는 함수.
*/

SELECT SIGN(20) FROM DUAL;
SELECT SIGN(0) FROM DUAL;
SELECT SIGN(-10) FROM DUAL;

-- 7을 3으로 나눈 나머지.
SELECT MOD(7,3) FROM DUAL;

SELECT CEIL(28.567) FROM DUAL;
SELECT CEIL(-28.567) FROM DUAL;
SELECT FLOOR(38.567) FROM DUAL;
SELECT FLOOR(-38.567) FROM DUAL;

SELECT ROUND(38.567,2) FROM DUAL;
SELECT TRUNC(38.567,2) FROM DUAL;

-- sin, cos, tan
SELECT SIN(1.5708) FROM DUAL;
SELECT cos(1.5708) FROM DUAL;
SELECT tan(-1.5708) FROM DUAL;

-- e(=2.718)의 n제곱을 반환
SELECT EXP(2) FROM DUAL;
SELECT EXP(5) FROM DUAL;

-- POWER(m,n) : m의 n제곱을 반환합니다.
SELECT POWER(2,3) FROM DUAL;

-- 4의 제곱근 sqrt(n) : n은 음수가 될 수 없음.
SELECT SQRT(4) FROM DUAL;

-- LOG(m,n) : 밑을 m으로 한 n의 로그 값을 반환.
SELECT LOG(10,100) FROM DUAL;

-- LN(n):n의 자연 로그 값을 반환.
SELECT LN(10) FROM DUAL;

-------------------------------------------------
SELECT SYSDATE FROM DUAL;

SELECT EXTRACT(YEAR FROM DATE '2023-10-10')
FROM DUAL;

SELECT TO_CHAR(SYSDATE,'YYYY. MON,DAY') FROM DUAL;

SELECT TO_NUMBER('888') + TO_NUMBER('111') FROM DUAL;

-- 데이터가 스스로 타입을 변경하여 계산...성능 저하 일어날 수 있음..
SELECT '2' + 1 FROM DUAL;
SELECT '4' * 2 FROM DUAL;


