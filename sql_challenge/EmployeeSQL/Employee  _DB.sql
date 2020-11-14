SELECT e.emp_no, e.last_name, e.first_name,e.hire_date, e.sex, s.salary
From "Salaries" AS s
INNER JOIN "Employees"  AS e ON 
e.emp_no=s.emp_no;

SELECT e.last_name, e.first_name, e.hire_date
FROM "Employees" AS e
WHERE
	hire_date >= '1/1/1986'
	AND hire_date <= '1/1/1987';
	
--List the manager of each department with the following 
--information: department number, department name, the 
--manager's employee number, last name, first name.

SELECT d.dept_no, d.emp_no, b.dept_name, e.last_name, e.first_name
From "Dept_Mgr" AS d 
From "Depts" AS b
From "Employees" AS e
INNER JOIN e ON 
d.emp_no=e.emp_no
INNER JOIN p ON 
d.dept_no=b.dept_no;

SELECT * FROM "Depts";

--List the department of each employee with the following 
--information: employee number, last name, first name, 
--and department name.


SELECT d.emp_no, e.last_name, e.first_name, b.dept_name
FROM "Dept_Employee" AS d
INNER JOIN "Employees" AS e ON 
d.emp_no=e.emp_no
INNER JOIN "Depts" AS b ON 
d.dept_no=b.dept_no;


--List first name, last name, and sex for employees whose 
--first name is "Hercules" and last names 
--begin with "B."

SELECT  e.last_name, e.first_name, e.sex
FROM "Employees" AS e
WHERE
	first_name = 'Hercules'
	AND last_name = 'B%' ;
		
SELECT * FROM "Employees";
	
--List all employees in the Sales department, including their employee number, 
--last name, first name, and department name.

SELECT e.last_name, e.first_name, b.dept_name
FROM "Dept_Employee" AS d
INNER JOIN "Employees" AS e ON 
d.emp_no=e.emp_no
INNER JOIN "Depts" AS b ON 
d.dept_no=b.dept_no
WHERE dept_name = 'Sales';

--List all employees in the Sales and Development departments,
--including their employee number, last name, first name, 
--and department name.
	
SELECT e.last_name, e.first_name, b.dept_name
FROM "Dept_Employee" AS d
INNER JOIN "Employees" AS e ON 
d.emp_no=e.emp_no
INNER JOIN "Depts" AS b ON 
d.dept_no=b.dept_no

WHERE dept_name = 'Sales'
AND dept_name = 'Developement';

--8. In descending order, list the frequency count of 
--employee last names, i.e., how many employees share 
--each last name.

SELECT COUNT(e.last_name)
FROM "Employees" AS e 

 