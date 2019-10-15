import numpy as np
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn import svm
from sklearn.ensemble import VotingClassifier
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import LinearSVC
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score


def read_file_r(train_file):
	X = []
	y = []

	with open(train_file, 'r') as file:
		for line in file:
			line = line.replace('\n',"")
			line = line.split('\t')
			
			aux_X = []
			aux_y = []
			
			for i in range (len(line)-3):
				aux_X.append(float(line[i]))

			aux_y.append(float(line[len(line)-3]))
			aux_y.append(float(line[len(line)-2]))

			X.append(aux_X)
			y.append(aux_y)

	return X,y

def read_file_c(train_file):
	X = []
	y = []

	with open(train_file, 'r') as file:
		for line in file:
			line = line.replace('\n',"")
			line = line.split('\t')
			
			aux_X = []
			aux_y = []
			
			for i in range (len(line)-3):
				aux_X.append(float(line[i]))

			aux_y.append(float(line[len(line)-2]))

			X.append(aux_X)
			y.append(aux_y)

	return X,y

def get_best_k(X,y,classifier):
	k_range = [15,20,25,30,36]

	feature_selection = SelectKBest(chi2)

	pipeline = Pipeline([('chi2', feature_selection),('classifier', classifier)])

	grid = GridSearchCV(pipeline, param_grid={'chi2__k':k_range}, scoring='accuracy',iid=True,cv=10)
	grid.fit(X, y)

	print(grid.best_params_,grid.best_score_,grid.best_index_)

	return grid.best_params_['chi2__k']


def regression():
	train_file_r = 'Data/Features/train_features.txt'
	test_file_r = 'Data/Features/1819features.txt'

	X_train,y_train = read_file_r(train_file_r)
	X_test, y_test = read_file_r(test_file_r)

	scaler = MinMaxScaler()
	scaler.fit(X_train)
	scaler.fit(X_test)

	mlp = MLPRegressor(
	solver='lbfgs',
	activation='identity',
	hidden_layer_sizes=(20,),
	warm_start=True,
	max_iter=100)

	mlp.fit(X_train,y_train)
	predicted = mlp.predict(X_test)
	
	win = 0
	for i in range(len(predicted)):
		if predicted[i][0] > predicted[i][1] and y_test[i][0] > y_test[i][1]:
			win += 1
		elif predicted[i][1] > predicted[i][0] and y_test[i][1] > y_test[i][0]:
			win += 1

	print (mlp.score(X_test,y_test), predicted.min(), win / len(predicted))

def classification():
	train_file_c = 'Data/Features/trainfeatures_binary.txt'
	test_file_c = 'Data/Features/1819features_binary.txt'

	X_train,y_train = read_file_c(train_file_c)
	X_test, y_test = read_file_c(test_file_c)

	kfold = KFold(n_splits=10, random_state=7)

	clf1 = svm.SVC(kernel='linear', C=0.1, probability=True)
	clf2 = GaussianNB()
	clf3 = MultinomialNB()
	clf4 = RandomForestClassifier(n_estimators=1000)
	clf5 = KNeighborsClassifier(n_neighbors=200)

	classifier = VotingClassifier(estimators=[('svm', clf1),('rf', clf4),('gnb', clf2)],voting='soft')
	y_train = np.array(y_train)
	y_train = y_train.ravel()

	#nr_features = get_best_k(X_train,y_train,classifier)
	#chi_2 = SelectKBest(chi2, k=36)

	#X_train = chi_2.fit_transform(X_train,y_train)
	#X_test = chi_2.fit_transform(X_test,y_test)

	result = cross_val_score(classifier, X_train, y_train.ravel(), cv=kfold, scoring='accuracy')

	classifier.fit(X_train,y_train)

	y_pred = classifier.predict(X_test)
	y_probs = classifier.predict_proba(X_test)

	print (y_test)

	report = classification_report(y_test,y_pred,output_dict=True)

	print (result.mean())
	print (accuracy_score(y_test,y_pred),y_probs)

	return y_probs, y_test
	
if __name__ == "__main__":

	#regression()
	classification()

