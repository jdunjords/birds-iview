# Database
    - must have mysql downloaded, and have the mysql.server running
        - '/usr/local/bin/mysql.server start' starts the server
    - CREATE DATABASE testflask;
    - use testflask;
    - CREATE TABLE user (
        id INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(20),
        email VARCHAR(20),
        PRIMARY KEY (id)
        );
    - SHOW TABLES; or DESCRIBE USER; for validation
    - CREATE USER 'root'@'localhost' IDENTIFIED BY 'root';
        - might have to use 127.0.0.1 instead of localhost, this was a little wonky for me
    - GRANT ALL PRIVILEGES ON testflask.* TO 'root'@'localhost';
    - create account "biv_admin"

    **NOTE:** consider mysql_secure_installation for deployment

    CREATE TABLE UserImages (
        ImageNumber INT NOT NULL AUTO_INCREMENT, 
        uid int,ImageFilePath VARCHAR(300), 
        PRIMARY KEY (ImageNumber), 
        FOREIGN KEY (uid) REFERENCES user (id));

# Frontend
    - index page will be login
        - it'll have a link to creat-account page
        - /create-account will redirect to profile page
    - profile page
        - display user id/name
        - input form for uploading new pics
        - input form for selecting images to classify


# Random notes
    - file extensions are being validated server-side right now, this should be done client side so we don't send anything that we can't accept
    - we need to set some standards for coding conventions
        * for example, we're using ES6 so we should likely use 'let' instead of 'var' in scripts
    - let's switch from yaml to json for config data