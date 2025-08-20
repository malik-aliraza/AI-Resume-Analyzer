📄 AI Resume Analyzer

An interactive Streamlit web application that analyzes resumes, recommends skills, courses, and generates insights to help candidates improve their chances of getting hired.
It also provides an Admin Dashboard for managing candidate data and visualizing analytics.

✨ Features

📤 Upload resumes in PDF format.

🧠 Extracts resume data using PyResparser and PDFMiner.

🤖 AI-based skill and career field recommendations:

Data Science

Web Development

Android Development

iOS Development

Cybersecurity

Cloud Computing

DevOps

Artificial Intelligence

UI/UX

Call Center/BPO

🎯 Resume improvement tips with scoring system.

🎓 Recommended courses and certifications.

🎥 Bonus videos for Resume Writing and Interview Preparation.

    📊 Admin Dashboard:

Candidate database management (MySQL).

Download user data as CSV.

Visualizations (Predicted Career Fields, Candidate Experience Levels).

    🛠️ Tech Stack

Frontend: Streamlit

Backend: Python (Pandas, PyResparser, PDFMiner)

Database: MySQL (via PyMySQL)

Visualization: Matplotlib, Plotly

Others: yt-dlp (YouTube API for fetching video titles), PIL, Streamlit-Tags

📂 Project Structure
├── Logo/
│   ├── logo.png
│   ├── resume_icon.jpg
├── Uploaded_Resumes/
│   └── (user resumes saved here)
├── Courses.py       # Contains predefined course/video lists
├── app.py           # Main application (your code)
└── README.md        # Documentation

⚙️ Installation

Clone this repository

git clone https://github.com/yourusername/ai-resume-analyzer.git
cd ai-resume-analyzer


Create a virtual environment

python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows


Install dependencies

pip install -r requirements.txt


Example requirements.txt:

streamlit
pandas
pyresparser
pdfminer3
pillow
pymysql
matplotlib
plotly
streamlit-tags
yt-dlp
nltk


Set up MySQL database

Install MySQL and run it locally.

Create a database named cv.

Update your MySQL username & password inside the script:

connection = pymysql.connect(host='localhost', user='root', password='YOUR_PASSWORD', db='cv')

▶️ Usage

Run the application using:

streamlit run app.py


Select User: Upload resume → Get analysis, score, recommendations & videos.

Select Admin: Login with credentials → View candidates, download data, see analytics.

Default Admin Credentials:

Username: Malik Ali Raza
Password: Cyberwar

📊 Example Dashboard

Resume Score: Visual progress bar of resume quality.

Predicted Career Path: Smart field suggestion based on skills.

Pie Charts: Admin overview of candidate career preferences & experience levels.

🚀 Future Enhancements

Integration with LinkedIn API for profile parsing.

NLP-powered Job Description → Resume Matching.

Deployment on Cloud (Heroku/Streamlit Cloud/AWS).

👨‍💻 Author

Developed with ❤️ by Malik Ali Raza