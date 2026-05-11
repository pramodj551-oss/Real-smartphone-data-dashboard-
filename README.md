# 📱 Smartphone Market Dashboard

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red?logo=streamlit)
![Plotly](https://img.shields.io/badge/Charts-Plotly-purple)
![Pandas](https://img.shields.io/badge/Data-Pandas-green?logo=pandas)
![License](https://img.shields.io/badge/License-MIT-yellow)

An interactive data analysis dashboard for **smartphone specifications, prices, and market trends** — built with Pandas and Streamlit for real-time filtering and visualization.

---

## ✨ Features

| Feature | Detail |
|--------|--------|
| 🔍 Multi-filter Sidebar | Filter by Brand, Price Range, OS, Connectivity (5G/Non-5G) |
| 📊 8 Interactive Charts | Bar, Histogram, Scatter, Pie, Donut — all Plotly powered |
| 💡 5 KPI Metrics | Total models, brands, avg price, avg rating, 5G% |
| 🎯 Price Segmentation | Auto-segments: Budget / Mid-Low / Mid / Premium / Ultra |
| ⬇️ CSV Download | Download filtered dataset directly from dashboard |
| 🗃️ Raw Data View | Expandable table with all filtered records |

---

## 📊 Dashboard Sections

| Section | Chart Type | What it Shows |
|---------|-----------|---------------|
| Models by Brand | Horizontal Bar | Top N brands by model count (adjustable slider) |
| Price Distribution | Histogram | Price spread across all filtered devices |
| Median Price by Brand | Vertical Bar | Top 15 brands by median price (₹) |
| Rating vs Price | Scatter | Avg rating vs price — color-coded by brand |
| OS Share | Donut Pie | Android / iOS / Other split |
| 5G Adoption | Donut Pie | 5G vs Non-5G model count |
| Price Segments | Bar | Budget / Mid-Low / Mid / Premium / Ultra count |
| RAM Distribution | Bar | RAM variant breakdown (GB) |
| Battery vs Price | Scatter | Battery mAh vs price — sized by RAM, colored by 5G |

---

## 🔍 Sidebar Filters

```
Brand          → Multi-select (all brands)
Price Range    → ₹ slider (min to max)
OS             → Multi-select (Android / iOS / Other)
Connectivity   → Radio: All / 5G Only / Non-5G Only
Top N Brands   → Slider (5 to max brands)
```

---

## 📋 Dataset — `smartphones.csv`

| Column | Description |
|--------|-------------|
| `brand_name` | Manufacturer (Apple, Samsung, Xiaomi...) |
| `model` | Device name |
| `price` | Price in ₹ |
| `avg_rating` | User rating (out of 10) |
| `5G_or_not` | 1 = 5G, 0 = Non-5G |
| `processor_brand` | Snapdragon, Bionic, Dimensity, Kirin... |
| `num_cores` | CPU core count |
| `processor_speed` | Clock speed (GHz) |
| `battery_capacity` | Battery (mAh) |
| `fast_charging_available` | 1 = Yes, 0 = No |
| `fast_charging` | Fast charge wattage |
| `ram_capacity` | RAM (GB) |
| `internal_memory` | Storage (GB) |
| `screen_size` | Display size (inches) |
| `refresh_rate` | Hz (60 / 90 / 120 / 144 / 165...) |
| `num_rear_cameras` | Rear camera count |
| `os` | Operating System |
| `primary_camera_rear` | Rear MP |
| `primary_camera_front` | Front MP |
| `extended_memory_available` | 1 = MicroSD slot |
| `resolution_height` | Display height (px) |
| `resolution_width` | Display width (px) |

**Sample brands covered:** Apple, Samsung, OnePlus, Xiaomi, Realme, Vivo, OPPO, Google, iQOO, Asus, Honor, Huawei, Infinix, Motorola, Nokia...

---

## 💰 Price Segments (Auto-Generated)

| Segment | Price Range |
|---------|------------|
| Budget | < ₹10,000 |
| Mid-Low | ₹10,000 – ₹20,000 |
| Mid | ₹20,000 – ₹40,000 |
| Premium | ₹40,000 – ₹80,000 |
| Ultra | > ₹80,000 |

---

## 📁 Project Structure

```
Real-smartphone-data-dashboard/
├── app.py                  # Streamlit dashboard (main file)
├── smartphones.csv         # Dataset — 900+ smartphone records
├── requirements.txt        # Dependencies
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

```bash
# 1. Clone
git clone https://github.com/pramodj551-oss/Real-smartphone-data-dashboard
cd Real-smartphone-data-dashboard

# 2. Virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux

# 3. Install
pip install -r requirements.txt
```

---

## 🚀 How to Run

```bash
streamlit run app.py
```

Open browser → `http://localhost:8501`

---

## 💡 Usage Guide

**Filter devices:**
- Use sidebar to select brands, price range, OS, 5G preference
- Dashboard updates all 8 charts instantly

**Explore trends:**
- Adjust "Top N brands" slider to compare brand spread
- Rating vs Price scatter — hover any dot to see exact model + specs

**Export data:**
- Scroll to bottom → **"⬇️ Download filtered CSV"** button

---

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| `FileNotFoundError: smartphones.csv` | Make sure `smartphones.csv` is in the same folder as `app.py` |
| Charts not loading | Run `pip install plotly --upgrade` |
| Streamlit port in use | `streamlit run app.py --server.port 8502` |
| Blank chart after filter | Selected filter has 0 results — widen price range or add more brands |

---

## 🚧 Planned Improvements

- [ ] Add processor brand comparison chart
- [ ] Add refresh rate distribution
- [ ] Compare two specific models side-by-side
- [ ] Add camera MP vs price scatter
- [ ] Deploy on Streamlit Cloud

---

## 🤝 Contributing

1. Fork → `git checkout -b feature/add-camera-analysis`
2. Commit → `git commit -m 'Add camera MP comparison chart'`
3. Push → `git push origin feature/add-camera-analysis`
4. Open a Pull Request

---

## 📝 License

MIT License — see [LICENSE](LICENSE)

---

## 📧 Contact

**Pramod** · IIT Patna Applied AI & ML Program  
GitHub: [@pramodj551-oss](https://github.com/pramodj551-oss)

> ⭐ Star this repo if it helped you!
