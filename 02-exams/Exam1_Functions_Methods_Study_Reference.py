# Imports
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels.formula.api as smf
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Python
print(...)
len(...)
sum(...)
min(...)
max(...)
type(...)
list(...)

# Paths and files
Path.cwd()
Path("filename.csv")
Path("filename.csv").exists()

# DataFrames and Series
pd.read_csv("filename.csv")
pd.read_csv("filename.csv", encoding="cp1252")
pd.DataFrame({...})
pd.Series({...})
df.head()
df.head(10)
df.shape
df.columns
df.dtypes
df.info()
df.describe()
df["column"]
df[["column_1", "column_2"]]
df.loc[rows, columns]
df.isna()
df.isna().sum()
series.sum()
series.mean()
series.median()
series.min()
series.max()
series.abs()
series.value_counts()
series.sort_values()
series.index
series.values
series.tolist()
series.isin([value_1, value_2])
df.rename(columns={"old_name": "new_name"})
df.to_csv("filename.csv", index=False)
df.dropna()
df.dropna(subset=["column_1", "column_2"])
df.assign(new_column=...)
df.sort_values("column")
df.sort_values("column", ascending=False)
df.sort_values(by=["column_1", "column_2"], ascending=[True, False])
df.reset_index()
df.groupby("group_column")["value_column"].mean()
df.groupby("group_column", as_index=False)["value_column"].mean()
df.groupby("group_column").agg(
    count_name=("value_column", "size"),
    mean_name=("value_column", "mean"),
    median_name=("value_column", "median"),
)
pd.crosstab(df["row_variable"], df["column_variable"])
pd.concat([df_1, df_2], ignore_index=True)
pd.crosstab(
    df["row_variable"],
    df["column_variable"],
    values=df["value_variable"],
    aggfunc="mean",
)
pd.pivot_table(
    df,
    index="row_variable",
    columns="column_variable",
    values="value_variable",
    aggfunc="mean",
)
df.melt(
    id_vars="id_column",
    var_name="category_column",
    value_name="value_column",
)
df[condition]
df[(condition_1) & (condition_2)]
df[(condition_1) | (condition_2)]

# Method chains
result = (
    df.dropna(subset=["column"])
    .assign(new_column=...)
    .groupby("group_column", as_index=False)
    .agg(summary_name=("value_column", "median"))
    .sort_values("summary_name", ascending=False)
)

# Pandas plots
series.plot.bar()
df.plot.bar(x="category_column", y="value_column")
df.plot(x="x_column", y="y_column", kind="bar")

# Matplotlib
fig, ax = plt.subplots()
fig, ax = plt.subplots(figsize=(8, 5))
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))
ax.bar(categories, values)
ax.hist(values, bins=12)
ax.hist(values, bins=12, density=True)
ax.scatter(x_values, y_values)
ax.plot(x_values, y_values)
ax.fill_between(x_values, lower_values, upper_values)
ax.axhline(0, color="black", linestyle="--")
ax.axvline(0, color="black", linestyle="--")
ax.set_title("Title")
ax.set_xlabel("X-axis label")
ax.set_ylabel("Y-axis label")
ax.set(title="Title", xlabel="X-axis label", ylabel="Y-axis label")
ax.legend(title="Legend title")
ax.set_aspect("equal", adjustable="box")
plt.xlabel("X-axis label")
plt.ylabel("Y-axis label")
plt.title("Title")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
fig.tight_layout()
fig.savefig("figure.png", dpi=150, bbox_inches="tight")
plt.show()

# Seaborn
sns.scatterplot(data=df, x="x_column", y="y_column", ax=ax)
sns.scatterplot(data=df, x="x_column", y="y_column", hue="group_column", ax=ax)
sns.regplot(data=df, x="x_column", y="y_column", ax=ax)
sns.histplot(data=df, x="value_column", bins=15, ax=ax)
sns.histplot(
    data=df,
    x="value_column",
    hue="group_column",
    bins=15,
    element="step",
    fill=True,
    alpha=0.2,
    ax=ax,
)
sns.boxplot(data=df, x="group_column", y="value_column", ax=ax)
sns.boxplot(
    data=df,
    x="group_column",
    y="value_column",
    hue="second_group_column",
    order=category_order,
    palette="colorblind",
    ax=ax,
)
sns.displot(data=df, x="value_column", col="group_column", bins=15)
grid.set_axis_labels("X-axis label", "Y-axis label")
grid.set_titles("{col_name}")
grid.figure.suptitle("Title")
sns.kdeplot(data=df, x="value_column", hue="group_column")
sns.violinplot(data=df, x="group_column", y="value_column", ax=ax)

# NumPy
np.linspace(start, stop, number_of_values)
np.allclose(values_1, values_2)

# statsmodels
model = smf.ols("response ~ predictor", data=df).fit()
model.summary()
model.params
model.params["Intercept"]
model.params["predictor"]
model.conf_int()
model.pvalues
model.rsquared
model.fittedvalues
model.resid
model.predict(df)
prediction = model.get_prediction(new_data)
prediction.summary_frame()

# scikit-learn
X = df[["predictor"]]
y = df["response"]
model = LinearRegression()
model.fit(X, y)
model.intercept_
model.coef_
model.coef_[0]
predicted = model.predict(X)
mean_absolute_error(y, predicted)
mean_squared_error(y, predicted)
mean_squared_error(y, predicted) ** 0.5
r2_score(y, predicted)
