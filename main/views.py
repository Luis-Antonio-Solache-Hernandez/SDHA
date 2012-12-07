from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.template.context import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from models import *
from forms import *


def index(request):
    accedio = False
    secre = False
    if request.user.is_authenticated():
        accedio = True
    if request.user.has_perm('main.perm_secre'):
        secre = True
    return render_to_response('index.html', {
        'accedio': accedio,
        'secre': secre,
        }, RequestContext(request))


def aboutccm(request):
    accedio = False
    secre = False
    if request.user.is_authenticated():
        accedio = True
    if request.user.has_perm('main.perm_secre'):
        secre = True
    return render_to_response('aboutccm.html', {
        'accedio': accedio,
        'secre': secre,
        }, RequestContext(request))


def aboutha(request):
    accedio = False
    secre = False
    if request.user.is_authenticated():
        accedio = True
    if request.user.has_perm('main.perm_secre'):
        secre = True
    return render_to_response('aboutha.html', {
        'accedio': accedio,
        'secre': secre,
        }, RequestContext(request))


def aboutic(request):
    accedio = False
    secre = False
    if request.user.is_authenticated():
        accedio = True
    if request.user.has_perm('main.perm_secre'):
        secre = True
    return render_to_response('aboutic.html', {
        'accedio': accedio,
        'secre': secre,
        }, RequestContext(request))


def aboutnvpem(request):
    accedio = False
    secre = False
    if request.user.is_authenticated():
        accedio = True
    if request.user.has_perm('main.perm_secre'):
        secre = True
    return render_to_response('aboutnvpem.html', {
        'accedio': accedio,
        'secre': secre,
        }, RequestContext(request))


def contacto(request):
    accedio = False
    secre = False
    if request.user.is_authenticated():
        accedio = True
    if request.user.has_perm('main.perm_secre'):
        secre = True
    return render_to_response('contacto.html', {
        'accedio': accedio,
        'secre': secre,
        }, RequestContext(request))


def disi(request):
    accedio = False
    secre = False
    if request.user.is_authenticated():
        accedio = True
    if request.user.has_perm('main.perm_secre'):
        secre = True
    return render_to_response('disi.html', {
        'accedio': accedio,
        'secre': secre,
        }, RequestContext(request))


def diploma(request):
    accedio = False
    secre = False
    if request.user.is_authenticated():
        accedio = True
    if request.user.has_perm('main.perm_secre'):
        secre = True
    return render_to_response('diploma.html', {
        'accedio': accedio,
        'secre': secre,
        }, RequestContext(request))


def diplomanvpem(request):
    accedio = False
    secre = False
    if request.user.is_authenticated():
        accedio = True
    if request.user.has_perm('main.perm_secre'):
        secre = True
    return render_to_response('diplomanvpem.html', {
        'accedio': accedio,
        'secre': secre,
        }, RequestContext(request))


def esbi(request):
    accedio = False
    secre = False
    if request.user.is_authenticated():
        accedio = True
    if request.user.has_perm('main.perm_secre'):
        secre = True
    return render_to_response('esbi.html', {
        'accedio': accedio,
        'secre': secre,
        }, RequestContext(request))


def estudio(request):
    accedio = False
    secre = False
    if request.user.is_authenticated():
        accedio = True
    if request.user.has_perm('main.perm_secre'):
        secre = True
    return render_to_response('estudio.html', {
        'accedio': accedio,
        'secre': secre,
        }, RequestContext(request))


def eventoha(request):
    accedio = False
    secre = False
    if request.user.is_authenticated():
        accedio = True
    if request.user.has_perm('main.perm_secre'):
        secre = True
    return render_to_response('eventoha.html', {
        'accedio': accedio,
        'secre': secre,
        }, RequestContext(request))


