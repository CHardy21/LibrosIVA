-- invoices definition

CREATE TABLE invoices (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	code TEXT(4) NOT NULL UNIQUE,
	description TEXT(30) NOT NULL,
	observations TEXT(100),
	type_ret INTEGER DEFAULT (0) NOT NULL,
	type_cert INTEGER DEFAULT (0) NOT NULL,
	type_dc TEXT(1) NOT NULL,
	active_buy TEXT(1),
	active_sell TEXT(1),
	numeration TEXT(1),
	c_fiscal INTEGER DEFAULT (0) NOT NULL,
	code_a INTEGER,
	code_b INTEGER,
	code_c INTEGER,
	code_e INTEGER,
	code_m INTEGER,
	code_t INTEGER,
	code_o INTEGER
);