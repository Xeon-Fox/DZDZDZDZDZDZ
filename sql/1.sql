CREATE DATABASE Airport;

USE Airport;

CREATE TABLE Airlines (
    id INT AUTO_INCREMENT,
    name VARCHAR(255),
    country VARCHAR(255),
    PRIMARY KEY(id)
);

CREATE TABLE Airplanes (
    id INT AUTO_INCREMENT,
    model VARCHAR(255),
    airline_id INT,
    PRIMARY KEY(id),
    FOREIGN KEY (airline_id) REFERENCES Airlines(id)
);

CREATE TABLE Airports (
    id INT AUTO_INCREMENT,
    name VARCHAR(255),
    city VARCHAR(255),
    country VARCHAR(255),
    PRIMARY KEY(id)
);

CREATE TABLE Flights (
    id INT AUTO_INCREMENT,
    departure_airport_id INT,
    arrival_airport_id INT,
    departure_time DATETIME,
    arrival_time DATETIME,
    airplane_id INT,
    PRIMARY KEY(id),
    FOREIGN KEY (departure_airport_id) REFERENCES Airports(id),
    FOREIGN KEY (arrival_airport_id) REFERENCES Airports(id),
    FOREIGN KEY (airplane_id) REFERENCES Airplanes(id)
);

CREATE TABLE Passengers (
    id INT AUTO_INCREMENT,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    passport_number VARCHAR(255),
    PRIMARY KEY(id)
);

CREATE TABLE Tickets (
    id INT AUTO_INCREMENT,
    flight_id INT,
    passenger_id INT,
    seat_number VARCHAR(255),
    class ENUM('Economy', 'Business', 'First'),
    price DECIMAL(10, 2),
    PRIMARY KEY(id),
    FOREIGN KEY (flight_id) REFERENCES Flights(id),
    FOREIGN KEY (passenger_id) REFERENCES Passengers(id)
);

CREATE TABLE Employees (
    id INT AUTO_INCREMENT,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    position VARCHAR(255),
    airport_id INT,
    PRIMARY KEY(id),
    FOREIGN KEY (airport_id) REFERENCES Airports(id)
);





INSERT INTO Airlines (name, country) VALUES ('флайарыстан', 'кз'), ('флайдубай', 'оаэ');
INSERT INTO Airplanes (model, airline_id) VALUES ('боинг 747', 1), ('боинг 777', 2);
INSERT INTO Airports (name, city, country) VALUES ('аэропорт алмата', 'алмата', 'кз'), ('аэропорт дубая', 'дубай', 'оаэ');
INSERT INTO Flights (departure_airport_id, arrival_airport_id, departure_time, arrival_time, airplane_id) VALUES (1, 2, '2024-01-01 10:00:00', '2024-01-01 14:00:00', 1);
INSERT INTO Passengers (first_name, last_name, passport_number) VALUES ('сигма', 'крипер', '123456789'), ('кай', 'сенат', '987654321');
INSERT INTO Tickets (flight_id, passenger_id, seat_number, class, price) VALUES (1, 1, '12A', 'экокном', 100.00), (1, 2, '12B', 'бизнес', 100.00);
INSERT INTO Employees (first_name, last_name, position, airport_id) VALUES ('красава', 'крутой', 'капитан', 1), ('девушка', 'женщина', 'бортпроводница', 2);




SELECT Flights.id, departure_time, arrival_time, Airlines.name AS airline, Airplanes.model AS airplane, departure.name AS departure_airport, arrival.name AS arrival_airport
FROM Flights
JOIN Airplanes ON Flights.airplane_id = Airplanes.id
JOIN Airlines ON Airplanes.airline_id = Airlines.id
JOIN Airports AS departure ON Flights.departure_airport_id = departure.id
JOIN Airports AS arrival ON Flights.arrival_airport_id = arrival.id;