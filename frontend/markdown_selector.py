from altair.vegalite.v4.schema.channels import Color
import streamlit as st
import numpy as np
import pandas as pd
import joblib
import os
import altair as alt


TABLE_NAMES = {
               "reference_PRE": "Product ID",
               "reference_name_PRE": "Product Name",
               "markdown_PRE": "Markdown",
               "predicted_sales": "Predicted Sales (Units)"
               }

COLUMNS_TO_DROP = ["season_PRE", "full_stock", "predicted_sales"]

def page_2():
    
    st.title("Markdown Selector")
    if "df" not in st.session_state:
        return True

    df_copy = st.session_state.df.copy()[list(TABLE_NAMES.keys())][0:0]
    my_table = st.dataframe(df_copy.rename(columns=TABLE_NAMES))

    product_selections = (st.session_state.df.reference_name_PRE  +\
                              " (" + st.session_state.df.reference_PRE + ")" ).tolist()
    
    if not "product_idx" in st.session_state:
        st.session_state.product_idx = 0


    st.session_state.product_selected = st.selectbox('Select a Product', product_selections, index=st.session_state.product_idx)
    st.session_state.product_idx = product_selections.index(st.session_state.product_selected)
    key_ref = st.session_state.df.reference_PRE.iloc[st.session_state.product_idx]
    current_markdown = st.session_state.df.markdown_PRE.iloc[st.session_state.product_idx]
    st.session_state.product_price = st.session_state.df[st.session_state.df.reference_PRE == key_ref]["price_PRE"].iloc[0]

    # Predict sales at each markdown level
    if "product_selected_2" not in st.session_state or st.session_state.product_selected_2 == st.session_state.product_selected:
        for md in range(0, 6):
            md /= 10
            df_tmp = st.session_state.df[st.session_state.df.reference_PRE == key_ref].copy()
            df_tmp.markdown_PRE = md
            columns_to_drop = COLUMNS_TO_DROP
            if "image_url" in df_tmp.columns:
                columns_to_drop = COLUMNS_TO_DROP + ["image_url"]
            pred = st.session_state.model.predict(df_tmp.drop(columns_to_drop, axis=1))
            if md == 0:
                st.session_state.plot = [(round(pred[0],0), md * 10)]
            else:
                st.session_state.plot.append((round(pred[0],0), md * 100))

    st.write("")

    results = pd.DataFrame(st.session_state.plot, columns=["sales", "markdown"])
    results["original_price"] = st.session_state.product_price
    results["discounted_price"] = (results.original_price * ((100. - results.markdown)/100.)).apply(lambda n: round(n,2))
    
    st.sidebar.image(st.session_state.images[key_ref], width=310)
    
    base_chart = alt.Chart(results,
                 title=f"{st.session_state.product_selected} Unit Sales Forecast"
                ).properties(width=700, height=400).mark_line(point=True, color="#ec3361").encode(
        alt.X("markdown:O", title='Markdown %',  sort=None),
        alt.Y("sales:Q", title="Predicted 2-Week Unit Sales"),
        alt.Text("sales:Q"),
        tooltip = [alt.Tooltip("sum(sales)", title="Predicted Unit Sales"),
                   alt.Tooltip("sum(discounted_price)", title="Discount Price"),
                   alt.Tooltip("sum(original_price)", title="Original Price")]
    )
    base_chart_text = base_chart.mark_text(dy=10, dx=5, color="#ec3361").encode(text="sales:Q")
    final_chart = alt.layer(base_chart, base_chart_text)
    st.altair_chart(final_chart)
    
    markdown = st.slider("Select markdown (%)", min_value=0, max_value=50, step=10, value=int(current_markdown * 100))
    sumbit_markdown = st.button("Sumbit markdown")
    if sumbit_markdown:
        st.session_state.df.markdown_PRE[st.session_state.df.reference_PRE == key_ref] = float(markdown) / 100.
        updated_prediction = results.sales[results.markdown == float(markdown)].iloc[0]
        st.session_state.df.predicted_sales[st.session_state.df.reference_PRE == key_ref] = updated_prediction
        my_table.add_rows(st.session_state.df[["reference_PRE","reference_name_PRE","markdown_PRE","predicted_sales"]].rename(columns=TABLE_NAMES))
    else:
        my_table.add_rows(st.session_state.df[["reference_PRE","reference_name_PRE","markdown_PRE","predicted_sales"]].rename(columns=TABLE_NAMES))

    sumbit_markdown = False
    
    st.session_state.product_selected_2 = st.session_state.product_selected

    # chart = (
    #     alt.Chart(
    #         data=results,
    #         title="Your title",
    #     )
    #     .mark_line()
    #     .encode(
    #         x=alt.X("Markdown %", axis=alt.Axis(title="Capacity 1")),
    #         y=alt.Y("Predicted 2-Week Unit Sales", axis=alt.Axis(title="Capacity 2")),
    #     )
    #       )

    # st.altair_chart(chart)



