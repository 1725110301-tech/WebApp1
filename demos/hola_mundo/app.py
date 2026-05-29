import web

urls = (
    '/', 'Index',
    '/about', 'About',
    '/contact', 'Contact',
    '/productos', 'Productos',
    r'/producto/(\d+)', 'ProductoDetalle',
    '/login', 'Login',
    '/logout', 'Logout',
    '/registro', 'Registro',
    '/dashboard', 'Dashboard',
    '/perfil', 'Perfil',
    '/admin', 'Admin',
)

app = web.application(urls, globals())

NAV = """
<a href="/">Inicio</a> |
<a href="/about">About</a> |
<a href="/productos">Productos</a> |
<a href="/dashboard">Dashboard</a> |
<a href="/perfil">Perfil</a> |
<a href="/admin">Admin</a> |
<a href="/contact">Contacto</a> |
<a href="/login">Login</a> |
<a href="/registro">Registro</a>
<hr>
"""

def html(contenido):
    web.header('Content-Type', 'text/html; charset=utf-8')
    return contenido

class Index:
    def GET(self):
        return html(NAV + "<h1>Inicio</h1>")

class About:
    def GET(self):
        return html(NAV + "<h1>About</h1>")

class Contact:
    def GET(self):
        return html(NAV + "<h1>Contacto</h1>")

class Productos:
    def GET(self):
        return html(NAV + "<h1>Productos</h1>")

class ProductoDetalle:
    def GET(self, id):
        return html(NAV + f"<h1>Producto #{id}</h1>")

class Login:
    def GET(self):
        return html(NAV + "<h1>Login</h1>")

class Logout:
    def GET(self):
        return html(NAV + "<h1>Logout</h1>")

class Registro:
    def GET(self):
        return html(NAV + "<h1>Registro</h1>")

class Dashboard:
    def GET(self):
        return html(NAV + "<h1>Dashboard</h1>")

class Perfil:
    def GET(self):
        return html(NAV + "<h1>Perfil</h1>")

class Admin:
    def GET(self):
        return html(NAV + "<h1>Admin</h1>")

if __name__ == "__main__":
    app.run()