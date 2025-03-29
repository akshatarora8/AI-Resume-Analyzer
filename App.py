
import streamlit as st
import time
import io
import os
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
import random
# Create directories if they don't exist
if not os.path.exists("./Uploaded_Resumes"):
    os.makedirs("./Uploaded_Resumes")

ds_course = [['Machine Learning Crash Course by Google [Free]', 'https://developers.google.com/machine-learning/crash-course'],
             ['Machine Learning A-Z by Udemy', 'https://www.udemy.com/course/machinelearning/'],
             ['Machine Learning by Andrew NG', 'https://www.coursera.org/learn/machine-learning'],
             ['Data Scientist Master Program of Simplilearn (IBM)',
              'https://www.simplilearn.com/big-data-and-analytics/senior-data-scientist-masters-program-training'],
             ['Data Science Foundations: Fundamentals by LinkedIn',
              'https://www.linkedin.com/learning/data-science-foundations-fundamentals-5'],
             ['Data Scientist with Python', 'https://www.datacamp.com/tracks/data-scientist-with-python'],
             ['Programming for Data Science with Python',
              'https://www.udacity.com/course/programming-for-data-science-nanodegree--nd104'],
             ['Programming for Data Science with R',
              'https://www.udacity.com/course/programming-for-data-science-nanodegree-with-R--nd118'],
             ['Introduction to Data Science', 'https://www.udacity.com/course/introduction-to-data-science--cd0017'],
             ['Intro to Machine Learning with TensorFlow',
              'https://www.udacity.com/course/intro-to-machine-learning-with-tensorflow-nanodegree--nd230']]

web_course = [['Django Crash course [Free]', 'https://youtu.be/e1IyzVyrLSU'],
              ['Python and Django Full Stack Web Developer Bootcamp',
               'https://www.udemy.com/course/python-and-django-full-stack-web-developer-bootcamp'],
              ['React Crash Course [Free]', 'https://youtu.be/Dorf8i6lCuk'],
              ['ReactJS Project Development Training',
               'https://www.dotnettricks.com/training/masters-program/reactjs-certification-training'],
              ['Full Stack Web Developer - MEAN Stack',
               'https://www.simplilearn.com/full-stack-web-developer-mean-stack-certification-training'],
              ['Node.js and Express.js [Free]', 'https://youtu.be/Oe421EPjeBE'],
              ['Flask: Develop Web Applications in Python',
               'https://www.educative.io/courses/flask-develop-web-applications-in-python'],
              ['Full Stack Web Developer by Udacity',
               'https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd0044'],
              ['Front End Web Developer by Udacity',
               'https://www.udacity.com/course/front-end-web-developer-nanodegree--nd0011'],
              ['Become a React Developer by Udacity', 'https://www.udacity.com/course/react-nanodegree--nd019']]

android_course = [['Android Development for Beginners [Free]', 'https://youtu.be/fis26HvvDII'],
                  ['Android App Development Specialization',
                   'https://www.coursera.org/specializations/android-app-development'],
                  ['Associate Android Developer Certification', 'https://grow.google/androiddev/#?modal_active=none'],
                  ['Become an Android Kotlin Developer by Udacity',
                   'https://www.udacity.com/course/android-kotlin-developer-nanodegree--nd940'],
                  ['Android Basics by Google',
                   'https://www.udacity.com/course/android-basics-nanodegree-by-google--nd803'],
                  ['The Complete Android Developer Course',
                   'https://www.udemy.com/course/complete-android-n-developer-course/'],
                  ['Building an Android App with Architecture Components',
                   'https://www.linkedin.com/learning/building-an-android-app-with-architecture-components'],
                  ['Android App Development Masterclass using Kotlin',
                   'https://www.udemy.com/course/android-oreo-kotlin-app-masterclass/'],
                  ['Flutter & Dart - The Complete Flutter App Development Course',
                   'https://www.udemy.com/course/flutter-dart-the-complete-flutter-app-development-course/'],
                  ['Flutter App Development Course [Free]', 'https://youtu.be/rZLR5olMR64']]

ios_course = [['IOS App Development by LinkedIn', 'https://www.linkedin.com/learning/subscription/topics/ios'],
              ['iOS & Swift - The Complete iOS App Development Bootcamp',
               'https://www.udemy.com/course/ios-13-app-development-bootcamp/'],
              ['Become an iOS Developer', 'https://www.udacity.com/course/ios-developer-nanodegree--nd003'],
              ['iOS App Development with Swift Specialization',
               'https://www.coursera.org/specializations/app-development'],
              ['Mobile App Development with Swift',
               'https://www.edx.org/professional-certificate/curtinx-mobile-app-development-with-swift'],
              ['Swift Course by LinkedIn', 'https://www.linkedin.com/learning/subscription/topics/swift-2'],
              ['Objective-C Crash Course for Swift Developers', 'https://www.udemy.com/course/objectivec/'],
              ['Learn Swift by Codecademy', 'https://www.codecademy.com/learn/learn-swift'],
              ['Swift Tutorial - Full Course for Beginners [Free]', 'https://youtu.be/comQ1-x2a1Q'],
              ['Learn Swift Fast - [Free]', 'https://youtu.be/FcsY1YPBwzQ']]
