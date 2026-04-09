
# 🎬 Netflix Data Analysis API

<p align="center">
  <b>A FastAPI-based analytics tool for Netflix content insights</b><br>
  Visualizations • PDF Reports • REST API • Data Analysis
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/FastAPI-Used-green?style=for-the-badge&logo=fastapi">
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-red?style=for-the-badge&logo=pandas">
  <img src="https://img.shields.io/badge/Matplotlib-Visualization-yellow?style=for-the-badge">
  <img src="https://img.shields.io/badge/Render-Deployed-purple?style=for-the-badge&logo=render">
  <img src="https://img.shields.io/badge/Status-Live%20✅-success?style=for-the-badge">
</p>

<p align="center">
  <b>🌐 Live Demo:</b> 
  <a href="https://netflix-data-api.onrender.com/docs">
    https://netflix-data-api.onrender.com
  </a>
</p>

---

## 🚀 Overview

**Netflix Data Analysis API** is a live REST API that analyzes Netflix content data and provides:

- 📊 **Visualizations** - Auto-generated charts saved as PNG
- 📑 **PDF Reports** - Simple reports with charts and descriptions  
- 🔌 **JSON Endpoints** - Raw data for external use
- 🧪 **Testing** - Basic pytest coverage

Built with **FastAPI**, this project uses:
- Standard function-based route handlers
- Pandas for data loading and analysis
- Matplotlib for chart generation
- FPDF for PDF creation

✅ **Now deployed and accessible worldwide on Render (Free Tier)**

---

## ✨ Features

### 🔍 Data Analysis
- ✅ Content Type Distribution (Movies vs TV Shows)
- ✅ Top 10 Producing Countries
- ✅ Yearly Release Trends (1942-2021)
- ✅ Rating Distribution Analysis
- ✅ Duration & Season Statistics

### 📈 Visualization Engine
- ✅ Matplotlib charts saved to `./images/`
- ✅ 300 DPI PNG exports
- ✅ On-demand generation if file missing

### 📄 PDF Report Generator
- ✅ Simple PDFs with embedded chart image
- ✅ Descriptive text below each chart
- ✅ Output files: `*_Report.pdf`

### 🔌 API Endpoints
- ✅ Visualization endpoints → return PNG images
- ✅ Report endpoints → return PDF files
- ✅ Summary endpoints → return JSON data
- ✅ Basic query parameter support (`top`, `from_year`, `to_year`)

---

## 🌐 Live Demo

### 🔗 Base URL
```
https://netflix-data-api.onrender.com
```

### 🧪 Try These Endpoints Now

```bash
# Home endpoint
curl https://netflix-data-api.onrender.com/

# Get JSON summary of content types
curl https://netflixodata-api.onrender.com/summary

# Download content distribution chart
curl https://netflix-data-api.onrender.com/content_distribution -o chart.png

# Download PDF report
curl https://netflix-data-api.onrender.com/report_content_distribution -o report.pdf

# Filter trends by year range
curl "https://netflix-data-api.onrender.com/trends?from_year=2018&to_year=2021"

# Get top 3 countries
curl "https://netflix-data-api.onrender.com/countries?top=3"
```

### 📚 Interactive API Docs
- **Swagger UI**: https://netflix-data-api.onrender.com/docs
- **ReDoc**: https://netflix-data-api.onrender.com/redoc

> ⏱️ *Note: Free tier instances spin down after 15 minutes of inactivity. First request may take ~30-60 seconds to respond.*

---

## 📸 Sample Outputs

