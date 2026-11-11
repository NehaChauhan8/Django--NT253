from django.shortcuts import render,redirect
from django.http import HttpResponse
def message(request):
    return HttpResponse("Welcome user!")

def details(request):
    name="Neha"
    program="BTech CSE"

    # return HttpResponse("The name of the student is " +name+" and the program is "+program)

    return HttpResponse(f"<p style='color:blue'>The name of the student is {name} and the program is {program}</p>") #f means format string, it allows you to embed expressions inside
    #string literals, using curly braces {}. The expressions are evaluated at runtime and then formatted using the format() protocol.

# Create your views here.



   
def newdetails(request):
    return HttpResponse("<h1>This is a heading</h1><h3>This is 3rd heading</h3><p>This is a paragraph</p>")

def marks(request):
    course1 = 98
    course2 = 99
    course3 = 100
    course4 = 57
    course5 = 78

    total = course1+course2+course3+course4+course5
    percent = (total/500)*100
    return HttpResponse(f"<p style = color:red>The Total marks is <b style = color:green>{total}</b> and Percentage is <b style = color:green>{percent}</b>%</p>")

def table(request):
    number = 5
    table = "<h1>Table 5</h1>"
    for i in range(1,11):
        table += f"{number}x{i}={number*i}<br>"
    return HttpResponse(table)
    
def result(request):
    marks = 39

    if marks >=80 and marks <=100:
        return HttpResponse(f"<h1 style=color:green>You scored {marks} and you have got Grade A</h1>")

    if marks >=60 and marks <80:
            return HttpResponse(f"<h1 style=color:blue>You scored {marks} and you have got Grade B</h1>")

    if marks >=40 and marks <60:
            return HttpResponse(f"<h1 style=color:orange>You scored {marks} and you have got Grade C</h1>")

    if marks <40:
            return HttpResponse(f"<h1 style=color:red>You scored {marks} and you have got Failed</h1>")

def food(request):
     fooditems=["Pizza", "Burger", "Sandwich", "Pasta", "Noodles"]
     itemContent = "<h1>Food Items</h1>"
     for item in fooditems:
         itemContent += f"<li>{item}</li>"
     return HttpResponse(itemContent)


# ----------------------------------------------------19 aug 2026
#creating table using list of lists
def studetails(request):
     studentinfo=[
          ["Vannu", 67],
          ["Neha",98],
          ["hihi",64]
     ]
     content="""<table border=1>
      <tr>
      <th>Name</th>
      <th>Marks</th>
     
      </tr> """
     for i in studentinfo:
          
          content += f"""
          <tr>
          <td>{i[0]}</td>
          <td>{i[1]}</td>
          </tr>
          """
     content += "</table>"
     return HttpResponse(content)

#--------------------easy way to create table using keys and values of dictionary------------
def studetails1(request):
     studentinfo=[
          {"Name":"Neha", "Marks":90, "Course":"Django"},
          {"Name":"V", "Marks":88, "Course":"React"},
          {"Name":"hihi", "Marks":70, "Course":"Django"},
          {"Name":"hahaha", "Marks":60, "Course":"Nodejs"}
     ]
     content ="""<table border=1>
      <tr>
      <th>Name</th>
      <th>Marks</th>
      <th>Course</th>
      </tr> """
     for i in studentinfo:
          content += f""" 
          <tr>
          <td>{i["Name"]}</td>
          <td>{i["Marks"]}</td>
          <td>{i["Course"]}</td>
          </tr>        
          """
     content += "</table>"
     return HttpResponse(content)

#--------------------easy way to create table using keys and values of dictionary------------
def studetails2(request):
     studentinfo=[
          {"Name":"Neha", "Marks":90, "Course":"Django"},
          {"Name":"V", "Marks":88, "Course":"React"},
          {"Name":"hihi", "Marks":70, "Course":"Django"},
          {"Name":"hahaha", "Marks":60, "Course":"Nodejs"}
     ]
     content ="<table border=1><tr>"
     for colnames in studentinfo[0].keys():
          content += f"""
          <th>{colnames}</th>"""
     content += "</tr>" 
     for i in studentinfo:
          content += "<tr>"
          for key,value in i.items():
               content += f"""
               <td>{value}</td>
               """
     content += "</tr></table>"
     return HttpResponse(content)