uiux_course = [['Google UX Design Professional Certificate',
                'https://www.coursera.org/professional-certificates/google-ux-design'],
               ['UI / UX Design Specialization', 'https://www.coursera.org/specializations/ui-ux-design'],
               ['The Complete App Design Course - UX, UI and Design Thinking',
                'https://www.udemy.com/course/the-complete-app-design-course-ux-and-ui-design/'],
               ['UX & Web Design Master Course: Strategy, Design, Development',
                'https://www.udemy.com/course/ux-web-design-master-course-strategy-design-development/'],
               ['The Complete App Design Course - UX, UI and Design Thinking',
                'https://www.udemy.com/course/the-complete-app-design-course-ux-and-ui-design/'],
               ['DESIGN RULES: Principles + Practices for Great UI Design',
                'https://www.udemy.com/course/design-rules/'],
               ['Become a UX Designer by Udacity', 'https://www.udacity.com/course/ux-designer-nanodegree--nd578'],
               ['Adobe XD Tutorial: User Experience Design Course [Free]',
                'https://youtu.be/68w2VwalD5w'],
               ['Adobe XD for Beginners [Free]', 'https://youtu.be/WEljsc2jorI'],
               ['Adobe XD in Simple Way', 'https://learnux.io/course/adobe-xd']]

resume_videos = {'How to Write a Resume (Resume Writing)': 'https://youtu.be/yp693O87GmM',
                 'Resume Hacks - How to Make a Resume Stand Out': 'https://youtu.be/UeMmCex9uTU',
                 '5 Resume Mistakes You Need to Avoid': 'https://youtu.be/dQ7Q8ZdnuN0',
                 'How to Get Your Resume Noticed by Employers in 5 Seconds Guaranteed': 'https://youtu.be/HQqqQx5BCFY',
                 'Resume Tips 2019: 3 Steps to a Perfect Resume': 'https://youtu.be/CLUsplI4xMU',
                 'Top Resume Mistakes to Avoid': 'https://youtu.be/pbczsLkv7Cc'}

interview_videos = {'How to Ace Your Job Interview': 'https://youtu.be/Ji46s5BHdr0',
                    'Interview Preparation Masterclass': 'https://youtu.be/seVxXHi2YMs',
                    '10 Most Common Interview Questions and Answers': 'https://youtu.be/9FgfsLa_SmY',
                    'Top 10 Job Interview Questions & Answers': 'https://youtu.be/2HQmjLu-6RQ',
                    'Job Interview Tips - How to Prepare for a Job Interview': 'https://youtu.be/DQd_AlIvHUw',
                    'Behavioral Interview Questions and Answers': 'https://youtu.be/oVVdezJ0e7w',
                    'How to Crack a Job Interview Successfully (7 Strategies)': 'https://youtu.be/JZK1MZwUyUU',
                    'Job Interview Tips (Part 1): Research the Company': 'https://youtu.be/CyXLhHQS3KY'}

def embed_youtube_thumbnail(video_url, width=576, height=576):
    try:
        if "youtu.be/" in video_url:
            video_id = video_url.split("/")[-1]
        elif "watch?v=" in video_url:
            video_id = video_url.split("watch?v=")[1].split("&")[0]
        else:
            return "Invalid YouTube URL"
        
        thumbnail_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
        return f'<a href="{video_url}"><img src="{thumbnail_url}" width="{width}" height="{height}"></a>'
    except Exception as e:
        return f"Error: {e}"

def extract_text_from_pdf(file):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams())
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
    with open(file, 'rb') as fh:
        for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
            page_interpreter.process_page(page)
        text = fake_file_handle.getvalue()
    converter.close()
    fake_file_handle.close()
    return text

def calculate_efficiency_score(resume_text, keywords):
    resume_text_lower = resume_text.lower()
    matched_keywords = [keyword for keyword in keywords if keyword.lower() in resume_text_lower]
    efficiency_score = (len(matched_keywords) / len(keywords)) * 100
    return efficiency_score, matched_keywords

def classify_efficiency_level(efficiency_score):
    if efficiency_score < 50:
        return "Poor"
    elif efficiency_score < 75:
        return "Intermediate"
    else:
        return "Excellent"

