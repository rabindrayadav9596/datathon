# Setup Instructions - Quick Reference

## For macOS/Linux Users

```bash
# 1. Navigate to project
cd ER_Analysis_Project

# 2. Create virtual environment
python3 -m venv venv

# 3. Activate environment
source venv/bin/activate

# 4. Install packages
pip install -r requirements.txt

# 5. Launch Jupyter
jupyter notebook ER_Analysis.ipynb
```

---

## For Windows Users

```bash
# 1. Navigate to project
cd ER_Analysis_Project

# 2. Create virtual environment
python -m venv venv

# 3. Activate environment
venv\Scripts\activate

# 4. Install packages
pip install -r requirements.txt

# 5. Launch Jupyter
jupyter notebook ER_Analysis.ipynb
```

---

## Using Conda (Alternative)

```bash
# 1. Create conda environment
conda create -n er_analysis python=3.10

# 2. Activate environment
conda activate er_analysis

# 3. Install packages
pip install -r requirements.txt

# 4. Launch Jupyter
jupyter notebook ER_Analysis.ipynb
```

---

## Verify Installation

After installation, verify everything works:

```python
# Run this in Python/Jupyter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor

print("✅ All libraries imported successfully!")
```

---

## Troubleshooting

### Issue: "jupyter: command not found"
```bash
pip install jupyter notebook
```

### Issue: "No module named 'sklearn'"
```bash
pip install scikit-learn
```

### Issue: Python version too old
- Ensure Python 3.8 or higher
- Check with: `python --version`

---

## Quick Test

```bash
# Test if notebook can load data
python test_setup.py  # Run environment test

# Or manually check
ls data/*.csv  # Should see all Hospital_*.csv files
```
