from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Note
from django import forms

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']

class NoteListView(ListView):
    model = Note
    template_name = 'note_list.html'  # Updated path
    context_object_name = 'notes'

class NoteDetailView(DetailView):
    model = Note
    template_name = 'note_detail.html'  # Updated path
    context_object_name = 'note'

class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'  # Updated path
    success_url = reverse_lazy('note-list')

class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'  # Updated path
    success_url = reverse_lazy('note-list')

class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'note_confirm_delete.html'  # Updated path
    success_url = reverse_lazy('note-list')
