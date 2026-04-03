import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 1. Load the model and preprocessing objects
model_filename = 'heatwave_rf_model.pkl'
with open(model_filename, 'rb') as file:
    model_data = pickle.load(file)

rf = model_data['model']
scaler = model_data['scaler']
le = model_data['label_encoder']
FEATURES = model_data['features']

print("✅ Model, Scaler, and Label Encoder loaded successfully.")

# 2. Load the test dataset
df = pd.read_csv('DailyDelhiClimateTest.csv')
print(f"✅ Loaded {len(df)} test rows.")

# 3. Data Cleaning and Feature Engineering (Exactly as trained)
df["date"] = pd.to_datetime(df["date"])
df.rename(columns={
    "meantemp"    : "temperature_c",
    "humidity"    : "humidity_pct",
    "wind_speed"  : "wind_speed_kmh",
    "meanpressure": "pressure_mb",
}, inplace=True)

df["heat_index_c"] = (df["temperature_c"] + (df["humidity_pct"] * 0.33) - (df["wind_speed_kmh"] * 0.07) - 4)
df["dew_point_c"] = (df["temperature_c"] - ((100 - df["humidity_pct"]) / 5))

df = df.sort_values("date").reset_index(drop=True)
df["is_hot_day"] = (df["temperature_c"] > 35).astype(int)
df["consecutive_hot_days"] = (
    df["is_hot_day"]
    .groupby((df["is_hot_day"] != df["is_hot_day"].shift()).cumsum())
    .transform("cumsum") * df["is_hot_day"]
)
df["month"] = df["date"].dt.month

# 4. Filter features and predict
X = df[FEATURES]
X_sc = scaler.transform(X)
y_pred = rf.predict(X_sc)
y_prob = rf.predict_proba(X_sc)

# Add predictions back to dataframe
df["predicted_risk_encoded"] = y_pred
df["predicted_risk"] = le.inverse_transform(y_pred)

print("✅ Predictions generated.")
print("Risk Distribution:")
print(df["predicted_risk"].value_counts())

# 5. Extract probabilities for plotting
probs_df = pd.DataFrame(y_prob, columns=le.classes_)
df["prob_High"] = probs_df["High"]
df["prob_Medium"] = probs_df["Medium"]
df["prob_Low"] = probs_df["Low"]

# 6. Make the Output Plot
sns.set_style("whitegrid")
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), sharex=True, gridspec_kw={'height_ratios': [2, 1]})

# Top Plot: Temperature & Heat Index over Time
ax1.plot(df["date"], df["temperature_c"], label="Temperature (°C)", color="#DD6B20", linewidth=2.5)
ax1.plot(df["date"], df["heat_index_c"], label="Heat Index (°C)", color="#E53E3E", linewidth=2, linestyle='--')
ax1.axhline(37, color="black", linestyle=":", linewidth=1.5, label="High Risk Temp Threshold (37°C)")

# Overlay risk zones visually
for idx, row in df.iterrows():
    color = "red" if row["predicted_risk"] == "High" else "orange" if row["predicted_risk"] == "Medium" else "green"
    alpha = 0.5 if row["predicted_risk"] == "High" else 0.3 if row["predicted_risk"] == "Medium" else 0.05
    ax1.axvspan(row["date"], row["date"] + pd.Timedelta(days=1), color=color, alpha=alpha, lw=0)

ax1.set_title("Delhi Climate Test Data - Heatwave Risk Timeline", fontsize=16, fontweight="bold")
ax1.set_ylabel("Temperature / Heat Index (°C)", fontsize=13)
ax1.legend(loc="upper left")

# Bottom Plot: Prediction Probabilities
ax2.plot(df["date"], df["prob_High"] * 100, label="High Risk %", color="#E53E3E", linewidth=2)
ax2.plot(df["date"], df["prob_Medium"] * 100, label="Medium Risk %", color="#DD6B20", linewidth=2)
ax2.plot(df["date"], df["prob_Low"] * 100, label="Low Risk %", color="#38A169", linewidth=2, linestyle=":")
ax2.set_title("Machine Learning Risk Probability (%)", fontsize=14, fontweight="bold")
ax2.set_xlabel("Date (Jan 2017 - Apr 2017)", fontsize=13)
ax2.set_ylabel("Probability (%)", fontsize=13)
ax2.set_ylim(0, 105)
ax2.legend(loc="upper left")

plt.tight_layout()

# Save the graph directly to the artifacts directory so the AI system can display it
out_file = r"C:\Users\asus\.gemini\antigravity\brain\f9da4a6c-59ff-47ba-9321-d47d93eda887\test_predictions_graph.png"
plt.savefig(out_file, dpi=150)
print(f"✅ Graph successfully saved to {out_file}!")
