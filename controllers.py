from extensions import *
from flask import render_template, request, redirect
from app import app
from models import *
from forms import *
from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash



@app.route("/")
def index():
    r = Books.query.all()
    return render_template("homepage.html", active = 'index', books = r)


@app.route("/book/<int:id>", methods= ["GET", "POST"])
def book(id):
    form = Comment_section()
    book = Books.query.filter(Books.id == id).first()
    if form.validate_on_submit():
        commented_book = User_comment( username = form.username.data,
            user_comment = form.user_comment.data,
            book_id= id)
        db.session.add(commented_book)
        db.session.commit()
    user_comment = User_comment.query.filter(User_comment.book_id == id ).all()
    if form.errors != {}:
        for err_msg in form.errors.values():
            print(f"There was an error with commenting: {err_msg}")
    return render_template("book.html", _book = book, form = form, user_comment = user_comment)


@app.route("/product")
def product():
    home_active = False
    product_active = True
    book_name = "Inkognito (beynin gizli həyatı)"
    book_url = "https://fatimekerimli.files.wordpress.com/2016/09/41cj2rizml-_sx320_bo1204203200_.jpg"
    old_price = "12.00"
    new_price = "15.00"
    description = """Tanınmış nevroloq D.İqlmenin 20-dən çox dilə tərcümə edilən və indidən klassik asara çevrilən
                        bu kitabı beynin sirli dünyasına təcrübələr, elmi biliklər və tarixi faktlar işığında
                        səyahət edir. Kİtab tibbi mövzuda olsa da, müəllif yazarlıq məharətini və zəngin biliyini
                        birləşdirərək elmi faktları sadə və müqayisəli dillə oxucularına təqdim edir. Müəllif əsər
                        boyu sədaqət geni, qumarbazlara çevrilən parkinson xəstələri, gen-mühit əlaqəsi,yaxşı və
                        pis gen, şüuraltı və qərarvermə mexanizmi , məsuliyyət anlayışı, beynin insan həyatında
                        roıu kimi bir çox mövzulara toxunur. Alim bu mövzuların beyinlə əlaqəsini izah etməklə
                        kifayətlənmir, beyinlə bağlı müxtəlif formullar və modellər irəli sürür. İnsan psixologiyası
                        və davranışlarına neyron və gen prizmasından baxmağı öyrədir. Elmi-populyar dildə yazılmış
                        bu kitab xüsusən müəllimlər, psixoloqlar, valideynlər, həkimlər üçün mühüm bilikləri ehtiva
                        edir."""
    book_author = "David Eagleman"
    book_genre = "Psixologiya"
    published_at = "Qanun nəşriyyatı"
    book_language = "Azərbaycan"
    active = "active"
    return render_template("product.html", book_name = book_name,  book_url =  book_url, old_price = old_price, new_price = new_price, description = description, book_author = book_author, book_genre = book_genre, published_at = published_at, book_language = book_language, active = 'product')


@app.route("/register", methods= ["GET", "POST"])
def register():
    post_data = request.form
    form = Register()
    if request.method == "POST":
        form = Register(data = post_data)
        if form.validate_on_submit():
            x = User(username = form.username.data, name = form.name.data, surname = form.surname.data, email = form.email.data, password = form.password.data)
            x.save()
            return redirect("/login")
    return render_template("register.html", form = form)

@app.route("/login", methods= ["GET", "POST"])
def login():
    post_data = request.form
    form =  Login()
    if request.method == "POST":
        form = Login(data = post_data)
        if form.validate_on_submit():
            user = User.query.filter_by(username = form.username.data).first()
            if check_password_hash(user.password, form.password.data ):
                login_user(user) 
                return redirect("/")
    return render_template("login.html", form = form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')