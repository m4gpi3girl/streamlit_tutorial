# import packages

# streamlit to make the app
import streamlit as st

# pandas to be our excel
import pandas as pd 

# to do vizzz
pip install matplotlib
import matplotlib.pyplot as plt



# for the csv to be read
def read_csv(file):
    df_info = pd.read_csv(file)
    return df_info



# the app
def main():

    secret_key = st.text_input("Enter the secret key")

    if secret_key == 'ANIMALS':

        # title 
        st.title("CSV Test")

        # give user option to upload file
        uploaded_file = st.file_uploader("Upload your csv containing postcodes. Please make sure your postcode column is called 'Postcode'", type=["csv"])


        # if successful:
        if uploaded_file is not None:

            # confirm upload
            st.success("File uploaded")

            st.write("Here is your breakdown!")

            # read csv into pandas df
            df_info = read_csv(uploaded_file)

            # read geog data
            imd_info = pd.read_csv('pc_data.csv')

            # merge csv and imd data
            new_df = df_info.merge(imd_info, left_on='Postcode', right_on='pcds', how='left')

            # drop unnessary cols
            new_df = new_df.drop(columns=['Unnamed: 0', 'pcds', 'rgn', 'lsoa21', 'lsoa11', 'RUC11CD'])
    
            # drop blanks
            new_df = new_df.dropna(subset="Index of Multiple Deprivation (IMD) Decile")

            # imd freq
            counts = new_df['Index of Multiple Deprivation (IMD) Decile'].value_counts()
            counts_df = counts.reset_index()
            counts_df.columns = ['IMD Decile', 'Number in DF']
            counts_df['IMD Decile'] = counts_df['IMD Decile'].astype(str)

            # imd 1 to 3


            # test statement
            st.write('Info test:')
            # print number of cols in df
            st.write(f"Number of columns: {df_info.shape[0]}")
            # print IMD head
            # st.write(imd_counts_df.head())

            # button for getting more info
            
            # if button clicked
            if st.button("IMD Breakdown"):

                # show imd dist as a pie chart
                df = counts_df
                plt.pie(df['IMD Decile'], labels=df['IMD Decile'], autopct='%1.1f%%', startangle=90)
                plt.title('Distribution Across IMD Areas')
                st.pyplot()




            # button to show full dataframe
            if st.button('See full table'):
                st.write(new_df)



            # button to see rural urban split
            #if st.button('See Rural Urban Split'):
                #st.write(grouped_df)

        else:
            st.warning('No file uploaded.')

# run app
if __name__ == "__main__":
    main()


# could add the option to share data with sib for us to perform further analysis
    
# customers - compare against the average

# using YIF data for a YIF 2 - based on prior data, your areas of difficulty could be x y z
    
# demographic breakdown (imd, ethnicity etc)
    
