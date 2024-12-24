from django.shortcuts import render, redirect
from django.urls import reverse

def dashboard(request):
    return render(request, 'calculators/dashboard.html')

def sip_calculator(request):
    if request.method == 'GET': # Handle GET requests
        try:
            principal = float(request.GET.get('principal'))
            rate = float(request.GET.get('rate')) / 100 / 12
            time = int(request.GET.get('time')) * 12

            future_value = 0
            for i in range(time):
                future_value += principal * (((1 + rate) ** (time - i)))

            invested_amount = round(principal * time, 2)
            expected_returns = round(future_value - invested_amount, 2)
            total_value = round(future_value, 2)

            result = {
                'invested_amount': invested_amount,
                'expected_returns': expected_returns,
                'total_value': total_value
            }
            return render(request, 'calculators/sip_result.html', {'result': result}) # Render result page directly
        except (ValueError, TypeError):
            result = "Invalid input. Please enter numbers only."
            return render(request, 'calculators/sip.html', {'result': result}) # Render the form with the error message
    return render(request, 'calculators/sip.html') # Render the initial form

def sip_result(request):
    return render(request, 'calculators/sip_result.html')


def rd_calculator(request):
    result = None
    if request.method == 'POST':
        try:
            principal = float(request.POST.get('principal'))
            rate = float(request.POST.get('rate')) / 100 / 4
            time = int(request.POST.get('time')) * 4

            maturity_value = principal * (((1 + rate)**time - 1) / rate)
            result = round(maturity_value, 2)
        except (ValueError, TypeError):
            result = "Invalid input. Please enter numbers only."
    return render(request, 'calculators/rd.html', {'result': result})

def pomis_calculator(request):
    result = None
    if request.method == 'POST':
        try:
            investment = float(request.POST.get('investment'))
            rate = float(request.POST.get('rate')) / 100 / 12
            monthly_income = investment * rate
            result = round(monthly_income, 2)
        except (ValueError, TypeError):
            result = "Invalid input. Please enter numbers only."
    return render(request, 'calculators/pomis.html', {'result': result})

def gst_calculator(request):
    result = None
    if request.method == 'POST':
        try:
            amount = float(request.POST.get('amount'))
            gst_rate = float(request.POST.get('gst_rate')) / 100
            gst_amount = amount * gst_rate
            net_amount = amount + gst_amount
            result = {"gst":round(gst_amount,2),"net":round(net_amount,2)}
        except (ValueError, TypeError):
            result = "Invalid input. Please enter numbers only."
    return render(request, 'calculators/gst.html', {'result': result})

def simple_interest_calculator(request):
    result = None
    if request.method == 'POST':
        try:
            principal = float(request.POST.get('principal'))
            rate = float(request.POST.get('rate')) / 100
            time = float(request.POST.get('time'))
            interest = (principal * rate * time)
            result = round(interest, 2)
        except (ValueError, TypeError):
            result = "Invalid input. Please enter numbers only."
    return render(request, 'calculators/simple_interest.html', {'result': result})

def compound_interest_calculator(request):
    result = None
    if request.method == 'POST':
        try:
            principal = float(request.POST.get('principal'))
            rate = float(request.POST.get('rate')) / 100
            time = float(request.POST.get('time'))
            n = float(request.POST.get('n')) #compounded n times per year
            amount = principal * (1 + (rate / n))**(n * time)
            ci = amount - principal
            result = round(ci, 2)
        except (ValueError, TypeError):
            result = "Invalid input. Please enter numbers only."
    return render(request, 'calculators/compound_interest.html', {'result': result})

def ssy_calculator(request):
    result = None
    if request.method == 'POST':
        try:
            annual_investment = float(request.POST.get('annual_investment'))
            rate = float(request.POST.get('rate')) / 100
            years = int(request.POST.get('years'))
            total_investment = 0
            maturity_amount = 0

            for i in range(years):
                if i < 15:
                    total_investment += annual_investment
                    maturity_amount += annual_investment * (1 + rate) ** (15-i)

            result = round(maturity_amount, 2)
        except (ValueError, TypeError):
            result = "Invalid input. Please enter numbers only."
    return render(request, 'calculators/ssy.html', {'result': result})

def fd_calculator(request):
    result = None
    if request.method == 'POST':
        try:
            principal = float(request.POST.get('principal'))
            rate = float(request.POST.get('rate')) / 100
            time = float(request.POST.get('time'))
            interest = principal * rate * time
            maturity_amount = principal + interest
            result = round(maturity_amount, 2)
        except (ValueError, TypeError):
            result = "Invalid input. Please enter numbers only."
    return render(request, 'calculators/fd.html', {'result': result})

def emi_calculator(request):
    result = None
    if request.method == 'POST':
        try:
            principal = float(request.POST.get('principal'))
            rate = float(request.POST.get('rate')) / 100 / 12  # Monthly interest rate
            time = int(request.POST.get('time')) * 12        # Loan term in months

            emi = (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
            result = round(emi, 2)
        except (ValueError, TypeError):
            result = "Invalid input. Please enter numbers only."
    return render(request, 'calculators/emi.html', {'result': result})