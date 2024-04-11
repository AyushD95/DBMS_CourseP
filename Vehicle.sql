CREATE TABLE vehicles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    vehicle_owner VARCHAR(255) NOT NULL,
    vehicle_model VARCHAR(255) NOT NULL,
    vehicle_type VARCHAR(255) NOT NULL,
    vehicle_colour VARCHAR(255) NOT NULL,
    vehicle_number VARCHAR(255) NOT NULL,
    parking_spot VARCHAR(255) NOT NULL,
    purpose VARCHAR(255) NOT NULL,
    entry_date DATE NOT NULL,
    entry_time TIME NOT NULL,
    exit_date DATE NOT NULL,
    exit_time TIME NOT NULL
);

select*from vehicles;