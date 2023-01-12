import datetime
import os
import random
import sqlite3
#import mammoth, webbrowser, tempfile
import requests
from urllib.parse import urljoin
#from docx2html import convert

# URL for print routine: https://www.youtube.com/watch?v=fziZXbeaegc&list=PL7QI8ORyVSCavY8MYL3dM54SviNlnEA3T&index=11
# for print routine
from pathlib import Path

from docxtpl import DocxTemplate

from app import app, constants


def getDatabase(dataBaseName: str) -> str:
    return (os.path.join(app.root_path, dataBaseName))


def getConnection(db: str) -> sqlite3.Connection:
    conn = None

    try:
        # database will be created if doesn't already exist
        conn = sqlite3.connect(db)
        # conn = sqlite3.connect(r'C:\Users\wayne\APP\app\mysite.db')

        conn.row_factory = sqlite3.Row

        return (conn)

    except Exception as e:
        print(f'Could not establish a connection with database {db}, error {e}')


def reloadDatabase():
    try:
        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        conn.row_factory = sqlite3.Row

        schema = os.path.join(app.root_path, 'SQL\schema.sql')

        with open(schema) as f:
            conn.executescript(f.read())

        conn.close()

    except Exception as e:
        print(f'problem in reloadDatabase: {e}')


def getUnitDesc(id: int) -> str:
    try:
        row: str = None
        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        parm = (id,)
        stmt = 'select unitDesc from unit where id = ?'
        cur.execute(stmt, parm)
        row = cur.fetchone()
        # for row in cur:
        #    print(f'row:{row}')
        print(f'row: {row[0]}')
        cur.close()
        conn.close()

        return (row[0])


    except Exception as e:
        print(f'problem in getUnitDesc: {e}')


def getUnitId(desc: str) -> int:
    try:
        row: int = None
        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        parm = (desc,)
        stmt = 'select Id from unit where unitDesc = ?'
        cur.execute(stmt, parm)
        row = cur.fetchone()
        print(f'row: {row[0]}')
        cur.close()
        conn.close()

        return (row[0])


    except Exception as e:
        print(f'problem in getUnitId: {e}')


def getALLUnitDesc() -> list:
    try:
        row: list = []
        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        stmt = 'select unitDesc from unit'
        # cur.execute('select unitDesc from unit where id = ?', parm)
        cur.execute(stmt)
        row = cur.fetchall()
        row = list(row)
        cur.close()
        conn.close()

        return (row)


    except Exception as e:
        print(f'problem in getALLUnitDesc: {e}')


def getPartId(Desc: str) -> int:
    try:
        row: list = []

        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        parm = (Desc,)
        stmt = 'select Id from Part where partNbr = ? and partInStock is True'
        cur.execute(stmt, parm)
        row = cur.fetchone()

        cur.close()
        conn.close()

        return (row[0])

    except Exception as e:
        print(f'problem in getPartId: {e}')


def updatePurchaser(id: int, purchaserName: str, purchaserDeptId: int, purchaserActive: bool,
                    purchaserDateInActive: str, purchaserDateCreated: str) -> None:
    try:
        # soft delete
        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        parms = (purchaserName, purchaserDeptId, purchaserActive, purchaserDateInActive, purchaserDateCreated, id,)
        stmt = 'update Purchaser set purchaserName = ?, purchaserDeptId = ?, purchaserActive = ?, purchaserDateInActive = ?, purchaserDateCreated = ? where id = ?'
        cur.execute(stmt, parms)
        cur.close()
        conn.commit()
        conn.close()

        return ()

    except Exception as e:
        print(f'problem in updatePurchaser: {e}')


