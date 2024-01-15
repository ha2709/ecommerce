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


`uvicorn main:app --reload`

`alembic revision --autogenerate -m "create_relationship"`

`alembic upgrade head`

`build -t backend .`

`docker run -p 8000:8000 backend`

`systemctl stop postgresql`

`systemctl start postgresql`

`docker-compose up --build`

To run docker :
`docker-compose up`

To stop docker: 
`docker-compose down`