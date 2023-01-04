import datetime

from app import app
from flask import render_template, request, redirect
import datetime as dt
from app import utilities
import json
#from app import models

#print(f'inside routes')


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/addPurchaser', methods=['GET', 'POST'])
def addPurchaser():

    try:
        if request.method == "POST":
            req = request.form
            name = req['pName']
            active = True if req['pActive'] == 'YES' else False  # 1=true, 0=false
            deptName = req['selectDepartment']
            dateCreated = dt.date.today()
            deptId = utilities.getDepartmentId(deptName)
            parms =(name, deptId, active, dateCreated)
            utilities.insertPurchaser(parms)


    except Exception as e:
        print(f'problem in addPurchaser: {e}')

    listDeptNames = utilities.getALLDepartmentNames()
    return render_template('addPurchaser.html', listDeptNames = listDeptNames)


@app.route('/addDepartment', methods=['GET', 'POST'])
def addDepartment():

    try:
        if request.method == "POST":
            req = request.form
            deptName = req['deptName']
            active = True if req['deptActive'] == 'YES' else False  # 1=true, 0=false
            dateCreated = dt.date.today()
            parms =(deptName, active, dateCreated)
            utilities.insertDepartment(parms)


    except Exception as e:
        print(f'problem in addDepartment: {e}')

    return render_template('addDepartment.html')


@app.route('/addSupplier', methods=['GET', 'POST'])
def addSupplier():

    try:
        if request.method == "POST":
            req = request.form
            supplierName = req['supplierName']
            supplierAddr = req['supplierAddr']
            supplierContactName = req['supplierContactName']
            supplierTel = req['supplierTel']
            supplierEmail = req['supplierEmail']
            supplierActive = True
            supplierDateCreated = dt.date.today()
            parms =(supplierName, supplierAddr, supplierContactName, supplierEmail, supplierTel, supplierActive, supplierDateCreated)
            utilities.insertSupplier(parms)



    except Exception as e:
        print(f'problem in addSupplier: {e}')

    return render_template('addSupplier.html')



@app.route('/listPurchaseOrder')
def listPurchaseOrder():
    resultList: list
    resultList = utilities.getALLPurchaseOrders() #returns a list of a list, so indice 1 = row, indice 2 = col within row, i.e. mylist[0][1]
    #print(f'len of mylist indicates number of row: {len(resultList)}')
    #print(f'each row contains cols {list(resultList[0])}')
    return render_template('listPurchaseOrder.html', rowColData=resultList)







@app.route('/addOrder', methods=['GET', 'POST'])
def addOrder():

    try:
        if request.method == "POST":
            req = request.form
            print(f'This is a request - {req}')
            resultList = list(req.values())

            #1st update the purchaseOrder table then update the order table
            purchaseOrderNbr = resultList[0]
            purchaserName = resultList[1]
            aList = utilities.getPurchaserId(purchaserName)
            purchaserId = aList[0]
            purchaserDeptId = utilities.getPurchaserDeptId(purchaserName)
            utilities.insertPurchaseOrder(purchaseOrderNbr, purchaserId, purchaserDeptId)


            #resultList minus 3 gives total nbr of order items, less PONbr and purchaser
            #take total nbr of order items and divide by seven gives nbr of recs to insert

            nbrOfOrderItems = len(resultList) - 3
            nbrOfRecs = nbrOfOrderItems / 7


            j: int = 0
            k: int = 2
            #2nd update order table
            x = len(resultList)
            for i in range(2, x):
                if  (i == k):
                    j += 1
                    if j > nbrOfRecs:
                        break
                    orderNbr =  purchaseOrderNbr
                    partNbrId = utilities.getPartId(resultList[k])  #2
                    k += 2
                    supplierId = utilities.getSupplierId(resultList[k]) #4
                    k += 1
                    quantity = resultList[k] #5
                    k += 1
                    unitId = utilities.getUnitId(resultList[k]) #6
                    k += 1
                    cost = resultList[k] #7
                    k += 1
                    totalCost = resultList[k] #8
                    k += 1
                    parms = (orderNbr, partNbrId, supplierId, quantity, unitId, cost, totalCost)
                    utilities.insertOrder(parms)

            utilities.updateMaxOrderNbr(orderNbr)


    except Exception as e:
        print(f'problem in addOrder: {e}')

    orderNbr = utilities.getMaxOrderNbr() + 1

    listPurchaserName = utilities.getALLITEMS('purchaser', 'purchaserName')
    listPartDesc = utilities.getALLITEMS('part', 'partDesc')
    listPartNbr = utilities.getALLITEMS('part', 'partNbr')
    listSupplierNames = utilities.getALLITEMS('supplier', 'SupplierName')
    listUnits = utilities.getALLITEMS('UNIT', 'UnitDesc')
    return render_template('addOrder.html', listPartDesc=listPartDesc, listPartNbr=listPartNbr, listPurchaserName=listPurchaserName, listSupplierNames=listSupplierNames, listUnits=listUnits, orderNbr=orderNbr)