def updateParts(id: int, partNbr: int, partDesc: str, partSupplierId: int, partQuantity: int, partInStock: bool,
                partDateOutOfStock: str, partDateCreated: str):
    try:
        # soft delete
        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        parms = (partNbr, partDesc, partSupplierId, partQuantity, partInStock, partDateOutOfStock, partDateCreated, id,)
        stmt = 'update Part set partNbr = ?, partDesc = ?, partSupplierId = ?, partQuantity = ?, partInStock = ?, partDateOutOfStock = ?, partDateCreated = ? where id = ?'
        cur.execute(stmt, parms)
        cur.close()
        conn.commit()
        conn.close()

        return ()

    except Exception as e:
        print(f'problem in updateParts: {e}')


def updateSupplier(id: int, supplierName: str, supplierAddr: str, supplierTel: str, supplierEmail: str,
                   supplierContact: str, supplierActive: bool, supplierDateInActive: str,
                   supplierDateCreated: str) -> None:
    try:
        # soft delete
        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        parms = (
        supplierName, supplierAddr, supplierTel, supplierEmail, supplierContact, supplierActive, supplierDateInActive,
        supplierDateCreated, id,)
        stmt = 'update Supplier set supplierName = ?, supplierAddr = ?, supplierTel = ?, supplierEmail = ?, supplierContact = ?, supplierActive = ?, supplierDateInActive = ?, supplierDateCreated = ? where id = ?'
        cur.execute(stmt, parms)
        cur.close()
        conn.commit()
        conn.close()

        return ()


    except Exception as e:
        print(f'problem in updateSupplier: {e}')


def updateUser(id: int, username: str, password: str, createDate: str, active: bool, dateInactive: str,
               securityLevel: int) -> None:
    try:
        # soft delete
        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        parms = (username, password, createDate, active, dateInactive, securityLevel, id,)
        stmt = 'update User set username = ?, password = ?, createDate = ?, active = ?, dateInactive = ?, securityLevel = ? where id = ?'
        cur.execute(stmt, parms)
        cur.close()
        conn.commit()
        conn.close()

        return ()


    except Exception as e:
        print(f'problem in updateUser: {e}')


def getSupplierName(id: int) -> str:
    try:
        row: list = []
        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        parm = (id,)
        stmt = 'select supplierName from supplier where id = ? and supplierActive is True'
        # cur.execute('select unitDesc from unit where id = ?', parm)
        cur.execute(stmt, parm)
        row = cur.fetchone()
        # for row in cur:
        #    print(f'row:{row}')
        print(f'row: {row[0]}')
        cur.close()
        conn.close()
        return (row[0])


    except Exception as e:
        print(f'problem in getSupplierName: {e}')


def insertPurchaser(parms):
    try:
        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        stmt = 'INSERT INTO Purchaser (purchaserName, purchaserDeptId, purchaserActive, purchaserDateCreated) values (?, ?, ?, ?)'
        cur.execute(stmt, parms)
        cur.close()
        conn.commit()
        conn.close()

        return ()


    except Exception as e:
        print(f'problem in insertPurchaser: {e}')


def getPurchaserId(name: str) -> int:
    try:
        row: list = []

        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        parm = (name,)
        stmt = 'select Id from purchaser where purchaserName = ? and purchaserActive is True'
        # cur.execute('select unitDesc from unit where id = ?', parm)
        cur.execute(stmt, parm)
        row = cur.fetchone()
        cur.close()
        conn.close()
        return (row[0])


    except Exception as e:
        print(f'problem in getPurchaserId: {e}')


def getPurchaserDeptId(purchaserName: str) -> int:
    try:
        row: list = []

        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        parm = (purchaserName,)
        stmt = 'select purchaserDeptId from purchaser where purchaserName = ? and purchaserActive is True'
        # cur.execute('select unitDesc from unit where id = ?', parm)
        cur.execute(stmt, parm)
        row = cur.fetchone()
        cur.close()
        conn.close()
        return (row[0])


    except Exception as e:
        print(f'problem in getPurchaserId: {e}')


