
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


CREATE TABLE company (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	cuit INTEGER NOT NULL UNIQUE,
	company_name TEXT(50) NOT NULL,
	fantasy_name TEXT(50),
	working_path TEXT(100) NOT NULL,
	adress TEXT(50) NOT NULL,
	phone INTEGER,
	dependency_afip INTEGER,
	activity_code INTEGER,
	iva_conditions TEXT(3) NOT NULL,
	month_close INTEGER DEFAULT (12) NOT NULL,
	taxpayer_type INTEGER,
	undersigned TEXT(50),
	undersigner_character TEXT(15)
);

CREATE TABLE tax_status (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	code TEXT(3) NOT NULL UNIQUE,
	description TEXT(30) NOT NULL,
	detail_buy NUMERIC DEFAULT (0) NOT NULL,
	detail_sell NUMERIC DEFAULT (0) NOT NULL,
	monotributo NUMERIC DEFAULT (0) NOT NULL,
	magnetic_bracket INTEGER
);

CREATE TABLE aliquots_iva (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	code INTEGER NOT NULL,
	description TEXT(40) NOT NULL,
	is_gral INTEGER DEFAULT (0) NOT NULL
);
