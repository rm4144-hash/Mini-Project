CREATE TABLE customers(
 id INTEGER PRIMARY KEY,
 name TEXT,
 email TEXT,
 dob DATE
);

INSERT INTO customers VALUES
(1, 'Alice', 'alice@example.com', '1985-06-10'),
(2, 'Bob', NULL, '1978-11-02'),
(2, 'Bob', 'bob.jones@example.com', '1978-11-02'),
(3, 'Carol', 'carol_at_example.com', '1990-02-29'),
(4, NULL, 'john.doe@example.com', '1992-04-01');
