import json
from datetime import date
from decimal import Decimal
import uuid
from tinydb import TinyDB


class Receipt(object):
    """ Creates a receipt from user input """
    def __init__(self):
        self._count = 0
        self._store_names = None
        self._receipt_count = 0
        self._id = self.generate_id()
        self._receipt = {'id': self._id, 'store': None, 'date':None,
                         'entry_date':date.today(), 'items':[],
                         'tax': None, 'total': None} 
        print 'Please enter info from receipt!\n'
        pass

    def get_store_name(self):
        "User enters store's name"
	store = raw_input('{0}. Store Name:  '.format(self._count))
	if not isinstance(store,str):
            print 'Store name must be a string!\n'
            self.get_store_name()
        return store

    def get_purchase_date(self):
        purchase_date = raw_input('Enter date of purchase:  ')
        return purchase_date

    def enter_items(self):
        item_name = raw_input('Enter Item\'s name:  ')
        item_qty = raw_input('Enter number of {0} purchased:  '.format(item_name))
        item_price = raw_input('Enter item cost:  ')
        self._count += 1
        self._receipt['items'].append({'name':item_name, 'qty':item_qty, 'price':item_price})
        more = raw_input('CONTINUE entering items:  yes/y or no/n ')
        more = more.lower()
        if more == 'yes' or more == 'y':
            self.enter_items()
        if more == 'no' or more == 'n':
            pass
        return
   
    def get_tax(self):
        tax = raw_input('Enter Total tax paid:  ')
        return Decimal(tax)

    def get_total(self):
        total = raw_input('Enter total cost:  ')
        return Decimal(total)
    
    def save_data(self):
        '''To be used to save receipt info to tinydb'''
        pass

    def read_data(self):
        '''To be used to read receipt info from tinydb'''
        pass
 
    def start(self):
        self._receipt['store'] = self.get_store_name() 
        self._receipt['date'] = self.get_purchase_date()
        self.enter_items()
        self._receipt['tax'] = self.get_tax()
        self._receipt['total'] = self.get_total()
        print json.dumps(self._receipt, indent=4)
        return 
        
    def generate_id(self):
        tag = uuid.uuid4()
        return tag


def run():
    bill = Receipt()
    bill.start()


if __name__ == '__main__':
    bill = Receipt()
    bill.start()