def studetails3(request):
     studentinfo={
          "neha":{"Marks":90, "Course":"React"},
          "nikki":{"Marks":80, "Course":"Node"},
          "kissi":{"Marks":70, "Course":"Django"},
     }
     content ="""
     <table border=1>
     <tr>
     <th>Name</th>
     <th>Marks</th>
     <th>Course</th>
     </tr>
     """
     #f means format string, it allows you to embed expressions inside
     #string literals, using curly braces {}. The expressions are evaluated at runtime and then formatted
     #using the format() protocol.
     for key,value in studentinfo.items():
          content += f"""
          <tr>
          <td>{key}</td>
          <td>{value["Marks"]}</td> 
          <td>{value["Course"]}</td>
          </tr>
          """
     content += "</table>"
     return HttpResponse(content)

#-----------------DYNAMIC URLS----------------------
#20-aug-2026-----------------------------
#Types of URLS
#1. Static URLS - These are fixed and do not change. For example, /about-us or /contact.
#2. Dynamic URLS - These can change based on user input or other factors. For example, /user/<username> or /product/<product_id>.

def greetings(request, name):
     return HttpResponse(f"Welcome, {name}!")


def add(request, num1, num2):
     result = num1 + num2
     return HttpResponse(f"The sum of {num1} and {num2} is {result}.")
#run the server and check the following URL in browser
#http://127.0.0.1:8000/sum/5/10/



def food(request, foodvalue):
     fooditems={
          "pizza": "Size is regular,  Price is 500",
          "burger": "Size is regular,  Price is 200",
          "sandwich": "Size is regular,  Price is 150",
          "pasta": "Size is regular,  Price is 300",
     }
     return HttpResponse(fooditems[foodvalue])


def foodie(request, foodvalue):
     fooditems={
          "pizza": "Size is regular,  Price is 500",
          "burger": "Size is regular,  Price is 200",
          "sandwich": "Size is regular,  Price is 150",
          "pasta": "Size is regular,  Price is 300",
     }
     if not foodvalue in fooditems:
          return HttpResponse(f"<p style='color: red;'>Food item not found.</p>")
     return HttpResponse(f"""You selected {foodvalue}. <h1 style="color: blue;">{fooditems.get(foodvalue)}</h1>""")    

#run the server and check the following URL in browser
#http://127.0.0.1:8000/foodie/pizza/


#----------------26 Aug 2026------------------
def mart(request):
     item = request.GET.get('item')
     return HttpResponse(f"<p>You selected {item}.</p>")
# run the server and check the following URL in browser
#http://127.0.0.1:8000/mart/?item=phone



#Create a view function for performing basic calculations
#1 addition 2 subtraction 3 multiplication 4 division
#localhost:8000/calculate?op=add&value1=10&value2=5
def calculate(request):
     op=request.GET.get('op')
     value1=int(request.GET.get('value1'))
     value2=int(request.GET.get('value2'))
     result=0
     try:
          value1=int(value1)
          value2=int(value2)
     except ValueError:
          return HttpResponse("Please enter valid numbers.")
     if op == 'add':
          result = value1 + value2
     elif op == 'subtract':
          result = value1 - value2
     elif op == 'multiply':
          result = value1 * value2
     elif op == 'divide':
          result = value1 / value2
     else:
          return HttpResponse("Invalid operation.")
     return HttpResponse(f"The result of {op} between {value1} and {value2} is {result}.")

#--------------------27 Aug 2026------------------
#regex based URL pattern example
def customer_profile(request, customername):
     return HttpResponse(f"<h1>Customer Profile : {customername}</h1>")
def user_profile(request, username):
     return HttpResponse(f"<h1>User Profile : {username}</h1>")


def item_detail(request, item_id):
     return HttpResponse(f"<h1>Item Detail : {item_id}</h1>")

def archive_detail(request, year, month):
     return HttpResponse(f"<h1>Archive Detail : Year {year}, Month {month}</h1>")

def name(request, name):
     return HttpResponse(f"Name is : {name}")

def price(request, price):
     return HttpResponse(f" Price is : {price}")

#create a path 'menu'. Use regex to pass two parameters category and subcategory.subcategory is optional. 
#Both can accept digits, alphabets and space.
#case1 if you specify subcategory in URL localhost:8000/menu/chinese/noodles
#You have choosen category chinese and subcategory noodles
#case2 if you do not specify subcategory in URL localhost:8000/menu/chinese
#You have choosen category chinese and no subcategory
def menu(request, category, subcategory=None):
     if subcategory:
          return HttpResponse(f"You have choosen category {category} and subcategory {subcategory}")
     else:
          return HttpResponse(f"You have choosen category {category} and no subcategory")

