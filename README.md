**Content-Based Image Retrieval (CBIR)**
Content-Based Image Retrieval (CBIR) is a Python-based image search engine developed as part of my undergraduate coursework (B.Tech in Computer Science, 2016). Think of it as an early, simplified version of Google Image Search — without the reasoning or learning capabilities available in modern tools today (as of 2025).

**🔍 What It Does**
CBIR enables users to search for similar images by comparing visual features directly from the image itself — not using any metadata or tags. It uses color histograms as the core image descriptor to identify and rank similar images in a dataset using digital image processing concepts like Histograms of a digital image and Chi-squared distance algorithm to find similarity between images.

Given a query image, the system returns a set of images from the database ranked by their similarity (from most to least similar) based purely on color proximity.

**🧠 Key Features**
Searches images based on visual content (color histogram)

No metadata, tags, or text input required

Displays search results in descending order of similarity

Lightweight and easy to extend for other feature types (e.g., texture, shape)

**🛠️ Technologies Used**
Python

OpenCV (for image processing and histogram generation)

**📁 Project Structure**
CBIR/
├── src/
│   ├── dataset/          # Image dataset used for training and retrieval
│   ├── index.py          # Indexing logic for feature extraction
│   ├── search.py         # Search algorithm using histogram comparison
│   └── query.py          # Entry point for querying an image
└── README.md

**📌 Value Proposition**
In an era (2016) before consumer-grade deep learning image APIs were widely accessible, CBIR showcases the potential of traditional computer vision techniques like histogram analysis to build functional visual search systems.

**📂 Dataset** 
The image dataset used for training and testing is located at:

bash
Copy
Edit
CBIR/src/dataset/

**✅ How to Run**
Clone the repository

Install dependencies:

nginx
Copy
Edit
pip install opencv-python
Place your query image in the src/ directory

Run the query script:

arduino
Copy
Edit
python query.py --image your_query_image.jpg
Let me know if you'd like to include sample images, results, or screenshots!
