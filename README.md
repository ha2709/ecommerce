# Pinchi Inc E-Commerce System

## 1. Project Overview
### 1.1 Problem Statement

Pinchi Inc, a leading grocery supplier, is expanding into the e-commerce domain in response to the challenges posed by the COVID-19 pandemic. This strategic move aims to enhance customer service through a robust and scalable online system. The following document outlines the business requirements that will guide the development of this e-commerce platform.

## 2. Business Requirements
### 2.1 Users
The system is designed for two primary user groups:

- Internal Staff: Assigned to specific departments with unique access privileges.
- External Customers: Regular consumers of Pinchi Inc's products.

### 2.2 Onboarding
- Customer Registration: Customers register using their email addresses. A verification email is sent to complete the registration process.

#### 2.3 Products Management
- Product Categories: Includes various categories like frozen foods and fresh produce. Each category is linked to a specific department.
- Product Attributes: Includes details like price and name.
- Staff Access: Staff can manage (add, update, or delete) products specific to their department.

###  2.4 Customer Categorization
Customers are categorized based on the number of successful orders:

- Bronze: 0-20 orders
- Silver: 21-49 orders
- Gold: 50 or more orders

### 2.5 Discounts

- Periodic Discounts: Offered on selected products.
- Discount Criteria: Based on the combination of customer and product categories.

### 2.6 Shopping Cart

Functionality: Both registered and unregistered customers can view products, add to the shopping cart, and remove items.
### 2.7 Order and Checkout
- Exclusive to Registered Customers: Only registered customers can place orders.
- Discount Application: Applied during payment if applicable.
- Order History: Customers can view their past orders.

## 3. Implementation Notes
- This document serves as a preliminary guide for the development team.
- Further specifications and technical details will be provided in subsequent documentation.

I use a common architectural pattern known as "Separation of Concerns." This pattern is about organizing code in a way that separates different responsibilities into distinct modules or functions.

Here's how the code relates to the Separation of Concerns pattern:

# 1.  Responsibility Separation  : 
The code separates different responsibilities into different sections or functions. For example:

- Registration and email verification logic are encapsulated in the /users/ and /verify/ endpoints.
- Database-related operations are handled by the create_user function and the use of the database session.
# 2. Modularity: 
The code is organized into functions and modules that focus on specific tasks:

- The /users/ endpoint handles user registration and sends verification emails.
- The /verify/ endpoint handles email verification.
- Database operations are separated into the create_user function.
- Email sending functionality is encapsulated in the send_verification_email function.
# 3.  Single Responsibility Principle: 
Each function or module has a single responsibility. 
For example, the send_verification_email function is responsible for sending emails, and the /users/ endpoint is responsible for user registration.
# Dependency injection:
The parameter `db` is being injected into the `verify_user` function using FastAPI's dependency injection mechanism. This is a form of Dependency Injection, which is an architectural pattern used to manage and provide dependencies to components of an application. It helps in decoupling the code and making it more modular and testable
I use Asynchoronous paradigm for these benefits: 

- 1. Improved Performance for I/O Bound Tasks: Asynchronous endpoints are highly efficient for I/O-bound operations (like database access, network calls). They don't block the server thread while waiting for the I/O operation to complete. This allows handling more requests simultaneously, leading to better throughput.
- 2. Better Scalability: Since async endpoints can handle multiple requests concurrently without creating new threads or processes, the server can serve more requests with fewer resources, enhancing scalability.
- 3. Non-blocking Nature: Async allows for non-blocking code execution, which is particularly beneficial in scenarios where a service needs to make multiple external API calls or database queries.
- 4. Modern Python Features: Asynchronous programming is supported natively in modern Python (3.7+), allowing developers to leverage features like async/await syntax, which leads to cleaner and more maintainable code for asynchronous operations.

schedule the `categorize_customers.py` function to run periodically, such as daily or weekly, to update customer categories based on their order history.

`python3 -m venv env`

`source env/bin/activate`

# Project Deployment Instructions
This document outlines the necessary steps for deploying the project using Docker and managing PostgreSQL. Follow these instructions for a smooth deployment process.

## Deployment Steps
### Managing PostgreSQL Service
### 1. Stop the Local PostgreSQL Service:
Before proceeding with Docker, ensure the local PostgreSQL service is stopped to avoid any conflicts:

`systemctl stop postgresql`

## Running Docker for Deployment
### 1. Build and Start Docker Services:
Build and start all services defined in your docker-compose file. This command also rebuilds the services if there have been changes:
 
 `docker-compose up --build`

 ## 2. Start Docker Services Without Rebuilding:
To start all services defined in your docker-compose file without rebuilding:

`docker-compose up`

## 3. Stopping Docker Services:
To stop all services and remove the associated containers, networks, and volumes:

`docker-compose down`

# Database Migration in Docker
## 1. Attach to the Backend Container:
After starting Docker, attach to the backend container to run the Alembic commands for database migration.

## 2. Creating a New Database Migration:
Generate a new migration file with the specified message:

`alembic revision --autogenerate -m "create_relationship"`

## 3. Upgrading the Database to the Latest Revision:
Apply the latest migration to the database:

`alembic upgrade head`

on browser, navigate to:

`http://localhost:3000`

See the documentation of Back end at :

`http://localhost:8000/docs`


## Additional Notes

- Ensure all Docker services are running smoothly before proceeding with database migrations.
- Monitor the Docker containers and PostgreSQL service for any errors during startup or operation.
- Regularly update your Docker configurations and database schema as needed.

For further assistance or queries, please contact the development team.