def blog(request, post_slug=None):
     if post_slug:
          return HttpResponse(f"Blog Post: {post_slug}")
     else:
          return HttpResponse("Blog Home Page")
#Error handling - in settings.py line no 26 set Debug = False and Allowed host mein khali ki jgh ["*"]
#go to myproject -> create views.py ->write code -> and open url.py of same folder and write handler404 = 'myproject.views.handler404'  # Custom 404 error handler at end
#

#simulate divide by zero error
def dividebyzero(request):
     a=10
     result=a/0
     return HttpResponse(f"Result is {result}")

def handler500(request, exception):
     return HttpResponse("<h1 style=color:red> Internal Server Error. Please try again later.</h1>", status=500)

def mytemplate(request):
     data={'name':'Neha'}
     return render(request, 'test.html', data)

def fooddata(request):
     newmenu = [
          {'name':'pizza', 'price':500},
          {'name':'burger', 'price':200},
          {'name':'sandwich', 'price':150},
          {'name':'pasta', 'price':300},
     ]
     return render(request, 'menu.html', {'menu':newmenu})

#Create a function that creates a list of dictionaries having food items with keys as "name" and "price".
#render the items as an html table using DTL. Also the background color of the free items should be pink.
def foodfree(request):
     newmenu = [
          {'name':'pizza', 'price':500},
          {'name':'burger', 'price':200},
          {'name':'sandwich', 'price':150},
          {'name':'pasta', 'price':300},
          {'name':'ice cream', 'price':'free'},
     ]
     return render(request, 'freemenu.html', {'menu':newmenu})

#the user must be able to pass the URL parameter as itemname and fetch the information of the specified item name.
def food_data(request, itemname):
     newmenu = [
          {'name':'pizza', 'price':500},
          {'name':'burger', 'price':200},
          {'name':'sandwich', 'price':150},
          {'name':'pasta', 'price':300},
          {'name':'ice cream', 'price':'free'},
     ]
     return render(request, 'find.html', {'menu':newmenu, 'itemname':itemname})


#-----------9 sep 2026 -------------------
def testimage(request):
     return render(request, 'testimage.html')

def productlist(request):
     products = [
          {name: 'product1', 'brand':'abc', 'price': 4000, 'image':'images/img1.webp'},
          {name: 'product2', 'brand':'xyz', 'price': 4500, 'image':'images/img3.jpg'},
          {name: 'product3', 'brand':'aaa', 'price': 6000, 'image':'images/img4.jpg'},
          {name: 'product4', 'brand':'aba', 'price': 6800, 'image':'images/img.png'},
     ]
     return render(request, 'products.html', {'product_list':products})


#----------10 sep 2026-------------------
def shoppinglist(request):
     products = [
          {'name': 'product1', 'brand':'abc', 'price': 4000, 'image':'images/img1.webp'},
          {'name': 'product2', 'brand':'xyz', 'price': 4500, 'image':'images/img3.jpg'},
          {'name': 'product3', 'brand':'aaa', 'price': 6000, 'image':'images/img4.jpg'},
          {'name': 'product4', 'brand':'aba', 'price': 6800, 'image':'images/img.png'},
     ]
     return render(request, 'shopping.html', {'product_list':products})

def shoppingdetails(request, shoppingitem):
     products = [
          {'name': 'product1', 'brand':'abc', 'price': 4000, 'image':'images/img1.webp'},
          {'name': 'product2', 'brand':'xyz', 'price': 4500, 'image':'images/img3.jpg'},
          {'name': 'product3', 'brand':'aaa', 'price': 6000, 'image':'images/img4.jpg'},
          {'name': 'product4', 'brand':'aba', 'price': 6800, 'image':'images/img.png'},
     ]
     return render(request, 'shoppingdetails.html', {'product_list':products, 'shopping_item':shoppingitem})


#--------------16 sep 2026 --------------------
#template inheritance ------- means that you can create a base template that contains the common 
# structure and layout of your website, and then create child templates that inherit from the
#  base template and override or extend specific blocks of content.
#----------header.html and base.html----------food home about.html--------templates

def home(request):
     return render(request, 'home.html')
def about(request):
     return render(request, 'about.html')
def food(request):
     newmenu = [
          {'name':'pizza', 'price':500, 'size':'medium','image':'images/pizza.jpg'},
          {'name':'burger', 'price':200, 'size':'small','image':'images/burger.jpg'},
          {'name':'sandwich', 'price':150, 'size':'large','image':'images/avocado-sandwich.jpg'},
     ]
     return render(request, 'food.html',{'menu':newmenu})

