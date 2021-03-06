from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('main.views',
    url(r'^$', 'index', name='index'),
    url(r'^aboutccm$', 'aboutccm', name='aboutccm'),
    url(r'^aboutha$', 'aboutha', name='aboutha'),
    url(r'^aboutic$', 'aboutic', name='aboutic'),
    url(r'^aboutnvpem$', 'aboutnvpem', name='aboutnvpem'),
    url(r'^contacto$', 'contacto', name='contacto'),
    url(r'^disi$', 'disi', name='disi'),
    url(r'^diploma$', 'diploma', name='diploma'),
    url(r'^diplomanvpem$', 'diplomanvpem', name='diplomanvpem'),
    url(r'^esbi$', 'esbi', name='esbi'),
    url(r'^estudio$', 'estudio', name='estudio'),
    url(r'^eventoha$', 'eventoha', name='eventoha'),
    url(r'^familia$', 'familia', name='familia'),
    url(r'^indexcantares$', 'indexcantares', name='indexcantares'),
    url(r'^indexha$', 'indexha', name='indexha'),
    url(r'^indexnvpem$', 'indexnvpem', name='indexnvpem'),
    url(r'^mediaccm$', 'mediaccm', name='mediaccm'),
    url(r'^mediaha$', 'mediaha', name='mediaha'),
    url(r'^ministerio$', 'ministerio', name='ministerio'),
    url(r'^noticiasccm$', 'noticiasccm', name='noticiasccm'),
    url(r'^recursonvpem$', 'recursonvpem', name='recursonvpem'),
    url(r'^recursos$', 'recursos', name='recursos'),
    url(r'^seminario$', 'seminario', name='seminario'),
    url(r'^servicio$', 'servicio', name='servicio'),
    url(r'^terapia$', 'terapia', name='terapia'),
    url(r'^accounts/login/$', 'login', name='login'),
    url(r'^secre$', 'home_secre', name='home_secre'),
    url(r'^registro$', 'registro', name='registro'),
    url(r'^micuenta$', 'consultas', name='consultas'),
    url(r'^micuenta/solicitarcita$', 'addcita', name='addcita'),
    url(r'^secre/usuarios$', 'secre_usuarios', name='secre_usuarios'),
    url(r'^secre/perfil/(?P<username>[a-zA-Z0-9\\_\\.]+)/edit/$', 'edit_perfil', name='edit'),
    url(r'^agenda$', 'agenda', name='agenda'),
    url(r'^agenda/(?P<pk>\d+)/$', 'lista', name='lista'),
    url(r'^agenda/inv(?P<pk>\d+)/$', 'listainv', name='listainv'),
    url(r'^agregar/$', 'agregar'),

    #url(r'^registro/perfil/(?P<pk>\d+)$', 'edit_perfil', name='edit'),
    #url(r'^twitt/add/$', 'add_twitt', name='add_twitt'),
)
