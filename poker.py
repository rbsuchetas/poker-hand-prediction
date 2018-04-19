# Euclidean Distance
from scipy.spatial import distance
def euc(a, b):
  return distance.euclidean(a, b)

# KNN Classifer
class KNN():
  def fit(self, X, y):
    self.X = X
    self.y = y

  def predict(self, listx):
    predictions = []
    #for listx in X:
    label = self.closest(listx)
    predictions.append(label)
    return predictions

  def closest(self, listx):
    best_dist = euc(listx, self.X[0])
    best_index = 0
    for i in range(1, len(self.X)):
      dist = euc(listx, self.X[i])
      if(dist<best_dist):
        best_dist = dist
        best_index = i
    return self.y[best_index]

#Loading CSV file to the program
import csv
filename = "training_data.csv"
rows = []
X = []
y = []
with open(filename,'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        rows.append(row)

#Dividing the dataset into attributes and class label
    for row in rows:
            X.append(map(int, row[0:2]))
            y.append(map(int, row[2]))

# Data Input
prediction = []
itemColor = []
itemSpecs = []
print("Product 1: ")
itemColor.append(raw_input("Enter the color: "))
itemSpecs.append(input("Enter the specification: "))
print("\nProduct 2: ")
itemColor.append(raw_input("Enter the color: "))
itemSpecs.append(input("Enter the specification: "))

#Train and classify the data
for i in range(2):
    z = [itemSpecs[i]]
    my_classifier = KNN()
    my_classifier.fit(X, y)
    prediction.append(my_classifier.predict(z))

print ("The predicted class is: " +str(prediction))

#Display
if all(c ==prediction[0] for c in prediction) and itemColor[0]==itemColor[1]:
        print("The products are similar")
else:
        print("The products are different")
