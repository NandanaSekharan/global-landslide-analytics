"""
Landslide Fatality Prediction Model
-------------------------------------
Predicts whether a landslide event was fatal (fatality_count > 0) using
categorical features: trigger, size, setting, and country.
Compares Random Forest vs Logistic Regression.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

sns.set_style("whitegrid")

# -----------------------------
# 1. LOAD CLEANED DATA
# -----------------------------
df = pd.read_csv("../data/landslide_cleaned.csv")

# Target: fatal vs non-fatal
df["fatal_label"] = (df["fatality_count"] > 0).astype(int)

# -----------------------------
# 2. FEATURES
# -----------------------------
features = ["landslide_trigger", "landslide_size", "landslide_setting", "country_name"]
X = df[features].fillna("Unknown")
y = df["fatal_label"]

# Encode categorical variables
encoders = {}
for col in X.columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    encoders[col] = le

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# -----------------------------
# 3. RANDOM FOREST MODEL
# -----------------------------
rf = RandomForestClassifier(
    n_estimators=200, max_depth=15, min_samples_split=10,
    class_weight="balanced", random_state=42, n_jobs=-1
)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)
rf_acc = accuracy_score(y_test, y_pred_rf)

print("=== Random Forest ===")
print("Accuracy:", round(rf_acc, 4))
print(classification_report(y_test, y_pred_rf))

# -----------------------------
# 4. LOGISTIC REGRESSION MODEL
# -----------------------------
lr = LogisticRegression(max_iter=1000)
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)
lr_acc = accuracy_score(y_test, y_pred_lr)

print("\n=== Logistic Regression ===")
print("Accuracy:", round(lr_acc, 4))
print(classification_report(y_test, y_pred_lr))

# -----------------------------
# 5. CONFUSION MATRIX (Random Forest)
# -----------------------------
cm = confusion_matrix(y_test, y_pred_rf)
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=["Non-fatal", "Fatal"], yticklabels=["Non-fatal", "Fatal"])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Random Forest — Confusion Matrix")
plt.tight_layout()
plt.savefig("../outputs/chart_confusion_matrix.png", dpi=150)
plt.close()

# -----------------------------
# 6. FEATURE IMPORTANCE
# -----------------------------
importance = pd.Series(rf.feature_importances_, index=features).sort_values(ascending=False)
plt.figure(figsize=(8, 5))
importance.plot(kind="bar", color="teal")
plt.title("Feature Importance — Random Forest")
plt.ylabel("Importance")
plt.tight_layout()
plt.savefig("../outputs/chart_feature_importance.png", dpi=150)
plt.close()

print("\n=== Model Comparison ===")
print(f"Random Forest Accuracy: {rf_acc:.2%}")
print(f"Logistic Regression Accuracy: {lr_acc:.2%}")
print("\nCharts saved to ../outputs/. Model training complete.")
