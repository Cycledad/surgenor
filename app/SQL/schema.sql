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
	OrderReceivedDate TEXT,
	OrderReturnDate Text,
	OrderReturnQuantity integer,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY(OrderSupplierId) REFERENCES Supplier (id),
	FOREIGN KEY(OrderNbr) REFERENCES purchaseOrder (purchaseOrderNbr),
	FOREIGN KEY(OrderPartId) REFERENCES Part (id)
);
/*
INSERT INTO OrderTbl(OrderNbr, OrderSupplierId, OrderPartId, OrderQuantity, OrderUnitId, OrderPartPrice, OrderTotalCost, orderReceivedDate)
values(1, 1, 1, 1, 1, 20.50, 20.50, DATE('now'));
INSERT INTO OrderTbl(OrderNbr, OrderSupplierId, OrderPartId, OrderQuantity, OrderUnitId, OrderPartPrice, OrderTotalCost, orderReceivedDate)
values(2, 1, 1, 1, 1, 20.50, 20.50, DATE('now'));
INSERT INTO OrderTbl(OrderNbr, OrderSupplierId, OrderPartId, OrderQuantity, OrderUnitId, OrderPartPrice, OrderTotalCost, orderReceivedDate)
values(3, 1, 1, 1, 1, 20.50, 20.50, DATE('now'));
INSERT INTO OrderTbl(OrderNbr, OrderSupplierId, OrderPartId, OrderQuantity, OrderUnitId, OrderPartPrice, OrderTotalCost, orderReceivedDate)
values(4, 1, 1, 1, 1, 20.50, 20.50, DATE('now'));
INSERT INTO OrderTbl(OrderNbr, OrderSupplierId, OrderPartId, OrderQuantity, OrderUnitId, OrderPartPrice, OrderTotalCost, orderReceivedDate)
values(5, 1, 1, 1, 1, 20.50, 20.50, DATE('now'));
INSERT INTO OrderTbl(OrderNbr, OrderSupplierId, OrderPartId, OrderQuantity, OrderUnitId, OrderPartPrice, OrderTotalCost, orderReceivedDate)
values(6, 1, 1, 1, 1, 20.50, 20.50, DATE('now'));
INSERT INTO OrderTbl(OrderNbr, OrderSupplierId, OrderPartId, OrderQuantity, OrderUnitId, OrderPartPrice, OrderTotalCost, orderReceivedDate)
values(7, 1, 1, 1, 1, 20.50, 20.50, DATE('now'));
INSERT INTO OrderTbl(OrderNbr, OrderSupplierId, OrderPartId, OrderQuantity, OrderUnitId, OrderPartPrice, OrderTotalCost, orderReceivedDate)
values(8, 1, 1, 1, 1, 20.50, 20.50, DATE('now'));
INSERT INTO OrderTbl(OrderNbr, OrderSupplierId, OrderPartId, OrderQuantity, OrderUnitId, OrderPartPrice, OrderTotalCost, orderReceivedDate)
values(9, 1, 1, 1, 1, 20.50, 20.50, DATE('now'));
INSERT INTO OrderTbl(OrderNbr, OrderSupplierId, OrderPartId, OrderQuantity, OrderUnitId, OrderPartPrice, OrderTotalCost, orderReceivedDate)
values(10, 1, 1, 1, 1, 20.50, 20.50, DATE('now'));
*/

DROP TABLE IF EXISTS Part;
CREATE TABLE Part (
	id INTEGER NOT NULL,
	partNbr TEXT NOT NULL,
	partDesc TEXT NOT NULL,
	partSupplierId integer,
	partQuantity INTEGER NOT NULL,
	partInStock boolean NOT NULL,  /* boolean */
	partDateOutOfStock text,
	partDateCreated TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	UNIQUE ("partNbr"),
	FOREIGN KEY(partSupplierId) REFERENCES Supplier (id)
);
/*
INSERT into Part(partNbr,PartDesc,partSupplierId,partQuantity,partInStock,partDateCreated) VALUES('A1000', 'BOLT', 1, 20, True, "20220101");
INSERT into Part(partNbr,PartDesc,partSupplierId,partQuantity,partInStock,partDateCreated) VALUES('A2000', 'CHAIN', 2, 20, False, "25122022");
INSERT into Part(partNbr,PartDesc,partSupplierId,partQuantity,partInStock,partDateCreated) VALUES('BBBBB', 'Bottom Bracket Clamp', 2, 20, True, "25122022");
*/

