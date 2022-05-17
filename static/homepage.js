let arr = [{
    url: "https://fatimekerimli.files.wordpress.com/2016/09/41cj2rizml-_sx320_bo1204203200_.jpg",
    title: 'Inkognito',
    author: 'David Eagleman'
},
{
    url: "https://static.insales-cdn.com/files/1/5920/9262880/original/large_5387fd1b8dd9bd9524cc0177110771a0.jpg",
    title: 'Səfillər',
    author: 'Viktor Hugo'
},
{
    url: "https://image.winudf.com/v2/image/Y29tLmNvc21vZHJvbmUuYm9vay5BT1ZTUEZBVkZaQ0FSWVdHTF9zY3JlZW5zaG90c18wX2RlOTUxZWRl/screen-0.jpg?fakeurl=1&type=.jpg",
    title: "Dostoyevski",
    author: "Cinayət və Cəza"
},
{
    url: "https://upload.wikimedia.org/wikipedia/az/e/e1/%C3%87%C9%99rp%C9%99l%C9%99ng_u%C3%A7uran.jpeg",
    title: "Çərpələng Uçuran",
    author: "Xalid Hüseyni"
},
{
    url: 'https://upload.wikimedia.org/wikipedia/az/8/85/%C6%8Flamut_%28Vladimir_Bartol%29.jpg',
    title: "Əlamut",
    author: "Bartol"
},
{
    url: "https://m.media-amazon.com/images/I/51Sn8PEXwcL.jpg",
    title: "Sapiens",
    author: "Harari"
}];
let counter = 0;
$('#plus').click(function x() {
    var index = Math.floor(Math.random() * arr.length);
    if ($('#books #lastDiv p').last().text() !== arr[index]["author"]) {
        $('#books').append(`
            <div id="lastDiv" class="card mb-5 p-0" style="width: 12rem; margin-left: 58px; margin-right: 58px;">
                <img src="${arr[index]['url']}" class="card-img-top">
                <div class="card-body">
                    <h6 class="card-title">${arr[index]["title"]}</h6>
                    <p class="card-text">${arr[index]["author"]}</p>
                    <a href="#" class="btn text-light" style="background-color: #2FA3B8;">Ətraflı</a>
                </div>
            </div>`)
        counter += 1;
        $('#bookCounter').val(counter);
    } else {
        x()
    }
});
$('#minus').click(() => {
    counter -= 1;
    if (counter < 0) {
        $('#bookCounter').val(0);
        counter = 0;
    } else {
        $('#bookCounter').val(counter);
    }
    $('#books #lastDiv').last().remove();
});
$('#start').click(() => {
    $('#start').hide();
    $('#hideShow').removeClass('d-none');
    $('#alertshow').text('');
    $('#num1').val('');
    $('#num2').val('');
});
$('#end').click(() => {
    $('#start').show();
    $('#hideShow').addClass('d-none');
});
$('#count').click(() => {
    $('#alertshow').text('');
    if ($('#num1').val() <= 0 || $('#num2').val() <= 0) {
        $('#alertshow').append(`
            <div class="alert alert-danger my-4" role="alert">Hesablamada xəta baş verdi!</div>
        `);
    } else {
        let result = Math.ceil($('#num1').val() / $('#num2').val());
        $('#alertshow').append(`
            <div class="alert alert-success my-4" role="alert">Hər gün ən az <b class="fs-3">${result}</b> səhifə oxumalısınız!</div>
        `);
    };
});