import streamlit as st
import pandas as pd

def main():
    # Read the Excel file
    df = pd.read_csv('drug.csv')

    # Set Streamlit page configuration to wide layout
    st.set_page_config(layout="wide")

    # Add custom CSS styles
    st.markdown(
        """
        <style>
        /* Add your CSS styles here */
        body {
            font-family: Arial, sans-serif;
        }
        .title {
            color: #1f7ddb;
            font-size: 24px;
            text-align: center;
            margin-bottom: 20px;
        }
        .home-link {
            text-align: right;
            margin-top: -30px;
            margin-bottom: 20px;
        }
        .home-link a {
            color: #1f7ddb;
            text-decoration: none;
            font-size: 16px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Add JavaScript snippet for fullscreen display
    st.markdown(
        """
        <script>
        document.addEventListener('DOMContentLoaded', function() {
            const elem = document.documentElement;
            if (elem.requestFullscreen) {
                elem.requestFullscreen();
            } else if (elem.mozRequestFullScreen) { /* Firefox */
                elem.mozRequestFullScreen();
            } else if (elem.webkitRequestFullscreen) { /* Chrome, Safari and Opera */
                elem.webkitRequestFullscreen();
            } else if (elem.msRequestFullscreen) { /* IE/Edge */
                elem.msRequestFullscreen();
            }
        });
        </script>
        """,
        unsafe_allow_html=True
    )
    
    # Display the contents of the Excel file
    st.markdown("<h1 class='title'>Dataset</h1>", unsafe_allow_html=True)
    
    # Add a Home link
   

    
    
    # Display the contents of the Excel file
    st.dataframe(df)

if __name__ == '__main__':
    main()
