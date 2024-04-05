try:
    import abcdefgh
except ImportError as e:
    print(e)
    print(e.name)
    print(e.path)
