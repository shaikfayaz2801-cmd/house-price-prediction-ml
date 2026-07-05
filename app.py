import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide"
)


df = pd.read_csv("house_price_dataset.csv")

X = df.drop("Price", axis=1)
y = df["Price"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)


if "page" not in st.session_state:
    st.session_state.page = "home"

if "price" not in st.session_state:
    st.session_state.price = None


if st.session_state.page == "home":

    st.markdown("""
    <div style="
    background:linear-gradient(135deg,#4F46E5,#06B6D4);
    padding:50px;
    border-radius:25px;
    text-align:center;
    color:white;
    margin-bottom:30px;
    ">
        <h1>🏠 Smart House Price Prediction</h1>
        <h3>AI Powered Real Estate Valuation</h3>
        <p>Predict house prices instantly using Machine Learning</p>
    </div>
    """, unsafe_allow_html=True)

    
    c1, c2, c3 = st.columns(3)

    with c1:
        st.success("🤖 AI Prediction")

    with c2:
        st.info("📈 Market Analysis")

    with c3:
        st.warning("💰 Price Estimation")

    st.markdown("---")

    st.subheader("📋 Property Information")

    left, right = st.columns(2)

    with left:

        area = st.number_input(
            "📐 Area (sqft)",
            min_value=0,
            max_value=10000,
            value=None,
            placeholder="Enter property area"
        )

        bathrooms = st.number_input(
            "🛁 Bathrooms",
            min_value=0,
            max_value=10,
            value=None,
            placeholder="Enter bathrooms"
        )

        house_age = st.number_input(
            "🏡 House Age",
            min_value=0,
            max_value=100,
            value=None,
            placeholder="Enter house age"
        )

        distance = st.number_input(
            "📍 Distance From City (km)",
            min_value=0.0,
            max_value=100.0,
            value=None,
            placeholder="Enter distance"
        )

    with right:

        bedrooms = st.number_input(
            "🛏 Bedrooms",
            min_value=0,
            max_value=10,
            value=None,
            placeholder="Enter bedrooms"
        )

        parking = st.number_input(
            "🚗 Parking Spaces",
            min_value=0,
            max_value=10,
            value=None,
            placeholder="Enter parking spaces"
        )

        location_rating = st.selectbox(
            "⭐ Location Rating",
            [
                "Select Rating",
                1,2,3,4,5,
                6,7,8,9,10
            ]
        )

    st.write("")

    if st.button(
        "💰 Predict House Price",
        use_container_width=True,
        type="primary"
    ):

        if (
            area is None or
            bedrooms is None or
            bathrooms is None or
            parking is None or
            house_age is None or
            distance is None or
            location_rating == "Select Rating"
        ):

            st.error(
                "⚠ Please fill all fields before prediction."
            )

        else:

            prediction = model.predict([[
                area,
                bedrooms,
                bathrooms,
                parking,
                house_age,
                location_rating,
                distance
            ]])

            st.session_state.price = prediction[0]
            st.session_state.page = "result"

            st.rerun()

elif st.session_state.page == "result":

    price = st.session_state.price

    st.balloons()

    st.markdown(f"""
    <div style="
    background:linear-gradient(135deg,#10B981,#059669);
    padding:50px;
    border-radius:25px;
    text-align:center;
    color:white;
    margin-top:40px;
    ">
        <h2>🏠 Estimated House Price</h2>
        <h1 style="font-size:60px;">
            ₹ {price:,.0f}
        </h1>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    if price > 15000000:
        st.success("🏆 Premium Property")

    elif price > 10000000:
        st.info("📈 Excellent Investment Opportunity")

    else:
        st.warning("💡 Budget Friendly Property")

    st.write("")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Property Grade", "A+")

    with c2:
        st.metric("Investment Score", "95%")

    with c3:
        st.metric("Market Trend", "📈 Rising")

    st.write("")

    if st.button(
        "Back",
        use_container_width=True
    ):
        st.session_state.page = "home"
        st.session_state.price = None
        st.rerun()

