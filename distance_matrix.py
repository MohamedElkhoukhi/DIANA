import numpy as np 
from pathlib import Path
import pandas as pd 
from calculate_similarity import SimilarityMeasure
import pickle

#this function calculates Distance Matrix or Similarity matrix
def DistanceMatrix(data =None):
	'''
	arguement
	---------
	data - the dataset whose Similarity matrix we are going to calculate
	returns
	-------
	the distance matrix by loading th pickle file
	'''
	pickleFilePath = Path('SimMat.pkl') #checking if the distance matrix was saved from last run to save processing
	Data_list = []
	for index, rows in data.iterrows():
		my_data = [rows.Hobby, rows.Age, rows.Educational_Level, rows.Marital_Status]
		Data_list.append(my_data)

	if pickleFilePath.is_file():
		temp_file=open(pickleFilePath, 'rb')
		return pickle.load(temp_file)

	else:
		N = len(data)
		similarity_mat = np.zeros([N, N]) #for cosine np.ones
		for i in range(N):
			for j in range(N):
				similarity_mat[i][j]=SimilarityMeasure(Data_list[i],Data_list[j])


			with open('SimMat.pkl', 'wb') as file:
				pickle.dump(similarity_mat, file)

		temp_file=open(pickleFilePath, 'rb')
		return pickle.load(temp_file)


if __name__=='__main__':
	# for testing the module
	data = pd.read_csv('HAYES_ROTH.csv')
	data = data.drop(columns="Name")
	data = data.drop(columns="Class")
	Data_list = []
	for index, rows in data.iterrows():
		my_data = [rows.Hobby, rows.Age, rows.Educational_Level, rows.Marital_Status]
		Data_list.append(my_data)
	dist_mat = DistanceMatrix(Data_list)
	print(dist_mat.shape)
