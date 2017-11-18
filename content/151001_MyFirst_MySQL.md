Title: MyFIRST MySQL
Date: 2015-10-01 10:20
Modified: 2015-10-01 19:30
Category: blog
Tags: MySQL, data science
Slug: myfirst-mysql
Authors: Peter Frick
Summary: Intro to SQL. I've looked at a couple tutorials on SQL, but the best way to learn is to play around right? Let's get started.

# Description
In this post, my goals are: 
1. Get a SQL database using bash
2. Try some basic SQL commands
I'll be using a public database of population statistics (from [this site](http://moderndata.plot.ly/graph-data-from-mysql-database-in-python/)).

### First, get the data using bash

```bash
sudo mysql -uroot
wget http://downloads.mysql.com/docs/world.sql.zip
unzip world.sql.zip
```

### Now, use mysql scripts to create/load the database 
```sql
mysql> /*This is a comment*/
mysql> CREATE database world;
mysql> USE world;
mysql> SOURCE /home/ubuntu/world.sql;
```

### Toes dipping slowly into the water

So what's in the database? Let's take a look.
```sql
mysql> show tables;
+-----------------+
| Tables_in_world |
+-----------------+
| City            |
| Country         |
| CountryLanguage |
+-----------------+
3 rows in set (0.00 sec)
```

Looks like there are three `tables` within `world`. Let's explore one of the tables, `City`.
```sql
mysql> select * from City limit 10;
+----+----------------+-------------+---------------+------------+
| ID | Name           | CountryCode | District      | Population |
+----+----------------+-------------+---------------+------------+
|  1 | Kabul          | AFG         | Kabol         |    1780000 |
|  2 | Qandahar       | AFG         | Qandahar      |     237500 |
|  3 | Herat          | AFG         | Herat         |     186800 |
|  4 | Mazar-e-Sharif | AFG         | Balkh         |     127800 |
|  5 | Amsterdam      | NLD         | Noord-Holland |     731200 |
|  6 | Rotterdam      | NLD         | Zuid-Holland  |     593321 |
|  7 | Haag           | NLD         | Zuid-Holland  |     440900 |
|  8 | Utrecht        | NLD         | Utrecht       |     234323 |
|  9 | Eindhoven      | NLD         | Noord-Brabant |     201843 |
| 10 | Tilburg        | NLD         | Noord-Brabant |     193238 |
+----+----------------+-------------+---------------+------------+
10 rows in set (0.00 sec)

```

### What are the top ten biggest cities in the dataset?

```sql
mysql> select CountryCode, Name, Population from City
    -> order by population desc
    -> limit 10;
+-------------+-------------------+------------+
| CountryCode | Name              | Population |
+-------------+-------------------+------------+
| IND         | Mumbai (Bombay)   |   10500000 |
| KOR         | Seoul             |    9981619 |
| BRA         | São Paulo         |    9968485 |
| CHN         | Shanghai          |    9696300 |
| IDN         | Jakarta           |    9604900 |
| PAK         | Karachi           |    9269265 |
| TUR         | Istanbul          |    8787958 |
| MEX         | Ciudad de México  |    8591309 |
| RUS         | Moscow            |    8389200 |
| USA         | New York          |    8008278 |
+-------------+-------------------+------------+
10 rows in set (0.01 sec)
```

### How many cities are there in the dataset? How many countries?
```sql
mysql> select count(Name), count(distinct(CountryCode)) from City;
+-------------+------------------------------+
| count(Name) | count(distinct(CountryCode)) |
+-------------+------------------------------+
|        4079 |                          232 |
+-------------+------------------------------+
1 row in set (0.36 sec)
```
Looks like 4079 cities total and 232 countries.

### What countries have the highest total populations?
```sql
mysql> select CountryCode, sum(Population) from City
    -> group by CountryCode
    -> order by sum(Population) desc
    -> limit 10;
+-------------+-----------------+
| CountryCode | sum(Population) |
+-------------+-----------------+
| CHN         |       175953614 |
| IND         |       123298526 |
| BRA         |        85876862 |
| USA         |        78625774 |
| JPN         |        77965107 |
| RUS         |        69150700 |
| MEX         |        59752521 |
| KOR         |        38999893 |
| IDN         |        37485695 |
| PAK         |        31546745 |
+-------------+-----------------+
10 rows in set (0.01 sec)
```
