import matplotlib.pyplot as plt
from sklearn import datasets, metrics, svm
from sklearn.model_selection import train_test_split

digits = datasets.load_digits()

_, axes = plt.subplots(nrows=1, ncols=4, figsize=(10, 3))
for ax, image, label in zip(axes, digits.images, digits.target):
  ax.set_axis_off()
  ax.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
  ax.set_title("Training: %i" % label)

from numpy import False_
# flatten the images
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

#create a classfier: a support vector classifier
clf = svm.SVC(gamma=0.001)

#split data into 50% train and 50% test subsets
x_train, x_test, y_train, y_test = train_test_split(
    data, digits.target, test_size=0.5, shuffle=False
)

#learn the digit on the train subset
clf.fit(x_train, y_train)

#predict the value of the digit on the test subset
predicted = clf.predict(x_test)

_, axes = plt.subplots(nrows=1, ncols=4, figsize=(80, 20))
for ax, image, prediction in zip(axes, x_test, predicted):
  ax.set_axis_off()
  image = image.reshape(8, 8)
  ax.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
  ax.set_title(f"prediction:{prediction}")

print(
    f"Classification report for classifier {clf}: \n"
    f"{metrics.classification_report(y_test,predicted)}\n"
)

disp = metrics.ConfusionMatrixDisplay.from_predictions(y_test, predicted)
disp.figure_.suptitle("Confusion Matrix")
print(f"Confusion matrix: \n{disp.confusion_matrix}")

plt.show()

# the ground truth and predicted lists
y_true = []
y_pred = []
cm = disp.confusion_matrix

#for aech cell in the confusion matrix, add the corresponding grounp trusths
#and predictions to the lists
for gt in range(len(cm)):
  for pred in range(len(cm)):
    y_true += [gt] * cm[gt][pred]
    y_pred += [pred] * cm[gt][pred]

    print(
        "Classification report rebuit from confusion matrix:\n"
        f"{metrics.classification_report(y_true, y_pred)}\n"
    )


from dateutil.relativedelta import TU
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import svm

x, y = datasets.load_iris(return_X_y=True)
x.shape, y.shape

x_train, x_test, y_train, y_test = train_test_split(
    x,y, test_size=0.4, random_state=0
)

x_train.shape, y_train.shape

x_test.shape, y_test.shape

clf = svm.SVC(kernel='linear', C=1).fit(x_train, y_train)
clf.score(x_test, y_test)

from sklearn.ensemble import RandomForestClassifier
x = [[0, 0], [1,1]]
y = [0, 1]
clf = RandomForestClassifier(n_estimators=10)
clf = clf.fit(x, y)
