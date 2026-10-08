WITH dept_avg AS (
    SELECT
        dept_name,
        AVG(salary) AS avg_salary
    FROM employees
    GROUP BY dept_name
),
above_avg AS (
    SELECT
        e.name,
        e.dept_name,
        e.salary,
        d.avg_salary,
        ROUND(
            ((e.salary - d.avg_salary) / d.avg_salary) * 100,
            2
        ) AS pct_above
    FROM employees e
    JOIN dept_avg d
        ON e.dept_name = d.dept_name
    WHERE e.salary > d.avg_salary
)
SELECT
    name,
    dept_name,
    salary,
    avg_salary,
    pct_above
FROM above_avg
ORDER BY pct_above DESC;