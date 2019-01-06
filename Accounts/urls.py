from django.contrib.auth.urls import views as auth_views
from django.urls import path, include, re_path
from Accounts import views

urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up'),
    path('', include('django.contrib.auth.urls')),
    path('password/reset/',
         auth_views.PasswordResetView.as_view(template_name='accounts/password_reset/password_reset.html',
                                              email_template_name='password_reset_email.html',
                                              subject_template_name='password_reset_subject.txt'),
         name='password_reset'),
    path('password/reset_done/',
         auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset/password_reset_done.html'),
         name='password_reset_done'),
    re_path(r'^password/reset_(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            auth_views.PasswordResetConfirmView.as_view(
                template_name='accounts/password_reset/password_reset_confirm.html'),
            name='password_reset_confirm'),
    path('password/reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset/password_reset_complete.html'),
         name='password_reset_complete'),
    path('password/change/',
         auth_views.PasswordChangeView.as_view(template_name='accounts/password_change/password_change.html'),
         name='password_change'),
    path('password/change_done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/password_change/password_change_done.html'), name='password_change_done'),
    path('profile/', views.profile, name='profile'),
]
