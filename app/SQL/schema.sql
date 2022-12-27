--SET FOREIGN KEYS OFF INORDER TO DROP & CREATE TABLES
PRAGMA foreign_keys = OFF;
PRAGMA foreign_keys;


DROP TABLE IF EXISTS OrderTbl;
CREATE TABLE OrderTbl (
	id INTEGER NOT NULL,
	OrderNbr INTEGER NOT NULL,
	OrderSupplierId INTEGER,
	OrderPartId INTEGER,
	OrderQuantity INTEGER NOT NULL,
	OrderUnitId INTEGER NOT NULL,
	OrderPartPrice REAL NOT NULL,
	OrderTotalCost REAL NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(OrderSupplierId) REFERENCES Supplier (id),
	FOREIGN KEY(OrderNbr) REFERENCES purchaseOrder (purchaseOrderNbr),
	FOREIGN KEY(OrderPartId) REFERENCES Part (id)
);
/*
INSERT INTO OrderTbl(OrderNbr, OrderSupplierId, OrderPartId, OrderQuantity, OrderUnitId, OrderPartPrice, OrderTotalCost)
values(1, 1, 1, 1, 1, 20.50, 20.50);
INSERT INTO OrderTbl(OrderNbr, OrderSupplierId, OrderPartId, OrderQuantity, OrderUnitId, OrderPartPrice, OrderTotalCost)
values(2, 1, 1, 1, 1, 20.50, 20.50);
INSERT INTO OrderTbl(OrderNbr, OrderSupplierId, OrderPartId, OrderQuantity, OrderUnitId, OrderPartPrice, OrderTotalCost)
values(3, 1, 1, 1, 1, 20.50, 20.50);
INSERT INTO OrderTbl(OrderNbr, OrderSupplierId, OrderPartId, OrderQuantity, OrderUnitId, OrderPartPrice, OrderTotalCost)
values(4, 1, 1, 1, 1, 20.50, 20.50);
INSERT INTO OrderTbl(OrderNbr, OrderSupplierId, OrderPartId, OrderQuantity, OrderUnitId, OrderPartPrice, OrderTotalCost)
values(5, 1, 1, 1, 1, 20.50, 20.50);
INSERT INTO OrderTbl(OrderNbr, OrderSupplierId, OrderPartId, OrderQuantity, OrderUnitId, OrderPartPrice, OrderTotalCost)
values(6, 1, 1, 1, 1, 20.50, 20.50);
INSERT INTO OrderTbl(OrderNbr, OrderSupplierId, OrderPartId, OrderQuantity, OrderUnitId, OrderPartPrice, OrderTotalCost)
values(7, 1, 1, 1, 1, 20.50, 20.50);
INSERT INTO OrderTbl(OrderNbr, OrderSupplierId, OrderPartId, OrderQuantity, OrderUnitId, OrderPartPrice, OrderTotalCost)
values(8, 1, 1, 1, 1, 20.50, 20.50);
INSERT INTO OrderTbl(OrderNbr, OrderSupplierId, OrderPartId, OrderQuantity, OrderUnitId, OrderPartPrice, OrderTotalCost)
values(9, 1, 1, 1, 1, 20.50, 20.50);
INSERT INTO OrderTbl(OrderNbr, OrderSupplierId, OrderPartId, OrderQuantity, OrderUnitId, OrderPartPrice, OrderTotalCost)
values(10, 1, 1, 1, 1, 20.50, 20.50);
*/

DROP TABLE IF EXISTS Part;
CREATE TABLE Part (
	id INTEGER NOT NULL,
	partNbr TEXT NOT NULL,
	partDesc TEXT NOT NULL,
	partSupplierId integer,
	partQuantity INTEGER NOT NULL,
	partInStock BOOLEAN NOT NULL,
	partDateCreated TEXT NOT NULL,
	PRIMARY KEY (id),
	UNIQUE ("partNbr"),
	FOREIGN KEY(partSupplierId) REFERENCES Supplier (id)
);

INSERT into Part(partNbr,PartDesc,partSupplierId,partQuantity,partInStock,partDateCreated) VALUES('A1000', 'BOLT', 1, 20, TRUE, "AUG");
INSERT into Part(partNbr,PartDesc,partSupplierId,partQuantity,partInStock,partDateCreated) VALUES('A2000', 'CHAIN', 2, 20, FALSE, "25122022");


DROP TABLE IF EXISTS PurchaseOrder;
CREATE TABLE PurchaseOrder(
id INTEGER NOT NULL,
purchaseOrderDate TEXT NOT NULL,
purchaseOrderReceivedDate TEXT,
purchaseOrderDeleteFlg BOOLEAN NOT NULL,
purchaseOrderNbr INTEGER,
purchaseOrderPurchaserId integer not null,
PRIMARY KEY (id)

);

