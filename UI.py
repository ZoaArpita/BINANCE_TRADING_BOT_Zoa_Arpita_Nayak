import streamlit as st
from bot.orders import  OrderManager

st.set_page_config(page_title="Binance Trading Bot", page_icon= "<UNK>", layout="centered")
st.title("Binance Trading Bot UI")
st.markdown("Place Testnet orders using the Python backened engine.")
form_triggerd = False

with st.form(key="my_order_form"):
    col1, col2 = st.columns(2)

    with col1:
        symbol = st.text_input("Symbol",value = "BTCUSDT").upper()
        side = st.selectbox("Side",["BUY","SELL"])
    with col2:
        order_type = st.selectbox("Order Type",["MARKET","LIMIT"])
        quantity = st.number_input("Quantity",min_value=0.001, value=0.01, step=0.01, format="%f")
    price = st.number_input("Price",min_value=0.0,value=0.0,step=100.0)

    submit_button = st.form_submit_button(label="Execute Trade")
    if submit_button:
        form_triggerd = True
    if form_triggerd:
        if order_type == "LIMIT" and price <=0:
            st.error("Error: A valid price is required for LIMIIT orders.")
        else:
            try:
                with st.spinner("Authenticating and sending order..."):
                    manager = OrderManager()
                    final_price = price if order_type == "LIMIT" else None

                    response = manager.place_order(
                        symbol=symbol,
                        side=side,
                        order_type=order_type,
                        quantity=quantity,
                        price= final_price
                )
                st.success("Order placed successfully!")

                st.write("Order details:")
                st.json({
                "Order ID": response.get("orderId"),
                "Status": response.get("status"),
                "Executed Qty": response.get("executedQty"),
                "Average Price": response.get("avgPrice")
                    })
            except Exception as e:
                st.error(f"Order failed: {e}")