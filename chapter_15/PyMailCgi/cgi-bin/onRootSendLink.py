"The Message Composition Page"
'''
The root page Send function steps users through two other pages: one to edit a message
and one to confirm delivery.
'''

#!/usr/bin/python
"""
################################################################################
On 'send' click in main root window: display composition page
################################################################################
"""
import commonhtml
from externs import mailconfig

commonhtml.editpage(kind='Write', headers={'From': mailconfig.myaddress})
