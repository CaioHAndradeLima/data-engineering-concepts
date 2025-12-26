SELECT
  activity_date,
  COUNT(DISTINCT user_id) AS daily_active_users
FROM user_activity_daily
GROUP BY activity_date
ORDER BY activity_date;