def familia(request):
    accedio = False
    secre = False
    if request.user.is_authenticated():
        accedio = True
    if request.user.has_perm('main.perm_secre'):
        secre = True
    return render_to_response('familia.html', {
        'accedio': accedio,
        'secre': secre,
        }, RequestContext(request))


def indexcantares(request):
    accedio = False
    secre = False
    if request.user.is_authenticated():
        accedio = True
    if request.user.has_perm('main.perm_secre'):
        secre = True
    return render_to_response('indexcantares.html', {
        'accedio': accedio,
        'secre': secre,
        }, RequestContext(request))


def indexha(request):
    accedio = False
    secre = False
    if request.user.is_authenticated():
        accedio = True
    if request.user.has_perm('main.perm_secre'):
        secre = True
    return render_to_response('indexha.html', {
        'accedio': accedio,
        'secre': secre,
        }, RequestContext(request))


def indexnvpem(request):
    accedio = False
    secre = False
    if request.user.is_authenticated():
        accedio = True
    if request.user.has_perm('main.perm_secre'):
        secre = True
    return render_to_response('indexnvpem.html', {
        'accedio': accedio,
        'secre': secre,
        }, RequestContext(request))


def mediaccm(request):
    accedio = False
    secre = False
    if request.user.is_authenticated():
        accedio = True
    if request.user.has_perm('main.perm_secre'):
        secre = True
    return render_to_response('mediaccm.html', {
        'accedio': accedio,
        'secre': secre,
        }, RequestContext(request))


def mediaha(request):
    accedio = False
    secre = False
    if request.user.is_authenticated():
        accedio = True
    if request.user.has_perm('main.perm_secre'):
        secre = True
    return render_to_response('mediaha.html', {
        'accedio': accedio,
        'secre': secre,
        }, RequestContext(request))


def ministerio(request):
    accedio = False
    secre = False
    if request.user.is_authenticated():
        accedio = True
    if request.user.has_perm('main.perm_secre'):
        secre = True
    return render_to_response('ministerio.html', {
        'accedio': accedio,
        'secre': secre,
        }, RequestContext(request))


def noticiasccm(request):
    accedio = False
    secre = False
    if request.user.is_authenticated():
        accedio = True
    if request.user.has_perm('main.perm_secre'):
        secre = True
    return render_to_response('noticiasccm.html', {
        'accedio': accedio,
        'secre': secre,
        }, RequestContext(request))


def recursonvpem(request):
    accedio = False
    secre = False
    if request.user.is_authenticated():
        accedio = True
    if request.user.has_perm('main.perm_secre'):
        secre = True
    return render_to_response('recursonvpem.html', {
        'accedio': accedio,
        'secre': secre,
        }, RequestContext(request))


def recursos(request):
    accedio = False
    secre = False
    if request.user.is_authenticated():
        accedio = True
    if request.user.has_perm('main.perm_secre'):
        secre = True
    return render_to_response('recursos.html', {
        'accedio': accedio,
        'secre': secre,
        }, RequestContext(request))


def seminario(request):
    accedio = False
    secre = False
    if request.user.is_authenticated():
        accedio = True
    if request.user.has_perm('main.perm_secre'):
        secre = True
    return render_to_response('seminario.html', {
        'accedio': accedio,
        'secre': secre,
        }, RequestContext(request))


def servicio(request):
    accedio = False
    secre = False
    if request.user.is_authenticated():
        accedio = True
    if request.user.has_perm('main.perm_secre'):
        secre = True
    return render_to_response('servicio.html', {
        'accedio': accedio,
        'secre': secre,
        }, RequestContext(request))


def terapia(request):
    accedio = False
    secre = False
    if request.user.is_authenticated():
        accedio = True
    if request.user.has_perm('main.perm_secre'):
        secre = True
    return render_to_response('terapia.html', {
        'accedio': accedio,
        'secre': secre,
        }, RequestContext(request))


