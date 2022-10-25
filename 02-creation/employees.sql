CREATE TABLE departments (
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR(60) UNIQUE NOT NULL,
    employee_id INTEGER,
    director_id INTEGER
    );
    
CREATE TABLE directors (
    id SERIAL PRIMARY KEY,
    director_name VARCHAR(60) UNIQUE NOT NULL,
    department_id INTEGER REFERENCES departments(department_id)
    );
    
CREATE TABLE employees ( 
    id SERIAL PRIMARY KEY, 
    employee_name VARCHAR(60) UNIQUE NOT NULL,
    department_id INTEGER REFERENCES departments(department_id),
    director_id INTEGER REFERENCES directors(id)
    );