## 09 - SQL Challenge
**Note:** 07 is "Team Project 1" forked as a separate repository,  hosted by teammate StephenCYang. Section 08 covered GitHub mechanics utilized during Project 1.

### Employee Database: Historical Investigation

Historical data modeling/analysis research project on employees from the 1980s and 1990s using 6 remaining .csv files. Design PostgreSQL tables in PGAdmin4 to hold and review .csv data.

1. Sketch an Entity Relationship Digram (ERD) using http://www.quickdatabasediagrams.com. 

2. Create a table schema for each of the 6 files, specifying data tyes, primary keys, foreign keys, and other constraints. Import each file into their respective table. [tables.sql]

3. After the database is created, write SQL queries [queries.sql] answering the following:

    * For all employees in the database: Employee number, last name, first name, gender, and salary 

    * Employees hired in 1986.

    * For all Department Managers in the database: department number, department name, the manager's employee number, last name, first name, and start and term dates.

    * For each employee, by Department: employee number, last name, first name, and department name.

    * All employees whose first name is "Hercules" and last names begin with "B."

    * For all Sales Department employees: employee number, last name, first name, and department name.

    * For all Sales and Development employees: employee number, last name, first name, and department name.

    * In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.