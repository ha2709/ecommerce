-- Create the public schema if it doesn't exist
CREATE SCHEMA IF NOT EXISTS public;

-- Create the customercategory ENUM type
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'customercategory') THEN
        CREATE TYPE public.customercategory AS ENUM ('BRONZE', 'SILVER', 'GOLD');
    END IF;
END
$$;

-- Create the alembic_version table
CREATE TABLE IF NOT EXISTS public.alembic_version (
    version_num character varying(32) NOT NULL
);

-- Create the customers table
CREATE TABLE IF NOT EXISTS public.customers (
    id uuid NOT NULL,
    email character varying,
    successful_orders integer
);

-- Create the departments table
CREATE TABLE IF NOT EXISTS public.departments (
    id uuid NOT NULL,
    name character varying
);

-- Create the discounts table
CREATE TABLE IF NOT EXISTS public.discounts (
    id uuid NOT NULL,
    customer_category public.customercategory NOT NULL,
    product_category_id uuid,
    percentage double precision NOT NULL
);

-- Create the order_items table
CREATE TABLE IF NOT EXISTS public.order_items (
    id uuid NOT NULL,
    order_id uuid,
    product_id uuid,
    quantity integer NOT NULL,
    unit_price double precision NOT NULL,
    total_price double precision NOT NULL
);

-- Create the order_products table
CREATE TABLE IF NOT EXISTS public.order_products (
    id uuid NOT NULL,
    order_id uuid,
    product_id uuid
);

-- Create the orders table
CREATE TABLE IF NOT EXISTS public.orders (
    id uuid NOT NULL,
    user_id uuid,
    status character varying,
    total_price double precision,
    customer_id uuid
);

-- Create the product_categories table
CREATE TABLE IF NOT EXISTS public.product_categories (
    id uuid NOT NULL,
    name character varying,
    department_id uuid
);

-- Create the products table
CREATE TABLE IF NOT EXISTS public.products (
    id uuid NOT NULL,
    name character varying,
    price double precision,
    department_id uuid,
    discount_id uuid,
    category_id uuid
);

-- Create the shopping_cart table
CREATE TABLE IF NOT EXISTS public.shopping_cart (
    id uuid NOT NULL
);

-- Create the shopping_cart_items table
CREATE TABLE IF NOT EXISTS public.shopping_cart_items (
    id uuid NOT NULL,
    product_id uuid,
    quantity integer,
    shopping_cart_id uuid
);

-- Create the users table
CREATE TABLE IF NOT EXISTS public.users (
    id uuid NOT NULL,
    email character varying,
    hashed_password character varying,
    is_staff boolean,
    department_id uuid,
    customer_id uuid
);

-- Create the verification_tokens table
CREATE TABLE IF NOT EXISTS public.verification_tokens (
    id uuid NOT NULL,
    email character varying,
    token character varying NOT NULL
);

-- Create PRIMARY KEY constraints
ALTER TABLE public.alembic_version ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);
ALTER TABLE public.customers ADD CONSTRAINT customers_pkey PRIMARY KEY (id);
ALTER TABLE public.departments ADD CONSTRAINT departments_pkey PRIMARY KEY (id);
ALTER TABLE public.discounts ADD CONSTRAINT discounts_pkey PRIMARY KEY (id);
ALTER TABLE public.order_items ADD CONSTRAINT order_items_pkey PRIMARY KEY (id);
ALTER TABLE public.order_products ADD CONSTRAINT order_products_pkey PRIMARY KEY (id);
ALTER TABLE public.orders ADD CONSTRAINT orders_pkey PRIMARY KEY (id);
ALTER TABLE public.product_categories ADD CONSTRAINT product_categories_pkey PRIMARY KEY (id);
ALTER TABLE public.products ADD CONSTRAINT products_pkey PRIMARY KEY (id);
ALTER TABLE public.shopping_cart_items ADD CONSTRAINT shopping_cart_items_pkey PRIMARY KEY (id);
ALTER TABLE public.shopping_cart ADD CONSTRAINT shopping_cart_pkey PRIMARY KEY (id);
ALTER TABLE public.users ADD CONSTRAINT users_pkey PRIMARY KEY (id);
ALTER TABLE public.verification_tokens ADD CONSTRAINT verification_tokens_pkey PRIMARY KEY (id);
ALTER TABLE public.verification_tokens ADD CONSTRAINT verification_tokens_token_key UNIQUE (token);

-- Create FOREIGN KEY constraints
ALTER TABLE public.discounts ADD CONSTRAINT discounts_product_category_id_fkey FOREIGN KEY (product_category_id) REFERENCES public.product_categories(id);
ALTER TABLE public.order_items ADD CONSTRAINT order_items_order_id_fkey FOREIGN KEY (order_id) REFERENCES public.orders(id);
ALTER TABLE public.order_items ADD CONSTRAINT order_items_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(id);
ALTER TABLE public.order_products ADD CONSTRAINT order_products_order_id_fkey FOREIGN KEY (order_id) REFERENCES public.orders(id);
ALTER TABLE public.order_products ADD CONSTRAINT order_products_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(id);
ALTER TABLE public.orders ADD CONSTRAINT orders_customer_id_fkey FOREIGN KEY (customer_id) REFERENCES public.customers(id);
ALTER TABLE public.orders ADD CONSTRAINT orders_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);
ALTER TABLE public.product_categories ADD CONSTRAINT product_categories_department_id_fkey FOREIGN KEY (department_id) REFERENCES public.departments(id);
ALTER TABLE public.products ADD CONSTRAINT products_category_id_fkey FOREIGN KEY (category_id) REFERENCES public.product_categories(id);
ALTER TABLE public.products ADD CONSTRAINT products_department_id_fkey FOREIGN KEY (department_id) REFERENCES public.departments(id);
ALTER TABLE public.products ADD CONSTRAINT products_discount_id_fkey FOREIGN KEY (discount_id) REFERENCES public.discounts(id);
ALTER TABLE public.shopping_cart_items ADD CONSTRAINT shopping_cart_items_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(id);
ALTER TABLE public.shopping_cart_items ADD CONSTRAINT shopping_cart_items_shopping_cart_id_fkey FOREIGN KEY (shopping_cart_id) REFERENCES public.shopping_cart(id);
ALTER TABLE public.users ADD CONSTRAINT users_customer_id_fkey FOREIGN KEY (customer_id) REFERENCES public.customers(id);
ALTER TABLE public.users ADD CONSTRAINT users_department_id_fkey FOREIGN KEY (department_id) REFERENCES public.departments(id);
