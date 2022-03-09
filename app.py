
import streamlit as st 
import streamlit.components.v1 as stc 
from eda_app import run_eda
from ml_app import run_ml
from PIL import Image

html_temp = """
		<div style="background-color:#3872fb;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Black Friday Sales App</h1>
		<h4 style="color:white;text-align:center;">Happy Thanksgiving</h4>
		</div>
		"""

model= pickle.load(open('model.sav', 'rb'))
image = Image.open('Black-Friday-Sale.jpg')
streamlit.image(image,'')


def main():
	stc.html(html_temp)
	menu = ["EDA","ML","About"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "EDA":
		run_eda()
		pass
	elif choice == "ML":
		run_ml()
	else:
		st.subheader("About")
		st.info("Built with Streamlit")
		st.text("Source Code: Jesse E.Agbe(JCharis)")
		st.text("By Amirah Hanum")



if __name__ == '__main__':
	main()
	
# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style.css")

animation_symbol = "❄"

st.markdown(
    f"""
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    """,
    unsafe_allow_html=True,
)

