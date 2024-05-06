-- NVL(NULL_판단_대상,NULL 일 때 대체값)
SELECT NVL(NULL,'NVL-OK') FROM DUAL;

/*다음 데이터에서 NULL이 허용된 칼럼 중 NULL이 존재한다면 문자형 칼럼인 경우
'알 수 없음'을 숫자형 칼럼인 경우는 999를 출력하여 전체 데이터의 칼럼을
조회해보세요.*/

CREATE TABLE pokemon (
pm_id NUMBER PRIMARY KEY NOT NULL,
name VARCHAR2(20) NOT NULL,
attr VARCHAR2(20) DEFAULT 'normal',
weight NUMBER
);

INSERT INTO pokemon VALUES (1, 'Bulbasaur', 'Grass', 30);
INSERT INTO pokemon VALUES (4, 'Charmander', 'Fire', 80);
INSERT INTO pokemon VALUES (25, 'Pikachu', 'Electric', 15);
INSERT INTO pokemon (pm_id, name) VALUES (54, 'Psyduck');
INSERT INTO pokemon (pm_id, name, attr) VALUES (76, 'Golem', 'Rock');
INSERT INTO pokemon (pm_id, name, weight) VALUES (86, 'Seel', 85);

SELECT * FROM pokemon;
-- 전체 데이터 확인(null 값이 유무 확인)

SELECT pm_id, name, NVL(attr, '알 수 없음'), NVL(weight, 999) FROM pokemon;

SELECT name, attr FROM pokemon;
SELECT name, NULLIF(attr, 'normal') FROM pokemon;
-- attr이 'normal'로 일치하면 >> NULL 출력

SELECT name, NULLIF(attr, 'genius') FROM pokemon;
-- attr, 'genius' 두 조건이 일치하지 않으면 >> attr 출력


/*
pm_id 가 30 이상인 포켓몬의 pm_id, name을 조회하는데,
이 때 추가로 attr, weight 중에서 NULL이 아닌 값을 같이 출력해주세요.
만약 attr, weight 둘 다 NULL인 경우 NULL을 그대로 출력해주세요.
*/
CREATE TABLE pokemon (
pm_id NUMBER PRIMARY KEY NOT NULL,
name VARCHAR2(20) NOT NULL,
attr VARCHAR2(20),
weight VARCHAR2(20)
);
INSERT INTO pokemon VALUES (1, 'Bulbasaur', 'Grass', '30');
INSERT INTO pokemon VALUES (4, 'Charmander', 'Fire', '80');
INSERT INTO pokemon VALUES (25, 'Pikachu', 'Electric', '15');
INSERT INTO pokemon (pm_id, name) VALUES (54, 'Psyduck');
INSERT INTO pokemon (pm_id, name, attr) VALUES (76, 'Golem', 'Rock');
INSERT INTO pokemon (pm_id, name, weight) VALUES (86, 'Seel', '85');

SELECT * FROM pokemon;

/*
기타 null 관련 함수(COALESCE)
COALESCE 함수는 여러 값 중에서 NULL이 아닌 첫 번째 값을 찾을 때 사용한다 만약에 모든 값들이
NULL이라면 NULL을 리턴합니다.
COALESCE -> '합치다' 라는 의미.
*/

SELECT pm_id, name, COALESCE(attr,weight)
FROM pokemon
WHERE pm_id >= 30;

DROP TABLE pokemon;

CREATE TABLE pokemon (
pm_id NUMBER PRIMARY KEY NOT NULL,
name VARCHAR2(20) NOT NULL,
attr VARCHAR2(20) DEFAULT 'normal',
weight NUMBER
);
INSERT INTO pokemon VALUES (1, 'Bulbasaur', 'Grass', 30);
INSERT INTO pokemon VALUES (2, 'Ivysaur', 'Grass', 50);
INSERT INTO pokemon VALUES (3, 'Venusaur', 'Grass', 150);
INSERT INTO pokemon VALUES (4, 'Charmander', 'Fire', 80);
INSERT INTO pokemon VALUES (5, 'Charmeleon', 'Fire', 200);
INSERT INTO pokemon VALUES (25, 'Pikachu', 'Electric', 15);

SELECT name,
CASE attr
	WHEN 'Grass' THEN '풀 속성'
	WHEN 'Fire' THEN '불 속성'
	WHEN 'Electric' THEN '전기 속성'
	ELSE '노말 속성'
	END AS 속성
FROM pokemon;

/*
다음 포켓몬의 몸무게로 소형, 중형, 대형 포켓몬으로 구분하여 이름과 함께
조회해보세요. ( 0 ~30 : 소형, 31~100: 중형, 101 ~ : 대형 )
*/

DROP TABLE pokemon;

CREATE TABLE pokemon (
pm_id NUMBER PRIMARY KEY NOT NULL,
name VARCHAR2(20) NOT NULL,
attr VARCHAR2(20) DEFAULT 'normal',
weight NUMBER
);
INSERT INTO pokemon VALUES (1, 'Bulbasaur', 'Grass', 30);
INSERT INTO pokemon VALUES (2, 'Ivysaur', 'Grass', 50);
INSERT INTO pokemon VALUES (3, 'Venusaur', 'Grass', 150);
INSERT INTO pokemon VALUES (4, 'Charmander', 'Fire', 80);
INSERT INTO pokemon VALUES (5, 'Charmeleon', 'Fire', 200);
INSERT INTO pokemon VALUES (25, 'Pikachu', 'Electric', 15);

SELECT * FROM pokemon;
SELECT name,
CASE
	WHEN weight <= 30 THEN '소형'
	WHEN weight <= 100 THEN '중형'
	ELSE '대형'
	END as 몸무게
FROM pokemon;

-- DECODE 는 CASE 다
SELECT name,
DECODE(attr,'Grass','풀속성','Fire','화염속성','Electric','전기속성','노말속성') as decode_property
FROM pokemon;

SELECT CASE 
    	WHEN 1=1 THEN 1 
    	ELSE 0 
    	END AS RESULT 
    	FROM DUAL;

