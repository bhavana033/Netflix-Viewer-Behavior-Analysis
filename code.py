import pandas as pd
import matplotlib.pyplot as plt

# ===============================
# Step 1: Read Dataset
# ===============================
df = pd.read_csv("data/netflix_user_dataset_cleaned.csv")

print(df.head())

# ===============================
# Step 2: Dataset Information
# ===============================
print("\nDataset Information:")
print(df.info())

# ===============================
# Step 3: Missing Values
# ===============================
print("\nMissing Values:")
print(df.isnull().sum())

# ===============================
# Step 4: Remove Duplicates
# ===============================
print("\nDuplicate Rows:", df.duplicated().sum())

df = df.drop_duplicates()

# ===============================
# Step 5: Save Cleaned Dataset
# ===============================
df.to_csv("data/netflix_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully!")

# ===============================
# Step 6: Exploratory Data Analysis (EDA)
# ===============================
df = pd.read_csv("data/netflix_cleaned.csv")

# Total users
print("Total Users:", len(df))

# Gender distribution
print("\nGender Distribution:")
print(df["gender"].value_counts())

# Subscription plans
print("\nSubscription Plans:")
print(df["subscription_plan"].value_counts())

# Content types
print("\nContent Types:")
print(df["content_type"].value_counts())

# Device types
print("\nDevice Types:")
print(df["device_type"].value_counts())

# Top 10 countries
print("\nTop 10 Countries:")
print(df["country"].value_counts().head(10))

# Average rating
print("\nAverage Rating:")
print(df["rating"].mean())

# Average watch time
print("\nAverage Watch Time:")
print(df["watch_time_minutes"].mean())
# ===============================
# Graph 1: Users by Subscription Plan
# ===============================

plan_counts = df["subscription_plan"].value_counts()

plt.figure(figsize=(6,4))
plan_counts.plot(kind="bar")

plt.title("Users by Subscription Plan")
plt.xlabel("Subscription Plan")
plt.ylabel("Number of Users")

plt.tight_layout()
plt.savefig("graphs/subscription_plan.png")
plt.show()

# ===============================
# Graph 2: Gender Distribution
# ===============================

gender_counts = df["gender"].value_counts()

plt.figure(figsize=(6,6))
gender_counts.plot(kind="pie", autopct="%1.1f%%")

plt.title("Gender Distribution")
plt.ylabel("")

plt.tight_layout()
plt.savefig("graphs/gender_distribution.png")
plt.show()

# ===============================
# Graph 3: Top 10 Countries
# ===============================

top_countries = df["country"].value_counts().head(10)

plt.figure(figsize=(8,5))
top_countries.plot(kind="bar")

plt.title("Top 10 Countries by Users")
plt.xlabel("Country")
plt.ylabel("Number of Users")

plt.tight_layout()
plt.savefig("graphs/top10_countries.png")
plt.show()

# ===============================
# Graph 4: Device Type
# ===============================

device = df["device_type"].value_counts()

plt.figure(figsize=(6,4))
device.plot(kind="bar")

plt.title("Users by Device Type")
plt.xlabel("Device Type")
plt.ylabel("Number of Users")

plt.tight_layout()
plt.savefig("graphs/device_type.png")
plt.show()

# ===============================
# Graph 5: Content Type
# ===============================

content = df["content_type"].value_counts()

plt.figure(figsize=(6,4))
content.plot(kind="bar")

plt.title("Movies vs TV Shows")
plt.xlabel("Content Type")
plt.ylabel("Number of Users")

plt.tight_layout()
plt.savefig("graphs/content_type.png")
plt.show()

# ===============================
# Graph 6: Top Genres
# ===============================

genre = df["genre"].value_counts().head(10)

plt.figure(figsize=(8,5))
genre.plot(kind="bar")

plt.title("Top 10 Genres")
plt.xlabel("Genre")
plt.ylabel("Number of Users")

plt.tight_layout()
plt.savefig("graphs/top_genres.png")
plt.show()

# ===============================
# Graph 7: Recommendation Source
# ===============================

recommend = df["recommendation_source"].value_counts()

plt.figure(figsize=(7,4))
recommend.plot(kind="bar")

plt.title("Recommendation Sources")
plt.xlabel("Source")
plt.ylabel("Number of Users")

plt.tight_layout()
plt.savefig("graphs/recommendation_source.png")
plt.show()

# ===============================
# Graph 8: Rating Distribution
# ===============================

rating = df["rating"].value_counts().sort_index()

plt.figure(figsize=(8,5))
rating.plot(kind="bar")

plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Users")

plt.tight_layout()
plt.savefig("graphs/rating_distribution.png")
plt.show()

# ===============================
# Graph 9: Average Watch Time by Age Group
# ===============================

watch_time = df.groupby("age_group")["watch_time_minutes"].mean()

plt.figure(figsize=(8,5))
watch_time.plot(kind="line", marker="o")

plt.title("Average Watch Time by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Average Watch Time (Minutes)")

plt.tight_layout()
plt.savefig("graphs/watchtime_agegroup.png")
plt.show()

# ===============================
# Graph 10: Liked vs Not Liked
# ===============================

liked = df["liked"].value_counts()

plt.figure(figsize=(6,6))
liked.plot(kind="pie", autopct="%1.1f%%")

plt.title("Liked vs Not Liked")
plt.ylabel("")

plt.tight_layout()
plt.savefig("graphs/liked_content.png")
plt.show()

# ===============================
# Graph 11: Watch Time by Release Year
# ===============================

release = df.groupby("release_year")["watch_time_minutes"].mean()

plt.figure(figsize=(10,5))
release.plot(kind="line")

plt.title("Average Watch Time by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Average Watch Time (Minutes)")

plt.tight_layout()
plt.savefig("graphs/release_year_watchtime.png")
plt.show()

df = pd.read_csv("data/netflix_cleaned.csv")
print(df.shape)



df1 = pd.read_csv("data/netflix_user_dataset_cleaned.csv")
df2 = pd.read_csv("data/netflix_cleaned.csv")

print("User dataset:", df1.shape)
print("Netflix cleaned:", df2.shape)