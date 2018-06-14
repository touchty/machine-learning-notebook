from sklearn import tree
X = [[0, 0], [1, 1]]
Y = [0, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)
predictedCluster = clf.predict([[2., 2.]])
print(predictedCluster)

# iris database
from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)
predictedCluster = clf.predict(iris.data[:1, :])
print(predictedCluster)

# Below is an example graphviz export of the above tree trained 
# on the entire iris dataset; the results are saved in an output file iris.pdf:
import graphviz 
dot_data = tree.export_graphviz(clf, out_file=None) 
graph = graphviz.Source(dot_data) 
graph.render("iris") 
graph.view