-- company definition

CREATE TABLE company (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	cuit INTEGER NOT NULL UNIQUE,
	company_name TEXT(50) NOT NULL,
	fantasy_name TEXT(50),
	working_path TEXT(100) NOT NULL,
	address TEXT(50) NOT NULL,
	phone INTEGER,
	dependency_afip INTEGER,
	activity_code INTEGER,
	iva_conditions TEXT(3) NOT NULL,
	month_close INTEGER DEFAULT (12) NOT NULL,
	taxpayer_type INTEGER,
	undersigned TEXT(50),
	undersigned_character TEXT(15)
);