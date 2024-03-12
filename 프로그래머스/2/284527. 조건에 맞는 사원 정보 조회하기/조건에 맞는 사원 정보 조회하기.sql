-- 코드를 작성해주세요
# SUM(SCORE) AS SCORE,EMP_NO,EMP_NAME,POSITION,EMAIL
SELECT SUM(SCORE) AS SCORE,A.emp_no, A.emp_name, A.position, A.email 
FROM HR_EMPLOYEES  A
JOIN HR_DEPARTMENT B ON A.DEPT_ID=B.DEPT_ID
JOIN HR_GRADE C ON A.EMP_NO=C.EMP_NO
GROUP BY C.EMP_NO
ORDER BY SCORE DESC LIMIT 1
# select e.emp_no, e.emp_name, e.position, e.email 
# from hr_employees e
# join hr_grade g using(emp_no)
# join hr_department d using(dept_id)
# group by e.emp_no