def getSupplierId(Name: str) -> int:
    try:
        row: list = []

        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        parm = (Name,)
        stmt = 'select Id from supplier where supplierName = ? and supplierActive is True'
        # cur.execute('select unitDesc from unit where id = ?', parm)
        cur.execute(stmt, parm)
        row = cur.fetchone()
        cur.close()
        conn.close()
        return (row[0])


    except Exception as e:
        print(f'problem in getSupplierId: {e}')


def getALLSupplierName() -> list:
    try:
        row: list = []
        myList: list = []

        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        # parm=(Name,)
        stmt = 'select distinct supplierName from supplier where supplierActive is True'
        # cur.execute('select unitDesc from unit where id = ?', parm)
        cur.execute(stmt)
        row = cur.fetchall()
        for r in row:
            myList.append(r[0])
        cur.close()
        conn.close()
        return (myList)


    except Exception as e:
        print(f'problem in getALLSupplierName: {e}')


def insertSupplier(parms):
    try:
        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        stmt = 'INSERT INTO supplier (supplierName, supplierAddr, supplierContact, supplierEmail, supplierTel, supplierActive, supplierDateCreated) values (?, ?, ?, ?, ?, ?, ?)'
        cur.execute(stmt, parms)
        cur.close()
        conn.commit()
        conn.close()

        return ()


    except Exception as e:
        print(f'problem in insertSupplier: {e}')


def insertDepartment(parms) -> None:
    try:
        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        stmt = 'INSERT INTO Department (deptName, active, dateCreated) values (?, ?, ?)'
        cur.execute(stmt, parms)
        cur.close()
        conn.commit()
        conn.close()

        return ()


    except Exception as e:
        print(f'problem in insertDepartment: {e}')


def deleteDepartment(id: int) -> None:
    try:
        # soft delete
        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        dt = datetime.date.today()
        parms = (dt, id,)
        stmt = 'update Department set active = False, dateInActive = ? where id = ?'
        cur.execute(stmt, parms)
        cur.close()
        conn.commit()
        conn.close()

        return ()


    except Exception as e:
        print(f'problem in deleteDepartment: {e}')


def updateDepartment(id: int, dept: str, dateCreated: str, active: bool, dateInActive: str) -> None:
    try:

        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        parms = (dept, dateCreated, active, dateInActive, id,)
        stmt = 'update Department set deptName = ?, dateCreated = ?, active = ?, dateInActive = ? where id = ?'
        cur.execute(stmt, parms)
        cur.close()
        conn.commit()
        conn.close()

        return ()


    except Exception as e:
        print(f'problem in updateDepartment: {e}')


def getDepartmentId(deptName: str) -> int:
    try:
        id: list = []
        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        parm = (deptName,)
        stmt = 'select Id from department where deptName = ? and active is True'
        cur.execute(stmt, parm)
        id = cur.fetchone()
        cur.close()
        conn.commit()
        conn.close()

        return (id[0])


    except Exception as e:
        print(f'problem in getDepartmentId: {e}')


def getALLDepartmentNames() -> list:
    try:
        row: list = []
        myList: list = []

        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        stmt = 'select deptName from Department where active is True'
        cur.execute(stmt)
        row = cur.fetchall()
        for r in row:
            myList.append(r[0])
        cur.close()
        conn.close()

        return (myList)


    except Exception as e:
        print(f'problem in getALLDepartmentNames: {e}')


def getTableItemById(id: int, tableName: str, colName: str) -> str:
    try:
        row: list = []
        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        parm = (id,)
        stmt = f'select {colName} from {tableName} where id = ?'
        # cur.execute('select unitDesc from unit where id = ?', parm)
        cur.execute(stmt, parm)
        row = cur.fetchone()
        cur.close()
        conn.close()
        return (row[0])


    except Exception as e:
        print(f'problem in getTableItemById: {e}')


