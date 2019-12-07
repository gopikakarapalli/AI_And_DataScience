import importlib

packages = ['pandas', 'numpy','IPython', 'statsmodels', 'sklearn', 'seaborn',
            'toolz', 'requests', 'scipy']

bad = []
for package in packages:
    try:
        importlib.import_module(package)
    except ImportError:
        bad.append("Can't import %s" % package)
else:
    if len(bad) > 0:
        print('\n'.join(bad))

