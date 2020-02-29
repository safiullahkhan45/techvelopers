from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def home_view(request):
	if request.method == 'POST':
		firstname = request.POST['fname']
		lastname = request.POST['lname']
		phone = request.POST['phone']
		email = request.POST['email']
		message = request.POST['message']
		information = ltos(firstname, lastname, phone, email, message)

		send_mail('Contact Us from Techvelopers',
			information,
			settings.EMAIL_HOST_USER,
			['safiullah.khan145@gmail.com'],
			fail_silently = False)
	return render(request, 'portfolio/home.html')


def ltos(firstname, lastname, phone, email, message):
	info = ''
	for i in firstname:
		info += i

	info += '  '
	for i in lastname:
		info += i

	info += '\n'
	for i in phone:
		info += i

	info += '\n'
	for i in email:
		info += i

	info += '\n'
	for i in message:
		info += i

	return info