#--------------------17 sep 2026 --------------------
#-------------------created css folder in static folder and created styles.css file in it and added some css code in it. then added testcss.html in temolates.
def testcss(request):
     return render(request, 'testcss.html')

def items(request):
     products = [
          {'name': 'pizza'},
          {'name': 'burger'},
          {'name': 'sandwich'},
          {'name': 'moisturizer'},
     ]
     return render(request, 'items.html', {'products':products})
def itemdetails(request, name):
     products = {
          'pizza':{'size':'medium','price':500,'image':'images/pizza.jpg'},
          'burger':{'size':'small','price':200,'image':'images/burger.jpg'},
          'sandwich':{'size':'large','price':150,'image':'images/avocado-sandwich.jpg'},
          'moisturizer':{'size':'medium','price':100,'image':'images/img1.webp'},
     }
     item = products.get(name)
     if item:
          return render(request, 'itemdetails.html', {'name':name, 'size':item['size'], 'price':item['price'], 'image':item['image']})

#forms
# Forms in Django
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def simpleform(request):
    if request.method == "GET":
        htmlform="""
        <form method="POST">    
            <input type="text"  name="textbox1"><br><br>
            <input type="text"  name="textbox2"><br><br>
            <input type="submit">
        </form>
        """
        return HttpResponse(htmlform)
    else:
        t1=request.POST.get("textbox1")
        t2=request.POST.get("textbox2")

        return HttpResponse(f"Textbox1: {t1}, Textbox2: {t2}")



from django.middleware.csrf import get_token
def simpleform1(request):
    csrf_token= get_token(request)
    if request.method == "GET":
        htmlform=f"""
        <form method="POST">  
            <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
            <input type="text"  name="textbox1"><br><br>
            <input type="text"  name="textbox2"><br><br>
            <input type="submit">
        </form>
        """
        return HttpResponse(htmlform)
    else:
        t1=request.POST.get("textbox1")
        t2=request.POST.get("textbox2")

        return HttpResponse(f"Textbox1: {t1}, Textbox2: {t2}")



from django.middleware.csrf import get_token

def simpleform2(request):
    csrf_token= get_token(request)
    if request.method == "POST":
        try:
            num1 = int(request.POST.get("num1"))
            num2 = int(request.POST.get("num2"))

            result = num1 + num2

            return HttpResponse(f"""
                <h2>Result: {result}</h2>
                <a href="/simpleform2/">Go Back</a>
            """)

        except ValueError:
            return HttpResponse(f"""
                <h2>Please enter valid numbers!</h2>
                <a href="/simpleform2/">Go Back</a>
            """)

    return HttpResponse(f"""
        <h2>Add Two Numbers</h2>

        <form method="POST">
            <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
            <input type="text" name="num1" placeholder="Enter first number">
            <br><br>

            <input type="text" name="num2" placeholder="Enter second number">
            <br><br>

            <input type="submit" value="Add">
        </form>
    """)

# Post Redirect refresh pattern
from django.middleware.csrf import get_token
def success(request):
    return render(request, 'success.html')

def simpleform3(request):
    csrf_token= get_token(request)
    if request.method == "POST":
        t1 = request.POST.get("textbox1")
        t2 = request.POST.get("textbox2")

        return redirect("success")

    else:
        return HttpResponse(f"""

        <form method="POST">
            <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
            Name:<input type="text" name="textbox1" >
            <br><br>

            Email:<input type="text" name="textbox2">
            <br><br>

            <input type="submit" value="submit">
        </form>
        """)

def htmlform(request):
     if request.method == "POST":
          name=request.POST.get("name")
          email=request.POST.get("email")
          password=request.POST.get("password")
          if name and email and password:
               return HttpResponse(f"Form submitted successfully.<br> The details are:<br> Name: {name}, Email: {email}, Password: {password}")

          else:
               return HttpResponse("Please fill all the fields.")
     else:
          return render(request, 'htmlform.html')


