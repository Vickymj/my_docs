---
id: sql_basic_CRUD
title: SQL - Basic CRUD
---

### Some of The Most Important SQL Commands

- `SELECT` - extracts data from a database
- `UPDATE` - updates data in a database
- `DELETE` - deletes data from a database
- `INSERT INTO` - inserts new data into a database
- `CREATE DATABASE` - creates a new database
- `ALTER DATABASE` - modifies a database
- `CREATE TABLE` - creates a new table
- `ALTER TABLE` - modifies a table
- `DROP TABLE` - deletes a table
- `CREATE INDEX` - creates an index (search key)
- `DROP INDEX` - deletes an index


### SELECT Syntax
```sql
SELECT column1, column2, ...
FROM table_name;
```

### DISTINCT Statement
The `SELECT DISTINCT` statement is used to return only distinct (unique) values
```sql

SELECT DISTINCT column1, column2, ...
FROM table_name;
```

### SQL WHERE Clause
The `WHERE` clause is used to filter records
```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```
The following operators can be used in the WHERE clause:
| Operator     | Description              | Example                                           |
| ------------ | ------------------------ | ------------------------------------------------- |
| `=`          | Equal to                 | `SELECT * FROM users WHERE age = 25;`             |
| `>`          | Greater than             | `SELECT * FROM users WHERE age > 18;`             |
| `<`          | Less than                | `SELECT * FROM users WHERE age < 60;`             |
| `>=`         | Greater than or equal to | `SELECT * FROM users WHERE salary >= 50000;`      |
| `<=`         | Less than or equal to    | `SELECT * FROM users WHERE salary <= 100000;`     |
| `<>` or `!=` | Not equal to             | `SELECT * FROM users WHERE status <> 'inactive';` |
| BETWEEN      |Between a certain range   |`SELECT * FROM users WHERE name LIKE 'A%';`        |
| LIKE         |Search for a pattern      |`WHERE status IN ('pending','shipped','delivered')`|
| IN           |multiple possible values  |`WHERE department IN ('HR', 'IT')`                 |

### SQL Wildcards
A wildcard character is used to substitute one or more characters in a string.

Wildcard characters are used with the LIKE operator. The LIKE operator is used in a WHERE clause to search for a specified pattern in a column.

SQL Wildcards (Real Examples)

| Wildcard | Description                      | Example Query                                      |
|----------|----------------------------------|---------------------------------------------------|
| `%`      | Zero or more characters          | `SELECT * FROM users WHERE name LIKE 'Jo%';`      |
| `_`      | Exactly one character            | `SELECT * FROM users WHERE name LIKE 'J_n';`      |




### SQL ORDER BY
```sql
SELECT column1, column2, ...
FROM table_name
ORDER BY column1, column2, ... ASC|DESC;
```

### SQL AND Operator
The `AND` operator is used to filter records based on more than one condition.
:::info
The `AND` operator displays a record if all the conditions are TRUE.
:::
```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition1 AND condition2 AND condition3 ...;
```
### SQL OR Operator
- The `WHERE` clause can contain one or more `OR` operators.

- The `OR` operator is used to filter records based on more than one condition.
```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition1 OR condition2 OR condition3 ...;
```

### SQL NOT Operator
The `NOT` operator is used in the `WHERE` clause to return all records that DO NOT match the specified criteria

```sql
SELECT column1, column2, ...
FROM table_name
WHERE NOT condition;
```
Example: 
```Sql
SELECT * FROM Customers
WHERE NOT Country = 'Spain';
```
### combine AND OR NOT
```sql
SELECT * FROM Customers
WHERE Country = 'Spain' AND (CustomerName LIKE 'G%' OR CustomerName LIKE 'R%') NOT STATUS=0
```

### SQL INSERT INTO Statement
The `INSERT INTO` statement is used to insert new records in a table.
```sql
--Syntax 1:
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
--Syntax 2:
INSERT INTO table_name
VALUES (value1, value2, value3, ...);
```

### SQL NULL Values
If a field in a table is optional, it is possible to insert or update a record without adding any value to this field. This way, the field will be saved with a NULL value.
:::info
A NULL value is different from zero (0) or an empty string (''). A field with a NULL value is one that has been left blank upon record creation.
:::
#### How to Test for NULL Values?
IS NULL Syntax
```sql
SELECT column_names
FROM table_name
WHERE column_name IS NULL;
```
IS NOT NULL Syntax
```sql
SELECT column_names
FROM table_name
WHERE column_name IS NOT NULL;
```

### SQL UPDATE Statement
```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```
### SQL DELETE Statement
The `DELETE` statement is used to delete existing records in a table.
```sql
DELETE FROM table_name WHERE condition;
```

### Delete a Table
```sql
DROP TABLE table_name;
```

### SQL SELECT TOP, LIMIT and FETCH FIRST
Syntax for SQL Server / MS Access
```sql
SELECT TOP number|percent column_name(s)
FROM table_name
WHERE condition;

SELECT TOP 50 PERCENT * FROM Customers;
SELECT * TOP 50 FROM Customers;
```
Syntax for MySQL
```sql
SELECT column_name(s) FROM table_name WHERE condition
LIMIT number;

SELECT * FROM Customers LIMIT 3;
```