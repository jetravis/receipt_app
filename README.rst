Cart
==========

	Python script to take the information from receipt and place in database

Summary
-------

The script is apart of a larger app that allows receipts to be photographed, stored, and queried.

Links to Discussion
-------------------
MN-Slack: <jetravis@slack.com>


Quick Start
-----------
Requires that python2.7 is intalled

::
    $ pip install .
    $ ./cart 

Input
--------
	Please Enter info from receipt
	1. Store Name:  
	2. Date of Purchase(mm/dd/yy):
	3. Sales Tax:
    4. Food Item 1:
	5. Food Item 1 Cost:
	Any more items to enter? yes/no?

Output
--------
	filename: receipt.json
{
        "date": "01/01/17", 
        "items": [
            {
                "cost": 1.5, 
                "item": "apple",
            	"qty': 4
			}, 
            {
                "cost": 4.0, 
                "item": "grapes",
				'qty': 1
            }
        ], 
        "sales_tax": 0.08, 
        "store": "Target"
} 
	
Contributing
------------

Contributions to this library are always welcome and highly encouraged.

See `CONTRIBUTING`_ for more information on how to get started.

.. _CONTRIBUTING: https://github.com/GoogleCloudPlatform/gcloud-python/blob/master/CONTRIBUTING.rst

License
-------

The MIT License (MIT) - See `LICENSE`_ for more information.

.. _LICENSE: https://github.com/lwgray/PyEntrezID/blob/master/LICENSE