def insertPart(parms) -> None:
    try:
        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        supplierName = parms[2]
        # supplierId = getSupplierId(supplierName)

        stmt = 'insert into Part(partNbr, partDesc, partSupplierId, partQuantity, partInStock, partDateCreated) values (?, ?, ?, ?, ?, ?)'
        cur.execute(stmt, parms)
        cur.close()
        conn.commit()
        conn.close()

        return ()


    except Exception as e:
        print(f'problem in insertPart: {e}')


def getALLPartDesc() -> list:
    try:
        row: list = []
        myList: list = []

        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        stmt = 'select partDesc from part where partInStock is True'
        cur.execute(stmt)
        row = cur.fetchall()
        for r in row:
            myList.append(r[0])
        cur.close()
        conn.close()

        return (myList)


    except Exception as e:
        print(f'problem in getALLPartDesc: {e}')


def getALLPartNbr() -> list:
    try:
        row: list = []
        myList: list = []

        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        stmt = 'select partNbr from part where partInStock is True'
        cur.execute(stmt)
        row = cur.fetchall()
        for r in row:
            myList.append(r[0])
        cur.close()
        conn.close()

        return (myList)


    except Exception as e:
        print(f'problem in getALLPartDesc: {e}')


def getALLPurchasers() -> list:
    try:
        row: list = []
        myList: list = []

        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        stmt = 'select purchaserName from purchaser where purchaserActive is True'
        cur.execute(stmt)
        row = cur.fetchall()
        for r in row:
            myList.append(r[0])
        cur.close()
        conn.close()

        return (myList)


    except Exception as e:
        print(f'problem in getALLPurchaser: {e}')


def getALLITEMS(tblName: str, colName: str) -> list:
    try:
        row: list = []
        mylist: list = []

        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        # conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        stmt = f'select {colName} from {tblName}'
        cur.execute(stmt)
        row = cur.fetchall()
        for r in row:
            mylist.append(r[0])

        cur.close()
        conn.close()
        return (mylist)

    except Exception as e:
        print(f'problem in getALLITEMS: {e}')


def getMaxOrderNbr() -> int:
    try:
        result: int = None
        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        # conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        stmt = f'select max(orderNbr) from OrderNbrTbl'
        cur.execute(stmt)
        row = cur.fetchone()

        result = row[0]
        if row[0] == None:
            result = 0

        cur.close()
        conn.close()

        return (result)


    except Exception as e:
        print(f'problem in getMaxOrderNbr: {e}')


def updateMaxOrderNbr(orderNbr: int):
    try:
        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()

        parm = (orderNbr,)
        if int(orderNbr) > 1:
            stmt = f'update OrderNbrTbl set orderNbr = ?'
        else:
            stmt = f'insert into OrderNbrTbl values(?)'

        cur.execute(stmt, parm)
        cur.close()
        conn.commit()
        conn.close()

        return ()


    except Exception as e:
        print(f'problem in updateMaxOrderNbr: {e}')


def insertOrder(parms):
    try:
        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        stmt = 'INSERT INTO OrderTbl(OrderNbr, OrderSupplierId, OrderPartId, OrderQuantity, OrderUnitId, OrderPartPrice, orderTotalCost) values (?, ?, ?, ?, ?, ?, ?)'
        cur.execute(stmt, parms)
        cur.close()
        conn.commit()
        conn.close()

        return ()


    except Exception as e:
        print(f'problem in insertOrder: {e}')


def insertPurchaseOrder(purchaseOrderNbr: int, purchaserId: int, purchaserDept: int) -> None:
    try:
        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        orderDt = datetime.date.today()
        receivedDt = ''
        deleteFlg = False
        parms = (orderDt, receivedDt, deleteFlg, purchaseOrderNbr, purchaserId, purchaserDept)
        stmt = 'INSERT INTO PurchaseOrder(purchaseOrderDate, purchaseOrderReceivedDate, purchaseOrderDeleteFlg, purchaseOrderNbr, purchaseOrderpurchaserId, purchaseOrderPurchaserDeptId) values (?, ?, ?, ?, ?, ?)'
        cur.execute(stmt, parms)
        cur.close()
        conn.commit()
        conn.close()

        return ()


    except Exception as e:
        print(f'problem in insertPurchaseOrder: {e}')


