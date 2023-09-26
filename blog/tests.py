from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Publicacion

# Create your tests here.
class PruebasBlog(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username = 'usuarioPrueba',
            email = 'prueba@email.com',
            password = 'secreto'
        )

        cls.pub = Publicacion.objects.create(
            titulo = 'Un buen titulo',
            cuerpo = 'Un bonito contenido',
            autor = cls.user,
        )

    def test_modelo_publicacion(self):
        self.assertEqual(self.pub.titulo, 'Un buen titulo')
        self.assertEqual(self.pub.cuerpo, 'Un bonito contenido')
        self.assertEqual(self.pub.autor.username, 'usuarioPrueba')
        self.assertEqual(str(self.pub), 'Un buen titulo')            
        self.assertEqual(self.pub.get_absolute_url(), '/pub/1/') 

    def test_url_existe_ubicacion_correcta_listview(self):
        respuesta = self.client.get('/')
        self.assertEqual(respuesta.status_code, 200)

    def test_url_existe_ubicacion_correcta_detailview(self):
        respuesta = self.client.get(reverse('inicio'))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, 'Un bonito contenido')
        self.assertTemplateUsed(respuesta, 'inicio.html')

    #kwargs son los parametros, de los cuales obtiene la url
    def test_detailview_publicacion(self):
        respuesta = self.client.get(reverse('detalle_pub', kwargs={'pk': self.pub.pk}))
        sin_respuesta = self.client.get(reverse('detalle_pub', kwargs={'pk': 100000}))
        sin_respuesta = self.client.get('/pub/100000/')
        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(sin_respuesta.status_code, 404)
        self.assertContains(respuesta, 'Un buen titulo')
        self.assertTemplateUsed(respuesta, 'detalle_publicacion.html')
        
    def test_vistacrearpublicacion(self):
        respuesta = self.client.post(
            reverse('pub_nuevo'),
            {
             'titulo': 'Nuevo titulo',
             'cuerpo': 'Nuevo texto',
             'sutor' : self.user.id ,                     
            },                              
        )
        self.assertEqual(respuesta.status_code, 302)
        self.assertEqual(Publicacion.objects.last().titulo, 'Nuevo titulo')
        self.assertEqual(Publicacion.objects.last().cuerpo, 'Nuevo texto')
        
    def test_vistaeditarpublicacion(self):
        respuesta = self.client.post(
            reverse('editar_pub', args='1'),
            {
                'titulo': 'titulo modificado',
                'cuerpo': 'texto modificado',
            },
        )
        self.assertEqual(respuesta.status_code, 302)
        self.assertEqual(Publicacion.objects.last().titulo, 'titulo modificado')
        self.assertEqual(Publicacion.objects.last().cuerpo, 'texto modificado')

    def test_vistaeliminarpublicacion(self):
        respuesta = self.client.post(reverse('eliminar_pub', args='1'))
        self.assertEqual(respuesta.status_code, 302)
        
