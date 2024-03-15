-- Convert the hbtn_0c_0 database, the first_table table, and the name field
-- in first_table to UTF-8 (utf8mb4) with the collation utf8mb4_unicode_ci
USE hbtn_0c_0
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
