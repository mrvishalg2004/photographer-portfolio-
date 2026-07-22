import os
import glob

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RG_CREATION - Gallery</title>
    <!-- font awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta2/css/all.min.css" integrity="sha512-YWzhKL2whUzgiheMoBFwW8CKV4qpHQAEuvilg9FAn5VJUDwKZZxkJNuGM4XkWuk94WCrrwslk8yWNGmY1EduTA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <link rel="stylesheet" href="css/style.css">
    <style>
        .gallery-header {
            padding: 4rem 0;
            text-align: center;
            background-color: var(--dark-color);
            color: var(--light-color);
        }
        .gallery-header h1 {
            color: var(--light-color);
            margin-bottom: 1rem;
        }
        .gallery-container {
            padding: 5rem 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }
        .masonry-grid {
            column-count: 1;
            column-gap: 1.5rem;
        }
        @media(min-width: 576px){
            .masonry-grid { column-count: 2; }
        }
        @media(min-width: 768px){
            .masonry-grid { column-count: 3; }
        }
        @media(min-width: 1200px){
            .masonry-grid { column-count: 4; }
        }
        .masonry-item {
            break-inside: avoid;
            margin-bottom: 1.5rem;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            transition: var(--transition);
            cursor: pointer;
        }
        .masonry-item img {
            width: 100%;
            display: block;
            transition: transform 0.5s ease;
        }
        .masonry-item:hover img {
            transform: scale(1.05);
        }
        .back-btn {
            display: inline-block;
            margin-top: 2rem;
            padding: 1rem 2.5rem;
            background-color: var(--light-color);
            color: var(--dark-color);
            border-radius: 3rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
            transition: var(--transition);
        }
        .back-btn:hover {
            background-color: #f0f0f0;
            transform: translateY(-3px);
        }

        /* Lightbox styling */
        #lightbox {
            display: none;
            position: fixed;
            z-index: 9999;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.9);
            align-items: center;
            justify-content: center;
        }
        #lightbox img {
            max-width: 90%;
            max-height: 90%;
            box-shadow: 0 0 20px rgba(0,0,0,0.5);
            border-radius: 5px;
        }
        #lightbox:target {
            display: flex;
        }
        .lightbox-close {
            position: absolute;
            top: 20px;
            right: 30px;
            color: white;
            font-size: 40px;
            font-weight: bold;
            cursor: pointer;
            text-decoration: none;
        }
    </style>
</head>
<body>

    <header class="gallery-header">
        <div class="container">
            <h1>Complete Portfolio</h1>
            <p class="lead">A collection of our latest captures and moments.</p>
            <a href="index.html" class="back-btn"><i class="fas fa-arrow-left"></i> Back to Home</a>
        </div>
    </header>

    <main class="gallery-container">
        <div class="masonry-grid">
            {images}
        </div>
    </main>

    <div id="lightbox">
        <a href="#!" class="lightbox-close">&times;</a>
        <img id="lightbox-img" src="" alt="Expanded Image">
    </div>

    <!-- footer -->
    <footer id="footer" class="py-7">
        <div class="container">
            <div class="footer-content">
                <div>
                    <h3>Raju Giri </h3>
                    <div><img src="images/about-pic.png" alt=""></div>
                </div>
                <div>
                    <h3>Links</h3>
                    <ul class="flex">
                        <li><a href="index.html#about">About Me</a></li>
                        <li><a href="index.html#work">Work</a></li>
                        <li><a href="gallery.html">Portfolio</a></li>
                        <li><a href="index.html#contact">Contact Me</a></li>
                    </ul>
                </div>
            </div>
        </div>
    </footer>
    
    <!-- Footer -->
    <footer class="py-3 text-center">
        <p>&copy; 2024 Developed By durga roy and Vishal</p>
    </footer>

    <script>
        const lightbox = document.getElementById('lightbox');
        const lightboxImg = document.getElementById('lightbox-img');
        
        document.querySelectorAll('.masonry-item').forEach(item => {
            item.addEventListener('click', function() {
                const imgSrc = this.querySelector('img').getAttribute('src');
                lightboxImg.setAttribute('src', imgSrc);
                lightbox.style.display = 'flex';
            });
        });

        document.querySelector('.lightbox-close').addEventListener('click', function(e) {
            e.preventDefault();
            lightbox.style.display = 'none';
        });

        lightbox.addEventListener('click', function(e) {
            if (e.target !== lightboxImg) {
                lightbox.style.display = 'none';
            }
        });
    </script>
</body>
</html>
"""

import fnmatch

def find_images(directory):
    matches = []
    extensions = ['*.jpg', '*.jpeg', '*.png', '*.webp', '*.gif', '*.JPG', '*.JPEG', '*.PNG', '*.WEBP', '*.GIF']
    for root, dirnames, filenames in os.walk(directory):
        for ext in extensions:
            for filename in fnmatch.filter(filenames, ext):
                matches.append(os.path.join(root, filename))
    return matches

images = find_images('images/New photos')
images.sort()

image_tags = []
for img in images:
    # Escape quotes if necessary, though mostly not needed
    img_path = img.replace('"', '&quot;')
    tag = f'<div class="masonry-item"><img src="{img_path}" alt="Gallery Image" loading="lazy"></div>'
    image_tags.append(tag)

final_html = html_template.replace('{images}', '\n            '.join(image_tags))

with open('gallery.html', 'w') as f:
    f.write(final_html)

print(f"Generated gallery.html with {len(images)} images.")
