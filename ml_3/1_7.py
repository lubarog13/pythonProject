from sklearn import datasets
iris = datasets.load_iris()
iris_X = iris.data


from sklearn import decomposition

pca = decomposition.PCA(n_components=2)
iris_X_prime = pca.fit_transform(iris_X)
iris_X_prime.shape

from matplotlib import pyplot as plt

f = plt.figure(figsize=(5,5))
ax = f.add_subplot(111)
ax.scatter(iris_X_prime[:,0], iris_X_prime[:, 1], c=iris.target)
ax.set_title('PCA: 2 components')

print(pca.explained_variance_ratio_.sum())
plt.show()