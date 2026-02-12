function openCol3() {
    if (window.innerWidth <= 768) {
        document.getElementById('col3-container').classList.add('active');
        document.getElementById('toggleBtn').classList.add('active');  // این خط رو اضافه کن
        document.getElementById('backBtn').classList.add('active');
    }
}

function closeCol3() {
    document.getElementById('col3-container').classList.remove('active');
    document.getElementById('toggleBtn').classList.remove('active');  // این خط رو اضافه کن
    document.getElementById('backBtn').classList.remove('active');
}

// اطمینان حاصل کن که وقتی صفحه لود میشه، دکمه هست
document.addEventListener('DOMContentLoaded', function() {
    if (window.innerWidth <= 768) {
        document.getElementById('toggleBtn').style.display = 'block';
    }
});