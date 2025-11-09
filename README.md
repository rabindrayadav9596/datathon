# Emergency Room Efficiency Analysis
## Meridian City Hospital - East ER Location

**Datathon Project: Emergency Room Efficiencies - From Bottleneck to Breakthrough**

Presented by: East Texas A&M
Sponsored by: Alteryx
Date: November 6th, 2025

---

## 📋 Project Overview

This project analyzes patient flow and operational data from Meridian City Hospital's East ER to identify bottlenecks causing delays and provide actionable recommendations to improve:
- ER throughput
- Staffing efficiency
- Operational performance
- Patient satisfaction

### Current Performance Issues
- Only **40%** of patients seen within 15 minutes
- Average wait time: **45+ minutes**
- Average total ER time: **2.5 hours**

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip or conda package manager

### Installation

1. **Navigate to the project directory:**
   ```bash
   cd ER_Analysis_Project
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   # Using venv
   python -m venv venv

   # Activate on macOS/Linux
   source venv/bin/activate

   # Activate on Windows
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start Jupyter Notebook:**
   ```bash
   jupyter notebook ER_Analysis.ipynb
   ```

---

## 📁 Data Files

All data files are included in the `data/` folder:

- `Hospital_Patients.csv` - Patient demographics
- `Hospital_Visits.csv` - Visit timestamps and triage data
- `Hospital_Staffing_EAST_LOCATION.csv` - Staffing schedules
- `Hospital_Facility.csv` - Facility capacity information
- `Hospital_Outcomes.csv` - Patient dispositions and satisfaction

The project is self-contained and ready to run!

---

## 📊 Analysis Components

### 1. Data Preparation
- Handles inconsistent date formats across datasets
- Standardizes triage levels and shift classifications
- Filters for East ER location only
- Engineers key features (wait times, temporal patterns, staffing ratios)

### 2. Exploratory Data Analysis (EDA)
- Current performance metrics vs targets
- Wait time breakdown by ER stage
- Temporal patterns (hourly, daily, by shift)
- Staffing analysis and patient-to-staff ratios
- Patient demographics and satisfaction analysis

### 3. Machine Learning Models
- **Model 1:** Wait Time Prediction (Regression)
  - Compares Random Forest, Gradient Boosting, and Linear Regression
  - Predicts time to see doctor based on operational factors

- **Model 2:** Patient Satisfaction Prediction (Classification)
  - Identifies factors most impacting satisfaction scores

- **Model 3:** 15-Minute Threshold Classifier (Binary Classification)
  - Predicts whether a patient will wait more than 15 minutes

### 4. Visualizations Generated
The notebook creates 9 high-quality visualizations:
- Wait time analysis
- Temporal patterns
- Staffing analysis
- Demographics and outcomes
- Correlation matrix
- Feature importance plots
- Model prediction visualizations

### 5. Recommendations
- High-priority interventions
- Medium-priority optimizations
- Quick wins
- Projected impact analysis

---

## 🎯 Key Findings

### Primary Bottlenecks
1. **Wait to see doctor** - Largest delay component
2. **Staffing misalignment** - Capacity issues during specific shifts
3. **Fast-track inefficiencies** - Potential patient misrouting
4. **Triage inconsistencies** - Classification standardization needed

### ML Model Performance
- Wait time predictions: High accuracy for operational planning
- Satisfaction predictions: Identifies key drivers
- Threshold classifier: Enables proactive patient management

### Projected Impact
Implementing recommendations could:
- Reduce average wait times by **30-40%**
- Increase 15-minute compliance from **40% to 60-70%**
- Improve patient satisfaction by **20-30%**

---

## 🛠️ Troubleshooting

### Common Issues

**Issue:** `ModuleNotFoundError` when running notebook
- **Solution:** Make sure you've activated the virtual environment and run `pip install -r requirements.txt`

**Issue:** `FileNotFoundError` when loading data
- **Solution:** Ensure all CSV files are in the `data/` folder. Run `python test_setup.py` to check.

**Issue:** Date parsing errors
- **Solution:** The notebook includes flexible date parsing to handle multiple formats. If issues persist, check your data for unexpected formats.

**Issue:** Memory errors with large datasets
- **Solution:** The notebook is optimized for efficiency, but if you encounter memory issues, consider:
  - Closing other applications
  - Using a machine with more RAM
  - Processing data in chunks (code modifications needed)

---

## 📦 Project Structure

```
ER_Analysis_Project/
├── data/                           # Data files
│   ├── Hospital_Patients.csv
│   ├── Hospital_Visits.csv
│   ├── Hospital_Staffing_EAST_LOCATION.csv
│   ├── Hospital_Facility.csv
│   └── Hospital_Outcomes.csv
├── outputs/                        # Generated visualizations and CSVs
│   ├── wait_time_analysis.png
│   ├── temporal_patterns.png
│   ├── staffing_analysis.png
│   ├── demographics_outcomes.png
│   ├── correlation_matrix.png
│   ├── feature_importance_wait_time.png
│   ├── wait_time_predictions.png
│   ├── satisfaction_confusion_matrix.png
│   ├── feature_importance_satisfaction.png
│   ├── summary_statistics.csv
│   └── shift_analysis.csv
├── ER_Analysis.ipynb              # Main analysis notebook
├── requirements.txt                # Python dependencies
├── test_setup.py                   # Environment test script
├── setup_instructions.md           # Quick setup guide
├── README.md                       # This file
└── .gitignore                      # Git ignore rules
```

---

## 💡 Usage Tips

1. **Run cells sequentially** - The notebook is designed to be run from top to bottom
2. **Check data paths** - Verify CSV files are in the correct location before running
3. **Adjust parameters** - Feel free to modify ML model parameters for experimentation
4. **Export results** - All visualizations are automatically saved as PNG files
5. **Presentation ready** - Generated visualizations are high-resolution (300 DPI) for presentations

---

## 📝 Deliverables

This project supports the datathon requirements:

✅ **Required:**
- Alteryx Workflow (separate file)
- PowerPoint presentation with voiceover (use generated visualizations)
- 200-300 word executive summary

✅ **Bonus Materials:**
- Python/Jupyter analysis (this notebook)
- Machine Learning models
- Statistical analysis
- Comprehensive visualizations
- Data-driven recommendations

---

## 🤝 Contributing

For questions or improvements, please contact the project team.

---

## 📄 License

This project is created for the East Texas A&M Datathon 2025.

---

## 🙏 Acknowledgments

- **Sponsor:** Alteryx
- **Curator:** Capitalize Consulting
- **Data Source:** Meridian City Hospital (simulated data)

---

**Last Updated:** November 2025
