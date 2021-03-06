from . import views
from django.conf.urls import url
from django.contrib.staticfiles import views as v
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', views.contest),
    url(r'^home', views.login_view),
    url(r'^main_ques', views.contest),
    url(r'^questions', views.questions),
    url(r'^leaderboard',views.leader_board),
    url(r'^logout',views.logout_view),
    url(r'^change_password',views.change_password),
    url(r'^final_leaderboard',views.dummy_leader_board),
    url(r'^rules',views.rules),
    url(r'^configure_question', views.configure_question),
    url(r'^contest_admin', views.contest_admin),
    url(r'^register', views.register),
    # url(r'^header', views.header),
]
#
# urlpatterns += [
#         url(r'^static/(?P<path>.*)$', v.serve),
#     ]