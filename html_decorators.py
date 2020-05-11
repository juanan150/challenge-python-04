def div(func):
    def wrapper(*args,**kwargs):
        return f'<div>{func(*args,**kwargs)}</div>'
    return wrapper


def article(func):
    def wrapper(*args,**kwargs):
        return f'<article>{func(*args,**kwargs)}</article>'
    return wrapper


def p(func):
    def wrapper(*args,**kwargs):
        return f'<p>{func(*args,**kwargs)}</p>'
    return wrapper


# Here you must apply the decorators, uncomment this later
@div
#@article
#@p
def saludo(nombre):
    return f'¡Hola {nombre}, ¿Cómo estás?'


def run():
    print(saludo('Jorge'))


if __name__ == '__main__':
    run()

# We want to have three different outputs 👇🏼

# <div>¡Hola Jorge, ¿Cómo estás?'</div>
# <article>¡Hola Jorge, ¿Cómo estás?'</article>
# <p>¡Hola Jorge, ¿Cómo estás?'</p>
