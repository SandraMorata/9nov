def log(*args, **kwargs):
    prefix = kwargs.get("prefix", "LOG:")
    sep = kwargs.get("sep", " ")
    print(prefix, sep.join(map(str, args)))