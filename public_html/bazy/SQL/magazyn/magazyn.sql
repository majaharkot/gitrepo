DROP TABLE IF EXISTS tbCustomers;
CREATE TABLE tbCustomers (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	customer_name TEXT,
	adres INTEGER
);

DROP TABLE IF EXISTS tbOrders;
CREATE TABLE tbOrders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
	customer_id INTEGER,
	subscription_id INTEGER,
	purchase_date DATE,
	FOREIGN KEY (customer_id) REFERENCES tbCustomers(id),
	FOREIGN KEY (subscription_id) REFERENCES tbSubscription(id)
);

DROP TABLE IF EXISTS tbSubscription;
CREATE TABLE tbSubscription (
	subscription_id INTEGER PRIMARY KEY AUTOINCREMENT,
	description TEXT,
	price_per_month INTEGER,
	subscription_length TEXT	
);
