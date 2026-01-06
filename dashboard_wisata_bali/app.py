import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================
# PAGE CONFIG
# =====================================
st.set_page_config(
    page_title="Dashboard Wisata Bali",
    page_icon="🌴",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

/* =========================
   MODE ADAT BALI THEME
   ========================= */

/* Background Utama */
.main {
    background: linear-gradient(
        180deg,
        #fffaf0 0%,
        #fdf2d0 35%,
        #f6d365 70%,
        #d4af37 100%
    );
    background-attachment: fixed;
}

/* Container seperti ukiran kayu */
/* Paksa konten jadi FULL LEBAR */
/* Container seperti ukiran kayu – FULL WIDTH */
.block-container {
    max-width: 100% !important;
    padding: 2.5rem 4rem;
    background: rgba(255, 255, 255, 0.85);
    backdrop-filter: blur(12px);
    border-radius: 28px;
    box-shadow:
        0 12px 40px rgba(0,0,0,0.15),
        inset 0 0 0 3px rgba(212,175,55,0.3);
    border: 1px solid rgba(212,175,55,0.2);
}

/* Paksa layout Streamlit melebar */
section.main > div {
    max-width: 100% !important;
}


/* Sidebar – kain poleng */
[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #1c1c1c 0%,
        #2f2f2f 50%,
        #1c1c1c 100%
    );
    border-right: 3px solid #d4af37;
}

/* Sidebar text */
[data-testid="stSidebar"] * {
    color: #f6d365;
    font-weight: 500;
}

/* Metric Card – emas adat */
[data-testid="metric-container"] {
    background: linear-gradient(
        135deg,
        #ffd700 0%,
        #d4af37 50%,
        #b8962e 100%
    );
    color: #1c1c1c;
    padding: 28px;
    border-radius: 24px;
    box-shadow: 
        0 10px 35px rgba(212,175,55,0.4),
        inset 0 -2px 10px rgba(0,0,0,0.1),
        inset 0 2px 10px rgba(255,255,255,0.3);
    border: 3px solid rgba(255,215,0,0.6);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

[data-testid="metric-container"]::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: linear-gradient(
        45deg,
        transparent,
        rgba(255,255,255,0.3),
        transparent
    );
    transform: rotate(45deg);
    animation: shine 3s infinite;
}

@keyframes shine {
    0%, 100% { transform: translateX(-100%) rotate(45deg); }
    50% { transform: translateX(100%) rotate(45deg); }
}

[data-testid="metric-container"]:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 
        0 15px 45px rgba(212,175,55,0.5),
        inset 0 -2px 10px rgba(0,0,0,0.1);
}

/* Metric label & value */
[data-testid="metric-container"] label {
    color: #3b2f1b !important;
    font-weight: 700;
    font-size: 16px;
    text-shadow: 1px 1px 2px rgba(255,255,255,0.5);
}

[data-testid="metric-container"] [data-testid="stMetricValue"] {
    font-size: 38px;
    font-weight: 900;
    color: #1c1c1c;
    text-shadow: 2px 2px 4px rgba(255,255,255,0.3);
}

/* Judul Utama dengan Shadow */
h1 {
    color: #3b2f1b;
    font-weight: 900;
    letter-spacing: 2px;
    text-shadow: 
        3px 3px 6px rgba(212,175,55,0.3),
        -1px -1px 2px rgba(255,255,255,0.8);
    padding: 20px 0;
    border-bottom: 4px solid #d4af37;
    margin-bottom: 10px;
}

h2, h3 {
    color: #4b3621;
    font-weight: 700;
    text-shadow: 1px 1px 3px rgba(212,175,55,0.2);
    padding: 10px 0;
    border-left: 5px solid #d4af37;
    padding-left: 15px;
    margin: 15px 0;
}

/* Select & multiselect */
.stSelectbox > div > div,
.stMultiSelect > div > div {
    background: linear-gradient(
        135deg,
        #fffaf0 0%,
        #fff8e7 100%
    );
    border-radius: 16px;
    border: 3px solid #d4af37;
    box-shadow: 
        inset 0 2px 8px rgba(0,0,0,0.08),
        0 4px 15px rgba(212,175,55,0.2);
    font-weight: 600;
    transition: all 0.3s ease;
}

