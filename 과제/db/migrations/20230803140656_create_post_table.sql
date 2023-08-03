-- migrate:up
CREATE TABLE posts(
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(1000),
  content VARCHAR(2000),
  created_at TIMESTAMP,
  link VARCHAR(3000)
);

-- migrate:down
DROP TABLE posts;
