import configparser

config = configparser.ConfigParser()


def read_ini():
    config.read('mess.ini')
    sections = config.sections()
    return sections


def get_env(env):
    sections = read_ini()
    list_env = []
    for section in sections:
        if config[section]['env'] == env:
            section_dict = set_dict(section)
            list_env.append(section_dict)
    return list_env


def set_dict(section):
    items = config.items(section)
    dict_section = {section: dict(items)}
    return dict_section


def show_sections(env):
    for section in env:
        items = config.items(section)
        print(f'\n[{section}]')
        for k, v in items:
            if k == 'env':
                continue
            print(k, ' = ', v)


def create_ini(file, sections):
    config = configparser.ConfigParser()
    for section in sections:
        name = ''
        section_keys = section.keys()
        for section_name in section_keys:
            name = section_name
        config[name] = section.get(name)
    with open(file, 'w') as configfile:
        config.write(configfile)


prod_list = get_env('prod')
create_ini('prod_config.ini', prod_list)
dev_list = get_env('dev')
create_ini('dev_config.ini', dev_list)
