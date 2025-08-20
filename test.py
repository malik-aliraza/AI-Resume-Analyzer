import streamlit as st
import time
import pymysql
import base64
import io
from pdfminer.high_level import extract_text
from pdfminer.converter import PDFPageAggregator, TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pyresparser import ResumeParser


def pdf_reader(file):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams())
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
    file_stream = io.BytesIO(file.getvalue())  # Use BytesIO for handling file

    for page in PDFPage.get_pages(file_stream, caching=True, check_extractable=True):
        page_interpreter.process_page(page)
    text = fake_file_handle.getvalue()

    converter.close()
    fake_file_handle.close()
    return text


def show_pdf(file):
    base64_pdf = base64.b64encode(file.getvalue()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)


def connect_db():
    try:
        connection = pymysql.connect(host='localhost', user='root', password='Codex', db='cv')
        cursor = connection.cursor()
        return connection, cursor
    except Exception as e:
        st.error(f"Database connection failed: {e}")
        return None, None


def insert_user_data(cursor, connection, data):
    query = """
    INSERT INTO user_data (name, email, resume_text, skills, experience, education)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (
        data['name'], data['email'], data['resume_text'],
        ', '.join(data['skills']), data['experience'], data['education']
    ))
    connection.commit()


def run():
    st.title("Resume Uploader and Viewer")
    activities = ['User', 'Admin']
    choice = st.sidebar.selectbox('Choose among the options:', activities)
    
    if choice == 'User':
        st.markdown("Upload your resume in PDF format:")
        pdf_file = st.file_uploader("Upload PDF", type=['pdf'])
        
        if pdf_file is not None:
            with st.spinner('Uploading your Resume...'):
                time.sleep(4)
            
            # Display the PDF
            show_pdf(pdf_file)
            
            try:
                # Read and parse the PDF
                resume_data = ResumeParser(pdf_file).get_extracted_data()
                resume_text = pdf_reader(pdf_file)
                
                # Ensure resume data was extracted
                if resume_data:
                    # Display extracted resume data
                    st.write("### Extracted Data from Resume:")
                    st.write(f"**Name:** {resume_data.get('name')}")
                    st.write(f"**Email:** {resume_data.get('email')}")
                    st.write(f"**Skills:** {', '.join(resume_data.get('skills', []))}")
                    st.write(f"**Experience:** {resume_data.get('experience')}")
                    st.write(f"**Education:** {resume_data.get('education')}")
                    
                    # Insert data into database
                    connection, cursor = connect_db()
                    if connection and cursor:
                        insert_user_data(cursor, connection, {
                            'name': resume_data.get('name'),
                            'email': resume_data.get('email'),
                            'resume_text': resume_text,
                            'skills': resume_data.get('skills', []),
                            'experience': resume_data.get('experience'),
                            'education': resume_data.get('education')
                        })
                        st.success("Data inserted into database successfully.")
                        cursor.close()
                        connection.close()
                    else:
                        st.error("Failed to connect to the database.")
                else:
                    st.error("Failed to extract data from the resume.")
            
            except Exception as e:
                st.error(f"Error processing PDF: {e}")
    
    elif choice == 'Admin':
        st.success('Welcome to Admin Side')
        st.write("### Registered Users in Database")
        
        # Connect to the database and fetch data
        connection, cursor = connect_db()
        if connection and cursor:
            cursor.execute("SELECT name, email, skills, experience, education FROM user_data")
            data = cursor.fetchall()
            
            # Display data if available
            if data:
                for i, row in enumerate(data, start=1):
                    st.write(f"**User {i}**")
                    st.write(f"**Name:** {row[0]}")
                    st.write(f"**Email:** {row[1]}")
                    st.write(f"**Skills:** {row[2]}")
                    st.write(f"**Experience:** {row[3]}")
                    st.write(f"**Education:** {row[4]}")
                    st.write("---")
            else:
                st.info("No user data found in the database.")
            
            cursor.close()
            connection.close()
        else:
            st.error("Failed to connect to the database.")


if __name__ == "__main__":
    run()
