# Imorting Pandas
import pandas as pd

# Reading The CSV File
df = pd.read_csv("data.csv")

# Checking The Number Of Rows And Coloumns
print("Earliar; Number Of Rows And Coloums: " + str(df.shape))
print()

# Deleting The Non-Required Coloums
del df["Serial"]
del df["Luminosity(ly)"]
del df["Star"]
del df["Distance"]
del df["Mass"]
del df["Radius"]

# Checking The Number Of Rows And Coloumns After Deleting
print("After; Number Of Rows And Coloums: " + str(df.shape))
print()

# Renaming The Coloums
df = df.rename(
    {
        "Star_name": "Star Name",
        "Distance()": "Distance From Earth",
        "Mass(M)": "Mass Of Star",
        "Radius(R)": "Radius Of Star",
    },
    axis='columns'
)

# Printing The Head Of Dataframe
print(df.head())

# # Creating A Clean CSV File
df.to_csv("final.csv", index=True, index_label="Serial No.")