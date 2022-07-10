from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from matplotlib.style import context
from .models import NoteApp

# Create your views here.
def home(request,msg=False):
    all_note = NoteApp.objects.all()
    if request.method == 'GET' and 'id' in request.GET:
        note_id = request.GET['id']
        note = all_note.get(id=note_id)
        return render(request,'index.html',{'note':note})
    else:
        return render(request,'index.html',{'all_note':all_note,'msg':msg})

def create_note(request):
    if request.method=='POST':
        title=request.POST['note_title']
        description=request.POST['note_description']
        note_obj=NoteApp()
        note_obj.note_title=title
        note_obj.note_description=description
        note_obj.save()
        return redirect('/')
    pass

def notes(request, note_id):
    note = NoteApp.objects.filter(id=note_id).first()
    return render(request, 'notes.html', {'note':note})

def edit_note(request,edit_id):
    if request.method=='POST':
        get_note=NoteApp.objects.get(id=edit_id)
        get_note.note_title=request.POST['note_title']
        get_note.note_description=request.POST['note_description']
        get_note.save()
        msg="Note Updated Successfully...."
        return HttpResponseRedirect(f'/{msg}')
    pass

def delete_note(request,delete_id):
    my_note=NoteApp.objects.get(id=delete_id)
    my_note.delete()
    msg='Note Deleted Successfully......'
    return HttpResponseRedirect(f'/{msg}')