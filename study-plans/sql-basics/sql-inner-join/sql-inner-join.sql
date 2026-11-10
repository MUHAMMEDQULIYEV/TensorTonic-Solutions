-- Returns: name, salary, dept_name.
select  e.name ,salary ,d.dept_name from employees e
inner join  departments d on d.id=e.dept_id
order by e.name asc NULLS LAST 