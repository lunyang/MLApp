'''
Description: 
Author: lunyang
Github: 
Date: 2022-02-02 15:03:13
LastEditors: lunyang
LastEditTime: 2022-02-02 17:22:06
'''
import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def app():
    local_css("style/style.css")
    # ---- LOAD ASSETS ----
    lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_zzytykf2.json")
    img_sphere = Image.open("images/sphere.jpg")
    img_phase_separation = Image.open("images/phase_separation.jpg")
    img_nano = Image.open("images/nano.jpg")


    # ---- HEADER SECTION ----
    with st.container():
        st.subheader("Hi, I am PolyAI :wave:")
        st.title("A Researcher from CAS")
        st.write(
            "I'm passionate on fusing polymer physics and artificial intelligence technology.."
        )
        st.write("[Learn More >](https://space.bilibili.com/76811961)")

    # ---- WHAT I DO ----
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("What I do")
            st.write("##")
            st.write(
                """
                On my Bilibili channel I am creating tutorials for people who:
                - are looking for a way to leverage the power of Blender in their scientific research.
                - are struggling with data visualization.
                - want to learn Data Analysis & Data Science about polymer science and chemistry.

                如果有用，请点个关注，O(∩_∩)O.
                """
            )
            st.write("[Bilibili Channel >](https://space.bilibili.com/76811961)")
        with right_column:
            st_lottie(lottie_coding, height=300, key="coding")

    # ---- Blender ----
    # Sphere
    with st.container():
        st.write("---")
        st.header("Blender tutorials")
        st.write("##")
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_sphere)
        with text_column:
            st.subheader("The explosion ball")
            st.write(
                """
                Learn how to model a explosion ball!
                In this tutorial, I'll show you exactly how to do it
                """
            )
            st.markdown("[Watch Video...](https://www.bilibili.com/video/BV1DK411H795)")
    
    # phase separation
    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_phase_separation)
        with text_column:
            st.subheader("Phase Separation")
            st.write(
                """
                Learn how to create a phase separation texture!
                In this tutorial, I'll show you exactly how to do it.
                """
            )
            st.markdown("[Watch Video...](https://www.bilibili.com/video/BV1TT4y1J72n)")
    
    # nano
    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_nano)
        with text_column:
            st.subheader("Nano Sphere")
            st.write(
                """
                Discover how to make a visually appealing Nano Sphere!
                In this tutorial, I'll show you exactly how to do it.
                """
            )
            st.markdown("[Watch Video...](https://www.bilibili.com/video/BV1yt4y1277N)")

    # ---- CONTACT ----
    with st.container():
        st.write("---")
        st.header("Get In Touch With Me!")
        st.write("##")

        # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
        contact_form = """
        <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()