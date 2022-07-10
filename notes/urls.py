from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('', views.home, name='home'),
    path('<str:msg>', views.home, name='home'),
    path('create-note/', views.create_note, name='create-note'),
    path('notes/<int:note_id>',views.notes, name="notes"),
    path('edit/<int:edit_id>', views.edit_note, name="edit-note"),
    path('delete/<int:delete_id>', views.delete_note, name="delete-note"),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)