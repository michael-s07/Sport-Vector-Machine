#import codecademylib3_seaborn
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from svm_visualization import draw_boundary
from players import aaron_judge, jose_altuve, david_ortiz

fig, ax = plt.subplots()

def find_strike_zone(dataset, x, y):
  dataset.type = dataset.type.map({'S':1, 'B':0})
  print(dataset.columns)
  print(dataset.description)
  print(dataset.type)
  print(dataset.plate_z)

  dataset = dataset.dropna(subset = ['type', 'plate_x', 'plate_z'])
  print(dataset)

  plt.scatter(x = dataset.plate_x, y = dataset. plate_z, c = dataset.type, cmap = plt.cm.coolwarm, alpha=0.25)
  training_set, validation_set = train_test_split(dataset, random_state = 1)

  largest = {'value':0, 'gamma':1, 'C':1}
  for gamma in range(1, 5):
   for C in range(1, 5):
      classifier = SVC(kernel = 'rbf', gamma= gamma, C=C)
      classifier.fit(training_set[[x, y]], training_set.type)

      score = classifier.score(validation_set[['plate_x', 'plate_z']], validation_set.type)
      if(score > largest['value']):
        largest['value']=score
        largest['gamma']=gamma
        largest['C']=C
   print(largest)
   draw_boundary(ax, classifier)
   ax.set_ylim(-2, 6)
   ax.set_xlim(-3, 3)
   plt.show()

find_strike_zone(aaron_judge, 'plate_x', 'plate_z')
find_strike_zone(jose_altuve, 'plate_x', 'plate_z')