def getALLPurchaseOrders() -> list:
    try:
        row: list = []

        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        # conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        stmt = 'select p.id, o.id, purchaser.purchaserName, deptName, orderNbr,s.supplierName,part.partNbr,part.partDesc,o.OrderQuantity,o.OrderPartPrice,o.OrderTotalCost, o.orderReceivedDate, o.OrderReceivedBy, o.orderReturnDate, o.orderReturnQuantity from purchaseOrder p, OrderTbl o, supplier s, Part, Purchaser, Department where p.purchaseOrderNbr = o.orderNbr AND o.OrderSupplierId = s.id and o.OrderPartId = part.id and Purchaser.id = p.purchaseOrderPurchaserId and purchaserDeptid = department.id'
        cur.execute(stmt)
        row = cur.fetchall()
        cur.close()
        conn.close()
        return (row)

    except Exception as e:
        print(f'problem in getALLPurchaseOrders: {e}')


def deletePurchaseOrder(id: int) -> list:
    # There is ONE purchaseOrder id used to track orders.
    # there can be MANY orders per purchaseOrder
    try:

        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        parm1 = (id,)
        stmt1 = 'select o.OrderNbr from orderTbl o where o.id = ?'
        cur.execute(stmt1, parm1)
        orderNbr = cur.fetchone()
        orderNbr = orderNbr[0]

        parm2 = (orderNbr,)
        stmt2 = 'select count(*) from orderTbl o where o.orderNbr = ?'
        cur.execute(stmt2, parm2)
        nbrOfOrders = cur.fetchone()
        nbrOfOrders = nbrOfOrders[0]

        # if NbrOfOrders = 1 then delete from order table and purchaseOrder table
        # if NbrOfOrders > 1 then delete only specific purchase form purchaseorder, other purchases remain in order

        stmt3 = 'delete from orderTbl where orderTbl.id = ?'
        cur.execute(stmt3, parm1)
        cur.fetchone()

        if nbrOfOrders == 1:
            stmt4 = 'delete from purchaseOrder where purchaseOrder.purchaserOrderNbr = ?'
            cur.execute(stmt3, parm2)
            cur.fetchone()

        cur.close()
        conn.commit()
        conn.close()

        return ()

    except Exception as e:
        print(f'problem in deletePurchaseOrder: {e}')


def updateOrderReceivedDate(id: int, dt_order_received: str, dt_order_returned: str) -> None:
    # There is ONE purchaseOrder id used to track orders.
    # there can be MANY orders per purchaseOrder
    try:

        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        parm1 = (id,)
        stmt1 = 'select o.OrderNbr from orderTbl o where o.id = ?'
        cur.execute(stmt1, parm1)
        orderNbr = cur.fetchone()
        orderNbr = orderNbr[0]

        parm2 = (orderNbr,)
        stmt2 = 'select count(*) from orderTbl o where o.orderNbr = ?'
        cur.execute(stmt2, parm2)
        nbrOfOrders = cur.fetchone()
        nbrOfOrders = nbrOfOrders[0]

        # if NbrOfOrders = 1 then delete from order table and purchaseOrder table
        # if NbrOfOrders > 1 then delete only specific purchase form purchaseorder, other purchases remain in order

        # currentDate = datetime.date.today()
        stmt1 = f"update orderTbl set orderreceivedDate = '{dt_order_received}', orderReturndate = '{dt_order_returned}' where id = ?"
        cur.execute(stmt1, parm1)
        conn.commit()

        if nbrOfOrders == 1:
            stmt3 = f"update purchaseOrder set purchaseOrderReceivedDate = '{dt_order_received}' where purchaseOrderNbr = ?"
            cur.execute(stmt3, parm2)

        cur.close()
        conn.commit()
        conn.close()

        return ()

    except Exception as e:
        print(f'problem in updateOrderReceivedDate: {e}')


