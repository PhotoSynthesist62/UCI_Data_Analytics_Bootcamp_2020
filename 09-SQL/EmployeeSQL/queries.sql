--Once you have a complete database, do the following:
--List the following details of each employee: employee number, last name, first name, gender, and salary.
SELECT employees.emp_no, employees.last_name, employees.first_name, employees.sex, salaries.salary
FROM employees
RIGHT JOIN salaries ON employees.emp_no = salaries.emp_no

--List employees who were hired in 1986.
SELECT * FROM employees WHERE hire_date	BETWEEN '1965-01-01' AND '1965-12-31';

--List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name, and start and end employment dates.
SELECT dept_manager.dept_no, departments.dept_name, dept_manager.emp_no, employees.last_name, employees.first_name, employees.hire_date
FROM departments
INNER JOIN dept_manager ON dept_manager.dept_no = departments.dept_no
INNER JOIN employees ON dept_manager.emp_no = employees.emp_no;


--List the department of each employee with the following information: employee number, last name, first name, and department name.
SELECT dept_emp.emp_no, employees.last_name, employees.first_name, departments.dept_name
FROM departments
RIGHT JOIN dept_emp ON dept_emp.dept_no = departments.dept_no
RIGHT JOIN employees ON dept_emp.emp_no = employees.emp_no;

--List all employees whose first name is "Hercules" and last names begin with "B."
SELECT * FROM employees WHERE first_name = 'Hercules' INTERSECT 
SELECT * FROM employees WHERE last_name LIKE 'B%'

--List all employees in the Sales department, including their employee number, last name, first name, and department name.
SELECT dept_emp.emp_no, employees.last_name, employees.first_name, departments.dept_name
FROM departments
RIGHT JOIN dept_emp ON dept_emp.dept_no = departments.dept_no
RIGHT JOIN employees ON dept_emp.emp_no = employees.emp_no
WHERE departments.dept_name = 'Sales';

--List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
SELECT dept_emp.emp_no, employees.last_name, employees.first_name, departments.dept_name
FROM departments
RIGHT JOIN dept_emp ON dept_emp.dept_no = departments.dept_no
RIGHT JOIN employees ON dept_emp.emp_no = employees.emp_no
WHERE departments.dept_name = 'Sales' OR  departments.dept_name = 'Development';

--In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
SELECT last_name, COUNT(last_name) AS "No_With_Last_Name"
FROM employees
GROUP BY last_name
ORDER BY "No_With_Last_Name" DESC;
