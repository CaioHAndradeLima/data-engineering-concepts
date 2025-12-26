SELECT
  user_id,
  SUM(action_count) AS total_actions
FROM user_activity_daily
GROUP BY user_id
ORDER BY total_actions DESC
LIMIT 10;
