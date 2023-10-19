-- creates the MySQL server user user_0d_1
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
CRANT ALL PRIVILEGES ON * . * user_0d_1@localhost;
