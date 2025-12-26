CREATE TABLE IF NOT EXISTS user_activity_daily (
    activity_date DATE NOT NULL,
    user_id INTEGER NOT NULL,
    action_count INTEGER NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT now(),
    CONSTRAINT user_activity_daily_pk
        PRIMARY KEY (activity_date, user_id)
);
