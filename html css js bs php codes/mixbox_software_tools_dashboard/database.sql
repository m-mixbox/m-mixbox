-- Drop existing tables if they exist
DROP TABLE IF EXISTS admin_logs;
DROP TABLE IF EXISTS file_conversions;
DROP TABLE IF EXISTS users;

-- Create users table with role
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role ENUM('user', 'admin') NOT NULL DEFAULT 'user',
    email VARCHAR(100),
    last_login TIMESTAMP NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create file_conversions table
CREATE TABLE file_conversions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    original_filename VARCHAR(255) NOT NULL,
    converted_filename VARCHAR(255) NOT NULL,
    conversion_type ENUM('image_to_docx', 'json_to_excel', 'pdf_to_excel', 'excel_to_xml') NOT NULL,
    status ENUM('pending', 'completed', 'failed') NOT NULL DEFAULT 'pending',
    file_size INT,
    ip_address VARCHAR(45),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Create admin_logs table
CREATE TABLE admin_logs (
    id INT PRIMARY KEY AUTO_INCREMENT,
    admin_id INT,
    action_type ENUM('login', 'user_management', 'system_config', 'view_logs') NOT NULL,
    description TEXT,
    ip_address VARCHAR(45),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (admin_id) REFERENCES users(id)
);

-- Insert default admin account
INSERT INTO users (username, password, role, email) 
VALUES ('admin', '$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi', 'admin', 'admin@example.com');
-- Default password: 'password'