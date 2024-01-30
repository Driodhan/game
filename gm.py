import streamlit as st

def main():
    st.title("Curriculum Vitae - Your Name")

    # Personal Information
    st.header("Personal Information")
    st.write("- **Name:** DRIODHAN")
    st.write("- **RollNo:** 20sw45")
    st.write("- **Dept:** Software")
    st.write("- **year:** Final Year")
   

    # Summary
    st.header("Summary")
    st.write(" i am driodhan rathore 20sw45 i am software Engineers wrok as a flutter developer ")

    # Education
    st.header("Education")
    st.subheader("B.E software Engineering ")
    st.write("QUEST Nawabshah, 2024 Year")

    # Work Experience
    st.header("Work Experience")
    st.subheader("Software Developer at Iskiller Company")
    st.write("- Worked on [image caption Generation]")
    st.write("- Collaborated with [QSES] to achieve [Mermber goals]")
   

    # Skills
    st.header("Skills")
    st.write("- Programming Languages: [Dart Language]")
    st.write("- Web Technologies: [Web Development]")
    st.write("- Database: [List databases]")
    st.write("- Version Control: [10.2]")
    st.write("- Problem Solving")
    st.write("- Team Collaboration")

    # Projects
    st.header("Projects 01 image caption generation")
    st.subheader("image caption generation ")
    st.write("- image caption generation by using CNN and RNN ")
    st.write("- Technologies used: [Deep Learning]")

    st.subheader(" Projects 01 portal job ")
    st.write("- i am create App that helpFull for job and  intership .")
    st.write("- Technologies used: [flutter and Dart language]")

    # Certifications
    st.header("Certifications")
    st.write("- National Vocational and Technical Training Commission (NAVTTC), 20223")

    # Awards and Achievements
    st.header("Awards and Achievements")
    st.write("- [selected in muet university award 2020]")

    # Languages
    st.header("Languages")
    st.write("- English: Fluent")
    st.write("- [Urdu]")
    st.write("- [Sindhi]")

    # Hobbies
    st.header("Hobbies")
    st.write("- web development ")

    # References
    st.header("References")
    st.write("Available upon request.")

if __name__ == '__main__':
    main()
