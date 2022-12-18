import datetime
import sqlite3
from app import app, constants
import os


def getDatabase(dataBaseName: str) -> str:
    return(os.path.join(app.root_path, dataBaseName))


def getConnection(db:str) -> sqlite3.Connection:

    conn = None

    try:
        #database will be created if doesn't already exist
        conn = sqlite3.connect(db)
        conn.row_factory = sqlite3.Row
        print(f'Opened database successfully')

        return(conn)

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

def getUnitDesc(id:int) -> str:

    try:
        row: str = None
        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        parm=(id,)
        stmt = 'select unitDesc from unit where id = ?'
        cur.execute(stmt, parm)
        row= cur.fetchone()
        #for row in cur:
        #    print(f'row:{row}')
        print(f'row: {row[0]}')
        cur.close()
        conn.close()

        return(row[0])


    except Exception as e:
        print(f'problem in getUnitDesc: {e}')

def getUnitId(desc:str) -> int:

    try:
        row: int = None
        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        parm=(desc,)
        stmt = 'select Id from unit where unitDesc = ?'
        cur.execute(stmt, parm)
        row= cur.fetchone()
        print(f'row: {row[0]}')
        cur.close()
        conn.close()

        return(row[0])


    except Exception as e:
        print(f'problem in getUnitId: {e}')

def getALLUnitDesc() -> list:

    try:
        row: list = None
        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        stmt = 'select unitDesc from unit'
        #cur.execute('select unitDesc from unit where id = ?', parm)
        cur.execute(stmt)
        row = cur.fetchall()
        row = list(row)
        cur.close()
        conn.close()

        return(row)


    except Exception as e:
        print(f'problem in getALLUnitDesc: {e}')


def getPartId(Desc: str) -> int:

        try:
            row: int = None

            db = getDatabase(constants.DATABASE_NAME)
            conn = getConnection(db)
            cur = conn.cursor()
            parm = (Desc,)
            stmt = 'select Id from Part where partNbr = ?'
            cur.execute(stmt, parm)
            row = cur.fetchone()

            cur.close()
            conn.close()

            return (row[0])

        except Exception as e:
            print(f'problem in getPartId: {e}')

def getSupplierName(id:int) -> str:

    try:
        row: str = None
        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        parm=(id,)
        stmt = 'select supplierName from supplier where id = ?'
        #cur.execute('select unitDesc from unit where id = ?', parm)
        cur.execute(stmt, parm)
        row= cur.fetchone()
        #for row in cur:
        #    print(f'row:{row}')
        print(f'row: {row[0]}')
        cur.close()
        conn.close()
        return(row[0])


    except Exception as e:
        print(f'problem in getSupplierName: {e}')

def getPurchaserId(name: str) -> int:
    try:
        row: list = []

        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        parm=(name,)
        stmt = 'select Id from purchaser where purchaserName = ?'
        #cur.execute('select unitDesc from unit where id = ?', parm)
        cur.execute(stmt, parm)
        row = cur.fetchone()
        cur.close()
        conn.close()
        return(row[0])


    except Exception as e:
        print(f'problem in getPurchaserId: {e}')




def getSupplierId(Name: str) -> int:

    try:
        row: list = []

        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        parm=(Name,)
        stmt = 'select Id from supplier where supplierName = ?'
        #cur.execute('select unitDesc from unit where id = ?', parm)
        cur.execute(stmt, parm)
        row = cur.fetchone()
        cur.close()
        conn.close()
        return(row[0])


    except Exception as e:
        print(f'problem in getSupplierId: {e}')




def getALLSupplierName() -> list:

    try:
        row: list = []

        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        #parm=(Name,)
        stmt = 'select supplierName from supplier'
        #cur.execute('select unitDesc from unit where id = ?', parm)
        cur.execute(stmt)
        row = cur.fetchall()
        row = list(row)
        cur.close()
        conn.close()
        return(row)


    except Exception as e:
        print(f'problem in getALLSupplierName: {e}')


