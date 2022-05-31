import os
import streamlit as st

#DA Package
import pandas as pd 

#Visual Packages
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib



###Main Funtion

def main():

	html_header = """<div style = "background-color:White"><div align="center";><h1>Lazy Learner - Data Explorer</h1></div></div>"""
	st.markdown(html_header,unsafe_allow_html=True)
	st.sidebar.title("COLUMBUS - The Explorer")
	
	def file_selector():
		#filenames=os.listdir(folder_path)		
		selected_filename=st.file_uploader("Upload your dataset", type=None, encoding='auto', key=None)
		return (selected_filename)
	
	filename=file_selector()

	#Read data using Pandas
	if not filename:
		df =pd.DataFrame()
	else:
		df = pd.read_csv(filename)

	#Show dataset values
	st.sidebar.subheader("Data Description")
	if st.sidebar.checkbox("Describe the data"):
		number = st.number_input("Select row count",value=1, step=1, max_value=len(df))
		st.dataframe(df.head(number))

	#Show Columns 
	if st.sidebar.checkbox("Show Column Names"):
		st.subheader("Columns in the dataset:")
		st.write(df.columns)

	#Show shapes
	if st.sidebar.checkbox("Show the data shape"):
		st.write(df.shape)
		data_dim=st.radio("Show Dimension by ",("Rows", "Columns"))
		if(data_dim) =='Rows':
			st.text("Number of Rows")
			st.write(df.shape[0])
		if(data_dim) =='Columns':
			st.text("Number of Columns")
			st.write(df.shape[1])

	#Select Columns
	if st.sidebar.checkbox("Select Columns to show"):
		all_columns = df.columns.tolist()
		selected_columns = st.multiselect("Select ",all_columns)
		new_df = df[selected_columns]
		new_df.size
		st.dataframe(new_df)



	#Show summmary
	if st.sidebar.checkbox("Data Summary"):
		st.write(df.describe().T)

	#Data Cleaning
	st.sidebar.subheader("Data Cleaning Options ")
	st.sidebar.info("Affects on the original dataset - Irreversible")
	if st.sidebar.checkbox("Remove Empty Rows - Removed NaN values too"):
		df= df.fillna('')
		df.dropna()

	#Drop column values
	if st.sidebar.checkbox("Remove Column - Removed NaN values too"):
		df= df.fillna('')
		df=df.replace('')
		df.dropna(axis='columns')


	#Convert to best fit datatypes
	if st.sidebar.checkbox("Convert to best fit datatypes"):
		dfn=df.convert_dtypes()
		df=dfn
	#Show DataTypes 
	if st.button("Show DataTypes"):
		df.dtypes


	#Plot and visualization
	st.sidebar.subheader("Data visualization")

	#Correlation

	#Seaborn Plot

	#Count Plot

	#Piechart 

	#Customizable Plot

	st.subheader("Data Representation")

	all_columns_names = df.columns.tolist()
	type_of_plot = st.sidebar.selectbox("Select Type of plot ",["area","bar","line"])
	selected_columns_names = st.multiselect("Select Columns to plot",all_columns_names)

	
	if st.button("Generate Plot(s)"):

		st.success("Generating Customizable Plot of {} for {}".format(type_of_plot,selected_columns_names))

		#Plot by stramlit
		if type_of_plot == 'area':
			cust_data = df[selected_columns_names]
			st.area_chart(cust_data)

		elif type_of_plot == 'bar':
			cust_data = df[selected_columns_names]
			st.bar_chart(cust_data)

		elif type_of_plot == 'line':
			cust_data = df[selected_columns_names]
			st.line_chart(cust_data)



		#Custom Plot
		elif type_of_plot:
			cust_plot = df[selected_columns_names].plot(kind=type_of_plot)
			st.write(cust_plot)
			st.pyplot()

	#Download Function
	def down_file(data,filename):
		with open(os.path.join("/",filename),"w") as f:
			dnfilename = f.write(df)
			return dnfilename



	#Download the updated dataset
	st.sidebar.subheader("Download the edited dataset")
	if st.sidebar.button("Download"):
		
		df.to_csv("~//Downloads//Fileclean12.csv")
		st.info("You file is downloaded at ~//Downloads//Fileclean1.csv")
		#down_file(df,"CleanFile.csv")


if __name__ == '__main__':
	main() 