.stSelectbox > div > div:hover,
.stMultiSelect > div > div:hover {
    border-color: #ffd700;
    box-shadow: 
        inset 0 2px 8px rgba(0,0,0,0.08),
        0 6px 20px rgba(212,175,55,0.35);
    transform: translateY(-2px);
}

/* Info / insight box */
.stAlert {
    background: linear-gradient(
        135deg,
        rgba(255,250,240,0.98),
        rgba(253,242,208,0.98)
    );
    border-left: 8px solid #d4af37;
    border-radius: 20px;
    box-shadow: 
        0 8px 25px rgba(0,0,0,0.15),
        inset 0 0 0 2px rgba(212,175,55,0.2);
    padding: 20px;
    backdrop-filter: blur(10px);
    font-size: 16px;
    line-height: 1.8;
}

/* Expander */
.streamlit-expanderHeader {
    background: linear-gradient(
        135deg,
        rgba(255,250,240,0.95),
        rgba(253,242,208,0.95)
    );
    border-radius: 16px;
    font-weight: 700;
    border: 2px solid #d4af37;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
}

.streamlit-expanderHeader:hover {
    background: linear-gradient(
        135deg,
        rgba(212,175,55,0.2),
        rgba(255,250,240,0.95)
    );
    transform: translateX(5px);
}

/* Dataframe */
[data-testid="stDataFrame"] {
    background: rgba(255,255,255,0.98);
    border-radius: 16px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.12);
    border: 2px solid rgba(212,175,55,0.3);
    overflow: hidden;
}

/* Button */
.stButton > button {
    background: linear-gradient(
        135deg,
        #ffd700 0%,
        #d4af37 50%,
        #8c6d1f 100%
    );
    color: #1c1c1c;
    border-radius: 14px;
    border: none;
    font-weight: 700;
    font-size: 16px;
    padding: 12px 30px;
    box-shadow: 
        0 6px 20px rgba(212,175,55,0.4),
        inset 0 -2px 5px rgba(0,0,0,0.2);
    transition: all 0.3s ease;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 
        0 10px 30px rgba(212,175,55,0.5),
        inset 0 -2px 5px rgba(0,0,0,0.2);
    background: linear-gradient(
        135deg,
        #ffed4e 0%,
        #ffd700 50%,
        #d4af37 100%
    );
}

/* Horizontal Rule Styling */
hr {
    border: none;
    height: 3px;
    background: linear-gradient(
        90deg,
        transparent,
        #d4af37,
        transparent
    );
    margin: 30px 0;
    box-shadow: 0 2px 8px rgba(212,175,55,0.3);
}

/* Caption styling */
.stCaption {
    color: #6c5b3e;
    font-weight: 600;
    font-size: 15px;
    padding: 10px;
    background: rgba(212,175,55,0.1);
    border-radius: 10px;
    border-left: 4px solid #d4af37;
    margin: 10px 0;
}

/* Chart containers */
[data-testid="stPlotlyChart"] {
    background: rgba(255,255,255,0.9);
    border-radius: 20px;
    padding: 15px;
    box-shadow: 
        0 8px 25px rgba(0,0,0,0.12),
        inset 0 0 0 2px rgba(212,175,55,0.15);
    border: 1px solid rgba(212,175,55,0.3);
    transition: all 0.3s ease;
}

[data-testid="stPlotlyChart"]:hover {
    box-shadow: 
        0 12px 35px rgba(0,0,0,0.18),
        inset 0 0 0 2px rgba(212,175,55,0.25);
    transform: translateY(-3px);
}

/* Decorative corner elements */
.block-container::before {
    content: '🌺';
    position: absolute;
    top: 20px;
    left: 20px;
    font-size: 40px;
    opacity: 0.3;
    animation: float 3s ease-in-out infinite;
}

.block-container::after {
    content: '🌊';
    position: absolute;
    bottom: 20px;
    right: 20px;
    font-size: 40px;
    opacity: 0.3;
    animation: float 3s ease-in-out infinite reverse;
}

@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
}

