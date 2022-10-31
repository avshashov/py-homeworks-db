CREATE TABLE departments (
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR(60) UNIQUE NOT NULL,
    employee_id INTEGER,
    director_id INTEGER
    );
    
    
CREATE TABLE employees ( 
    id SERIAL PRIMARY KEY, 
    employee_name VARCHAR(60) UNIQUE NOT NULL,
    department_id INTEGER REFERENCES departments(department_id),
    director_id INTEGER REFERENCES employees(id),
    director_name VARCHAR(60) NOT NULL
    );