from pathlib import Path
import streamlit as st
from PIL import Image

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_files = current_dir / "assets" / "CV - MiladYounis.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

PAGE_TITLE = "Data Nerd | Milad Younis"
PAGE_ICON = ":wave:"
NAME = "Milad Younis"
DESCRIPTION = """
Data Analyst and Project Coordinator Specialist, Translating Data into Actionable Improvements
"""
EMAIL = "miladyounis@pm.me"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/milad-younis/",
    "Github": "https://gist.github.com/miladyounis"
}
PROJECTS = {
    "🏆 Delivery Company SQL Queries": "https://gist.github.com/miladyounis/e7b57fca9a2688055bb464d69061d257",
    "🏆 Pulling Data from a Bitcoin Full Node": "https://gist.github.com/miladyounis/ea349cf09a982ee26a2e55986710a50c#blockchain-information",
    "🏆 Car Market Research & Analysis through scraping": "https://github.com/miladyounis/mobilebg_data_scraper"
}

TESTIMONIALS = [
    """
    "Working with Milad on TICO Reporting has been a real pleasure. Milad's knack for understanding complex concepts and the meticulous attention to detail Milad brings to the table is truly impressive. I appreciate the dedication and hard work Milad has put into this. Looking forward to more collaborations in the near future!"
    <br><br>
    <div style="text-align: right;">Rayan Dutta, Specialist DevOps Engineer at SAP</div>
    """,
    """
    "Thank you for constantly pushing your knowledge and understanding of how our team works as with your can-do attitude and automation abilities this will help our organization improve and achieve better results. Never give up and continue to improve and most importantly always stay curious about what’s out there, as currently the technological world is evolving at a rapid pace and we need more people like you to help guide us into this new reality."
    <br><br>
    <div style="text-align: right;">Alexander Alexandrov, Senior Continuous Improvement Lead at SAP</div>
    """,
    """
    "I wanted to take a moment to express my deepest gratitude for the outstanding job you did on the recent customer communication report.
    <br><br>
    Your dedication, attention to detail, and commitment to delivering high-quality work were truly evident in every aspect of the reports. The thorough analysis, clear point of view, and pure curiosity, the fact that you find a trend no one else could see, and the insightful conclusions not only met but exceeded our expectations.
    <br><br>
    Please accept my sincere appreciation for your efforts. Your contributions have not only made the TICO Reporting topic better but have also elevated the global organization's understanding. Your commitment to excellence does not go unnoticed, and I am grateful to have you as my colleague in TICO.
    <br><br>
    Once again, thank you for your exceptional work. I look forward to our continued collaboration and success on future projects."
    <br><br>
    <div style="text-align: right;">Kiril Krantev, Head of Cloud Operations Center Sofia</div>
    """,
    """
    "I want to express my sincere appreciation for your outstanding work during your internship. Your dedication, enthusiasm, and contributions have been truly impressive, making you an invaluable part of our team. Throughout your time here, you approached every task with a positive attitude and a hunger for learning. Your attention to detail and creative thinking significantly influenced the Reporting topics you worked on. The custom reports in SAC, dashboards in Snow, and swift additions to global topics in the Reporting stream were particularly noteworthy, showcasing professionalism and skill beyond your experience. Your positive attitude, willingness to help others, and initiative in seeking feedback have made you an inspiring team member. Thank you for your exceptional work and commitment to excellence. You've left a lasting impression on our team, and we are confident that you will continue to excel in your future endeavors."
    <br><br>
    <div style="text-align: right;">Ilia Kurdalanov, Cloud Operations Manager at SAP</div>
    """
]

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_files, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=265)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_files.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

    # Social media links below email side by side without icons
    st.markdown(
        """
        <div style="display: flex; gap: 10px;">
            <a href="https://www.linkedin.com/in/milad-younis/" target="_blank">LinkedIn</a> |
            <a href="https://gist.github.com/miladyounis" target="_blank">GitHub Gists</a> |
            <a href="https://github.com/miladyounis" target="_blank">GitHub Repos</a>
        </div>
        """,
        unsafe_allow_html=True
    )

# --- SUMMARY ---
st.write('\n')
st.subheader("Summary")
st.write(
    """
    I am a 22 years old data nerd, leveraging it in my professional career as well as personal life, what makes me a great asset is my knack for investigating the data
    heavily, finding anomalies and persisting on finding answers and generally being curious which oftentimes leads to great process improvements 
    and better business understanding.

    On the personal side I am huge family guy that enjoys climbing, football and karate, I am also a fan and proponent of Bitcoin and Nostr protocols, 
    running my own full bitcoin node, nostr relay, contributing to the space in various tangible ways, such as being a local meet-up organizer 
    and previously beingan ambassador for the Yzer Education app.
    """
)

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ 2 Years experience extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python, SQL and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Pandas, Matplotlib, Seaborn), SQL, VBA
- 📊 Data Visualization: SAP Analytics Cloud, MS Excel, Tableau, ServiceNow
- 🗄️ Databases: MySQL, SAP HANA
- 📚 Other: Git & Github, APIs, Streamlit 
"""
)

st.write('\n')
st.subheader("Soft Skills")
st.write(
    """
