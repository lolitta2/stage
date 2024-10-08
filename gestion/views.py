from django.shortcuts import redirect, render
from .forms import EmployeeForm, PerformanceForm, SatisfactionSurveyForm, FeedbackForm, BehaviorForm
from .models import Employee, Performance, SatisfactionSurvey, Feedback, ActionPlan



def home(request):
    return render(request, 'home.html')

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})


def add_performance(request):
    if request.method == "POST":
        form = PerformanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('performance_list')
    else:
        form = PerformanceForm()
    return render(request, 'gestion/add_performance.html', {'form': form})

def performance_list(request):
    performances = Performance.objects.all()
    return render(request, 'gestion/performance_list.html', {'performances': performances})


def add_satisfaction_survey(request):
    if request.method == 'POST':
        form = SatisfactionSurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirection après la soumission
    else:
        form = SatisfactionSurveyForm()
    return render(request, 'gestion/add_satisfaction_survey.html', {'form': form})

def add_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirection après la soumission
    else:
        form = FeedbackForm()
    return render(request, 'gestion/add_feedback.html', {'form': form})

def view_surveys(request):
    surveys = SatisfactionSurvey.objects.all()
    return render(request, 'gestion/view_surveys.html', {'surveys': surveys})

def view_feedbacks(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'gestion/view_feedbacks.html', {'feedbacks': feedbacks})



def success_view(request):
    return render(request, 'gestion/success.html')


def add_behavior(request):
    if request.method == 'POST':
        form = BehaviorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Assurez-vous que vous avez une URL nommée 'success'
    else:
        form = BehaviorForm()
    return render(request, 'gestion/add_behavior.html', {'form': form})

import joblib
import logging
from django.shortcuts import render
from .forms import PredictionForm
from .models import Employee
import pandas as pd
from .risk_classification import classify_risk  # Importation de la fonction de classification des risques

logger = logging.getLogger(__name__)

def predict_employee_retention(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            logger.debug("Form is valid")
            
            # Extraire les données du formulaire
            data = {
                'gender': form.cleaned_data['gender'],
                'position': form.cleaned_data['position'],
                'department': form.cleaned_data['department'],
                'age': form.cleaned_data['age'],
                'salary': form.cleaned_data['salary'],
                'performance_rating': form.cleaned_data['performance_rating'],
                'salary_increase': form.cleaned_data['salary_increase'],
                'absenteeism_days': form.cleaned_data['absenteeism_days'],
                'overtime_hours': form.cleaned_data['overtime_hours'],
                'satisfaction_score': form.cleaned_data['satisfaction_score'],
                'feedback_text': form.cleaned_data['feedback_text']
            }

            logger.debug(f"Data extracted: {data}")

            # Convertir en DataFrame pour être compatible avec le modèle
            df = pd.DataFrame([data])

            # Charger le modèle
            try:
                model = joblib.load('projet_rh/model.pkl')
                logger.debug("Model loaded successfully")
            except Exception as e:
                logger.error(f"Error loading model: {e}")
                return render(request, 'gestion/predict_form.html', {'form': form, 'error': 'Model loading error'})

            # Faire la prédiction
            try:
                prediction = model.predict(df)
                probability = model.predict_proba(df)[0][1]  # Probabilité que l'employé quitte l'entreprise
                logger.debug(f"Prediction made: {prediction}, Probability: {probability}")
            except Exception as e:
                logger.error(f"Error during prediction: {e}")
                return render(request, 'gestion/predict_form.html', {'form': form, 'error': 'Prediction error'})

            # Classifier le risque
            risk_level = classify_risk(probability)
            logger.debug(f"Risk level classified: {risk_level}")

            # Renvoyer la prédiction et la classification au template
            return render(request, 'gestion/predict_result.html', {
                'form': form,
                'prediction': prediction[0],
                'probability': probability,
                'risk_level': risk_level
            })
    else:
        form = PredictionForm()
        logger.debug("Form initialized")

    return render(request, 'gestion/predict_form.html', {'form': form})
    



from .dashboard import generate_retention_dashboard
from django.shortcuts import render
from .risk_assessment import assess_risk
from .recommendations import generate_recommendations

def retention_dashboard(request):
    # Générer le dashboard
    graph_satisfaction, graph_turnover = generate_retention_dashboard()

    # Évaluer les risques et générer des recommandations
    high_risk_employees = assess_risk()
    recommendations = generate_recommendations(high_risk_employees)

    context = {
        'graph_satisfaction': graph_satisfaction,
        'graph_turnover': graph_turnover,
        'recommendations': recommendations
    }
    
    return render(request, 'gestion/retention_dashboard.html', context)


from django.shortcuts import render, get_object_or_404, redirect
from .models import ActionPlan
from .forms import ActionPlanForm

def action_plans(request):
    plans = ActionPlan.objects.all()
    return render(request, 'gestion/action_plans.html', {'plans': plans})

def create_action_plan(request):
    if request.method == 'POST':
        form = ActionPlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('action_plans')
    else:
        form = ActionPlanForm()
    return render(request, 'gestion/create_action_plan.html', {'form': form})

def update_action_plan(request, action_plan_id):
    action_plan = get_object_or_404(ActionPlan, id=action_plan_id)
    if request.method == 'POST':
        form = ActionPlanForm(request.POST, instance=action_plan)
        if form.is_valid():
            form.save()
            return redirect('action_plans')
    else:
        form = ActionPlanForm(instance=action_plan)
    return render(request, 'gestion/update_action_plan.html', {'form': form})


from .forms import InterventionForm
from .models import Intervention

def add_intervention(request):
    if request.method == 'POST':
        form = InterventionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('intervention_list')
    else:
        form = InterventionForm()
    return render(request, 'gestion/add_intervention.html', {'form': form})

def intervention_list(request):
    interventions = Intervention.objects.all()
    return render(request, 'gestion/intervention_list.html', {'interventions': interventions})

from django.db.models import Count


def intervention_impact(request):
    impact_summary = Intervention.objects.values('outcome').annotate(count=Count('outcome'))
    return render(request, 'gestion/intervention_impact.html', {'impact_summary': impact_summary})
