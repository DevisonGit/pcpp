import shelve


shelve_name = 'first_shelve.shlv'

with shelve.open(shelve_name, flag='c') as my_shelve:
    my_shelve['EUR'] = {"code": "Euro", "symbol": "€"}
    my_shelve['GBP'] = {"code": "Pounds sterling", "symbol": "£"}
    my_shelve['USD'] = {"code": "US Dollar", "symbol": "$"}
    my_shelve['JPY'] = {"code": "Japanese yen", "symbol": '¥'}
