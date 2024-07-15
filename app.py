from pathlib import Path
import streamlit as st
from PIL import Image

current_dir = Path(__file__).parent if "__File__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_files = current_dir / "assets" / "CV - MiladYounis.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

PAGE_TITLE = "Data Nerd | Milad Younis"
PAGE_ICON = ":wave:"
NAME = "Milad Younis"
DESCRIPTION = """
Data Analyst and Project Coordinator Specialist, Translating Data to Actionable Improvements
"""
EMAIL = "miladyounis@pm.me"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/milad-younis/",
    "Github": "https://gist.github.com/miladyounis"
}
PROJECTS = {
    "🏆 Delivery Company SQL Queries": "https://gist.github.com/miladyounis/e7b57fca9a2688055bb464d69061d257",
    "🏆 Pulling Data from a Bitcoin Full Node": "https://gist.github.com/miladyounis/ea349cf09a982ee26a2e55986710a50c#blockchain-information"
}

TESTIMONIALS = {
    "Milad is a highly skilled data analyst with a keen eye for detail.",
    "His ability to translate data into actionable insights is unparalleled.",
    """\
"Working with Milad on TICO Reporting has been a real pleasure. Milad's knack for understanding complex concepts and the meticulous attention to detail Milad brings to the table is truly impressive. I appreciate the dedication and hard work Milad has put into this. Looking forward to more collaborations in the near future!"

{}""".format("Rayan Dutta, Specialist DevOps Engineer at SAP".rjust(100))
}

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
    st.image(profile_pic, width=230)

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

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

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
- 👩‍💻 Programming: Python (Pandas, Matplotlib, Numpy), SQL, VBA
- 📊 Data Visualization: SAP Analytics Cloud, MS Excel, Tableau, ServiceNow
- 📚 Modeling: Logistic regression, linear regression, decision trees
- 🗄️ Databases: MySQL, SAP HANA
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Data Analyst & Project Coordinator Specialist | SAP**")
st.write("04/2024 - Present")
st.write(
    """
- ► Used PowerBI and SQL to redefine and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
- ► Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
- ► Redesigned data model through iterations that improved predictions by 12%
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Intern in the Database Cloud Operations Team | SAP**")
st.write("10/2022 - 04/2024")
st.write(
    """
- ► Built data models and maps to generate meaningful insights from customer data, boosting successful sales efforts by 12%
- ► Modeled targets likely to renew, and presented analysis to leadership, which led to a YoY revenue increase of $300K
- ► Compiled, studied, and inferred large amounts of data, modeling information to drive auto policy pricing
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Data Processor Internship Program | Dynata**")
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

# --- TESTIMONIALS ---
st.write('\n')
st.subheader("Testimonials")
st.write("---")

st.markdown(
    """
    <div class="testimonial-slider">
        <div class="testimonial-item">Milad is a highly skilled data analyst with a keen eye for detail.</div>
        <div class="testimonial-item">His ability to translate data into actionable insights is unparalleled.</div>
        <div class="testimonial-item">
            "Working with Milad on TICO Reporting has been a real pleasure. Milad's knack for understanding complex concepts and the meticulous attention to detail Milad brings to the table is truly impressive. I appreciate the dedication and hard work Milad has put into this. Looking forward to more collaborations in the near future!"
            <br><br>
            <div style="text-align: right;">Rayan Dutta, Specialist DevOps Engineer at SAP</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)