DROP TABLE IF EXISTS PurchaseOrder;
CREATE TABLE PurchaseOrder(
id INTEGER NOT NULL,
purchaseOrderDate TEXT NOT NULL,
purchaseOrderReceivedDate TEXT,
purchaseOrderDeleteFlg BOOLEAN NOT NULL,
purchaseOrderDateDeleted Text,
purchaseOrderNbr INTEGER,
purchaseOrderPurchaserId integer not null,
purchaseOrderPurchaserDeptId integer not null,
PRIMARY KEY("id" AUTOINCREMENT)
);

/*
INSERT INTO PurchaseOrder(purchaseOrderDate, purchaseOrderReceivedDate, purchaseOrderDeleteFlg, purchaseOrderNbr, purchaseOrderPurchaserId,purchaseOrderPurchaserDeptId)
values('02112022', '15122023', False, 1,1,1);
INSERT INTO PurchaseOrder(purchaseOrderDate, purchaseOrderReceivedDate, purchaseOrderDeleteFlg, purchaseOrderNbr, purchaseOrderPurchaserId,purchaseOrderPurchaserDeptId)
values('01121999', '15121999', False, 2,2,1);
INSERT INTO PurchaseOrder(purchaseOrderDate, purchaseOrderReceivedDate, purchaseOrderDeleteFlg, purchaseOrderNbr, purchaseOrderPurchaserId,purchaseOrderPurchaserDeptId)
values('01121999', '15121999', False, 3,2,2);
INSERT INTO PurchaseOrder(purchaseOrderDate, purchaseOrderReceivedDate, purchaseOrderDeleteFlg, purchaseOrderNbr, purchaseOrderPurchaserId,purchaseOrderPurchaserDeptId)
values('01121999', '15121999', False, 4,2,2);
INSERT INTO PurchaseOrder(purchaseOrderDate, purchaseOrderReceivedDate, purchaseOrderDeleteFlg, purchaseOrderNbr, purchaseOrderPurchaserId,purchaseOrderPurchaserDeptId)
values('01121999', '15121999', False, 5,2,2);
INSERT INTO PurchaseOrder(purchaseOrderDate, purchaseOrderReceivedDate, purchaseOrderDeleteFlg, purchaseOrderNbr, purchaseOrderPurchaserId,purchaseOrderPurchaserDeptId)
values('01121999', '15121999', False, 6,2,1);
INSERT INTO PurchaseOrder(purchaseOrderDate, purchaseOrderReceivedDate, purchaseOrderDeleteFlg, purchaseOrderNbr, purchaseOrderPurchaserId,purchaseOrderPurchaserDeptId)
values('01121999', '15121999', False, 7,2,1);
INSERT INTO PurchaseOrder(purchaseOrderDate, purchaseOrderReceivedDate, purchaseOrderDeleteFlg, purchaseOrderNbr, purchaseOrderPurchaserId,purchaseOrderPurchaserDeptId)
values('01121999', '15121999', False, 8,2,1);
INSERT INTO PurchaseOrder(purchaseOrderDate, purchaseOrderReceivedDate, purchaseOrderDeleteFlg, purchaseOrderNbr, purchaseOrderPurchaserId,purchaseOrderPurchaserDeptId)
values('01121999', '15121999', False, 9,2,1);
INSERT INTO PurchaseOrder(purchaseOrderDate, purchaseOrderReceivedDate, purchaseOrderDeleteFlg, purchaseOrderNbr, purchaseOrderPurchaserId,purchaseOrderPurchaserDeptId)
values('01121999', '15121999', False, 10,2,1);

*/

