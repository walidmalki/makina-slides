from datetime import date
from rest_framework import viewsets

from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse

from todo.models import Task, TodoList
from todo.forms import AddTaskForm, EditTaskForm, TaskSearchForm
from todo.serializers import TodoListSerializer, TaskSerializer

# --- Lists -------------------------------------------------------------------


# --- TodoList list -----------------------------------------------------------

class TodoListList(ListView):
    model = TodoList


# --- Task list ---------------------------------------------------------------

# Solution 1 : class based view
class TaskList(ListView):
    model = Task


# Solution 2 : function based view
def task_list(request):

    tasks = Task.objects.get_urgent()

    return render(
        request,
        'todo/task_list.html',
        {
            'object_list': tasks
        })

# --- TodoList detail ---------------------------------------------------------


class TodoListDetail(DetailView):
    model = TodoList

    def get_context_data(self, **kwargs):
        context = DetailView.get_context_data(self, **kwargs)
        context['tasks'] = self.object.tasks.all()
        context['urgent_tasks'] = self.object.tasks.get_urgent()
        return context


# --- Task detail -------------------------------------------------------------


# Solution 1 : class based view
class TaskDetail(DetailView):
    model = Task

    def get_context_data(self, **kwargs):
        context = DetailView.get_context_data(self, **kwargs)
        context['today'] = date.today()
        return context


# Solution 2 : function based view
def task_detail(request, identifiant):

    task = Task.objects.get(pk=identifiant)

    return render(
        request,
        'todo/task_detail.html',
        {
            'task': task,
            'today': date.today()
        })


# --- Add a task --------------------------------------------------------------

# Solution 1: class based view
class AddTask(CreateView):
    model = Task
    form_class = AddTaskForm
    template_name = 'todo/add_task.html'

    def get_success_url(self):
        return reverse('task_detail', args=(self.object.pk, ))


# Solution 2 : function based view
def add_task(request):
    form = AddTaskForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        task = form.save()
        return redirect(
            reverse(
                'task_detail',
                args=(task.pk, ))
        )
    return render(
        request,
        'todo/add_task.html',
        {
            'form': form,
        })

# --- Edit a task -------------------------------------------------------------


# Solution 1: class based view
class EditTask(UpdateView):
    model = Task
    form_class = EditTaskForm
    template_name = 'todo/edit_task.html'

    def get_success_url(self):
        return reverse('task_detail', args=(self.object.pk, ))


# Solution 2 : function based view
def edit_task(request, pk):
    task = Task.objects.get(pk=pk)
    form = EditTaskForm(request.POST or None, instance=task)
    if form.is_valid():
        task = form.save()
        return redirect(
            reverse(
                'task_detail',
                args=(task.pk, ))
        )
    return render(
        request,
        'todo/edit_task.html',
        {
            'task': task,
            'form': form,
        })


# --- Task search -------------------------------------------------------------

@permission_required('search_task')
def task_search(request):

    form = TaskSearchForm(request.POST or None)

    tasks = Task.objects.all()
    if form.is_valid():

        filters = {}
        name = form.cleaned_data.get('name')
        if name:
            filters.update(name__icontains=name)

        deadline = form.cleaned_data.get('deadline')
        if deadline:
            filters.update(deadline__lte=deadline)

        done = form.cleaned_data.get('done', None)
        if done is not None:
            filters.update(done=done)

        tasks = tasks.filter(**filters)

    return render(
        request,
        'todo/task_search.html',
        {
            'tasks': tasks,
            'form': form,
        })


# ------ REST -----------------------------------------------------------------

class TodoListViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
