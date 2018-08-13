from django.shortcuts import render
from datetime import datetime

def index(request):
	return render(request, 'index.html')

def createtable(request):
	manage = []

	data = {}
	data['cliente'] = 'A LITORAL LOCADORA LTDA-ME'
	data['data'] = datetime.today()
	data['valor'] = 1250.00
	manage.append(data)

	data = {}
	data['cliente'] = 'ACESSORIA E SERVICOS LTDA-ME'
	data['data'] = datetime.today()
	data['valor'] = 3640.00
	manage.append(data)

	data = {}
	data['cliente'] = 'RESTAURANTE E LANCHONETE LTDA-ME'
	data['data'] = datetime.today()
	data['valor'] = 2200.00
	manage.append(data)

	data = {}
	data['cliente'] = 'CHURRASCARIA E RESTAURANTE LTDA-ME'
	data['data'] = datetime.today()
	data['valor'] = 500.00
	manage.append(data)

	data = {}
	data['cliente'] = 'AUTOCAR LTDA-EPP'
	data['data'] = datetime.today()
	data['valor'] = 4600.00
	manage.append(data)

	data = {}
	data['cliente'] = 'A & W PIZZARIA LTDA-ME'
	data['data'] = datetime.today()
	data['valor'] = 10450.00
	manage.append(data)

	data = {}
	data['cliente'] = 'M & C XEROX E ENCADERNACOES LTDA-ME'
	data['data'] = datetime.today()
	data['valor'] = 1080.00
	manage.append(data)

	data = {}
	data['cliente'] = 'MELHOR GESTAO EMPRESARIAL LTDA-ME'
	data['data'] = datetime.today()
	data['valor'] = 400.00
	manage.append(data)

	data = {}
	data['cliente'] = 'TOTAL'
	data['valor'] = 24130.25
	manage.append(data)


	context = {'dados': manage}

	return render(request, 'table.html', context)

	