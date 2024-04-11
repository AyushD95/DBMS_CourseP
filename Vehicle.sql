CREATE TABLE vehicles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    owner_name VARCHAR(255) NOT NULL,
    vehicle_name VARCHAR(255) NOT NULL,
    vehicle_number VARCHAR(255) NOT NULL,
    entry_date DATE NOT NULL,
    exit_date DATE NOT NULL
);

select*from vehicles;