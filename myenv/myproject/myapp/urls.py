from django.urls import path,re_path # re_path is used for regex based URL patterns -----27 aug 26-----
#re_path is used for regex based URL patterns, while path is used for simpler, non-regex URL patterns.
#  In most cases, path is sufficient and easier to read. Use re_path only when you need regex capabilities.
from . import views

urlpatterns = [
    path('', views.message),
    path('welcome/', views.message),
    path('info/', views.details),
    path('newhtml/', views.newdetails),
    path('marks/', views.marks),
    path('table/', views.table),
    path('result/', views.result),
    path('food/', views.food),
    path('student/',views.studetails),
    path('stu/',views.studetails1),
    path('stu1/',views.studetails2),
    path('stu2/',views.studetails3),
    path('greet/<str:name>/', views.greetings),  # Dynamic URL pattern
    path('sum/<int:num1>/<int:num2>/', views.add),  # Dynamic URL pattern for sum
    path('foodie/<str:foodvalue>/', views.foodie),  # Dynamic URL pattern for food
    path('mart/', views.mart),  #query parameter example
    path('calculate/', views.calculate),  #query parameter example
    re_path(r'^customer/(?P<customername>[a-zA-Z \s]+)/$', views.customer_profile),  #regex based URL pattern (+  means 1 or more times)-----Matches urls like /customer/john, /customer/jane, etc.
    re_path(r'^user/(?P<username>[a-zA-Z]*)$', views.user_profile),  #regex based URL pattern-----Matches urls like /user/john, /user/jane, /user/, etc.( * means 0 or more times.)
    re_path(r'^item/(?P<item_id>\d+)/$', views.item_detail),  #regex based URL pattern-----Matches urls like /item/123/, /item/456/, etc. (\d+ means 1 or more digits.)
    re_path(r'^archive/(?P<year>\d{4})/(?P<month>\d{2})/$', views.archive_detail),  #regex based URL pattern-----Matches urls like /archive/2023/08/, /archive/2024/01/, etc. (\d{4} means exactly 4 digits, \d{2} means exactly 2 digits.)
    re_path(r'^name/(?P<name>[\w \s -]+)/$', views.name),  #regex based URL pattern-----Matches urls like /name/product-name/, /name/another product/, etc. ([\w \s -]+ means 1 or more word characters, spaces, or hyphens.)
    re_path(r'^price/(?P<price>[0-9]+)/$', views.price),  #regex based URL pattern-----Matches urls like /price/10.50/, /price/25/, etc. (\d+(\.\d+)? means 1 or more digits, optionally followed by a decimal point and more digits.)
    re_path(r'^menu/(?P<category>[a-zA-Z0-9 \s -]+)/(?P<subcategory>[a-zA-Z0-9 \s -]+)?/$', views.menu),  #regex based URL pattern-----Matches urls like /menu/food/, /menu/food/pizza/, etc. (subcategory is optional)
    re_path(r'^blog(?:/(?P<post_slug>[\w-]+))*/$', views.blog),  #regex based URL pattern-----Matches urls like /blog/, /blog/my-first-post/, etc. (post_slug is optional)
    #---------Error handling---------
    path('dvz/', views.dividebyzero),  #simulate divide by zero error
    path('500/', views.handler500),  # Custom 500 error handler
    
    #---------templates---------
    path('mytemplate/', views.mytemplate),
    path('newmenu/', views.fooddata),
    path('free/', views.foodfree),
    path('food/<str:itemname>/', views.food_data),

    path('testimage/', views.testimage),  #9 sep 2026
    path('productimg/',views.productlist),

    path('shopping/',views.shoppinglist),  #10 sep 2026
    path('shoppingcart/<str:shoppingitem>/',views.shoppingdetails,name='shoppingdetails'),  #10 sep 2026
    path('home/', views.home,name='home'),  #16 sep 2026
    path('about/', views.about,name='about'),  #16 sep 2026
    path('food/', views.food,name='food'),  #16 sep 2026
    path('testcss/', views.testcss),  #17 sep 2026
    path('items/', views.items),  #17 sep 2026
    path('itemdetails/<str:name>/', views.itemdetails, name='itemdetails'),
    path("simpleform",views.simpleform,name="simpleform"),
    path("simpleform1/",views.simpleform1,name="simpleform1"),
    path("simpleform2/",views.simpleform2,name="simpleform2"),
    path("simpleform3/",views.simpleform3,name="simpleform3"),
    path("success/",views.success,name="success"),
    path("htmlform/",views.htmlform,name="htmlform"),
    path("validate/",views.validate,name="validate"),
    path('form_submission/', views.form_submission),
    path('form_submission2/', views.form_submission2),
    path('insertblogpost/',views.insertblogpost),
    path('blogposts/',views.blogposts,name='b'),
    path('blogpost_detail/<int:id>/',views.blogpost_detail, name='b_d'),#method to display the details of a specific blog post
    path('set_cookie/', views.set_cookie),  #method to set a cookie
    path('get_cookie/', views.get_cookie),  #method to get a cookie
    path('cookieview1/', views.cookieview1, name='cookieview1'),  #method to display a cookie value
    path('cookieview2/', views.cookieview2, name='cookieview2'),
    path('cookieview3/', views.cookieview3, name='cookieview3'),
    path('lastvisitedpage/', views.LastVisitedPage, name='lastvisitedpage'),
    ]

