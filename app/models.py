#from app import db, engine
#from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy import select
from datetime import datetime

print(f'inside models')

try:
    with engine.connect() as conn:
        #conn = engine.connect()
        metadata = db.MetaData()

        Student = db.Table('Student', metadata,
                      db.Column('Id', db.Integer(),primary_key=True),
                      db.Column('Major', db.String(255), default="Math", nullable=True),
                      db.Column('Pass', db.Boolean(), default=False, nullable=True)
                      )


#db.Column('Name', db.String(255), nullable=False),

        PurchaseOrder = db.Table('PurchaseOrder', metadata,
                                db.Column('id', db.Integer, primary_key=True, autoincrement=True),
                                db.Column('purchaserOrderDate', db.String, nullable=False),
                                db.Column('purchaseOrderRecievedDate', db.String, nullable=False),
                                db.Column('purchaseOrderDeleteFlg', db.Boolean, default=True, nullable=False),
                                db.Column('purchaseOrderPurchaserId', db.Integer, db.ForeignKey('Purchaser.id'))
                                 )

        Order = db.Table('Order', metadata,
                         db.Column('id', db.Integer, primary_key=True, autoincrement=True),
                         db.Column('purchaseOrderId', db.Integer, nullable=False),
                         db.Column('purchaseOrderSupplierId', db.Integer, db.ForeignKey('Supplier.id')),
                         db.Column('purchaseOrderPartId', db.Integer, db.ForeignKey('Part.id')),
                         db.Column('purchaseOrderQuantity', db.Integer, nullable=False),
                         db.Column('purchaseOrderUnitId', db.Integer, nullable=False),  #this will be link to units table
                         db.Column('purchaseOrderPartPrice', db.Integer, nullable=False) #this will be actual price when ordered, not a link to parts table
                         )


        Unit = db.Table('Unit', metadata,
                        db.Column('id', db.Integer, primary_key=True, autoincrement=True),
                        db.Column('unitDesc', db.String, nullable=False)
                        )

        # supplier can have many purchase orders, so one-to-many, supplier -> purchaseOrder
        Supplier = db.Table('Supplier', metadata,
                             db.Column('id', db.Integer, primary_key=True, autoincrement=True),
                             db.Column('supplierName', db.String(50), unique=True, nullable=False),
                             db.Column('supplierAddr', db.String(50), unique=True, nullable=False),
                             db.Column('supplierTel', db.String(10), unique=True, nullable=False),
                             db.Column('supplierEmail', db.String(50), unique=True, nullable=False),
                             db.Column('supplierContact', db.String(50), unique=True, nullable=False),
                             db.Column('supplierActive', db.Boolean, default=True, nullable=False),
                             db.Column('supplierDateCreated', db.String, nullable=False)
                             #db.relationship('supplierPurchaseOrder', 'PurchaseOrder', backref='supplierPurchaseOrder')
                            )



        # purchaser can have many purchase orders, so one-to-many, purchaser -> purchaseOrder
        Purchaser = db.Table('Purchaser', metadata,
                             db.Column('id', db.Integer, primary_key=True, autoincrement=True),
                             db.Column('purchaserName', db.String(50), unique=True, nullable=False),
                             db.Column('purchaseDept', db.String(50), unique=False, nullable=False),
                             db.Column('purchaserSecurityLevel', db.Integer),
                             db.Column('purchaserActive', db.Boolean, default=True, nullable=False),
                             db.Column('purchaseDateCreated', db.String, nullable=False)
                             #db.relationship('purchaserPurcherOrder', 'PurchaseOrder', backref='purchaserPurchaseOrder')
                            )

        Part= db.Table('Part', metadata,
            db.Column('id', db.Integer, primary_key=True, autoincrement=True),
            db.Column('partNbr', db.String(50), unique=True, nullable=False),
            db.Column('partDesc', db.String(50), unique=False, nullable=False),
            db.Column('partSupplier', db.String(50), unique=False, nullable=False),
            db.Column('partQuantity', db.Integer, unique=False, nullable=False),
            db.Column('partInStock', db.Boolean, default=True, nullable=False),
            db.Column('partDateCreated', db.String, nullable=False),
            db.Column('partPrice', db.Integer, nullable=False)
                       #db.relationship('partPurchaseOrder', 'PurchaseOrder', backref='partPurchaseOrder')
            )

        metadata.create_all(engine)




except Exception as e:
    print(e)


'''
if constants.DEBUG_MODE:
        db.drop_all()
    db.create_all()


    db.session.commit()
'''
