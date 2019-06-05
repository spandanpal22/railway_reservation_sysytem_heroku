from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('suggest', views.suggest, name='suggest'),
    path('complaints', views.complaintsUser, name='complaints'),
    path('foreignHolidays', views.foreignHolidayUser, name='holiday_foreign'),
    path('indianHolidays', views.indiaHolidayUser, name='holiday_india'),
    path('search-trains', views.searchTrainsUser, name='search_trains'),
    path('signin', views.SignInFormView.as_view(), name='signin'),
    path('signup', views.signup, name='signup'),
    path('signup2', views.UserFormView.as_view(), name='signup2'),
    path('signout', views.signout, name='signout'),

    path('api', views.TicketView.as_view(), name='api'),
    path('api/<int:pk>', views.TicketView.as_view(), name='api2'),

    path('home_user', views.indexUser, name='home_user'),
    path('suggest_user', views.suggestUser, name='suggest_user'),
    path('complaints_user', views.complaintsUser, name='complaints_user'),
    path('foreignHolidays_user', views.foreignHolidayUser, name='holiday_foreign_user'),
    path('indianHolidays_user', views.indiaHolidayUser, name='holiday_india_user'),
    path('book-tickets_user', views.bookTicketsUser, name='book_tickets_user'),
    path('cancel-tickets_user', views.cancelTicketsUser, name='cancel_tickets_user'),
    path('view-tickets_user', views.viewTicketsUser, name='view_tickets_user'),
    path('search-trains_user', views.searchTrainsUser, name='search_trains_user'),

    path('animations', views.animations, name='animations'),
    path('profile', views.profile, name='myProfile'),

]
