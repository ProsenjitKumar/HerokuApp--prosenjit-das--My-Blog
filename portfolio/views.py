from django.shortcuts import render
from django.views.generic import ListView
from .models import (
    Portfolio,
    Skills,
    Projects,
    CurrentPosition,
    Experience,
    EducationalBackground,
)


class PortfolioView(ListView):
    context_object_name = 'portfolio_list'
    queryset = Portfolio.objects.all()
    extra_context = {
        'projects_list': Projects.objects.all(),
        'skills_list': Skills.objects.all(),
        'current_position_list': CurrentPosition.objects.all(),
    }
    template_name = 'portfolio/index.html'

#
# class SkillsView(ListView):
#     model = Skills
#     context_object_name = 'skills_list'
#     template_name = 'portfolio/index.html'
#
#
# class ProjectsView(ListView):
#     model = Projects
#     context_object_name = 'project_list'
#     extra_context =
#     template_name = 'portfolio/index.html'
#
#
# class CurrentPositionView(ListView):
#     model = CurrentPosition
#     context_object_name = 'current_position_list'
#     template_name = 'portfolio/index.html'
#
#
# class ExperienceView(ListView):
#     model = Experience
#     template_name = 'portfolio/index.html'
#
#
# class EducationalBackgroundView(ListView):
#     model = EducationalBackground
#     template_name = 'portfolio/index.html'


