from django.shortcuts import render

def home(request):
    resume = {
        'name': 'Aswin',
        'age': 20,
        'gender': 'male',
        'email': 'aswin@email.com',
        'skills': ['Python', 'Django', 'HTML', 'CSS'],
        'education': {
            'Degree': 'BTech CS',
            'College': 'CUSAT',
            'Year': '1st Year'
        }
    }

    return render(request, 'resume.html', {'resume': resume})