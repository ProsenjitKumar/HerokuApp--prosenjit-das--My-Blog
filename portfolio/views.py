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
    model = Portfolio
    context_object_name = 'portfolio_list'
    template_name = 'portfolio/index.html'


class SkillsView(ListView):
    model = Skills
    context_object_name = 'skills_list'
    template_name = 'portfolio/index.html'


class ProjectsView(ListView):
    model = Projects
    context_object_name = 'project_list'
    template_name = 'portfolio/index.html'


class CurrentPositionView(ListView):
    model = CurrentPosition
    context_object_name = 'current_position_list'
    template_name = 'portfolio/index.html'


class ExperienceView(ListView):
    model = Experience
    template_name = 'portfolio/index.html'


class EducationalBackgroundView(ListView):
    model = EducationalBackground
    template_name = 'portfolio/index.html'


