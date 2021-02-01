# Setting up the database and user
    - must have mysql downloaded, and have the mysql.server running
        - '/usr/local/bin/mysql.server start' starts the server
    - CREATE DATABASE testflask;
    - use testflask;
    - CREATE TABLE user (name VARCHAR(20), EMAIL VARCHAR(20));
    - SHOW TABLES; or DESCRIBE USER; for validation
    - CREATE USER 'root'@'localhost' IDENTIFIED BY 'root';
        - might have to use 127.0.0.1 instead of localhost, this was a little wonky for me
    - GRANT ALL PRIVILEGES ON testflask.* TO 'root'@'localhost';

    **NOTE:** consider mysql_secure_installation for deployment


# Random notes
    - file extensions are being validated server-side right now, this should be done client side so we don't send anything that we can't accept
    - we need to set some standards for coding conventions
        * for example, we're using ES6 so we should likely use 'let' instead of 'var' in scripts