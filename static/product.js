const hand = document.querySelector('.fa-thumbs-up');
const heart = document.querySelector('.fa-heart');
const dropDownMenu = document.querySelector('#drop-down-menu');
const totalPrice = document.querySelector('#totalPrice');
const elaveEdilenKitabSayi = document.querySelector('#elaveEdilenKitabSayi');
const myModal = document.querySelector('.myModal');
const mehsul = document.querySelector('#mehsul');
const warning = document.querySelector('#warning');
const qalanKitabSayi = document.querySelector('#qalanKitabSayi');


let arr = [
    {
        id: 1,
        title: '1984',
        price: 16
    },
    {
        id: 2,
        title: "Səfillər",
        price: 21
    }
];


let obj = {
    id: 3,
    title: 'Incignito',
    price: 12
};


myModal.addEventListener('click', (event) => {
    if (myModal.style.backgroundColor == 'gray') {
        event.target.style.backgroundColor = '#2FA3B8';
        event.target.innerText = 'Səbətə əlavə et';
        mehsul.innerText = 'Məhsul səbətdən çıxarıldı';
        warning.classList.remove('alert-danger');
        warning.classList.add('alert-warning');
        qalanKitabSayi.innerText = 2;
        arr.pop(obj);
        yaz();
    } else {
        event.target.style.backgroundColor = 'gray';
        event.target.innerHTML = 'Səbətdən çıxart';
        mehsul.innerText = 'Məhsul səbətə əlavə edildi';
        warning.classList.remove('alert-warning');
        warning.classList.add('alert-danger');
        qalanKitabSayi.innerText = 1;
        arr.push(obj);
        yaz();
    };
});


function removeElement(thisId) {
    arr = arr.filter(({ id }) => id !== thisId);
    yaz();
    if (thisId == 3) {
        myModal.style.backgroundColor = "#2FA3B8";
        myModal.innerText = "Səbətə əlavə et";
        qalanKitabSayi.innerText = 2;
        warning.classList.remove('alert-danger');
        warning.classList.add('alert-warning');
    };
};


function yaz() {
    let string = '';
    let sum = 0;

    arr.forEach(({ id, title, price }) => {
        string += `
        <li class="">
            <a class="dropdown-item d-flex justify-content-between align-items-center py-1" href="#">
                <i onclick="removeElement(${id})" class="bi bi-x-circle-fill text-danger me-1"></i>
                <div class="d-flex justify-content-between align-items-center" style="flex: 1;">
                    <p class="mb-0">${title}</p>
                    <p class="mb-0">${price} AZN</p>
                </div>
            </a>
        </li>
        ` + "\n";
        sum += price;
    });
    dropDownMenu.innerHTML = string;
    totalPrice.innerHTML = sum + ' AZN';
    if (arr.length !== 0) {
        elaveEdilenKitabSayi.innerHTML = arr.length;
    } else {
        elaveEdilenKitabSayi.innerHTML = '';
    };
};
yaz();


heart.style.color = 'gray';
heart.addEventListener('click', (event) => {
    if (heart.style.color == 'gray') {
        event.target.style.color = 'red';
        alert('Kitabı bəyəndiniz!');
    } else {
        event.target.style.color = 'gray';
        alert('Bəyənməkdən imtina etdiniz!');
    };
});


hand.style.color = 'blue';
hand.addEventListener('click', (event) => {
    if (hand.classList.contains('fa-thumbs-up')) {
        event.target.classList.remove('fa-thumbs-up');
        event.target.classList.add('fa-thumbs-down');
    } else {
        event.target.classList.add('fa-thumbs-up');
        event.target.classList.remove('fa-thumbs-down');
    };
});

$('.slick-slider').slick({
    infinite: true,
    slidesToShow: 4,
    centerMode: true,
    variableWidth: true
});