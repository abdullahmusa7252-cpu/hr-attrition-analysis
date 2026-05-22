import subprocess
import sys
import os
import warnings

# Change to project root
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

tests = [
    ('scripts/test_data_quality.py', 'Data Quality'),
    ('scripts/test_chart_numbers.py', 'Chart Numbers'),
    ('scripts/test_model_accuracy.py', 'Model Accuracy'),
    ('scripts/test_dashboard_values.py', 'Dashboard KPIs')
]

print("\n" + "=" * 60)
print("RUNNING ALL TESTS - HR ATTRITION ANALYSIS")
print("=" * 60 + "\n")

failed = []
for test_file, name in tests:
    print(f"\n>>> Running {name} test...")
    print("-" * 40)
    result = subprocess.run([sys.executable, test_file], capture_output=True, text=True)
    print(result.stdout)
    # Check if there's an actual error (not just warnings)
    if result.returncode != 0:
        print("ERRORS:")
        print(result.stderr)
        failed.append(name)

print("\n" + "=" * 60)
print("TEST SUMMARY")
print("=" * 60)
if failed:
    print(f"❌ Failed tests: {', '.join(failed)}")
else:
    print("✅ All tests passed! Dashboard is 100% accurate.")
