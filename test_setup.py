#!/usr/bin/env python3
"""
Quick test script to verify environment setup and data availability.
Run this before opening the Jupyter notebook to ensure everything is ready.
"""

import sys

def test_imports():
    """Test if all required libraries can be imported"""
    print("Testing library imports...")
    required_libs = [
        ('pandas', 'pd'),
        ('numpy', 'np'),
        ('matplotlib.pyplot', 'plt'),
        ('seaborn', 'sns'),
        ('sklearn', None),
    ]

    failed = []
    for lib, alias in required_libs:
        try:
            if alias:
                exec(f"import {lib} as {alias}")
            else:
                exec(f"import {lib}")
            print(f"  ✅ {lib}")
        except ImportError:
            print(f"  ❌ {lib}")
            failed.append(lib)

    if failed:
        print(f"\n⚠️  Missing libraries: {', '.join(failed)}")
        print("Run: pip install -r requirements.txt")
        return False
    else:
        print("\n✅ All libraries imported successfully!")
        return True

def test_data_files():
    """Test if required data files are accessible"""
    import os
    print("\nTesting data file availability...")

    data_files = [
        'Hospital_Patients.csv',
        'Hospital_Visits.csv',
        'Hospital_Staffing_EAST_LOCATION.csv',
        'Hospital_Facility.csv',
        'Hospital_Outcomes.csv'
    ]

    missing = []
    for filename in data_files:
        filepath = os.path.join('data', filename)
        if os.path.exists(filepath):
            size = os.path.getsize(filepath) / 1024  # KB
            print(f"  ✅ {filename} ({size:.1f} KB)")
        else:
            print(f"  ❌ {filename} - NOT FOUND")
            missing.append(filename)

    if missing:
        print(f"\n⚠️  Missing data files: {', '.join(missing)}")
        print("Ensure CSV files are in the data/ folder.")
        return False
    else:
        print("\n✅ All data files found!")
        return True

def test_data_loading():
    """Test if data can be loaded successfully"""
    try:
        import pandas as pd
        print("\nTesting data loading...")

        visits = pd.read_csv('data/Hospital_Visits.csv')
        print(f"  ✅ Loaded Hospital_Visits.csv: {len(visits):,} records")

        patients = pd.read_csv('data/Hospital_Patients.csv')
        print(f"  ✅ Loaded Hospital_Patients.csv: {len(patients):,} records")

        print("\n✅ Data loading successful!")
        return True
    except Exception as e:
        print(f"\n❌ Error loading data: {e}")
        return False

def main():
    print("=" * 70)
    print("ER ANALYSIS PROJECT - ENVIRONMENT TEST")
    print("=" * 70)
    print()

    # Check Python version
    py_version = sys.version_info
    print(f"Python Version: {py_version.major}.{py_version.minor}.{py_version.micro}")
    if py_version < (3, 8):
        print("⚠️  Warning: Python 3.8 or higher recommended")
    print()

    # Run tests
    libs_ok = test_imports()
    files_ok = test_data_files()
    data_ok = False

    if libs_ok and files_ok:
        data_ok = test_data_loading()

    # Summary
    print("\n" + "=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)
    print(f"  Libraries:    {'✅ PASS' if libs_ok else '❌ FAIL'}")
    print(f"  Data Files:   {'✅ PASS' if files_ok else '❌ FAIL'}")
    print(f"  Data Loading: {'✅ PASS' if data_ok else '❌ FAIL'}")

    if libs_ok and files_ok and data_ok:
        print("\n🎉 All tests passed! You're ready to run the notebook.")
        print("\nNext step: jupyter notebook ER_Analysis.ipynb")
        return 0
    else:
        print("\n⚠️  Some tests failed. Please fix the issues above before proceeding.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