/* Hide branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

</style>
""", unsafe_allow_html=True)


# =====================================
# DATA LOADING & PREPROCESSING
# =====================================
@st.cache_data
def load_and_process_data():
    """Load dan preprocessing data wisata Bali"""
    df = pd.read_csv("data/dataset_wisata_bali.csv")
    
    # Normalisasi nama kolom
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    
    # Handle missing values
    df['rating'] = df['rating'].fillna(df['rating'].mean())
    df = df.dropna(subset=['latitude', 'longitude'])
    
    return df

# Load data
df = load_and_process_data()

# =====================================
# HEADER SECTION
# =====================================
st.markdown(
    """
    <div style='text-align:center; padding: 20px 0;'>
        <h1 style='font-size: 52px; margin: 0;'>🌴 Dashboard Pariwisata Bali 🌊</h1>
        <p style='font-size: 22px; color:#6c5b3e; font-weight: 600; margin-top: 10px; 
                  text-shadow: 1px 1px 3px rgba(212,175,55,0.3);'>
            ✨ Eksplorasi Data Tempat Wisata di Pulau Dewata ✨
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# =====================================
# KPI METRICS
# =====================================
st.markdown("<h2 style='text-align:center; font-size: 28px;'>📈 Key Performance Indicators</h2>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="🏝️ Total Tempat Wisata",
        value=f"{df['nama'].nunique():,}"
    )

with col2:
    st.metric(
        label="⭐ Rata-rata Rating",
        value=f"{df['rating'].mean():.2f}"
    )

with col3:
    st.metric(
        label="📂 Jumlah Kategori",
        value=df['kategori'].nunique()
    )

# =====================================
# INSIGHT BOX
# =====================================
st.markdown("---")

st.info(
    f"""
    ### 📊 **Insight Dashboard Wisata Bali**
    
    • 🏖️ Dataset mencakup **{df['nama'].nunique():,} tempat wisata** unik di seluruh Bali  
    • ⭐ Rating rata-rata: **{df['rating'].mean():.2f}** dari 5.0  
    • 🗺️ Tersebar di **{df['kabupaten_kota'].nunique()} kabupaten/kota**  
    • 🏷️ Terdiri dari **{df['kategori'].nunique()} kategori wisata** yang berbeda  
    
    💡 ***Data telah melalui preprocessing dan handling missing value***
    """
)

# =====================================
# DATA PREVIEW (EXPANDABLE)
# =====================================
with st.expander("🔍 Preview Data Wisata"):
    st.dataframe(
        df.head(10),
        use_container_width=True,
        hide_index=True
    )

st.markdown("---")

# =====================================
# FILTER SECTION
# =====================================
st.markdown("<h2 style='font-size: 28px;'>🔎 Filter Data Wisata</h2>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

col_filter1, col_filter2 = st.columns(2)

with col_filter1:
    kabupaten = st.selectbox(
        "📍 Pilih Kabupaten/Kota",
        options=["Semua"] + sorted(df['kabupaten_kota'].unique()),
        help="Filter data berdasarkan kabupaten/kota"
    )

with col_filter2:
    kategori = st.multiselect(
        "🏷️ Pilih Kategori Wisata",
        options=sorted(df['kategori'].unique()),
        default=sorted(df['kategori'].unique()),
        help="Pilih satu atau lebih kategori wisata"
    )

# Apply filters
df_filtered = df.copy()

if kabupaten != "Semua":
    df_filtered = df_filtered[df_filtered['kabupaten_kota'] == kabupaten]

if kategori:
    df_filtered = df_filtered[df_filtered['kategori'].isin(kategori)]

# Show filter results
st.caption(f"📌 Menampilkan **{len(df_filtered):,}** dari **{len(df):,}** tempat wisata")

st.markdown("---")

# =====================================
# VISUALISASI CHART
# =====================================
st.markdown("<h2 style='font-size: 28px;'>📊 Analisis Data Wisata</h2>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

col_chart1, col_chart2 = st.columns(2)

# ----- Chart 1: Wisata per Kabupaten -----
with col_chart1:
    kab_df = (
        df_filtered.groupby('kabupaten_kota')
        .size()
        .reset_index(name='jumlah')
        .sort_values('jumlah', ascending=False)
    )
    
    fig_bar = px.bar(
        kab_df,
        x='kabupaten_kota',
        y='jumlah',
        title='📍 Jumlah Tempat Wisata per Kabupaten/Kota',
        labels={
            'kabupaten_kota': 'Kabupaten/Kota',
            'jumlah': 'Jumlah Tempat Wisata'
        },
        color='jumlah',
        color_continuous_scale='Teal',
        text='jumlah'
    )
    
    fig_bar.update_traces(textposition='outside', textfont_size=12)
    
    fig_bar.update_layout(
        plot_bgcolor='rgba(247,243,235,0.5)',
        paper_bgcolor='rgba(255,255,255,0)',
        showlegend=False,
        xaxis_tickangle=-45,
        height=450,
        title_font_size=16,
        title_font_color='#3b2f1b',
        font=dict(family="Arial, sans-serif", size=12, color="#4b3621")
    )
    
    st.plotly_chart(fig_bar, use_container_width=True)

# ----- Chart 2: Wisata per Kategori -----
with col_chart2:
    kategori_df = (
        df_filtered.groupby('kategori')
        .size()
        .reset_index(name='jumlah')
        .sort_values('jumlah', ascending=False)
    )
    
    fig_cat = px.bar(
        kategori_df,
        x='kategori',
        y='jumlah',
        title='🏷️ Jumlah Tempat Wisata per Kategori',
        labels={
            'kategori': 'Kategori Wisata',
            'jumlah': 'Jumlah Tempat Wisata'
        },
        color='jumlah',
        color_continuous_scale='Viridis',
        text='jumlah'
    )
    
    fig_cat.update_traces(textposition='outside', textfont_size=12)
    
    fig_cat.update_layout(
        plot_bgcolor='rgba(247,243,235,0.5)',
        paper_bgcolor='rgba(255,255,255,0)',
        showlegend=False,
        xaxis_tickangle=-45,
        height=450,
        title_font_size=16,
        title_font_color='#3b2f1b',
        font=dict(family="Arial, sans-serif", size=12, color="#4b3621")
    )
    
    st.plotly_chart(fig_cat, use_container_width=True)

st.markdown("---")

# =====================================
# PETA INTERAKTIF
# =====================================
st.markdown("<h2 style='font-size: 28px;'>🗺️ Peta Persebaran Wisata di Bali</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#6c5b3e; font-size: 16px;'>📍 Klik marker untuk melihat detail informasi wisata</p>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

if len(df_filtered) > 0:
    fig_map = px.scatter_mapbox(
        df_filtered,
        lat="latitude",
        lon="longitude",
        size="rating",
        color="kategori",
        hover_name="nama",
        hover_data={
            "kabupaten_kota": True,
            "rating": ":.2f",
            "latitude": False,
            "longitude": False
        },
        zoom=9,
        height=600,
        title=""
    )
    
    fig_map.update_layout(
        mapbox_style="open-street-map",
        paper_bgcolor='rgba(255,255,255,0)',
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        legend=dict(
            bgcolor="rgba(255,250,240,0.95)",
            bordercolor="#d4af37",
            borderwidth=2,
            font=dict(size=12, color="#3b2f1b")
        )
    )
    
    st.plotly_chart(fig_map, use_container_width=True)
else:
    st.warning("⚠️ Tidak ada data untuk ditampilkan. Silakan ubah filter.")

# =====================================
# FOOTER
# =====================================
st.markdown("---")

st.markdown(
    """
    <div style='text-align:center; padding: 30px; background: linear-gradient(135deg, rgba(212,175,55,0.1), rgba(255,250,240,0.3)); border-radius: 20px; margin-top: 20px;'>
        <p style='color:#3b2f1b; font-size:20px; font-weight: 700; margin: 10px 0;'>
            🌺 <strong>Dashboard Wisata Bali</strong> 🌺
        </p>
        <p style='color:#6c5b3e; font-size:16px; margin: 5px 0;'>
            Dibuat dengan ❤️ menggunakan Python • Streamlit • Plotly
        </p>
        <p style='color:#9ca3af; font-size:14px; margin-top: 15px; font-style: italic;'>
            © 2024 - Visualisasi Data Pariwisata Bali
        </p>
    </div>
    """,
    unsafe_allow_html=True
)