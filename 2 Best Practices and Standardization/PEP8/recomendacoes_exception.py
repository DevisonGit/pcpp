# Quando capturar um exceção ser especifico
try:
    import my_module
except ImportError:
    my_module = None
