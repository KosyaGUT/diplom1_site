// const menuToggle = document.getElementById('menu-toggle');
// const nav = document.getElementById('nav');
//
// menuToggle.addEventListener('click', () => {
//     nav.classList.toggle('active');
// });

function toggleSidebar() {
    const container = document.querySelector('.container');
    container.classList.toggle('open'); // Добавляем/убираем класс 'open'
}

function closeSubMenu() {
    const submenus = document.querySelectorAll('.submenu');
    submenus.forEach(submenu => {
        submenu.style.display = 'none'; // Закрываем все подменю
    });
}

document.querySelectorAll('.dropdown > span').forEach(item => {
    item.addEventListener('click', function () {
        const submenu = this.nextElementSibling;
        if (submenu.style.display === 'flex') {
            submenu.style.display = 'none';
        } else {
            submenu.style.display = 'flex';
        }
    });
});