/*
INSERT INTO PurchaseOrder(purchaseOrderDate, purchaseOrderReceivedDate, purchaseOrderDeleteFlg, purchaseOrderNbr, purchaseOrderPurchaserId)
values('02112022', '15122023', false, 1,1);
INSERT INTO PurchaseOrder(purchaseOrderDate, purchaseOrderReceivedDate, purchaseOrderDeleteFlg, purchaseOrderNbr, purchaseOrderPurchaserId)
values('01121999', '15121999', false, 2,2);
INSERT INTO PurchaseOrder(purchaseOrderDate, purchaseOrderReceivedDate, purchaseOrderDeleteFlg, purchaseOrderNbr, purchaseOrderPurchaserId)
values('01121999', '15121999', false, 3,2);
INSERT INTO PurchaseOrder(purchaseOrderDate, purchaseOrderReceivedDate, purchaseOrderDeleteFlg, purchaseOrderNbr, purchaseOrderPurchaserId)
values('01121999', '15121999', false, 4,2);
INSERT INTO PurchaseOrder(purchaseOrderDate, purchaseOrderReceivedDate, purchaseOrderDeleteFlg, purchaseOrderNbr, purchaseOrderPurchaserId)
values('01121999', '15121999', false, 5,2);
INSERT INTO PurchaseOrder(purchaseOrderDate, purchaseOrderReceivedDate, purchaseOrderDeleteFlg, purchaseOrderNbr, purchaseOrderPurchaserId)
values('01121999', '15121999', false, 6,2);
INSERT INTO PurchaseOrder(purchaseOrderDate, purchaseOrderReceivedDate, purchaseOrderDeleteFlg, purchaseOrderNbr, purchaseOrderPurchaserId)
values('01121999', '15121999', false, 7,2);
INSERT INTO PurchaseOrder(purchaseOrderDate, purchaseOrderReceivedDate, purchaseOrderDeleteFlg, purchaseOrderNbr, purchaseOrderPurchaserId)
values('01121999', '15121999', false, 8,2);
INSERT INTO PurchaseOrder(purchaseOrderDate, purchaseOrderReceivedDate, purchaseOrderDeleteFlg, purchaseOrderNbr, purchaseOrderPurchaserId)
values('01121999', '15121999', false, 9,2);
INSERT INTO PurchaseOrder(purchaseOrderDate, purchaseOrderReceivedDate, purchaseOrderDeleteFlg, purchaseOrderNbr, purchaseOrderPurchaserId)
values('01121999', '15121999', false, 10,2);

*/

DROP TABLE IF EXISTS Purchaser;
CREATE TABLE Purchaser (
	id INTEGER NOT NULL,
	purchaserName TEXT NOT NULL,
	purchaseDept TEXT NOT NULL,
	purchaserSecurityLevel INTEGER,
	purchaserActive BOOLEAN NOT NULL,
	purchaseDateCreated TEXT NOT NULL,
	PRIMARY KEY (id),
	UNIQUE (purchaserName)
);

INSERT INTO Purchaser(purchaserName, PurchaseDept, purchaserSecurityLevel, 	purchaserActive, purchaseDateCreated)
VALUES('Kevin', 'Finance', 1, true, '25122022');
INSERT INTO Purchaser(purchaserName, PurchaseDept, purchaserSecurityLevel, 	purchaserActive, purchaseDateCreated)
VALUES('Jessie', 'Finance', 5, false, '25122022');


/*
DROP TABLE IF EXISTS teacher;
CREATE TABLE teacher (
	Id INTEGER PRIMARY KEY AUTOINCREMENT,
	studentID INTEGER,
	FOREIGN KEY(studentID) REFERENCES Student (id)

);

insert into teacher(studentID) values(1);

DROP TABLE IF EXISTS Student;
CREATE TABLE Student (
	Id INTEGER NOT NULL,
	Major TEXT,
	Pass BOOLEAN,
	PRIMARY KEY (Id)
);
INSERT INTO Student(Major, Pass) VALUES('Mathematics', true);
INSERT INTO Student(Major, Pass) VALUES('Biology', true);
INSERT INTO Student(Major, Pass) VALUES('French', true);

*/

DROP TABLE IF EXISTS Supplier;
CREATE TABLE Supplier (
	id INTEGER NOT NULL,
	supplierName TEXT NOT NULL,
	supplierAddr TEXT NOT NULL,
	supplierTel TEXT NOT NULL,
	supplierEmail TEXT NOT NULL,
	supplierContact TEXT NOT NULL,
	supplierActive BOOLEAN NOT NULL,
	supplierDateCreated TEXT NOT NULL,
	PRIMARY KEY (id),
	UNIQUE (supplierAddr),
	UNIQUE (supplierTel),
	UNIQUE (supplierEmail),
	UNIQUE (supplierContact)
);

INSERT INTO Supplier(supplierName, supplierAddr, supplierTel, supplierEmail, supplierContact, supplierActive, supplierDateCreated)
values('Surgenor Trucks', '100 St. Laurent', '613-123-4567', 'supplier@email.com', 'Mr. Right', true, '25021979');
INSERT INTO Supplier(supplierName, supplierAddr, supplierTel, supplierEmail, supplierContact, supplierActive, supplierDateCreated)
values('Canadian Tire', '2 Dump Road', '613-123-4568', 'supplierx@email.com', 'Mr. Wrong', true, '28012022');


DROP TABLE IF EXISTS Unit;
CREATE TABLE Unit (
	id INTEGER NOT NULL,
	unitDesc TEXT NOT NULL,
	PRIMARY KEY (id)
);

INSERT INTO Unit(unitDesc) values('KG');
INSERT INTO Unit(unitDesc) values('POUNDS');
INSERT INTO Unit(unitDesc) values('PIECES');


DROP TABLE IF EXISTS OrderNbrTbl;
CREATE TABLE OrderNbrTbl (
	orderNbr integer NOT NULL unique

);

--insert into OrderNbrTbl values(0);


PRAGMA foreign_keys = ON;
PRAGMA foreign_keys;