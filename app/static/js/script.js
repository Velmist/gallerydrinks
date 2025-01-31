document.addEventListener('DOMContentLoaded', function() {
    const images = document.querySelectorAll('.img-preview');
    images.forEach(img => {
        img.addEventListener('click', function() {
            const largeImage = document.createElement('img');
            largeImage.src = this.src;
            largeImage.classList.add('img-large');

            const overlay = document.createElement('div');
            overlay.style.position = 'fixed';
            overlay.style.top = '0';
            overlay.style.left = '0';
            overlay.style.width = '100%';
            overlay.style.height = '100%';
            overlay.style.backgroundColor = 'rgba(0, 0, 0, 0.8)';
            overlay.style.display = 'flex';
            overlay.style.justifyContent = 'center';
            overlay.style.alignItems = 'center';
            overlay.style.zIndex = '1000';
            overlay.appendChild(largeImage);

            overlay.addEventListener('click', function() {
                document.body.removeChild(overlay);
            });

            document.body.appendChild(overlay);
        });
    });
});