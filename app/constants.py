DATABASE_NAME: str = 'mysite.db'
RELOAD_DATABASE: bool = False

#LOCAL
DOC_DIRECTORY = r'c:/users/wayne/APP/app/static/purchaseOrders/'
TEMPLATE_DIRECTORY = r'c:/users/wayne/APP/app/templates/'

#SERVER
#DOC_DIRECTORY = r'/home/wayneraid/surgenor/app/static/purchaseOrders/'
#TEMPLATE_DIRECTORY = r'/home/wayneraid/surgenor/app/templates/'

langFR = {  'home' : 'Accueil',
            'purchaseOrder' : 'Commande d''achat',
            'admin' : 'admin',
            'create' : 'créer',
            'manage' : 'débrouiller',
            'print/view purchase order' : 'imprimez/voyez l''ordre d''achat',
            'purchaser' : 'acheteur',
            'department' : 'département',
            'supplier' : 'fournisseur',
            'user' : 'utilisateur',
            'statistics' : 'statistique'

}

GOD_LEVEL = 0  # bump this up in prod

currentLang = None

# sqlite:///site.db
