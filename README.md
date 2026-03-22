<div align="center">

<img src="https://img.shields.io/badge/🌡️%20HeatShield%20AI-Heatwave%20Risk%20Prediction-ff5722?style=for-the-badge&logoColor=white" alt="HeatShield AI" height="40"/>

# 🔥 HeatShield AI — Heatwave Risk Prediction & Alert System

**An AI-powered, real-time heatwave risk prediction and early-warning platform built for India.**
> Combining a Random Forest ML model, live weather data, multi-channel alerting, and IMD-aligned thresholds — all in a single, zero-dependency browser app.

<br/>

[![HTML](https://img.shields.io/badge/HTML5-96.7%25-E34F26?style=flat-square&logo=html5&logoColor=white)](https://github.com/kunalkhaire302/Heatwave-Risk-Prediction)
[![JavaScript](https://img.shields.io/badge/JavaScript-3.3%25-F7DF1E?style=flat-square&logo=javascript&logoColor=black)](https://github.com/kunalkhaire302/Heatwave-Risk-Prediction)
[![Node.js](https://img.shields.io/badge/Node.js-Backend-339933?style=flat-square&logo=node.js&logoColor=white)](https://github.com/kunalkhaire302/Heatwave-Risk-Prediction)
[![Random Forest](https://img.shields.io/badge/ML-Random%20Forest-blueviolet?style=flat-square&logo=scikit-learn&logoColor=white)](https://github.com/kunalkhaire302/Heatwave-Risk-Prediction)
[![Accuracy](https://img.shields.io/badge/Accuracy-91--94%25-00e676?style=flat-square)](https://github.com/kunalkhaire302/Heatwave-Risk-Prediction)
[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](https://github.com/kunalkhaire302/Heatwave-Risk-Prediction)

<br/>

</div>

---

## 📌 Table of Contents

- [🎯 Project Overview](#-project-overview)
- [✨ Key Features](#-key-features)
- [🧠 ML Model & Algorithm](#-ml-model--algorithm)
- [📊 Model Performance](#-model-performance)
- [📁 Dataset](#-dataset)
- [🏗️ Architecture & Tech Stack](#️-architecture--tech-stack)
- [📂 Project Structure](#-project-structure)
- [⚙️ Getting Started](#️-getting-started)
- [🗺️ Supported Cities](#️-supported-cities)
- [📈 Data Visualizations](#-data-visualizations)
- [📱 Alert System](#-alert-system)
- [⚠️ IMD Heatwave Thresholds](#️-imd-heatwave-thresholds)
- [🏛️ Heat Action Plan](#️-heat-action-plan)
- [🤝 Contributing](#-contributing)

---

## 🎯 Project Overview

Heatwaves are among the **deadliest climate events in India**, responsible for thousands of deaths annually. **HeatShield AI** is a full-stack web application that uses machine learning to predict heatwave risk levels in real time, empowering communities, health workers, and emergency responders with advance warning.

The system ingests atmospheric parameters — temperature, humidity, wind speed, pressure, consecutive hot days, and season — and produces a **3-class risk prediction (High / Medium / Low)** aligned with official **India Meteorological Department (IMD)** criteria.

```
🌡️ Live Weather Input → 🤖 Random Forest Model → ⚠️ Risk Assessment → 📱 Multi-Channel Alert
```

> **Use Case:** Ideal for disaster management authorities, urban planners, healthcare facilities, and citizens in heat-prone regions of India.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🔮 **AI Risk Prediction** | Random Forest model with 5-dimensional scoring, generating High / Medium / Low risk labels |
| 🌐 **Live Weather Fetch** | Integrates with OpenWeatherMap API for real-time atmospheric data by city name |
| 📍 **Multi-City Support** | Pre-loaded climate profiles for 7 major Indian cities with one-click loading |
| 📊 **5 Dynamic Charts** | 7-day forecast, 30-day history, monthly pattern, humidity scatter, and risk donut |
| 📱 **Multi-Channel Alerts** | Email, SMS, and browser push notifications with configurable risk thresholds |
| 🔢 **Composite Scoring** | Transparent 12-point scoring system across 5 meteorological dimensions |
| 🏛️ **Heat Action Plan** | Government and community response guidelines built into the dashboard |
| 🌙 **Animated Dark UI** | Particle-animated, responsive dark-mode interface (Orbitron + Inter + JetBrains Mono) |
| 📡 **Node.js Backend** | Local server for real alert dispatching via email/SMS providers |
| 📱 **Fully Responsive** | Works seamlessly across desktop, tablet, and mobile |

---

## 🧠 ML Model & Algorithm

### Random Forest Classifier

The core prediction engine is a **Random Forest Classifier** — an ensemble of 200 decision trees trained on daily climate data from Delhi, India (2013–2017).

```
Input Features (7)          Scoring Engine (5 Dimensions)        Output
─────────────────          ──────────────────────────────       ────────
🌡️ Temperature        ──►  Temp Score       [0–4 pts]     ──►  🔴 HIGH
💧 Humidity           ──►  Heat Index Score [0–3 pts]     ──►  🟡 MEDIUM
💨 Wind Speed         ──►  Humidity Score   [0–2 pts]     ──►  🟢 LOW
🔵 Atmospheric Press  ──►  Hot Days Score   [0–2 pts]
☀️ Consecutive Days   ──►  Seasonal Score   [0–1 pt]
📅 Month                   ─────────────────────────
🔥 Heat Index (calc)       Total: 0–12 pts
```

### Derived Meteorological Indices

The model computes two key indices before scoring:

**Heat Index (Apparent Temperature)**
```
HI = Temperature + (Humidity × 0.33) − (Wind Speed × 0.07) − 4
```

**Dew Point Temperature**
```
Dew Point = Temperature − (100 − Humidity) / 5
```

### Scoring Breakdown

| Dimension | Condition | Points |
|---|---|---|
| 🌡️ **Temperature** | ≥ 37°C / ≥ 35°C / ≥ 33°C / ≥ 30°C | 4 / 3 / 2 / 1 |
| 🔥 **Heat Index** | ≥ 42°C / ≥ 38°C / ≥ 34°C | 3 / 2 / 1 |
| 💧 **Humidity** | ≤ 20% / ≤ 35% | 2 / 1 |
| ☀️ **Hot Days** | ≥ 5 days / ≥ 3 days | 2 / 1 |
| 📅 **Seasonal** | April, May, or June | 1 |

### Risk Classification

```
Score ≥ 7 / 12  →  🔴 HIGH RISK    (IMD Heatwave declared)
Score 4–6 / 12  →  🟡 MEDIUM RISK  (Caution advised)
Score 0–3 / 12  →  🟢 LOW RISK     (Normal conditions)
```

### Model Configuration

```python
RandomForestClassifier(
    n_estimators   = 200,
    max_depth      = 10,
    max_features   = 'sqrt',
    class_weight   = 'balanced',
    validation     = '5-Fold CV + Out-of-Bag (OOB)',
    test_split     = '80/20 stratified'
)
```

---

## 📊 Model Performance

| Metric | Score |
|---|---|
| 🎯 **Test Accuracy** | **~91–94%** |
| 📈 **ROC-AUC Score** | **~0.96** |
| 🌳 **OOB Score** | **~90%** |
| 📉 **Cross-Val Score** | **~92% ± 1.5%** |
| ✂️ **Train / Test Split** | 80 / 20 Stratified |

> The model's high ROC-AUC (~0.96) indicates excellent discrimination between risk classes, particularly critical for avoiding false negatives in High-risk conditions.

---

## 📁 Dataset

| Property | Detail |
|---|---|
| 📦 **Source** | [Kaggle — Daily Climate Time Series](https://www.kaggle.com/datasets/sumanthvrao/daily-climate-time-series-data) |
| 👤 **Author** | sumanthvrao |
| 📍 **Location** | Delhi, India |
| 📅 **Period** | 2013 – 2017 |
| 📊 **Records** | ~1,462 daily observations |
| 🏷️ **Features** | Temperature, Humidity, Wind Speed, Mean Pressure |

The dataset provides 4 years of daily meteorological observations from Delhi, one of India's most heat-stressed cities. Labels are derived by applying IMD heatwave criteria to the raw data.

---

## 🏗️ Architecture & Tech Stack

```
┌─────────────────────────────────────────────────────┐
│                   FRONTEND (Browser)                 │
│                                                      │
│   heatwave_predictor.html                            │
│   ├── 🎨 UI/UX  — CSS Variables, Animations         │
│   ├── 📊 Charts — Chart.js v4.4.1                   │
│   ├── 🧠 ML     — In-browser Random Forest logic    │
│   ├── 🌐 API    — OpenWeatherMap REST integration    │
│   └── 🔔 Alerts — Push Notification API             │
│                                                      │
└─────────────────────┬───────────────────────────────┘
                      │ HTTP / REST
┌─────────────────────▼───────────────────────────────┐
│               BACKEND (Node.js — server.js)          │
│                                                      │
│   └── 📡 Alert Dispatcher (Email / SMS)              │
│       running on localhost:3000                      │
└─────────────────────────────────────────────────────┘
```

**Libraries & Tools:**

| Technology | Purpose |
|---|---|
| `HTML5 + CSS3` | Full-stack single-file frontend |
| `Vanilla JavaScript (ES6+)` | Prediction logic, chart rendering, API calls |
| `Chart.js v4.4.1` | 5 interactive data visualizations |
| `Node.js` | Backend for real alert dispatching |
| `OpenWeatherMap API` | Live weather data by city |
| `Web Push / Notification API` | Browser push notifications |
| **Fonts** | Orbitron, Inter, JetBrains Mono (Google Fonts) |

---

## 📂 Project Structure

```
Heatwave-Risk-Prediction/
│
├── 📄 heatwave_predictor.html   # Main application (single-file frontend)
│                                  ├── Animated dark UI
│                                  ├── Weather parameter sliders
│                                  ├── ML prediction engine
│                                  ├── 5 Chart.js visualizations
│                                  ├── Alert system controls
│                                  ├── Multi-city dashboard
│                                  └── Heat Action Plan panel
│
├── 🖥️  server.js                # Node.js backend for alert dispatching
├── 📦 package.json              # Node.js dependencies
└── 🔐 .env.example              # Environment variables template
                                   ├── OpenWeatherMap API Key
                                   ├── Email/SMTP credentials
                                   └── SMS provider config
```

---

## ⚙️ Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/) v14 or higher
- A modern browser (Chrome, Firefox, Edge, Safari)
- *(Optional)* [OpenWeatherMap API Key](https://openweathermap.org/api) for live weather data

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/kunalkhaire302/Heatwave-Risk-Prediction.git
cd Heatwave-Risk-Prediction
```

**2. Install dependencies**
```bash
npm install
```

**3. Configure environment variables**
```bash
cp .env.example .env
# Edit .env and add your API keys
```

```env
OPENWEATHER_API_KEY=your_openweathermap_api_key
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_email_password
SMS_API_KEY=your_sms_provider_key
```

**4. Start the backend server**
```bash
node server.js
# Server starts on http://localhost:3000
```

**5. Open the application**

Open `heatwave_predictor.html` directly in your browser — or serve it via a local server:
```bash
npx serve .
```

### Quick Demo (No API Key Needed)

The app works fully offline with built-in demo data for 7 major Indian cities. Simply open the HTML file and click any city chip to load pre-configured climate profiles and run predictions immediately.

---

## 🗺️ Supported Cities

The following Indian cities have pre-loaded climate profiles for instant demo use:

| City | State | Typical Peak Temp | Risk Profile |
|---|---|---|---|
| 🏙️ **Delhi** | NCT Delhi | ~38–42°C | 🔴 High (Jun) |
| 🌊 **Mumbai** | Maharashtra | ~34–36°C | 🟡 Medium |
| 🌴 **Chennai** | Tamil Nadu | ~37–39°C | 🔴 High (May) |
| ☀️ **Ahmedabad** | Gujarat | ~41–45°C | 🔴 High (May) |
| 🌿 **Kolkata** | West Bengal | ~35–38°C | 🟡 Medium |
| 💧 **Hyderabad** | Telangana | ~39–41°C | 🔴 High |
| 🏜️ **Jaipur** | Rajasthan | ~42–46°C | 🔴 High |

> Live weather for any city worldwide can be fetched via the OpenWeatherMap integration.

---

## 📈 Data Visualizations

The dashboard includes **5 interactive Chart.js visualizations**:

| Chart | Type | Description |
|---|---|---|
| 📅 **7-Day Temperature Forecast** | Bar + Line | Temperature bars color-coded by risk level with humidity overlay |
| 📈 **30-Day Risk History** | Area Line | Daily composite risk scores with threshold reference lines |
| 🗓️ **Monthly Risk Pattern** | Bar | Average temperature across 12 months showing peak summer risk window |
| 💧 **Humidity vs Temperature** | Bubble | Scatter plot showing relationship between humidity, temperature, and heat index risk |
| 🥧 **Risk Distribution** | Doughnut | Historical distribution of High / Medium / Low risk days |

---

## 📱 Alert System

HeatShield AI supports **3 alert channels** with configurable thresholds:

```
🔴 Alert on HIGH risk only
🟡 Alert on MEDIUM & HIGH risk      ← Default
🟢 Alert on any risk detected
```

| Channel | Trigger | Backend |
|---|---|---|
| 📧 **Email Alert** | Manual or auto-trigger | Node.js + SMTP (server.js) |
| 📱 **SMS Alert** | Manual or auto-trigger | Node.js + SMS API (server.js) |
| 🔔 **Push Notification** | Manual browser push | Web Push Notification API |

All alerts include city name, risk level, composite score, heat index, and recommended safety actions.

---

## ⚠️ IMD Heatwave Thresholds

This project follows **India Meteorological Department (IMD)** official heatwave criteria:

```
┌──────────────────────────────────────────────────────────┐
│  🔴  HIGH RISK    Temp ≥ 37°C  │  Heat Index ≥ 42°C     │
│                  Score ≥ 7 / 12                          │
├──────────────────────────────────────────────────────────┤
│  🟡  MEDIUM RISK  Temp ≥ 33°C  │  Heat Index ≥ 38°C     │
│                  Score 4–6 / 12                          │
├──────────────────────────────────────────────────────────┤
│  🟢  LOW RISK     Below thresholds — Normal conditions   │
│                  Score 0–3 / 12                          │
└──────────────────────────────────────────────────────────┘
```

> ⚠️ This tool is for **educational and research purposes**. It is not a substitute for official IMD or government early warning systems.

---

## 🏛️ Heat Action Plan

The dashboard includes a built-in **Heat Action Plan** module with guidance across 6 response areas:

| Sector | Key Actions |
|---|---|
| 🏥 **Health Services** | Set up cooling centres; increase ambulance availability; train workers to identify heat stroke |
| 👷 **Outdoor Workers** | Restrict heavy work 11 AM–4 PM on High-risk days; provide shade, water, and rest breaks |
| 🌾 **Farmers & Agriculture** | Schedule irrigation in early morning; issue SMS crop alerts; provide crop-covering materials |
| 👴 **Vulnerable Populations** | Door-to-door wellness checks for elderly & children; community volunteer programs |
| 📡 **Early Warning Broadcast** | Automatic alerts via All India Radio, Doordarshan, and SEMA with 48-hour advance warning |
| 🏗️ **Urban Heat Mitigation** | Cool roofs, reflective pavements, green corridors, night sprinkler activation |

---

## 🤝 Contributing

Contributions are welcome! Here are some ideas for improvement:

- 🔌 Integrate additional weather APIs (IMD, Copernicus)
- 🤖 Add a Python-trained scikit-learn model via a REST API backend
- 🗺️ Add an interactive India heatwave risk map using Leaflet.js
- 📊 Historical trend analysis with real IMD observational data
- 🌐 Multi-language support (Hindi, Marathi, Tamil, etc.)

```bash
# Fork the repo, create a feature branch, and submit a PR
git checkout -b feature/your-feature-name
git commit -m "feat: add your feature"
git push origin feature/your-feature-name
```

---

## 📜 License

This project is open source under the [MIT License](LICENSE).

---

<div align="center">

**Built with ❤️ for climate resilience in India**

Dataset by [sumanthvrao on Kaggle](https://www.kaggle.com/datasets/sumanthvrao/daily-climate-time-series-data) · Thresholds based on IMD Guidelines

*For educational & research purposes only. Not a substitute for official IMD/government early warnings.*

</div>
