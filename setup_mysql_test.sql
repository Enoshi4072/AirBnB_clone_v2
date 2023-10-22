-- Prepares a MySQL Test server for the project.
-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create the user 'hbnb_test' with password 'hbnb_dev_pwd' if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant all privileges on 'hbnb_dev_db' to 'hbnb_test' if it exists
GRANT ALL PRIVILEGES ON hbnb_test_db . * TO 'hbnb_test'@'localhost';
-- Grant SELECT privilege on 'performance_schema' to 'hbnb_test' if it exists
GRANT SELECT ON performance_schema . * TO 'hbnb_test'@'localhost';
