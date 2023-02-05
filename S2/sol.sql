WITH d_u AS (SELECT DISTINCT s.user_id, s.problem_id FROM submissions as s WHERE s.success = TRUE),
     d_t AS (SELECT DISTINCT s.user_id, s.problem_id FROM submissions as s),
     c_t AS (SELECT d_t.user_id as id, COUNT(DISTINCT p.contest_id)
             FROM d_t
                      JOIN problems as p ON p.id = d_t.problem_id
             GROUP BY d_t.user_id),
     c_u AS (SELECT d_u.user_id as id, COUNT(DISTINCT p.contest_id)
             FROM d_u
                      JOIN problems as p ON p.id = d_u.problem_id
             GROUP BY d_u.user_id)
SELECT u.id                   as id,
       u.name                 as name,
       COALESCE(c_u.count, 0) as solved_at_least_one_contest_count,
       COALESCE(c_t.count, 0) as take_part_contest_count
FROM users as u
         LEFT JOIN c_t ON c_t.id = u.id
         LEFT JOIN c_u ON c_u.id = u.id
ORDER BY solved_at_least_one_contest_count DESC, take_part_contest_count DESC, id;