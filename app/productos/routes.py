from . import productos
from flask import render_template
from .forms import NewProductFrom

# Crear las rutas de blueprint
@productos.route('/crear')
def crear ():
    form = NewProductFrom()
    return render_template('new.html'   ,form = form)