def recommend_skills(job_role):
    skills_dict = {
        "Data Analyst": {"data analysis", "data visualization", "SQL", "Excel", "statistics"},
        "Machine Learning Engineer": {"machine learning", "deep learning", "Python", "TensorFlow", "scikit-learn"},
    }
    return skills_dict.get(job_role, set())

def recommend_courses(skills):
    recommended_courses = []
    courses = [ds_course, web_course, android_course, ios_course, uiux_course]
    for skill in skills:
        for course in courses:
            for course_name, course_link in course:
                if skill.lower() in course_name.lower():
                    recommended_courses.append((course_name, course_link))
    return recommended_courses

def resume_tips(efficiency_level):
    tips_dict = {
        "Poor": [
            "Focus on showcasing relevant skills and experiences prominently.",
            "Consider taking additional courses or certifications to improve your skills."
        ],
        "Intermediate": [
            "Highlight your achievements and projects related to the job role.",
            "Customize your resume for each job application to emphasize relevant skills."
        ],
        "Excellent": [
            "Ensure your resume is concise and well-organized.",
            "Include quantifiable achievements to demonstrate your impact."
        ]
    }
    return tips_dict.get(efficiency_level, [])

def run_user_interface():
    st.title("Resume Efficiency Analyzer")
    st.sidebar.markdown("# Upload Resume")
    pdf_file = st.sidebar.file_uploader("Choose your Resume (PDF)", type=["pdf"])

    if pdf_file is not None:
        with st.spinner('Analyzing your Resume...'):
            time.sleep(4)
            save_pdf_path = os.path.join('./Uploaded_Resumes', pdf_file.name)
            with open(save_pdf_path, "wb") as f:
                f.write(pdf_file.getbuffer())

            st.subheader("Resume Content")
            resume_text = extract_text_from_pdf(save_pdf_path)
            st.write(resume_text)

            st.subheader("Efficiency Analysis")
            keywords = ['python', 'machine learning', 'data analysis', 'communication skills', 'problem solving']
            efficiency_score, matched_keywords = calculate_efficiency_score(resume_text, keywords)
            st.write(f"Efficiency Score: {efficiency_score:.2f}%")

            efficiency_level = classify_efficiency_level(efficiency_score)
            st.write(f"Efficiency Level: {efficiency_level}")

            st.write("Matched Keywords:")
            for keyword in matched_keywords:
                st.write(keyword)

            job_role = "Data Analyst"
            recommended_skills = recommend_skills(job_role)
            if recommended_skills:
                st.subheader("Recommended Skills:")
                for skill in recommended_skills:
                    st.write(skill)
            else:
                st.write("No recommended skills found for this job role.")

            recommended_courses = recommend_courses(matched_keywords)
            if recommended_courses:
                st.subheader("Recommended Courses:")
                for course_name, course_link in recommended_courses:
                    st.write(f"- {course_name}: {course_link}")
            else:
                st.write("No recommended courses found based on the skills in the resume.")

            tips = resume_tips(efficiency_level)
            if tips:
                st.subheader("Resume Improvement Tips:")
                for tip in tips:
                    st.write(tip)

            st.subheader("Resume Builder YouTube Videos:")
            resume_videos_keys = list(resume_videos.keys())
            random.shuffle(resume_videos_keys)
            for video_title in resume_videos_keys[:3]:
                video_link = resume_videos[video_title]
                st.write(f"### {video_title}")
                st.write(embed_youtube_thumbnail(video_link, width=768, height=480), unsafe_allow_html=True)

            st.subheader("Interview Preparation YouTube Videos:")
            interview_videos_keys = list(interview_videos.keys())
            random.shuffle(interview_videos_keys)
            for video_title in interview_videos_keys[:3]:
                video_link = interview_videos[video_title]
                st.write(f"### {video_title}")
                st.write(embed_youtube_thumbnail(video_link, width=768, height=480), unsafe_allow_html=True)

def run_admin_interface():
    st.title("Admin Interface")
    uploaded_files = os.listdir("./Uploaded_Resumes")
    num_uploaded_resumes = len(uploaded_files)
    st.write(f"Number of users who have uploaded their resume: {num_uploaded_resumes}")
    if num_uploaded_resumes > 0:
        st.subheader("List of Users:")
        for idx, file in enumerate(uploaded_files):
            st.write(f"{idx + 1}. {file}")

def main():
    st.sidebar.title("Navigation")
    selected_page = st.sidebar.radio("Go to", options=["User Interface", "Admin Interface"])

    if selected_page == "User Interface":
        run_user_interface()
    elif selected_page == "Admin Interface":
        run_admin_interface()

if __name__ == "__main__":
    main()