def updateOrderReturnQuantity(id: int, quantity: int) -> None:
    # There is ONE purchaseOrder id used to track orders.
    # there can be MANY orders per purchaseOrder
    try:

        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        parm = (quantity, id,)
        stmt = "update orderTbl set orderReturnQuantity = ? where id = ?"
        cur.execute(stmt, parm)
        conn.commit()
        cur.close()

        return ()

    except Exception as e:
        print(f'problem in updateOrderQuantity: {e}')


def updateOrderReceivedBy(parms) -> None:
    # There is ONE purchaseOrder id used to track orders.
    # there can be MANY orders per purchaseOrder
    try:

        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        stmt = "update orderTbl set orderReceivedBy = ? where id = ?"
        cur.execute(stmt, parms)
        conn.commit()
        cur.close()

        return ()

    except Exception as e:
        print(f'problem in updateOrderReceivedBy: {e}')


def registerUser(username: str, hashed_pw: int) -> None:
    try:

        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        createdate = datetime.date.today()
        active = True
        securityLevel = 0
        parm = (username, hashed_pw, createdate, active, securityLevel)
        stmt = "insert into user (username, password, createDate, active, securityLevel) values(?, ?, ?, ?, ?)"
        cur.execute(stmt, parm)
        conn.commit()
        cur.close()

        return ()

    except Exception as e:
        print(f'problem in updateOrderQuantity: {e}')


def getPassword(username: str) -> str:
    try:

        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        parm = (username,)
        stmt = "select password from user where username = ? and active is True"
        cur.execute(stmt, parm)
        pw = cur.fetchone()

        cur.close()

        return (pw[0])

    except Exception as e:
        print(f'problem in getPassword: {e}')


def getUserSecurityLevel(username: str) -> int:
    try:

        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        parm = (username,)
        stmt = "select securityLevel from user where username = ? and active is True"
        cur.execute(stmt, parm)
        level = cur.fetchone()
        conn.commit()
        cur.close()

        return (level[0])

    except Exception as e:
        print(f'problem in getUserSecurityLevel: {e}')


def getUserRegistered(username: str) -> bool:
    try:
        exists: bool = False
        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        parm = (username,)
        stmt = "select username from user where username = ? and active is True"
        cur.execute(stmt, parm)
        user = cur.fetchone()
        conn.commit()
        cur.close()
        if user != None:
            exists = True

        return (exists)

    except Exception as e:
        print(f'problem in getUserRegistered: {e}')


def getTable(tableName: str) -> list:
    try:

        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        parm = (tableName,)
        stmt = f"select * from {tableName}"
        cur.execute(stmt)
        rows = cur.fetchall()
        rows = list(rows)
        conn.commit()
        cur.close()
        return (rows)

    except Exception as e:
        print(f'problem in getTable: {e}')


def printPurchaseOrder(orderList: list) -> None:
    # https://nagasudhir.blogspot.com/2021/10/docxtpl-python-library-for-creating.html

    try:
        myList: list = []
        previousSupplierId = orderList[0][2]

        for order in orderList:

            supplierId = order[2]

            if previousSupplierId != supplierId:
                r = random.randint(0, 1000000)
                DocName = 'generatedDoc_' + str(r) + '.docx'
                printDoc('purchaseOrderTemplate.docx', DocName, myList, order, previousSupplierId)
                myList = []
                myList = buildDoc(order, myList)
                previousSupplierId = supplierId
            else:
                myList = buildDoc(order, myList)

        r = random.randint(0, 1000000)
        DocName = 'generatedDoc_' + str(r) + '.docx'
        printDoc('purchaseOrderTemplate.docx', DocName, myList, order, previousSupplierId)


    except Exception as e:
        print(f'problem in printPurchaseOrder: {e}')


