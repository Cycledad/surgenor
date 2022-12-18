import datetime

from app import app
from flask import render_template, request, redirect
import datetime as dt
from app import utilities
#from app import models

print(f'inside routes')

@app.route('/listPurchaseOrder')
def listPurchaseOrder():
    resultList: list
    resultList = utilities.getALLPurchaseOrders() #returns a list of a list, so indice 1 = row, indice 2 = col within row, i.e. mylist[0][1]
    print(f'len of mylist indicates number of row: {len(resultList)}')
    print(f'each row contains cols {list(resultList[0])}')
    return render_template('listPurchaseOrder.html', rowColData=resultList)







@app.route('/addRow', methods=['GET', 'POST'])
def addRow():

    try:
        if request.method == "POST":
            req = request.form
            print(f'This is a request - {req}')
            resultList = list(req.values())

            #1st update the purchaseOrder table then update the order table
            purchaseOrderNbr = resultList[0]
            purchaserId = utilities.getPurchaserId(resultList[1])
            utilities.insertPurchaseOrder(purchaseOrderNbr, purchaserId)


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
        print(e)

    orderNbr = utilities.getMaxOrderNbr() + 1

    listPurchaserName = utilities.getALLITEMS('purchaser', 'purchaserName')
    listPartDesc = utilities.getALLITEMS('part', 'partDesc')
    listPartNbr = utilities.getALLITEMS('part', 'partNbr')
    listSupplierNames = utilities.getALLITEMS('supplier', 'SupplierName')
    listUnits = utilities.getALLITEMS('UNIT', 'UnitDesc')
    return render_template('addRow.html', listPartDesc=listPartDesc, listPartNbr=listPartNbr, listPurchaserName=listPurchaserName, listSupplierNames=listSupplierNames, listUnits=listUnits, orderNbr=orderNbr)


@app.route('/part', methods=['GET', 'POST'])
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

            dtCreated = dt.datetime.now()
            inStock: bool = True if req['partInStock'] == 'YES' else False  #1=true, 0=false

            params = (req['partNbr'], req['partDesc'], req['partSupplier'], req['partQuantity'], inStock, dtCreated)
            utilities.insertPart(params)




    except Exception as e:
        print(e)

    listSupplierNames = utilities.getALLITEMS('supplier', 'SupplierName')
    listUnits = utilities.getALLITEMS('UNIT', 'UnitDesc')
    listPurchaserName = utilities.getALLITEMS('purchaser', 'purchaserName')


    return render_template('addPart.html', listSupplierNames=listSupplierNames, listUnits=listUnits, listPurchaserName=listPurchaserName)