@app.route('/addPart', methods=['GET', 'POST'])
def part():

    try:

        if request.method == 'POST':
            req = request.form
            print(f"request: {req}")

            # ternary if statement => <expr1> if <conditional_expr> else <expr2> =>  s = 'minor' if age < 21 else 'adult'
            # inStock = 1 if req['partInStock'] == 'on' else 0  #where 1=True, 0=False
            #query = db.insert(Student).values(Id=1, Name='Matthew', Major="English", Pass=True)
            #Result = conn.execute(query)




            #stmt = "insert into Part(id, partNbr, partDesc, partQuantity, partInStock, 'partDateCreated') values ( :partNbr, :partDesc, :partQuantity, :partInStock)"
            #stmt = "insert into Part(partNbr, partDesc, partSupplier, partQuantity, partInStock, partDateCreated) values (:partNbr, :partDesc, :partSupplier, :partQuantity, :partInStock, :partDateCreated)"

            dtCreated = dt.date.today()
            inStock: bool = True if req['partInStock'] == 'YES' else False  #1=true, 0=false

            params = (req['partNbr'], req['partDesc'], req['selectSupplier'], req['partQuantity'], inStock, dtCreated)
            utilities.insertPart(params)




    except Exception as e:
        print(f'problem in addPart: {e}')

    listSupplierNames = utilities.getALLITEMS('supplier', 'SupplierName')
    listUnits = utilities.getALLITEMS('UNIT', 'UnitDesc')
    listPurchaserName = utilities.getALLITEMS('purchaser', 'purchaserName')


    return render_template('addPart.html', listSupplierNames=listSupplierNames, listUnits=listUnits, listPurchaserName=listPurchaserName)



@app.route('/testme', methods=['GET', 'POST'])
def testme2():
    return render_template('testme2.html')



@app.route('/api/data/<orderId>/<quantity>', methods=['GET'])
@app.route('/api/data/<orderId>/<dt_order_received>/<dt_order_returned>', methods=['GET']) #/api/data?orderid=1&dt=28-12-2022
@app.route('/api/data', methods=['GET'])
def data(orderId=None, dt_order_received=None, dt_order_returned=None, quantity=None):
    orderId = request.args.get('orderId')
    dt_order_received = request.args.get('dt_order_received')
    dt_order_returned = request.args.get('dt_order_returned')
    quantity = request.args.get('quantity')
    if orderId != None and (dt_order_received or dt_order_returned):
        utilities.updateOrderReceivedDate(orderId, dt_order_received, dt_order_returned)
    if orderId != None and (quantity):
        utilities.updateOrderReturnQuantity(orderId, quantity)
    resultList: list
    resultList = utilities.getALLPurchaseOrders()  # returns a list of a list, so indice 1 = row, indice 2 = col within row, i.e. mylist[0][1]
    mylist: list = []
    alist:list = []
    for row in resultList:
        alist = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13])
        d1 = dict(enumerate(alist))
        mylist.append(d1)


    #return {'data': mylist} => use this format for datatables.js, dict of lists
    return (mylist) #arry list

@app.route('/managePurchaseOrder', methods=['GET', 'POST'])
def tabulator():
    return render_template('managePurchaseOrder.html')