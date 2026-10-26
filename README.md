# Huffman Encoding Lab

A web-based Huffman coding visualization and compression educational tool built with Python (Flask) and Vanilla JS/CSS.

## Features
- **Live Simulator:** See real-time bit savings and character-by-character Huffman token breakdown.
- **File Compression:** Compress `.txt` files into a custom binary format (`.huff` payload).
- **File Decompression:** Restore compressed payloads back to text and verify SHA-256 byte-for-byte correctness.
- **Experiment Suite:** Run multi-file benchmarks automatically across various sample datasets.

## Installation & Setup

### Prerequisites
- **Python 3.8+** (Ensure Python is added to your system PATH)

### Steps

1. **Download / Clone the Repository:**
   Open your terminal and navigate to the project folder.

2. **Create a Virtual Environment (Optional but Recommended):**
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On Mac/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   The only external dependency for the web application is Flask.
   ```bash
   pip install Flask
   ```

4. **Run the Application:**
   Start the local development server:
   ```bash
   python app.py
   ```

5. **Open in Browser:**
   Navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) in your preferred web browser.

## Running Tests
To verify the Huffman engine and API functionality, you can run the included test files:
```bash
python -m unittest test_huffman.py
python test_api_endpoints.py
```

## Deploying to Vercel

This repository is pre-configured for seamless deployment to Vercel as a Python Serverless Function.

### Option 1: Via Vercel Dashboard (Recommended)
1. Push your repository to GitHub, GitLab, or Bitbucket.
2. Go to [Vercel](https://vercel.com/) and click **Add New Project**.
3. Import your repository. Vercel will automatically detect `vercel.json`, `requirements.txt`, and `api/index.py`.
4. Click **Deploy**.

### Option 2: Via Vercel CLI
1. Install the Vercel CLI globally:
   ```bash
   npm install -g vercel
   ```
2. Run preview locally:
   ```bash
   vercel dev
   ```
3. Deploy to production:
   ```bash
   vercel --prod
   ```