- ⏰ Time Management Fundamentals
- 📋 Project Management Fundamentals
- 🗣️ Effective Communication
- 📚 Continuous Learning
- 🚀 Initiative Taker
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.markdown(
    "🚧 <span style='font-size:20px; font-weight: bold;'>Data Analyst for Product Security Analytics Specialist | SAP</span>",
    unsafe_allow_html=True
)
st.write("09/2024 - Present")
st.write(
    """
- ► Collecting data through APIs from various vulnerability and cyber databases as well as security scanners
- ► Modeling and transforming data with performance in mind for dashboard purposes that is consumed by management level
- ► Providing an API integration to 50,000+ SAP developers for security compliance metrics
- ► Fascilitating and harmonizing SAST, DAST and OSVM data for all of SAP applications, source code and open source libraries in use 
- ► Regularly presenting findings with security experts and supporting their processes
"""
)

# --- JOB 1
st.markdown(
    "🚧 <span style='font-size:20px; font-weight: bold;'>Data Analyst & ITSM Project Coordinator Specialist | SAP</span>",
    unsafe_allow_html=True
)
st.write("04/2024 - 09/2024")
st.write(
    """
- ► Used SQL Modeling in an organization wide team daily to build, maintain, upgrade and fix 5+ source of truth dashboards
- ► Spotted anomalies that shed light on certain business practices that led to improvements
- ► Initiated and coordinated an organization wide quality assurance project that helped increase incident quality by 36%
- ► Provided an overview of the whole customer communication landscape for the first time in the organization, which sparked 2+ improvement projects
- ► Presented and participated in CoP sessions on GenAI in the workplace organization-wide to 170+ people
"""
)

# --- JOB 2
st.write('\n')
st.markdown(
    "🚧 <span style='font-size:20px; font-weight: bold;'>Reporting Intern for Cloud Operations | SAP</span>",
    unsafe_allow_html=True
)
st.write("10/2022 - 04/2024")
st.write(
    """
- ► Automated and Upgraded 20+ monthly hours of manual reporting efforts using Macros, VBA and other BI tools
- ► Took initiative on ad-hoc reports and state analysis to derive business value and improvement plans
- ► Developed a python script to assist engineers in retrieving critical information in time-sensitive situations improving our KPIs by 300%
- ► Helped 5+ teams onboard to ServiceNow as a single point of reporting expertise
"""
)

# --- JOB 3
st.write('\n')
st.markdown(
    "🚧 <span style='font-size:20px; font-weight: bold;'>Data Processor Internship Program | Dynata</span>",
    unsafe_allow_html=True
)
st.write("03/2022 - 04/2022")
st.write(
    """
- ► Survey Programming & Analysis
- ► Data Visualization and Reporting
- ► Business Understanding and Critical Thinking
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

# Add disclaimer
st.write(
    """
    **Disclaimer**: Unforunately some of my coolest projects are confidential. If I told you, I'd have to make you sign an NDA 😅. However above are some things I did on the side.
    """
)

# --- TESTIMONIALS ---
st.write('\n')
st.subheader("Testimonials")
st.write("---")

# Testimonial navigation
testimonial_index = st.session_state.get('testimonial_index', 0)

col1, col2, col3 = st.columns([1, 8, 1])
with col1:
    if st.button('⟨', key='prev'):  # Use a different arrow symbol
        testimonial_index = (testimonial_index - 1) % len(TESTIMONIALS)
        st.session_state['testimonial_index'] = testimonial_index
with col3:
    if st.button('⟩', key='next'):  # Use a different arrow symbol
        testimonial_index = (testimonial_index + 1) % len(TESTIMONIALS)
        st.session_state['testimonial_index'] = testimonial_index

st.markdown(f"""
    <div class="testimonial-container">
        <div class="testimonial-item">{TESTIMONIALS[testimonial_index]}</div>
    </div>
""", unsafe_allow_html=True)

# --- DATA BOOKS I RECOMMEND ---
st.write('\n')
st.subheader("Data Books I Recommend")
st.write("---")

# Load book covers
books = [
    "big data.jpg",
    "calling bullshit.jpg",
    "math.png",
    "WMD.jpg"
]

cols = st.columns(len(books))

for col, book in zip(cols, books):
    with col:
        book_cover = current_dir / "assets" / book
        image = Image.open(book_cover)
        st.image(image, use_column_width=True)