### 📊 Content Distribution Chart
![Content Distribution](https://netflix-data-api.onrender.com/content_distribution)

### 📈 Yearly Trends
![Yearly Trends](https://netflix-data-api.onrender.com/yearly_trend)

### 🌍 Top Countries
![Top Countries](https://netflix-data-api.onrender.com/top_countries)

*(Images are generated on-demand — visit the URLs above to see live results)*

---

## ⚙️ Local Installation (Run It Yourself)

```bash
# Clone the repository
git clone https://github.com/SamratGhimire01/netflix-data-analysis.git
cd netflix-data-analysis

# Create virtual environment
python3 -m venv venv

# Activate environment
# Linux/macOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 📋 Requirements
- Python 3.9+
- FastAPI, Uvicorn
- Pandas, NumPy
- Matplotlib, FPDF2
- pytest

---

## ▶️ Local Usage

```bash
# Start the server
uvicorn main:app --reload

# Access locally at:
# http://localhost:8000
# http://localhost:8000/docs
```

---

## 🧠 API Endpoints Reference

### 📊 Visualization Endpoints (Images)

| Endpoint | Method | Description | Returns |
|----------|--------|-------------|---------|
| `/content_distribution` | GET | Movies vs TV Shows chart | PNG Image |
| `/yearly_trend` | GET | Release trends over time | PNG Image |
| `/top_countries` | GET | Top 10 producing countries | PNG Image |
| `/rating_distribution` | GET | Content rating breakdown | PNG Image |
| `/average-duration` | GET | Duration & seasons stats | PNG Image |

### 📄 Report Endpoints (PDFs)

| Endpoint | Method | Description | Returns |
|----------|--------|-------------|---------|
| `/report_content_distribution` | GET | Content distribution report | PDF |
| `/report_yearly_trend` | GET | Yearly trends analysis | PDF |
| `/report_top_countries` | GET | Country production report | PDF |
| `/report_rating_distribution` | GET | Rating demographics report | PDF |
| `/duration-report` | GET | Duration analysis report | PDF |

### 📈 Summary Endpoints (JSON)

| Endpoint | Method | Description | Parameters |
|----------|--------|-------------|------------|
| `/summary` | GET | Total movies & shows count | None |
| `/countries` | GET | Top producing countries | `top` (int, default: 10) |
| `/trends` | GET | Yearly release trends | `from_year`, `to_year` |
| `/ratings` | GET | Rating distribution | None |
| `/duration` | GET | Average duration stats | None |

---

## 💡 Quick Examples

### Get Top 5 Countries (Live)
```bash
curl "https://netflix-data-api.onrender.com/countries?top=5"
```
**Response:**
```json
{
  "United States": 2850,
  "India": 950,
  "United Kingdom": 720,
  "Japan": 450,
  "Canada": 380
}
```

### Filter Trends (Live)
```bash
curl "https://netflix-data-api.onrender.com/trends?from_year=2015&to_year=2020"
```

---

## 📊 Data Structure

### Expected CSV Format
The API expects cleaned Netflix data at `data/processed/netflix_cleaned.csv` with columns:
- `type` - "Movie" or "TV Show"
- `country` - Production country
- `release_year` - Year of release
- `rating` - Content rating (TV-MA, PG-13, etc.)
- `Total_minutes` - Duration in minutes (for movies)
- `Total_seasons` - Number of seasons (for TV shows)

---

## 🧪 Testing

```bash
# Run all tests locally
pytest tests/ -v

# Run specific test files
pytest tests/test_analysis.py -v
pytest tests/test_api.py -v
```

### Test Coverage
- ✅ Data loading and error handling
- ✅ Analysis function outputs
- ✅ API endpoint status codes
- ✅ Query parameter validation

---

## 📁 Project Structure

```
netflix-data-analysis/
├── main.py                    # FastAPI app entry point
├── requirements.txt           # Python dependencies
├── render.yaml                # Render deployment config
├── README.md                  # This file
│
├── src/
│   ├── __init__.py
│   ├── loader.py             # Load CSV with pandas
│   ├── analysis.py           # Analysis functions
│   ├── viz.py                # Matplotlib plotting
│   ├── reporter.py           # PDF generation with FPDF
│   │
│   └── api/
│       ├── __init__.py
│       ├── endpoints.py      # Image & PDF routes
│       └── summary.py        # JSON data routes
│
├── tests/
│   ├── __init__.py
│   ├── test_analysis.py      # Test analysis functions
│   └── test_api.py           # Test API endpoints
│
├── data/
│   └── processed/
│       └── netflix_cleaned.csv   # Input dataset
│
└── images/                    # Generated charts
    ├── content_distribution.png
    ├── yearly_trend.png
    ├── top_countries.png
    ├── rating_distribution.png
    └── average_duration.png
```

---

## 🎯 Key Technologies

| Technology | Purpose |
|------------|---------|
| **FastAPI** | Web framework for API routes |
| **Pandas** | Load and analyze CSV data |
| **NumPy** | Numerical calculations (mean, ceil) |
| **Matplotlib** | Generate bar/line charts |
| **FPDF2** | Create simple PDF reports |
| **pytest** | Run unit and integration tests |
| **Uvicorn** | Run the FastAPI server |
| **Render** | Cloud deployment platform |

---

## 🔐 Error Handling

- ✅ Invalid year ranges → returns error JSON
- ✅ Missing image/PDF files → generates on first request
- ✅ Data loading errors → raises descriptive exception
- ✅ Parameter validation → checks bounds for `top`, `from_year`, `to_year`

---

## 🎓 What This Project Shows

- ✅ Building a REST API with FastAPI
- ✅ Organizing code into modules (loader, analysis, viz, reporter)
- ✅ Generating charts with Matplotlib
- ✅ Creating PDFs programmatically
- ✅ Writing basic pytest tests
- ✅ Deploying to cloud with Render (free tier)

---

## 🔮 Possible Future Enhancements

- [ ] Add input validation with Pydantic models
- [ ] Use async/await for I/O operations
- [ ] Add database integration
- [ ] Create a frontend dashboard
- [ ] Add authentication
- [ ] Containerize with Docker

---

## 👨‍💻 Author

**Samrat Ghimire**  
🔗 GitHub: https://github.com/SamratGhimire01  
🔗 LinkedIn: https://www.linkedin.com/in/samratghimire01/  
🌐 Live API: https://netflix-data-api.onrender.com/docs

---

## 📄 License

This project is open-source and available for educational and personal use.

---

<p align="center">
  <b>⭐ If you find this project useful, please give it a star! ⭐</b>
</p>

<p align="center">
  <i>🚀 Live on Render • Built with Python & FastAPI</i>
</p>
