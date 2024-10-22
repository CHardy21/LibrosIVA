-- aliquots_by_date definition

CREATE TABLE aliquots_by_date (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	id_aliquots_iva INTEGER NOT NULL,
	from_date TEXT NOT NULL,
	rate NUMERIC NOT NULL,
	surcharge_rate NUMERIC NOT NULL,
	surcharge NUMERIC NOT NULL,
	inverse_coef REAL NOT NULL,
	FOREIGN KEY(id_aliquots_iva) REFERENCES aliquots_iva(id)
);