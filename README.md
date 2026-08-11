# capstone-backend

A high-performance asynchronous web server backend repository built on FastAPI and Uvicorn, exposing NLP text processing and Computer Vision AI modules as scalable REST API endpoints.

## 📅 Project Version History
- **Week 6**
   - [Day 1 Code Version](https://github.com/HamzaButt22/capstone-backend/blob/899cbac1a93e9242dc15d65e09d1aa226f9c9728/main.py) — Initialized the asynchronous FastAPI backend environment and local web routing systems.
   - [Day 2 Code Version](https://github.com/HamzaButt22/capstone-backend/blob/87bb7dc7292daede660320345e7e8bf2d602fd13/main.py) — Implemented asynchronous file ingestion multi-part streams and deployed the resume parser endpoint.
   - [Day 3 Code Version](https://github.com/HamzaButt22/capstone-backend/blob/f54987a74c6f50da414980273bbff5e52e3b194d/main.py) — Integrated modular OpenCV algorithms and deployed the asynchronous face-detection image parser endpoint.
   - [Day 4 Code Version](https://github.com/HamzaButt22/capstone-backend/blob/85ec3060bae9ef15e9d8d45982ea7352200fd9f6/main.py) — Engineered file validation constraint gates and custom HTTP exception handler routes across both endpoints.
   - [Day 5 Code Version](https://github.com/HamzaButt22/capstone-backend) — Finalized comprehensive integration cross-testing via terminal `curl` pipelines and deployed the complete backend architecture.

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

### Day 3 Milestone
- Integrated modular custom Computer Vision (CV) matrix calculations into asynchronous web routing structures.
- Developed an image ingestion gateway capable of standardizing multi-channel BGR spatial data streams via web requests.
- Verified system matrix output states side-by-side using automatic browser documentation interfaces.

#### Features Built Day 3
- Configured a dedicated media upload route utilizing the FastAPI post decorator (`@app.post("/analyze-image")`).
- Deployed asynchronous byte-stream file parsers using multi-part data tokens (`UploadFile = File(...)`).
- Integrated defensive `try/finally` block scopes ensuring the immediate deletion of buffered temporary images on disk.
- Refactored legacy computer vision print layers to protect modular server initialization pathways.

### Day 4 Milestone
- Engineered input data validation guard blocks intercepting incorrect client uploads prior to file system execution.
- Implemented defensive exception handlers mapping structural file properties to standard HTTP status codes.
- Conducted rigorous edge-case testing passing adversarial payloads through automated swagger panels.

#### Features Built Day 4
- Integrated native exception handling components utilizing FastAPI tracking classes (`HTTPException`).
- Built string suffix parsing filters checking low-level file parameters (`file.filename.lower().endswith()`).
- Configured rigid document type boundaries returning clean `400 Bad Request` states on non-PDF data uploads.
- Developed structural tuple verification indices checking multi-format image criteria strings (`.png`, `.jpg`, `.jpeg`).

### Day 5 Milestone
- Conducted exhaustive production integration testing via automated multi-part `curl` terminal operations.
- Compiled formal API blueprint design document parameters detailing active network methods and data contracts.
- Consolidated code versions and finalized the project backend workspace delivery.

#### Features Built Day 5
- Verified raw binary multi-part upload pathways over local loopback interfaces using explicit terminal command expressions.
- Developed standardized API contract schemas mapping out parameters, request signatures, and expected target outputs.
- Consolidated workspace scripts into clean, decoupled structures to ensure project deployment repeatability.

---

## 📋 Production API Reference Documentation

### 1. Root Server Status Entry
- **Endpoint Route:** `GET /`
- **Expected Success Output (`200 OK`):**
  ```json
  {
    "message": "Hello World",
    "status": "FastAPI Server Running Securely"
  }
  ```

### 2. Natural Language Processing Resume Analyzer
- **Endpoint Route:** `POST /analyze-resume`
- **Accepts Content-Type:** `multipart/form-data`
- **Required Param Fields:** `file: UploadFile` *(Strictly restricted to `.pdf` extensions)*
- **Expected Success Output (`200 OK`):**
  ```json
  {
    "filename": "resume_1.pdf",
    "status": "Success",
    "predicted_category": "Security Ops",
    "extracted_skills": ["safety", "defense", "security", "guard"]
  }
  ```
- **Expected Error Output (`400 Bad Request`):**
  ```json
  { "detail": "Invalid file type. Only PDF documents are permitted." }
  ```

### 3. Computer Vision Image Face Detection Engine
- **Endpoint Route:** `POST /analyze-image`
- **Accepts Content-Type:** `multipart/form-data`
- **Required Param Fields:** `file: UploadFile` *(PNG, JPG, or JPEG format types)*
- **Expected Success Output (`200 OK`):**
  ```json
  {
    "filename": "face_sample.jpeg",
    "status": "Success",
    "analysis": {
      "face_detected": true,
      "count": 1
    }
  }
  ```
- **Expected Error Output (`400 Bad Request`):**
  ```json
  { "detail": "Invalid image type. Only PNG, JPG, or JPEG formats are permitted." }
  ```

---

## ⚙️ How to Run and Test the API Backend

### 1. Installation & Setup
Ensure you have the required backend dependency modules installed in your Python environment:
```bash
pip install fastapi uvicorn python-multipart spacy pdfplumber opencv-contrib-python-headless
python3 -m spacy download en_core_web_sm
```

### 2. Boot Up the Local Server
Launch your Uvicorn application server engine inside your root project folder:
```bash
uvicorn main:app --reload
```

### 3. Accessing the Interactive API Documentation Dashboard
FastAPI automatically generates an interactive schema portal to test your endpoints visually:
- Open your browser and navigate to the dedicated testing path: **`http://127.0.0`**
- This loads the **Swagger UI Dashboard**, exposing an explicit blueprint of all active endpoints.
- **Testing Validation Routing:** Intentionally upload incorrect media attachments across endpoints to confirm the active exception-handling gates safely block execution and return clear `400 Bad Request` status blocks.

### 4. Testing via Terminal Command Lines
Open an independent secondary terminal window and execute direct `curl` data injections:
- **Test Resume Upload:**
  ```bash
  curl -X POST "http://127.0.0" -F "file=@/path/to/your/resume.pdf"
  ```
- **Test Image Face Detection:**
  ```bash
  curl -X POST "http://127.0.0" -F "file=@/path/to/your/image.jpeg"