def validate(request):
     submitted_details=None
     if request.method == "POST":
          name=request.POST.get("name")
          email=request.POST.get("email")
          password=request.POST.get("password")

          name_error = None
          email_error = None
          password_error = None

          if not name:
               name_error = "Name is required."

          if not email:
               email_error = "Email is required."

          if not password or len(password)<6:
               password_error = "Password should be at least 6 characters long."
          if name_error or email_error or password_error:
               return render(request, 'validate_form.html', {
                    'name': name,
                    'email': email,
                    'password': password,
                    'name_error': name_error,
                    'email_error': email_error,
                    'password_error': password_error,
               })
          submitted_details = {
               'name': name,
               'email': email,
               'password': password,
          }
     return render(request, 'validate_form.html', {'submitted_details': submitted_details})     



#--------------------------22 oct 2026----------------------
#django forms -----we will create a file in myapp folder named forms.py and write code in it.
#  then we will import that form in views.py and use it in our view function.

from .forms import InputForm1
def form_submission(request):
     if request.method == "POST":
          form = InputForm1(request.POST)
          if form.is_valid():
               return HttpResponse(f"Form submitted successfully.")
     form = InputForm1()
     return render(request, 'InputForm1.html', {'form': form})


# from .forms import InputForm2
# def form_submission2(request):
#      submitted_details=None
#      if request.method == "POST":
#           form = InputForm2(request.POST, request.FILES)
#           if form.is_valid():
#                submitted_details = form.cleaned_data #for getting the submitted data from the form and errors
#      form = InputForm2()
#      return render(request, 'InputForm2.html', {'form': form, 'submitted_details': submitted_details})
from  .forms import InputForm2
def form_submission2(request):
    submitted_details = None
    if request.method == 'POST':
        form = InputForm2(request.POST, request.FILES)
        if form.is_valid():
            submitted_details = form.cleaned_data
    else:
        form = InputForm2()
    return render(request, 'inputform2.html', {'form':form, 'submitted_details':submitted_details})


#----------28 oct 2026-------------------

# Create your models here.
# we creae a class and migration file in model 
# 1: create a class for model
# 2: create a migration file ( python manage.py makemigrations)
# 3: migrate the migration file( python manage.py migrate)

# After all this, the table will be created 
# we will use sqlite(install extension SQLite viewer in VS code)

#after writing python manage.py shell, we can use the following commands to interact with the database:
# from myapp.models import Emp
# Emp.objects.all()
# Emp.objects.create(firstname='Ayush',lastname='kumar',salary=56000,age=34)


#---------------29 oct 2026-------------------
#for updating the record we can use the following commands:>>> from myapp.models import Emp
#python manage.py shell
#from myapp.models import Emp
#>>> e = Emp.objects.get(pk=2)
#>>> e.salary = 54000
#>>> e.save()

#to delete the record we can use the following commands:
#python manage.py shell
#>>> from myapp.models import Emp
#>>> e = Emp.objects.get(pk=1)
#>>> e.delete()

#django admin panel is a built-in feature of Django that provides a web-based interface for managing the data in your application.
#  It allows you to perform CRUD (Create, Read, Update, Delete) operations on your models without writing any additional code.
#commands
#python manage.py createsuperuser
#python manage.py runserver
#admin name= neha
#password= 123
#python manage.py runserver
#localhost:8000/admin

#file= myenv/myproject/myapp/admin.py

from .forms import Blogpostform
def insertblogpost(request):
    blog_created = False
    form = Blogpostform()
    if request.method == 'POST':
        form = Blogpostform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            blog_created = True
    else:
        form = Blogpostform()
    return render(request, 'insertblogpost.html', {'form': form, 'blog_created': blog_created})

from .models import Blogpost
def blogposts(request):
     posts = Blogpost.objects.all()
     return render(request, 'blogposts.html', {'posts': posts})


def blogpost_detail(request,id):
     post=Blogpost.objects.get(id=id)
     return render(request, 'blogpost_detail.html', {'post': post})


#----------------cookies-------------------
def set_cookie(request):
    response = HttpResponse("Cookie has been Set")
    response.set_cookie('name', 'Neha', max_age=15)  # Cookie expires in 1 hour in seconds
    response.set_cookie('email', 'neha@example.com', max_age=15)
    return response


def get_cookie(request):
     value1 = request.COOKIES.get('name')
     value2 = request.COOKIES.get('email') 
     if(value1 or value1):
          return HttpResponse(f"The Cookie Value: {value1}, {value2}")
     else:
          return HttpResponse("Cookie not found.")

#Create threee views name as cookieview1, cookieview2,cookieview3 that set the cookie names "last_page" 
# to values "Page1", "Page2" and "Page3" respectively and also create responding URLS for the same. Now create a view named LastVisitedPage and fetch the last visited page via cookie and also create a corresponding URL for the same.
