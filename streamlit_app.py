import pdfkit
import streamlit as st


def html2pdf():
    pdfkit.from_url('https://www.google.de/', 'google.pdf')


if __name__ == "__main__":
    st.set_page_config(page_title="Selenium Test", page_icon='✅',
        initial_sidebar_state='collapsed')
    st.title('🔨 Selenium Test for Streamlit Sharing')
    st.markdown("""
        This app is only a very simple test for **Selenium** running on **Streamlit Sharing** runtime. <br>
        The suggestion for this demo app came from a post on the Streamlit Community Forum.  <br>
        <https://discuss.streamlit.io/t/deploying-an-app-using-using-wkhtmltopdf-on-herokou/12029>  <br>

        This is just a very very simple example and a proof of concept.
        A link is called and converted HTML to PDF.
        Afterwards the pdf file is displayed.
        ---
        """, unsafe_allow_html=True)
    st.balloons()
    if st.button('Start Selenium run'):
        st.info('Selenium is running, please wait...')
        html2pdf()
        st.info('Successful finished.')