def buildDoc(order, myList: list) -> list:
    partDesc = getTableItemById(order[3], 'Part', 'partDesc')
    orderQuantity = order[4]
    orderPartPrice = order[6]
    myList.append({'orderQuantity': orderQuantity, 'orderPartPrice': orderPartPrice, 'partDesc': partDesc})
    return (myList)


def printDoc(templateName: str, docName: str, myList: list, order, supplierId: int) -> None:
    try:
        docPath = Path(__file__).parent / templateName
        doc = DocxTemplate(docPath)

        # these are common to all rows in the order
        purchaseOrderId = order[1]
        purchaseOrderDate = getTableItemById(purchaseOrderId, 'PurchaseOrder', 'purchaseOrderDate')
        PONbr = purchaseOrderId
        supplierName = getSupplierName(supplierId)
        supplierAddr = getTableItemById(supplierId, 'Supplier', 'supplierAddr')
        receivedBy = order[9]

        # https://nagasudhir.blogspot.com/2021/10/docxtpl-python-library-for-creating.html

        context = {'supplierName': supplierName,
                   'supplierAddr': supplierAddr,
                   'receivedBy': receivedBy,
                   'purchaseOrderDate': purchaseOrderDate,
                   'PONbr': PONbr,
                   'items': myList
                   }

        doc.render(context)
        doc.save(Path(__file__).parent / docName)

        myDoc= Path(__file__).parent / docName

        #downloadDocToLocalHost(docName)


    except Exception as e:
        print(f'problem in printDoc: {e}')



def downloadDocToLocalHost(docName: str) -> None:
    try:
        #import requests
        username = 'wayneraid'
        api_token = '26351fda9e41892c159e6ddfb5b4bda44e2a88f1'
        host = 'www.pythonanywhere.com'
        api_base = "https://{host}/api/v0/user/{username}/".format(
            host=host,
            username=username,
        )

        resp = requests.get(
            urljoin(api_base, "files/path/home/{username}/surgenor/app/{docName}".format(username=username, docName=docName)),
            headers={"Authorization": "Token {api_token}".format(api_token=api_token)})


        #response = requests.get(
        #      'https://{host}/api/v0/user/{username}/files/{path}'.format(
        #          host=host, username=username
        #      ),
        #      headers={'Authorization': 'Token {token}'.format(token=token)}
        #  )


        if resp.status_code == 200:
            print('saving file:')
            print(resp.content)
            with open(docName, mode='wb') as localfile:
                localfile.write(resp.content)
        else:
            print('Got unexpected status code {}: {!r}'.format(resp.status_code, resp.content))

    except Exception as e:
        print(f'problem in printDoc: {e}')

def getPurchaseOrderById(orderId: int) -> list:
    try:
        myList = []
        row = []
        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        parm = (orderId,)
        stmt = "select * from PurchaseOrder where id = ? and purchaseOrderDeleteFlg = False"
        cur.execute(stmt, parm)
        row = cur.fetchone()
        conn.commit()
        cur.close()
        for i in len(row):
            myList.append(row[i])

        return (myList)

    except Exception as e:
        print(f'problem in getPurchaseOrderById: {e}')


'''
purchaseOrderDate  
purchaseOrderReceivedDate  
purchaseOrderDeleteFlg  
purchaseOrderDateDeleted  
purchaseOrderNbr  
purchaseOrderPurchaserId  
purchaseOrderPurchaserDeptId
'''


def getOrderById(orderId: int) -> list:
    try:
        myList = []
        row = []
        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        parm = (orderId,)
        stmt = "select * from OrderTbl where orderNbr = ? order by orderSupplierId asc"
        cur.execute(stmt, parm)
        rows = cur.fetchall()
        conn.commit()
        cur.close()
        for row in rows:
            myList.append(row)

        return (myList)  # myList[0][3]

    except Exception as e:
        print(f'problem in getPurchaseOrderById: {e}')
