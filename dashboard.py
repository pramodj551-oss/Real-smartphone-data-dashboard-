import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

st.set_page_config(page_title="📱 Smartphone Market Dashboard", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("smartphones.csv")
    df.columns = df.columns.str.strip()
    df["brand_name"] = df["brand_name"].str.title()
    df["os"] = df["os"].str.title()
    df["5G"] = df["5G_or_not"].map({1: "5G", 0: "Non-5G"})
    df["fast_charging_label"] = df["fast_charging_available"].map({1: "Yes", 0: "No"})
    df["price_segment"] = pd.cut(
        df["price"],
        bins=[0, 10000, 20000, 40000, 80000, df["price"].max() + 1],
        labels=["Budget (<10K)", "Mid-Low (10-20K)", "Mid (20-40K)", "Premium (40-80K)", "Ultra (80K+)"]
    )
    return df

df = load_data()

# ── Sidebar Filters ──────────────────────────────────────────────────────────
st.sidebar.title("🔍 Filters")

brands = sorted(df["brand_name"].unique())
selected_brands = st.sidebar.multiselect("Brand", brands, default=brands)

price_min, price_max = int(df["price"].min()), int(df["price"].max())
price_range = st.sidebar.slider("Price Range (₹)", price_min, price_max, (price_min, price_max), step=500)

os_opts = [x for x in sorted(df["os"].dropna().unique())]
selected_os = st.sidebar.multiselect("Operating System", os_opts, default=os_opts)

connectivity = st.sidebar.radio("Connectivity", ["All", "5G Only", "Non-5G Only"])

# Apply filters
fdf = df[
    df["brand_name"].isin(selected_brands) &
    df["price"].between(*price_range) &
    df["os"].isin(selected_os)
]
if connectivity == "5G Only":
    fdf = fdf[fdf["5G_or_not"] == 1]
elif connectivity == "Non-5G Only":
    fdf = fdf[fdf["5G_or_not"] == 0]

# ── Header ───────────────────────────────────────────────────────────────────
st.title("📱 Smartphone Market Dashboard")
st.caption(f"Showing **{len(fdf):,}** of {len(df):,} devices · Data filtered by sidebar controls")

# ── KPI Row ──────────────────────────────────────────────────────────────────
k1, k2, k3, k4, k5 = st.columns(5)
k1.metric("Total Models", f"{len(fdf):,}")
k2.metric("Brands", f"{fdf['brand_name'].nunique()}")
k3.metric("Avg Price (₹)", f"{fdf['price'].mean():,.0f}")
k4.metric("Avg Rating", f"{fdf['avg_rating'].mean():.2f} / 10" if fdf['avg_rating'].notna().any() else "N/A")
k5.metric("5G Models", f"{fdf['5G_or_not'].sum():,} ({fdf['5G_or_not'].mean()*100:.0f}%)")

st.divider()

# ── Row 1: Brand share + Price Distribution ───────────────────────────────────
c1, c2 = st.columns(2)

with c1:
    st.subheader("📊 Models by Brand")
    brand_counts = fdf["brand_name"].value_counts().reset_index()
    brand_counts.columns = ["Brand", "Count"]
    top_n = st.slider("Show top N brands", 5, len(brand_counts), min(15, len(brand_counts)), key="brand_slider")
    fig = px.bar(
        brand_counts.head(top_n), x="Count", y="Brand",
        orientation="h", color="Count",
        color_continuous_scale="Blues",
        template="plotly_white"
    )
    fig.update_layout(showlegend=False, coloraxis_showscale=False, height=400, margin=dict(l=0, r=0, t=10, b=0))
    fig.update_yaxes(categoryorder="total ascending")
    st.plotly_chart(fig, use_container_width=True)

with c2:
    st.subheader("💰 Price Distribution")
    fig = px.histogram(
        fdf, x="price", nbins=50,
        color_discrete_sequence=["#636EFA"],
        template="plotly_white",
        labels={"price": "Price (₹)"}
    )
    fig.update_layout(height=400, margin=dict(l=0, r=0, t=10, b=0), bargap=0.05)
    st.plotly_chart(fig, use_container_width=True)

# ── Row 2: Avg Price by Brand + Rating vs Price ───────────────────────────────
c3, c4 = st.columns(2)

with c3:
    st.subheader("🏷️ Median Price by Brand")
    median_price = (
        fdf.groupby("brand_name")["price"]
        .median().sort_values(ascending=False)
        .head(15).reset_index()
    )
    median_price.columns = ["Brand", "Median Price"]
    fig = px.bar(
        median_price, x="Brand", y="Median Price",
        color="Median Price", color_continuous_scale="Oranges",
        template="plotly_white",
        labels={"Median Price": "Median Price (₹)"}
    )
    fig.update_layout(showlegend=False, coloraxis_showscale=False, height=380,
                      margin=dict(l=0, r=0, t=10, b=0), xaxis_tickangle=-35)
    st.plotly_chart(fig, use_container_width=True)

with c4:
    st.subheader("⭐ Rating vs Price")
    scatter_df = fdf.dropna(subset=["avg_rating"])
    fig = px.scatter(
        scatter_df, x="price", y="avg_rating",
        color="brand_name", hover_name="model",
        hover_data={"price": ":,", "avg_rating": True},
        template="plotly_white",
        labels={"price": "Price (₹)", "avg_rating": "Avg Rating", "brand_name": "Brand"},
        opacity=0.7
    )
    fig.update_layout(height=380, margin=dict(l=0, r=0, t=10, b=0), legend=dict(font_size=10))
    st.plotly_chart(fig, use_container_width=True)

# ── Row 3: OS Share + 5G + Segment ───────────────────────────────────────────
c5, c6, c7 = st.columns(3)

with c5:
    st.subheader("🖥️ OS Share")
    os_counts = fdf["os"].value_counts().reset_index()
    os_counts.columns = ["OS", "Count"]
    fig = px.pie(os_counts, names="OS", values="Count",
                 hole=0.45, template="plotly_white",
                 color_discrete_sequence=px.colors.qualitative.Set2)
    fig.update_layout(height=320, margin=dict(l=0, r=0, t=10, b=0),
                      legend=dict(orientation="h", y=-0.1))
    st.plotly_chart(fig, use_container_width=True)

with c6:
    st.subheader("📶 5G Adoption")
    conn = fdf["5G"].value_counts().reset_index()
    conn.columns = ["Type", "Count"]
    fig = px.pie(conn, names="Type", values="Count",
                 hole=0.45, template="plotly_white",
                 color_discrete_map={"5G": "#00CC96", "Non-5G": "#EF553B"})
    fig.update_layout(height=320, margin=dict(l=0, r=0, t=10, b=0),
                      legend=dict(orientation="h", y=-0.1))
    st.plotly_chart(fig, use_container_width=True)

with c7:
    st.subheader("🎯 Price Segments")
    seg = fdf["price_segment"].value_counts().sort_index().reset_index()
    seg.columns = ["Segment", "Count"]
    fig = px.bar(seg, x="Segment", y="Count",
                 color="Count", color_continuous_scale="Purples",
                 template="plotly_white")
    fig.update_layout(showlegend=False, coloraxis_showscale=False, height=320,
                      margin=dict(l=0, r=0, t=10, b=0), xaxis_tickangle=-20)
    st.plotly_chart(fig, use_container_width=True)

# ── Row 4: RAM & Battery ──────────────────────────────────────────────────────
c8, c9 = st.columns(2)

with c8:
    st.subheader("🧠 RAM Distribution")
    ram_counts = fdf["ram_capacity"].value_counts().sort_index().reset_index()
    ram_counts.columns = ["RAM (GB)", "Count"]
    fig = px.bar(ram_counts, x="RAM (GB)", y="Count",
                 color="Count", color_continuous_scale="Teal",
                 template="plotly_white")
    fig.update_layout(showlegend=False, coloraxis_showscale=False, height=340,
                      margin=dict(l=0, r=0, t=10, b=0))
    st.plotly_chart(fig, use_container_width=True)

with c9:
    st.subheader("🔋 Battery Capacity vs Price")
    bat_df = fdf.dropna(subset=["battery_capacity"])
    fig = px.scatter(
        bat_df, x="battery_capacity", y="price",
        color="5G", size="ram_capacity",
        hover_name="model",
        template="plotly_white",
        labels={"battery_capacity": "Battery (mAh)", "price": "Price (₹)", "5G": "Connectivity"},
        color_discrete_map={"5G": "#00CC96", "Non-5G": "#EF553B"},
        opacity=0.65
    )
    fig.update_layout(height=340, margin=dict(l=0, r=0, t=10, b=0))
    st.plotly_chart(fig, use_container_width=True)

# ── Raw Data ──────────────────────────────────────────────────────────────────
with st.expander("🗃️ View Raw Data"):
    st.dataframe(
        fdf.drop(columns=["5G", "fast_charging_label", "price_segment"])
           .sort_values("price", ascending=False)
           .reset_index(drop=True),
        use_container_width=True,
        height=400
    )
    csv = fdf.to_csv(index=False).encode()
    st.download_button("⬇️ Download filtered CSV", csv, "smartphones_filtered.csv", "text/csv")
