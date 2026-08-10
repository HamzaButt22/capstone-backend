# capstone-backend

A high-performance asynchronous web server backend repository built on FastAPI and Uvicorn, exposing NLP text processing and Computer Vision AI modules as scalable REST API endpoints.

## 📅 Project Version History
- **Week 6**
   - [Day 1 Code Version](https://github.com/HamzaButt22/capstone-backend/blob/899cbac1a93e9242dc15d65e09d1aa226f9c9728/main.py) — Initialized the asynchronous FastAPI backend environment and local web routing systems.
   - [Day 2 Code Version](https://github.com/HamzaButt22/capstone-backend/blob/87bb7dc7292daede660320345e7e8bf2d602fd13/main.py) — Implemented asynchronous file ingestion multi-part streams and deployed the resume parser endpoint.

---

## Week 6

### Day 1 Milestone
- Initialized local workspace tracking environments for Project #4 (Capstone Backend).
- Configured local development servers using high-performance asynchronous execution wrappers.
- Implemented baseline web routing architectures returning structured JSON metadata payloads.

#### Features Built Day 1
- Bootstrapped an active REST API web gateway using Scikit-Learn/FastAPI application objects (`FastAPI()`).
- Developed a synchronous root-index router mapping (`@app.get("/")`) handling data state responses.
- Configured a local hot-reloading development server profile via the Uvicorn ASGI application server (`uvicorn main:app --reload`).

### Day 2 Milestone
- Developed an asynchronous web file upload ingestion endpoint to dynamically process unstructured multi-part document streams.
- Integrated modular custom Natural Language Processing (NLP) functions into core web routing layers.
- Conducted interactive data pipeline testing utilizing automatic Swagger UI schema frameworks.

#### Features Built Day 2
- Configured multi-part media upload handlers utilizing FastAPI data parameters (`UploadFile = File(...)`).
- Engineered local disk write buffers utilizing `shutil.copyfileobj()` to securely stage files for processing.
- Implemented robust operational safety frameworks using `try/finally` blocks to guarantee immediate temp file cleanup.
- Refactored core legacy script entries to protect runtime execution environments from layout-aware path failures.

---

## ⚙️ How to Run and Test the API Backend

### 1. Installation & Setup
Ensure you have the required backend dependency modules installed in your Python environment:
```bash
pip install fastapi uvicorn python-multipart spacy pdfplumber
python3 -m spacy download en_core_web_sm
```

### 2. Boot Up the Local Server
Launch your Uvicorn application server engine inside your root project folder:
```bash
uvicorn main:app --reload
```

### 3. Accessing the Interactive API Documentation Dashboard
By design, backend web endpoints process structured data behind the scenes. To visually test your multi-part upload routes without complex manual scripts, FastAPI generates an interactive schema portal:
- Open your browser and navigate to the dedicated testing path: **`http://127.0.0`**
- This loads the **Swagger UI Dashboard**, exposing an explicit blueprint of all active endpoints.
- Expand the **`POST /analyze-resume`** panel, click **"Try it out"**, attach a valid mock resume PDF, and click **"Execute"** to view live runtime analytical JSON response matrices.