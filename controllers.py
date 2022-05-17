from flask import render_template
from app import app
from models import *



@app.route("/")
def index():
    r = Books.query.all()
    return render_template("homepage.html", active = 'index', books = r)

@app.route("/book/<int:id>")
def book(id):
    book = Books.query.filter(Books.id == id).first()
    return render_template("book.html", _book = book)


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