def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        username = request.POST['username']
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                menerror = 'No te haz registrado, por favor registrate'
                return render_to_response('login.html', {
        'form': form, 'menerror': menerror,
        }, RequestContext(request))
        password = request.POST['password']
        user = auth.authenticate(username=user.username, password=password)
        form = AuthenticationForm(None, request.POST)
        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect('index')
    return render_to_response('login.html', {
        'form': form,
        }, RequestContext(request))


@login_required
def addcita(request):
    admin = User.objects.get(username="admin")
    percon = Perfil.objects.get(user=admin)
    perfil = Perfil.objects.get(user=request.user)
    cita = Consulta(tpx=perfil, consultor=percon,)
    form = ConsultaForm(instance=cita)
    if request.method == 'POST':
        form = ConsultaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            return redirect('consultas')
    return render_to_response('addcita.html', {
        'form': form,
    }, RequestContext(request))


@login_required
@permission_required('main.perm_secre')
def registro(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(username=request.POST['username'])
            user.get_profile()
            return redirect('/secre/perfil/' + user.username + '/edit/')
    return render_to_response('registro.html', {
        'form': form,
    }, RequestContext(request))


@login_required
@permission_required('main.perm_secre')
def edit_perfil(request, username):
    user = User.objects.get(username=username)
    try:
        perfil = get_object_or_404(Perfil, user=user)
    except Perfil.DoesNotExist:
        perfil = user.get_profile()
    form = PerfilForm(instance=perfil)
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('home_secre')
    return render_to_response('add_perfil.html', {
        'username': user.username,
        'form': form,
        }, RequestContext(request))


@login_required
@permission_required('main.perm_secre')
def home_secre(request):
    try:
        perfil = Perfil.objects.get(user=request.user)
    except Perfil.DoesNotExist:
        perfil = request.user.get_profile()
    return render_to_response('home_secre.html', {
        'perfil': perfil,
        }, RequestContext(request))


@login_required
@permission_required('main.perm_secre')
def agenda(request):
    listas = Lista.objects.all()
    form = ListaForm()
    if request.method == 'POST':
        form = ListaForm(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response('agenda.html', {
                'listas': listas,
                'form': form,
                }, RequestContext(request))
    return render_to_response('agenda.html', {
        'listas': listas,
        'form': form,
    }, RequestContext(request))


@login_required
@permission_required('main.perm_secre')
def secre_usuarios(request):
    perfils = Perfil.objects.all()
    return render_to_response('secre_usuarios.html', {
        'perfils': perfils,
        }, RequestContext(request))


@login_required
@permission_required('main.perm_secre')
def lista(request, pk):
    lista = Lista.objects.get(pk=pk)
    return render_to_response('lista.html', {
        'lista': lista,
    }, RequestContext(request))


@login_required
def consultas(request):
    perfil = Perfil.objects.get(user=request.user)
    consultas = Consulta.objects.filter(tpx=perfil) | Consulta.objects.exclude(tpx=perfil).filter(px=perfil)
    return render_to_response('consultas.html', {
        'consultas': consultas,
    }, RequestContext(request))


@login_required
@permission_required('main.perm_secre')
def listainv(request, pk):
    lista = Lista.objects.get(pk=pk)
    user = User.objects.filter(username="admin")
    personas = Perfil.objects.exclude(user=user)
    personas = filter(lambda x: x not in lista.persona.all(), personas)
    return render_to_response('listainv.html', {
        'lista': lista,
        'personas': personas,
    }, RequestContext(request))


@login_required
@permission_required('main.perm_secre')
def agregar(request):
    lista = Lista.objects.get(pk=request.POST['lista'])
    user = User.objects.get(username=request.POST['username'])
    perfil = Perfil.objects.get(user=user)
    try:
        Lista.objects.get(pk=request.POST['lista'], persona=perfil)
        lista.persona.remove(perfil)
    except Lista.DoesNotExist:
        lista.persona.add(perfil)
    return redirect(request.META['HTTP_REFERER'])
