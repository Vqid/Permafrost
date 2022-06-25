CREATE TABLE IF NOT EXISTS users(
    id BIGINT PRIMARY KEY,
    name TEXT,
    xp INT,
    level INT,
    date_created TIMESTAMP
)