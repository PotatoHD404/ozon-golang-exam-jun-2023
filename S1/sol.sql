WITH d_u AS (SELECT DISTINCT s.user_id, s.problem_id FROM submissions as s WHERE s.success = TRUE)
SELECT pr.*
FROM problems as pr
WHERE (SELECT COUNT(*) FROM d_u as s WHERE s.problem_id = pr.id) >= 2 ORDER BY pr.id;