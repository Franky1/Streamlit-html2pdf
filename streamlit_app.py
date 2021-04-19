import base64

import pdfkit
import streamlit as st


def html2pdf(url, pdf_file):
    pdfkit.from_url(url, pdf_file)


def readpdf(pdf_file):
    with open(pdf_file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
    return pdf_display


if __name__ == "__main__":
    st.set_page_config(page_title="HTML2PDF", page_icon='✅',
        initial_sidebar_state='collapsed')
    st.title('🔨 HTML2PDF Test for Streamlit Sharing')
    st.markdown("""
        This app is only a very simple test for html2pdf on **Streamlit Sharing** runtime. <br>
        The suggestion for this demo app came from a post on the Streamlit Community Forum.  <br>
        <https://discuss.streamlit.io/t/deploying-an-app-using-using-wkhtmltopdf-on-herokou/12029>  <br>

        This is just a very very simple example and a proof of concept.
        A link is called and converted HTML to PDF.
        Afterwards the pdf file is displayed.

        The downside is that websites with content created by javascript will probably not be rendered properly.
        Onyl static website content will be downloaded and therefore rendered to pdf.
        """, unsafe_allow_html=True)
    st.balloons()
    if st.button('Start html2pdf run'):
        url = "https://discuss.streamlit.io/"
        st.info(f'Download and render pdf from url: {url}')
        st.info('html2pdf is running, please wait...')
        pdf_file = "download.pdf"
        html2pdf(url=url, pdf_file=pdf_file)
        pdf_display = readpdf(pdf_file)
        st.info('Successful finished. See PDF below.')
        st.markdown(pdf_display, unsafe_allow_html=True)