DROP TABLE IF EXISTS Purchaser;
CREATE TABLE Purchaser (
	id INTEGER NOT NULL,
	purchaserName TEXT NOT NULL,
	purchaserDeptId integer not null,
	purchaserActive boolean NOT NULL,    /* boolean */
	purchaserDateInActive TEXT,
	purchaserDateCreated TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	UNIQUE (purchaserName)
);
/*
INSERT INTO Purchaser(purchaserName, PurchaserDeptId, purchaserActive, purchaserDateCreated)
VALUES('Kevin', 1, true, '25122022');
INSERT INTO Purchaser(purchaserName, PurchaserDeptId, purchaserActive, purchaserDateCreated)
VALUES('Jessie', 2, false, '25122022');
INSERT INTO Purchaser(purchaserName, PurchaserDeptId, purchaserActive, purchaserDateCreated)
VALUES('Wayne', 1, true, '25122022');

*/
DROP TABLE IF EXISTS Supplier;
CREATE TABLE Supplier (
	id INTEGER NOT NULL,
	supplierName TEXT NOT NULL,
	supplierAddr TEXT NOT NULL,
	supplierTel TEXT NOT NULL,
	supplierEmail TEXT NOT NULL,
	supplierContact TEXT NOT NULL,
	supplierActive boolean NOT NULL,    /* boolean */
	supplierDateInActive TEXT,
	supplierDateCreated TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
	--UNIQUE (supplierAddr),
	--UNIQUE (supplierTel),
	--UNIQUE (supplierEmail),
	--UNIQUE (supplierContact)
);
/*
INSERT INTO Supplier(supplierName, supplierAddr, supplierTel, supplierEmail, supplierContact, supplierActive, supplierDateCreated)
values('Surgenor Trucks', '100 St. Laurent', '613-123-4567', 'supplier@email.com', 'Mr. Right', true, '25021979');
INSERT INTO Supplier(supplierName, supplierAddr, supplierTel, supplierEmail, supplierContact, supplierActive, supplierDateCreated)
values('Canadian Tire', '2 Dump Road', '613-123-4568', 'supplierx@email.com', 'Mr. Wrong', true, '28012022');
INSERT INTO Supplier(supplierName, supplierAddr, supplierTel, supplierEmail, supplierContact, supplierActive, supplierDateCreated)
values('Window Max', '2 Glass Road', '613-123-4568', 'supplierx@email.com', 'Mr. Wright', true, '28012022');
*/

DROP TABLE IF EXISTS Unit;
CREATE TABLE Unit (
	id INTEGER NOT NULL,
	unitDesc TEXT NOT NULL,
	PRIMARY KEY ("id" AUTOINCREMENT)
);

INSERT INTO Unit(unitDesc) values('KG');
INSERT INTO Unit(unitDesc) values('POUNDS');
INSERT INTO Unit(unitDesc) values('PIECES');


DROP TABLE IF EXISTS OrderNbrTbl;
CREATE TABLE OrderNbrTbl (
	orderNbr integer NOT NULL unique

);

--insert into OrderNbrTbl values(0);

drop table if exists Department;
CREATE TABLE Department (
	id	INTEGER,
	deptName TEXT NOT NULL UNIQUE,
	dateCreated	INTEGER NOT NULL,
	active boolean NOT NULL,    /* boolean */
	dateInActive TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
/*
INSERT INTO Department(deptName, dateCreated, active) values('Finance', '28012022', true);
INSERT INTO Department(deptName, dateCreated, active) values('Admin', '28012022', true);
INSERT INTO Department(deptName, dateCreated, active) values('Parts', '28012022', true);
INSERT INTO Department(deptName, dateCreated, active) values('Sales', '28012022', true);
*/

drop table if exists User;
CREATE TABLE User (
	id	INTEGER,
	username	TEXT NOT NULL UNIQUE,
	password	TEXT NOT NULL UNIQUE,
	createDate	TEXT,
	active	BOOLEAN,
	dateInActive TEXT,
	securityLevel integer,
	PRIMARY KEY("id" AUTOINCREMENT));

PRAGMA foreign_keys = ON;
PRAGMA foreign_keys;