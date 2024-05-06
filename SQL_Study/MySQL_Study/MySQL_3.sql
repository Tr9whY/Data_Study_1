# 조건에 맞는 데이터 가져오기
# 조건 : where
SELECT 1 = 1;
SELECT 1 = 0;

SHOW DATABASES;
USE pokemon;

SELECT * FROM mypokemon;

# 요청 : pikachu의 number 찾아줘.
SELECT number
FROM mypokemon
WHERE name = 'pikachu';

# 요청 : 속도가 50보다 큰 포켓몬 이름 찾아줘
SELECT name
FROM mypokemon
WHERE speed > 50;

# 요청 : 전기타입이 아닌, 포켓몬 이름 찾아줘.
SELECT name
FROM mypokemon
WHERE type != 'electric';

SELECT name
FROM mypokemon
WHERE not(type = 'electric');

# 요청 : 속도가 100이하인 전기 타입 포켓몬 이름을 찾아줘.
SELECT name
FROM mypokemon
WHERE speed <= 100 AND type = 'electric';

# 요청 : 벌레 타입 이거나 노말타입 인 , 포켓몬의 이름 찾아줘.
SELECT name
FROM mypokemon
WHERE type = 'bug' or type ='normal';

# 요청 : 속도가 100 이하이고 벌레 타입이 아닌, 포켓몬 이름
SELECT name
FROM mypokemon
WHERE speed <= 100 AND type !='bug';

# 속도가 50과 100 사이인, 포켓몬 이름
SELECT name
FROM mypokemon
WHERE speed BETWEEN 50 AND 100;

# 요청 : 벌레타입 이거나 노말 타입인 포켓몬의 이름
SELECT name
FROM mypokemon
WHERE type in('bug','normal');  # or 연산자

# 요청 : 이름이 'chu'로 끝나는, 포켓몬 이름을 찾아주세요.
SELECT name
FROM mypokemon
WHERE name like '%chu';

# 요청 : 이름에 'a'가 포함된, 포켓몬 이름을 찾아주세요.
SELECT name
FROM mypokemon
WHERE name like '%a%';

# 요청 : 이름이 'c'로 시작되는, 포켓몬 이름을 찾아주세요.
SELECT name
FROM mypokemon
WHERE name like 'c%';

# null 데이터 다루기
# null 값이 지정되지 않음 >> 미정

SELECT * FROM mypokemon;

INSERT INTO mypokemon(name,type)
VALUES ('kkobuki','');

# 요청 : number가 null인 포켓몬의 이름을 찾아주세요.
SELECT name
FROM mypokemon
WHERE number is null;

# 요청 : type가 null이 아닌 포켓몬의 이름을 찾아주세요.
SELECT name
FROM mypokemon
WHERE type is not null;

SELECT *
FROM mypokemon;
# 공백도 문자니까 null이 아닌걸로 나옴
