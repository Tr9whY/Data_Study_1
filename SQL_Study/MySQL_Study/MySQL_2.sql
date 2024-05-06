DROP DATABASE IF EXISTS pokemon;        # 만약 데이터베이스에 pokemon이 존재한다면 drop 한다는 의미
CREATE DATABASE pokemon;		# 데이터베이스 pokemon 생성

USE pokemon;				# use 데이터 베이스
CREATE TABLE mypokemon(
		number		int,	# integer
        name		varchar(20),	# 가변 길이의 문자열 20byte까지 넣을 수 있다는 의미.
        type		varchar(20)
);					# mypokemon table 생성

SELECT * FROM mypokemon;		# 생성한 테이블 mypokemon 조회

INSERT INTO mypokemon(number,name,type)		#테이블 뒤에 컬럼 맞춰서 할 것.
VALUES (10,'caterpie','bug'),
       (25,'pikachu','electric'),
       (133,'eevee','normal');
       
SELECT * FROM mypokemon;

CREATE TABLE mynewpokemon(
		number		int,
        name		varchar(20),
        type		varchar(20)
);

INSERT INTO mynewpokemon(number,name,type)
VALUES (77,'포니타','불꽃'),
       (132,'메타몽','노말'),
       (151,'뮤','에스퍼');
       
SELECT * FROM mynewpokemon;

ALTER TABLE mypokemon		#alter : 바꾸다 라는 뜻을 가지고 있음.
RENAME myoldpokemon;		# table name 변경

SELECT * FROM myoldpokemon;

alter table myoldpokemon
change column name eng_nm varchar(20);		# 컬럼 변경( 뒤에 타입 반드시 적을것.)

ALTER TABLE mynewpokemon
CHANGE COLUMN name kor_nm varchar(20);

SELECT * FROM mynewpokemon;

truncate table myoldpokemon;			# truncate는 테이블의 값을 삭제
SELECT * FROM myoldpokemon;

drop table mynewpokemon;			# drop은 그냥 table을 삭제.
