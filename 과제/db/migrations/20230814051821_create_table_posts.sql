-- migrate:up
CREATE TABLE posts(
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  user_name VARCHAR(50),
  user_email VARCHAR(200),
  title VARCHAR(1000),
  content VARCHAR(2000),
  link VARCHAR(3000),
  created_at TIMESTAMP
);

-- migrate:down
DROP TABLE posts;
