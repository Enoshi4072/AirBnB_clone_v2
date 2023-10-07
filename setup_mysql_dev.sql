-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the user 'hbnb_dev' with password 'hbnb_dev_pwd' if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on 'hbnb_dev_db' to 'hbnb_dev' if it exists
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on 'performance_schema' to 'hbnb_dev' if it exists
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
