// header
document.querySelector('.hamburger-menu').addEventListener('click', () => {
    document.querySelector('.nav-links').classList.toggle('active');
});

// hero
new Glide('.glide', {
    type: 'carousel',
    autoplay: 5000, // Autoplay delay in milliseconds
}).mount();