def getTableItemById(id:int, tableName: str, colName: str) -> str:

    try:
        row: str = None
        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        parm=(id,)
        stmt = f'select {colName} from {tableName} where id = ?'
        #cur.execute('select unitDesc from unit where id = ?', parm)
        cur.execute(stmt, parm)
        row = cur.fetchone()
        cur.close()
        conn.close()
        return(row[0])


    except Exception as e:
        print(f'problem in getTableItemById: {e}')


def insertPart(parms):

    try:
        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        supplierId = getSupplierId(parms[2])

        stmt = 'insert into Part(partNbr, partDesc, partSupplierId, partQuantity, partInStock, partDateCreated) values (?, ?, ?, ?, ?, ?)'
        cur.execute(stmt, parms)
        cur.close()
        conn.commit()
        conn.close()

        return()


    except Exception as e:
        print(f'problem in insertPart: {e}')


def getALLPartDesc() -> list:

    try:
        row: list = None

        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        stmt = 'select partDesc from part'
        cur.execute(stmt)
        row = cur.fetchall()
        row = list(row)
        cur.close()
        conn.close()

        return(row)


    except Exception as e:
        print(f'problem in getALLPartDesc: {e}')

def getALLPurchasers() -> list:

    try:
        row: list = None

        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        stmt = 'select purchaserName from purchaser'
        cur.execute(stmt)
        row = cur.fetchall()
        row = list(row)
        cur.close()
        conn.close()

        return(row)


    except Exception as e:
        print(f'problem in getALLPurchaser: {e}')

def getALLITEMS(tblName: str, colName: str) -> list:

    try:
        row: list = None

        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        #conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        stmt = f'select {colName} from {tblName}'
        cur.execute(stmt)
        row = cur.fetchall()
        mylist: list = []
        for r in row:
            mylist.append(r[0])

        cur.close()
        conn.close()
        return(mylist)

    except Exception as e:
        print(f'problem in getALLITEMS: {e}')



def getMaxOrderNbr() -> int:

    try:
        result:int  = None
        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        #conn.row_factory = sqlite3.Row
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

        return()


    except Exception as e:
        print(f'problem in insertOrder: {e}')


def insertPurchaseOrder(purchaseOrderNbr: int, purchaserId: int):
    try:
        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        cur = conn.cursor()
        orderDt = datetime.datetime.now()
        receivedDt = None
        deleteFlg = False
        parms =(orderDt, receivedDt, deleteFlg, purchaseOrderNbr, purchaserId)
        stmt = 'INSERT INTO PurchaseOrder(purchaseOrderDate, purchaseOrderReceivedDate, purchaseOrderDeleteFlg, purchaseOrderNbr, purchaseOrderpurchaserId) values (?, ?, ?, ?, ?)'
        cur.execute(stmt, parms)
        cur.close()
        conn.commit()
        conn.close()

        return()


    except Exception as e:
        print(f'problem in insertPurchaseOrder: {e}')


def getALLPurchaseOrders() -> list:

    try:
        row: list = None

        db = getDatabase(constants.DATABASE_NAME)
        conn = getConnection(db)
        #conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        stmt = 'select purchaser.purchaserName,orderNbr,s.supplierName,part.partNbr,part.partDesc,o.OrderQuantity,o.OrderPartPrice,o.OrderTotalCost from purchaseOrder p, OrderTbl o, supplier s, Part, Purchaser where p.purchaseOrderNbr = o.orderNbr AND o.OrderSupplierId = s.id and o.OrderPartId = part.id and Purchaser.id = p.purchaseOrderPurchaserId'
        cur.execute(stmt)
        row = cur.fetchall()
        mylist: list = []
        for r in row:
            mylist.append(r)

        cur.close()
        conn.close()
        return(mylist)
    except Exception as e:
        print(f'problem in getALLPurchaseOrders: {e}')


