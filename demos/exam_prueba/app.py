import web

urls= (
    '/', 'Index',
    '/form','Formulario'
)

app= web.application(urls,globals())
render= web.template.render('views')

class Index:
    def GET(self):

        return render.index()
class Formulario:
    def GET(self):
        return render.form()
    

if __name__== '__main__':
    app.run()