import streamlit as st
import pandas as pd
import altair as alt

def eksplorasi_data():
    st.title("Explor Data Transactions")
    #st.markdown("Explore and filter the customer churn data interactively.")

    # --- Load Data ---
    df = pd.read_csv('Customer_Transaction_New.csv')

    # --- Filters ---
    with st.expander("🔎 Filter Data", expanded=True):
        col1, col2, col3  = st.columns(3)
        with col1:
            category = st.multiselect(
                "Category", 
                options=df['Category'].unique(), 
                default=list(df['Category'].unique())
            )
        with col2:
            gender = st.multiselect(
                "Gender",
                options=df['Gender'].unique(),
                default=list(df['Gender'].unique())
            )        
        with col3:
            age = st.slider(
                "Age", 
                int(df['Age'].min()), 
                int(df['Age'].max()), 
                (int(df['Age'].min()), int(df['Age'].max()))
            )
    df_transaction = df[
        (df['Category'].isin(category)) &
        ((df['Gender'].isin(gender))) &
        (df['Age'] >= age[0]) &
        (df['Age'] <= age[1])
    ]
    st.dataframe(df_transaction, use_container_width=True)

    # -- Visualizations ----
    st.subheader('Average Transaction Each Month')
    average_transaction = df_transaction.groupby("Month Name")["Transaction Amount"].mean().reset_index()
    # Urutan bulan sesuai kalender
    month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']

    # Mengatur kolom 'Month Name' sebagai kategori terurut
    average_transaction['Month Name'] = pd.Categorical(average_transaction['Month Name'],
                                                   categories=month_order,
                                                   ordered=True)
    average_transaction = average_transaction.sort_values('Month Name')

    # Gunakan Altair Chart
    line_chart = alt.Chart(average_transaction).mark_line(point=True).encode(
        x=alt.X('Month Name:N', sort=month_order, title='Month'),
        y=alt.Y('Transaction Amount:Q', title='Average Transaction'),
        tooltip=['Month Name', 'Transaction Amount']
    ).properties(
        width=900,
        height=500
    ).configure_axisX(
        labelAngle=0  # supaya axis-nya tidak miring
    )

    st.altair_chart(line_chart, use_container_width=True)

    st.subheader('Average Transaction Category with Gender')
    new_varians = pd.pivot_table(
    data = df_transaction ,
    index = ['Category','Gender'],
    values = 'Transaction Amount',
    aggfunc = 'mean'
    ).reset_index().sort_values(by ='Transaction Amount', ascending = False)

    # Bar chart dengan Altair
    bar_chart = alt.Chart(new_varians).mark_bar(size=20).encode(
        x=alt.X('Category:N', title='Category', axis=alt.Axis(labelAngle=0)),
        y=alt.Y('Transaction Amount:Q', title='Average Transaction'),
        color=alt.Color('Gender:N', title='Gender'),
        tooltip=['Category', 'Gender', 'Transaction Amount'],
        xOffset='Gender' # <<-- Ini yang bikin bar pria & wanita berdampingan
    ).properties(
        width=900,  # Perbesar width agar semua label muat
        height=400
    ).configure_scale(
        bandPaddingInner=0.5  # Tambah jarak antar kelompok bar
    )

    st.altair_chart(bar_chart, use_container_width=True)

    # --------- baris baru --------
    st.subheader('Count Buyer Each Month')
    buyer = df_transaction.groupby("Month Name")["Customer ID"].count().reset_index()

    # Mengatur kolom 'Month Name' sebagai kategori terurut
    buyer['Month Name'] = pd.Categorical(buyer['Month Name'],
                                        categories=month_order,
                                        ordered=True)

    # Mengurutkan dataframe berdasarkan urutan bulan
    buyer = buyer.sort_values('Month Name')

     # Gunakan Altair Chart
    line_chart_1 = alt.Chart(buyer).mark_line(point=True).encode(
        x=alt.X('Month Name:N', sort=month_order, title='Month'),
        y=alt.Y('Customer ID:Q', title='Customer ID'),
        tooltip=['Month Name', 'Customer ID']
    ).properties(
        width=900,
        height=500
    ).configure_axisX(
        labelAngle=0  # supaya axis-nya tidak miring
    )

    st.altair_chart(line_chart_1, use_container_width=True)
    


