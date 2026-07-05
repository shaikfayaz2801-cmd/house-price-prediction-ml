import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv("house_price_dataset.csv")

X = df.drop("Price", axis=1)
y = df["Price"]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = LinearRegression()
model.fit(X_train,y_train)

pred = model.predict(X_test)

print("R2 Score:", r2_score(y_test,pred))

area = float(input("Area (sqft): "))
bedrooms = int(input("Bedrooms: "))
bathrooms = int(input("Bathrooms: "))
parking = int(input("Parking: "))
house_age = int(input("House Age: "))
location_rating = int(input("Location Rating: "))
distance = float(input("Distance City (km): "))

result = model.predict([[area,bedrooms,bathrooms,parking,house_age,location_rating,distance]])
print(f"Estimated House Price: {result[0]:,.2f}")
