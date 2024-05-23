import requests
import sys


exit_code = 0
if len(sys.argv) not in [2, 3]:
    print('Improper number of arguments: at least one is required and not more than are allowed:'
          '\n- http serve\'s address (required)'
          '\n- port number (defaults to 80 if not specified)')
    exit_code = 1
elif len(sys.argv) > 2 and (not sys.argv[2].isdigit() or not 1 <= int(sys.argv[2]) <= 65535):
    print(f'Port number is invalid {sys.argv[2]}')
    exit_code = 2
else:
    try:
        address = sys.argv[1]
        port = sys.argv[2] if len(sys.argv) > 2 else "80"
        url = "http://" + address + ":" + port
        answer = requests.head(url)
        print(answer)
        print(answer.__dict__.get('reason'))
    except requests.exceptions.Timeout:
        print("Time out")
        exit_code = 3
    except requests.exceptions:
        print("Other Error")
        exit_code = 4

exit(exit_code)
