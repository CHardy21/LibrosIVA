CREATE TABLE IF NOT EXISTS tax_status (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	code TEXT(3) NOT NULL UNIQUE,
	description TEXT(30) NOT NULL,
	detail_buy NUMERIC DEFAULT (0) NOT NULL,
	detail_sell NUMERIC DEFAULT (0) NOT NULL,
	monotributo NUMERIC DEFAULT (0) NOT NULL,
	magnetic_bracket INTEGER
	);

INSERT INTO tax_status (code,description,detail_buy,detail_sell,monotributo,magnetic_bracket) VALUES
	 ('CE','Cliente de Exterior',0,0,0,),
	 ('CF','Consumidor Final',0,0,0,NULL),
	 ('EXE','Exento',0,0,0,NULL),
	 ('MT','Responsable Monotributo',0,0,0,NULL),
	 ('MTD','Resp. Monotributo Discr. IVA',0,0,0,NULL),
	 ('MTE','Rep. Monotributo Contr. Eventual',0,0,0,NULL),
	 ('NR','No Responsable',0,0,0,NULL),
	 ('PE','Proveedor del Exterior',0,0,0,NULL),
	 ('RI','Responsable Inscripto',1,1,0,NULL),
	 ('RNI','Responsable No Inscripto',0,0,0,NULL);
INSERT INTO tax_status (code,description,detail_buy,detail_sell,monotributo,magnetic_bracket) VALUES
	 ('SNC','Sujeto No Categorizado',0,0,0,NULL);
