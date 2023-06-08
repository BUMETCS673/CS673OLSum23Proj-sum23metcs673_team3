from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, get_user_model
from .forms import LoginForm, RegisterForm, ChangePass, ResetPass
from django.db.models.query_utils import Q
# the following are for email authentication, please don't remove them
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from .tokens import account_activation_token


# render index page as the homepage
def index(request):
    return render(request, 'homepage.html')


def homepage(request):
    return render(request,"homepage.html")


# registration function
def user_register(request):
    if request.user.is_authenticated: # check if user already logged in
        return redirect('homepage') # if so, redirect to homepage

    # when user submit the registration form
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid(): # check if valid (password complexity, email pattern, etc.)

            # if so, create user
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.is_active = False # set the user as not authenticated
            user.save() # save user's information

            # send confirmation link to user's email
            sendEmail(request, user, form.cleaned_data.get('email'), 'Confirmation Email')

            messages.success(request, 'You have registered successfully. Please check your email for the confirmation link.')
            return redirect('login')

        else: # if not valid, refresh the page and let the user try again
            return render(request, 'register.html', {'form': form})

    form = RegisterForm()
    return render(request, 'register.html', {'form': form})


# login function
def user_login(request):
    if request.user.is_authenticated: # check if user logged in
        return redirect('homepage') # if so, redirect to homepage

    # when user submit the login form
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid(): # check if form is valid
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # search database for such user or if user is authenticated
            user = authenticate(request, username=username, password=password)

            # if user exists
            if user:
                login(request, user) # allow login
                return redirect('homepage')

        # form is not valid or user is not authenticated
        messages.error(request, f'Invalid username or password')
        return render(request, 'login.html', {'form': form})

    form = LoginForm()
    return render(request, 'login.html', {'form': form})


# Logout function
def user_logout(request):
    logout(request)
    return redirect('homepage')


# Allow users change their password
def change_pass(request):
    if not request.user.is_authenticated: # check if user logged in
        return redirect('homepage') # if not, redirect to homepage

    # get user's information through request session
    user = request.user
    if request.method == 'POST': # when user submit the password changing form
        form = ChangePass(user, request.POST)
        if form.is_valid(): # if form is valid, save the new password
            form.save()
            messages.success(request, "Your password has been changed")
            return redirect('login')
        else:
            for error in list(form.errors.values()): # show error if form is not valid
                messages.error(request, error)

    # reset page
    form = ChangePass(user)
    messages.success(request, "Please double check your input.")
    return render(request, 'change_pass.html', {'form': form})


# Start the password reset function (sending email)
def reset_pass(request):
    if request.method == 'POST':
        form = ResetPass(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = get_user_model().objects.filter(Q(email=email)).first()
            if user:
                subject = 'Password Reset'
                sendEmail(request, user, form.cleaned_data.get('email'), subject, 1)
                messages.success(request, "Please check your email for password reset.")
                return redirect('homepage')

    form = ResetPass()
    messages.success(request, "The email is incorrect.")
    return render(request, "reset_pass.html", {"form": form})


# Finishing reset password
def reset_pass_done(request, uidb64, token):
    User = get_user_model()

    user, active = decipher(request, uidb64, token, User)

    # if such user exist, let the user change their password
    if user is not None and active:
        if request.method == 'POST':
            form = ChangePass(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Your password has been reset.")
                return redirect('homepage')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)

        form = ChangePass(user)
        return render(request, 'reset_pass_done.html', {'form': form})
    messages.error(request, 'Something went wrong, redirecting back to Homepage')
    return redirect("homepage")


# Send email to user based on function
def sendEmail(request, user, user_email, subject, reset=0):
    # default email template is to activate account
    template = 'template_activate_account.html'

    # if reset = 1, change the email template to password reset
    if reset == 1:
        template = 'template_reset_pass.html'

    # keywords for sending email
    message = render_to_string(template, {
        'user': user.username,
        'domain': get_current_site(request).domain, # Database domain name (127.0.0.1:8080)
        'uid': urlsafe_base64_encode(force_bytes(user.pk)), # Django default identifier generator
        'token': account_activation_token.make_token(user), # Django default secure token generator
        'protocol': 'https' if request.is_secure() else 'http' # Allow HTTPS if secure
    })
    email = EmailMessage(subject, message, to=[user_email])
    email.send()


# Activation function when user click on the confirmation link
def activate(request, uidb64, token):
    User = get_user_model()
    user, active = decipher(request, uidb64, token, User)

    # if such user exits, set the user active
    if user is not None and active:
        user.is_active = True
        user.save()
        messages.success(request, 'Your account is activated.')
        return redirect('login')
    else:
        messages.error(request, 'The confirmation link is invalid!')

    return redirect('homepage')



def decipher(request, uidb64, token, User):
    # decoding the "uidb64" and "token" to see if them match users in the database
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    active = account_activation_token.check_token(user, token)

    return user, active


