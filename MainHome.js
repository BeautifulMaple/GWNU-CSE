// Sample photo data for each date
const photoData = {
    '2024.03.01': ['photo1_thumb.jpg', 'photo2.jpg', 'photo3.jpg'],
    '2024.03.02': ['photo4.jpg', 'photo5.jpg'],
    '2024.03.03': ['photo6.jpg', 'photo7.jpg', 'photo8.jpg'],
    // Add more dates and photos as needed
};

// Function to load photos in the gallery based on the selected date
function loadGallery(date) {
    const gallery = document.getElementById("photoGallery");
    gallery.innerHTML = ''; // Clear current photos

    if (photoData[date]) {
        photoData[date].forEach(photo => {
            const img = document.createElement('img');
            img.src = `path/to/photos/${photo}`; // Update with actual photo path
            gallery.appendChild(img);
        });
    } else {
        gallery.innerHTML = '<p>No photos available for this date.</p>';
    }
}
