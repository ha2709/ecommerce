# ecommerce
Pinchi Inc is a leading supplier of groceries. The company has decided to venture into e-commerce
 
# Pinchi Inc E-Commerce System

## 1. Project Overview
### 1.1 Problem Statement

Pinchi Inc, a leading grocery supplier, is expanding into the e-commerce domain in response to the challenges posed by the COVID-19 pandemic. This strategic move aims to enhance customer service through a robust and scalable online system. The following document outlines the business requirements that will guide the development of this e-commerce platform.

### 2. Business Requirements
#### 2.1 Users
The system is designed for two primary user groups:

- Internal Staff: Assigned to specific departments with unique access privileges.
- External Customers: Regular consumers of Pinchi Inc's products.

#### 2.2 Onboarding
- Customer Registration: Customers register using their email addresses. A verification email is sent to complete the registration process.

#### 2.3 Products Management
- Product Categories: Includes various categories like frozen foods and fresh produce. Each category is linked to a specific department.
- Product Attributes: Includes details like price and name.
- Staff Access: Staff can manage (add, update, or delete) products specific to their department.

####  2.4 Customer Categorization
Customers are categorized based on the number of successful orders:

- Bronze: 0-20 orders
- Silver: 21-49 orders
- Gold: 50 or more orders

#### 2.5 Discounts

- Periodic Discounts: Offered on selected products.
- Discount Criteria: Based on the combination of customer and product categories.

#### 2.6 Shopping Cart

Functionality: Both registered and unregistered customers can view products, add to the shopping cart, and remove items.
#### 2.7 Order and Checkout
- Exclusive to Registered Customers: Only registered customers can place orders.
- Discount Application: Applied during payment if applicable.
- Order History: Customers can view their past orders.

### 3. Implementation Notes
- This document serves as a preliminary guide for the development team.
- Further specifications and technical details will be provided in subsequent documentation.

`uvicorn src.main:app --reload`