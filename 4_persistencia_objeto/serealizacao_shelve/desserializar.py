import shelve

shelve_name = 'first_shelve.shlv'

with shelve.open(shelve_name, flag='r') as my_shelve:
    print(my_shelve['USD'])
