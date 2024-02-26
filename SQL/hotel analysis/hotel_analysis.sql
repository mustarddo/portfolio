-- DDL
CREATE TABLE Rooms (
    room_id INT PRIMARY KEY,
    room_type VARCHAR(255) NOT NULL,
    status VARCHAR(20) NOT NULL CHECK (status IN ('available', 'occupied'))
);

CREATE TABLE Reservations (
    reservation_id INT PRIMARY KEY,
    room_id INT,
    customer_id INT NOT NULL,
    check_in_date DATE NOT NULL,
    check_out_date DATE NOT NULL,
    amount_paid DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (room_id) REFERENCES Rooms(room_id)
);

-- Inserting data into the Rooms table
INSERT INTO Rooms (room_id, room_type, status) VALUES
(1, 'Deluxe', 'available'),
(2, 'Deluxe', 'available'),
(3, 'Executive Suite', 'available'),
(4, 'Presidential Suite', 'available'),
(5, 'Deluxe', 'occupied'),
(6, 'Presidential Suite', 'occupied'),
(7, 'Executive Suite', 'occupied'),
(8, 'Deluxe', 'available'),
(9, 'Presidential Suite', 'available');

-- Inserting data into the Reservations table
INSERT INTO Reservations (reservation_id, room_id, customer_id, check_in_date, check_out_date, amount_paid) VALUES
(1, 1, 101, '2024-02-01', '2024-02-05', 500),
(2, 2, 102, '2024-02-02', '2024-02-07', 800),
(3, 3, 103, '2024-02-03', '2024-02-10', 1200),
(4, 4, 104, '2024-02-04', '2024-02-06', 1000),
(5, 5, 105, '2024-02-05', '2024-02-09', 1500),
(6, 6, 106, '2024-02-06', '2024-02-08', 2000),
(7, 7, 107, '2024-02-07', '2024-02-11', 1800),
(8, 8, 108, '2024-02-08', '2024-02-12', 1600),
(9, 9, 109, '2024-02-09', '2024-02-13', 1400);

.print #######################
.print #### SQL Challenge ####
.print #######################

.print \n Rooms table
.mode box
select * from Rooms limit 5;

.print \n Reservations table
.mode box
select * from Reservations limit 5;

--- Practice ---

>Call vacant room in each category
SELECT room_type, COUNT(*) AS available_room FROM Rooms WHERE status = "available" GROUP BY room_type

> Average paid per customer 
SELECT AVG(amount_paid) AS Average_paid FROM reservations

> The customer who has the highest spending amount and times he have reserved a room
  
SELECT customer_id, SUM(amount_paid), COUNT(*) AS booking_times
FROM reservations
WHERE customer_id = (
SELECT customer_id FROM reservations ORDER BY amount_paid DESC LIMIT 1 )
GROUP BY customer_id

>
