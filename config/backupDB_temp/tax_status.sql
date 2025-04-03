-- tax_status definition

CREATE TABLE tax_status (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT
	, code TEXT(3) NOT NULL UNIQUE, description TEXT(30) NOT NULL, detail_buy NUMERIC DEFAULT (0) NOT NULL, detail_sell NUMERIC DEFAULT (0) NOT NULL, monotributo NUMERIC DEFAULT (0) NOT NULL, magnetic_bracket INTEGER);