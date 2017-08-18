'''Never really understood difference between *args and **kwargs so learning it here'''

def many(*args, **kwargs):
    print(args)
    print(kwargs)

many(1, 2, 3, name='Phil', job='programmer')
