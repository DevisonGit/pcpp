import configparser

config = configparser.ConfigParser()
config.read('config_v3.ini')

sections = config.sections()
for section in sections:
    items = config.items(section)
    print(f'\n{section} section')
    for k, v in items:
        print(k, ': ', v)
