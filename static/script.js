// Image preview and upload functionality
const imageInput = document.getElementById('imageInput');
const uploadBox = document.getElementById('uploadBox');
const previewImg = document.getElementById('previewImg');
const emptyPreview = document.getElementById('emptyPreview');

// Handle file input change
imageInput.addEventListener('change', function(e) {
  const file = e.target.files[0];
  if (file) {
    displayImagePreview(file);
  }
});

// Click to upload
uploadBox.addEventListener('click', () => {
  imageInput.click();
});

// Drag over effect
uploadBox.addEventListener('dragover', (e) => {
  e.preventDefault();
  uploadBox.style.borderColor = '#667eea';
  uploadBox.style.transform = 'translateY(-5px)';
});

// Drag leave effect
uploadBox.addEventListener('dragleave', () => {
  uploadBox.style.borderColor = 'rgba(255, 255, 255, 0.1)';
  uploadBox.style.transform = 'translateY(0)';
});

// Drop handler
uploadBox.addEventListener('drop', (e) => {
  e.preventDefault();
  uploadBox.style.borderColor = 'rgba(255, 255, 255, 0.1)';
  uploadBox.style.transform = 'translateY(0)';
  
  const file = e.dataTransfer.files[0];
  if (file && file.type.startsWith('image/')) {
    // Update the file input
    imageInput.files = e.dataTransfer.files;
    displayImagePreview(file);
  }
});

// Function to display image preview
function displayImagePreview(file) {
  const reader = new FileReader();
  reader.onload = function(event) {
    previewImg.src = event.target.result;
    previewImg.style.display = 'block';
    emptyPreview.style.display = 'none';
  };
  reader.readAsDataURL(file);
}

// Smooth scroll to results if they exist
window.addEventListener('load', () => {
  const resultsSection = document.querySelector('.results-section');
  if (resultsSection) {
    setTimeout(() => {
      resultsSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 300);
  }
});