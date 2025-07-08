import streamlit as st

st.set_page_config(page_title="Portfolio",
                   layout="wide", page_icon=":rocket:")
st.title('Portofolio Streamlit')
#st.title("Portfolio Saya")
#st.header("Data Scientist & Developer")
st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman",
                       ["About Me", "Demo Data Science", 'Eksplor Data', "Kontak"])

if page == 'About Me':
    import aboutme
    aboutme.tentang_saya()
elif page == 'Eksplor Data':
    import eksplorasi
    eksplorasi.eksplorasi_data()
elif page == 'Demo Data Science':
    import demo
    demo.demo_DS()
elif page == 'Kontak':
    import kontak
    kontak.contact_person()
