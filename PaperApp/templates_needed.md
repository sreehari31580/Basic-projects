# Templates Needed for the Notes App

Create the following templates in `PaperApp/templates/paperapp/`:

1. `note_list.html` - To display all notes
2. `note_detail.html` - To view a single note
3. `note_form.html` - Form for creating and updating notes
4. `note_confirm_delete.html` - Confirmation page for note deletion

## Sample Template Content (note_list.html):

```html
{% extends 'base.html' %} {% block content %}
<h1>My Notes</h1>
<a href="{% url 'note-create' %}" class="btn btn-primary">Add New Note</a>

{% if notes %}
<div class="notes-list">
  {% for note in notes %}
  <div class="note-card">
    <h2><a href="{% url 'note-detail' note.pk %}">{{ note.title }}</a></h2>
    <p>Last updated: {{ note.updated_at }}</p>
    <a href="{% url 'note-update' note.pk %}">Edit</a>
    <a href="{% url 'note-delete' note.pk %}">Delete</a>
  </div>
  {% endfor %}
</div>
{% else %}
<p>No notes available. Create your first note!</p>
{% endif %} {% endblock %}
```

Note: You'll also need to create a base.html template in your templates directory.
