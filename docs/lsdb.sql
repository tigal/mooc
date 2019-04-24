INSERT INTO categories (category_id, name) VALUES (1, 'Категория 1');
INSERT INTO categories (category_id, name) VALUES (2, 'Категория 2');
INSERT INTO customers (customer_id, first_name, last_name, email, phone, birth_day, create_time, is_active) VALUES (1, 'Test ', 'MrTest', 'test@example.com', '911', '1970-02-05', '2019-04-02 00:40:52.000000', true);
INSERT INTO order_items (item_id, order_id, product_id, list_price, quantity) VALUES (1, 1, 4, 0, 2);
INSERT INTO order_items (item_id, order_id, product_id, list_price, quantity) VALUES (2, 1, 5, 0, 345);
INSERT INTO orders (order_id, customer_id, order_status, create_time) VALUES (1, 1, 'pre_order', '2019-04-02 00:41:05.000000');
INSERT INTO products (product_id, name, price, available_quantity, reserved_quantity, create_time, category_id) VALUES (4, 'Продукт 1', 10, 1222, 0, '2019-04-02 00:41:21.000000', 1);
INSERT INTO products (product_id, name, price, available_quantity, reserved_quantity, create_time, category_id) VALUES (5, 'Продукт 2', 600, 15000, 0, '2019-04-02 00:41:35.000000', 2);