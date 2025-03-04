import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time
from streamlit_lottie import st_lottie
import requests
import json
from streamlit_option_menu import option_menu
import altair as alt
import matplotlib.pyplot as plt
import streamlit_nested_layout

# Set page configuration
st.set_page_config(
    page_title="Animated Interactive Dashboard",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for animations and styling
st.markdown("""
<style>
    /* Animations for elements */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    
    @keyframes slideInLeft {
        from { transform: translateX(-30px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes slideInRight {
        from { transform: translateX(30px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes slideInUp {
        from { transform: translateY(30px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
    
    /* Apply animations to different elements */
    .css-1d391kg, .css-12oz5g7 {
        animation: fadeIn 1.2s ease-out;
    }
    
    .row-widget {
        animation: slideInUp 0.8s ease-out;
    }
    
    .stButton {
        animation: slideInLeft 0.6s ease-out;
    }
    
    .stRadio {
        animation: slideInRight 0.7s ease-out;
    }
    
    /* Custom card styling */
    .custom-card {
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .custom-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.12);
    }
    
    /* For light/dark theme */
    .light-theme {
        background-color: #ffffff;
        color: #333333;
    }
    
    .dark-theme {
        background-color: #1e1e1e;
        color: #f0f0f0;
    }
    
    /* Animation for page transitions */
    .page-transition {
        animation: fadeIn 0.8s ease-out;
    }
    
    /* Customize scrollbar */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #888;
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #555;
    }
</style>
""", unsafe_allow_html=True)

# Enhanced function to load Lottie animation from URL with fallback
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
        else:
            # Return a simple fallback animation if URL fails
            return {
                "v": "5.5.7",
                "fr": 30,
                "ip": 0,
                "op": 60,
                "w": 400,
                "h": 300,
                "nm": "Fallback Animation",
                "ddd": 0,
                "assets": [],
                "layers": [{
                    "ddd": 0,
                    "ind": 1,
                    "ty": 4,
                    "nm": "Circle",
                    "sr": 1,
                    "ks": {
                        "o": {"a": 0, "k": 100},
                        "r": {"a": 0, "k": 0},
                        "p": {"a": 0, "k": [200, 150, 0]},
                        "a": {"a": 0, "k": [0, 0, 0]},
                        "s": {
                            "a": 1,
                            "k": [
                                {"t": 0, "s": [100, 100, 100]},
                                {"t": 30, "s": [150, 150, 100]},
                                {"t": 60, "s": [100, 100, 100]}
                            ]
                        }
                    },
                    "shapes": [{
                        "ty": "el",
                        "p": {"a": 0, "k": [0, 0]},
                        "s": {"a": 0, "k": [50, 50]},
                        "d": 1,
                        "nm": "Ellipse Path 1",
                    }, {
                        "ty": "fl",
                        "c": {"a": 0, "k": [0.2, 0.5, 0.8, 1]},
                        "o": {"a": 0, "k": 100},
                        "r": 1,
                        "nm": "Fill 1",
                    }]
                }]
            }
    except:
        # Return a minimal fallback animation if the request fails completely
        return {
            "v": "5.5.7",
            "fr": 30,
            "ip": 0,
            "op": 60,
            "w": 100,
            "h": 100,
            "nm": "Minimal Fallback",
            "ddd": 0,
            "assets": [],
            "layers": [{
                "ddd": 0,
                "ind": 1,
                "ty": 4,
                "nm": "Square",
                "sr": 1,
                "ks": {
                    "o": {"a": 0, "k": 100},
                    "r": {"a": 1, "k": [{"t": 0, "s": [0]}, {"t": 60, "s": [360]}]},
                    "p": {"a": 0, "k": [50, 50, 0]},
                    "a": {"a": 0, "k": [0, 0, 0]},
                    "s": {"a": 0, "k": [100, 100, 100]}
                },
                "shapes": [{
                    "ty": "rc",
                    "d": 1,
                    "s": {"a": 0, "k": [20, 20]},
                    "p": {"a": 0, "k": [0, 0]},
                    "r": {"a": 0, "k": 0},
                    "nm": "Rectangle Path 1",
                }, {
                    "ty": "fl",
                    "c": {"a": 0, "k": [0.8, 0.2, 0.5, 1]},
                    "o": {"a": 0, "k": 100},
                    "r": 1,
                    "nm": "Fill 1",
                }]
            }]
        }

# Function to create animated progress bar
def animated_progress():
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for i in range(101):
        progress_bar.progress(i)
        status_text.text(f"Progress: {i}%")
        time.sleep(0.01)
    
    status_text.text("Complete!")
    time.sleep(1)
    status_text.empty()
    progress_bar.empty()

# Theme state management
if 'theme' not in st.session_state:
    st.session_state.theme = "light"

# Function to toggle theme
def toggle_theme():
    st.session_state.theme = "dark" if st.session_state.theme == "light" else "light"

# Sample data generation
@st.cache_data
def generate_data():
    dates = pd.date_range(start='2023-01-01', periods=100, freq='D')
    data = pd.DataFrame({
        'date': dates,
        'sales': np.random.normal(loc=100, scale=15, size=100).cumsum(),
        'customers': np.random.normal(loc=50, scale=10, size=100).cumsum(),
        'category': np.random.choice(['A', 'B', 'C', 'D'], size=100),
        'region': np.random.choice(['North', 'South', 'East', 'West'], size=100)
    })
    return data

data = generate_data()

# Lottie animations - using reliable URLs that work
lottie_data = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_UJNc2t.json")
lottie_chart = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_zzm4z9av.json")
lottie_dashboard = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_qgah66oi.json")

# Alternative option for loading local files if needed
"""
def load_lottie_file(filepath):
    with open(filepath, "r") as f:
        return json.load(f)

# Use these as alternatives if the URLs don't work
# lottie_data = load_lottie_file("path/to/your/animation1.json")
# lottie_chart = load_lottie_file("path/to/your/animation2.json")
# lottie_dashboard = load_lottie_file("path/to/your/animation3.json")
"""

# Apply theme styles
theme_bg_color = "#ffffff" if st.session_state.theme == "light" else "#1e1e1e"
theme_text_color = "#333333" if st.session_state.theme == "light" else "#f0f0f0"
theme_class = "light-theme" if st.session_state.theme == "light" else "dark-theme"

st.markdown(f"""
<div class="{theme_class}" style="padding: 10px; border-radius: 10px;">
    <h1 style="text-align: center; color: {"#0066cc" if st.session_state.theme == "light" else "#4da6ff"};">
        Interactive Animated Dashboard
    </h1>
</div>
""", unsafe_allow_html=True)

# Sidebar with animations
with st.sidebar:
    # Use try/except to handle any issues with Lottie animations
    try:
        st_lottie(lottie_dashboard, height=200, key="dashboard_animation")
    except Exception as e:
        st.warning("Could not load animation. Using fallback.")
        st.image("https://via.placeholder.com/200x100?text=Dashboard", use_column_width=True)
    
    st.markdown(f"""
    <div class="{theme_class} custom-card">
        <h3 style="color: {"#0066cc" if st.session_state.theme == "light" else "#4da6ff"};">
            Dashboard Settings
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Theme toggle
    theme_col1, theme_col2 = st.columns([3, 1])
    with theme_col1:
        st.write(f"Current theme: {st.session_state.theme.capitalize()}")
    with theme_col2:
        st.button("🔄 Toggle", on_click=toggle_theme)
    
    # Navigation menu with animation
    selected = option_menu(
        menu_title="Navigation",
        options=["Home", "Data Explorer", "Visualizations", "About"],
        icons=["house", "database", "graph-up", "info-circle"],
        menu_icon="cast",
        default_index=0,
        orientation="vertical",
        styles={
            "container": {"padding": "5px", "background-color": theme_bg_color},
            "icon": {"color": "orange", "font-size": "25px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee" if st.session_state.theme == "light" else "#333"},
            "nav-link-selected": {"background-color": "#ffa64d"},
        }
    )

# Main content based on navigation
if selected == "Home":
    st.markdown(f"""
    <div class="page-transition {theme_class} custom-card">
        <h2 style="color: {"#0066cc" if st.session_state.theme == "light" else "#4da6ff"};">
            Welcome to the Interactive Dashboard
        </h2>
        <p>This dashboard demonstrates various animations and interactive elements in Streamlit.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Display Lottie animation
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class="{theme_class} custom-card">
            <h3 style="color: {"#0066cc" if st.session_state.theme == "light" else "#4da6ff"};">
                Features
            </h3>
            <ul>
                <li>Animated page transitions and elements</li>
                <li>Light and dark theme switching</li>
                <li>Interactive data visualizations</li>
                <li>Scroll animations and hover effects</li>
                <li>Responsive layout design</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Show Animation Demo"):
            animated_progress()
    
    with col2:
        try:
            st_lottie(lottie_data, height=300, key="hello")
        except Exception as e:
            st.warning("Could not load animation. Using fallback.")
            st.image("https://via.placeholder.com/300x200?text=Animation", use_column_width=True)
    
    # Quick stats with animation
    st.markdown(f"""
    <div class="page-transition {theme_class} custom-card">
        <h3 style="color: {"#0066cc" if st.session_state.theme == "light" else "#4da6ff"};">
            Dashboard Overview
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="{theme_class} custom-card" style="text-align: center;">
            <h2 style="color: #ff6b6b;">$ {data['sales'].iloc[-1]:,.2f}</h2>
            <p>Total Sales</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="{theme_class} custom-card" style="text-align: center;">
            <h2 style="color: #4ecdc4;">{data['customers'].iloc[-1]:,.0f}</h2>
            <p>Total Customers</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="{theme_class} custom-card" style="text-align: center;">
            <h2 style="color: #ffe66d;">{len(data['region'].unique())}</h2>
            <p>Regions</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="{theme_class} custom-card" style="text-align: center;">
            <h2 style="color: #6a0572;">{len(data['category'].unique())}</h2>
            <p>Categories</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Sample chart
    st.markdown(f"""
    <div class="page-transition {theme_class} custom-card">
        <h3 style="color: {"#0066cc" if st.session_state.theme == "light" else "#4da6ff"};">
            Sales Trend
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    fig = px.line(
        data, 
        x='date', 
        y='sales',
        title=None,
        template='plotly_white' if st.session_state.theme == "light" else 'plotly_dark'
    )
    
    fig.update_layout(
        height=400,
        margin=dict(l=20, r=20, t=30, b=20),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis_title="Date",
        yaxis_title="Sales",
    )
    
    st.plotly_chart(fig, use_container_width=True)

elif selected == "Data Explorer":
    st.markdown(f"""
    <div class="page-transition {theme_class} custom-card">
        <h2 style="color: {"#0066cc" if st.session_state.theme == "light" else "#4da6ff"};">
            Data Explorer
        </h2>
        <p>Explore and filter the dataset with interactive controls</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col2:
        try:
            st_lottie(lottie_chart, height=200, key="chart_animation")
        except Exception as e:
            st.warning("Could not load animation. Using fallback.")
            st.image("https://via.placeholder.com/200x150?text=Chart", use_column_width=True)
        
        st.markdown(f"""
        <div class="{theme_class} custom-card">
            <h3 style="color: {"#0066cc" if st.session_state.theme == "light" else "#4da6ff"};">
                Data Filters
            </h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Filters
        date_range = st.date_input(
            "Select Date Range",
            [data['date'].min().date(), data['date'].max().date()]
        )
        
        selected_regions = st.multiselect(
            "Select Regions",
            data['region'].unique(),
            default=data['region'].unique()
        )
        
        selected_categories = st.multiselect(
            "Select Categories",
            data['category'].unique(),
            default=data['category'].unique()
        )
    
    with col1:
        # Filter data
        filtered_data = data[
            (data['date'].dt.date >= date_range[0]) &
            (data['date'].dt.date <= date_range[1]) &
            (data['region'].isin(selected_regions)) &
            (data['category'].isin(selected_categories))
        ]
        
        # Display filtered data
        st.markdown(f"""
        <div class="{theme_class} custom-card">
            <h3 style="color: {"#0066cc" if st.session_state.theme == "light" else "#4da6ff"};">
                Filtered Data
            </h3>
        </div>
        """, unsafe_allow_html=True)
        
        st.dataframe(
            filtered_data,
            use_container_width=True,
            height=400
        )
        
        # Download button with animation
        csv = filtered_data.to_csv(index=False)
        st.download_button(
            label="📥 Download Filtered Data",
            data=csv,
            file_name="filtered_data.csv",
            mime="text/csv",
        )

elif selected == "Visualizations":
    st.markdown(f"""
    <div class="page-transition {theme_class} custom-card">
        <h2 style="color: {"#0066cc" if st.session_state.theme == "light" else "#4da6ff"};">
            Interactive Visualizations
        </h2>
        <p>Explore the data through various chart types and visualizations</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Visualization selector with animation
    viz_type = st.selectbox(
        "Select Visualization Type",
        ["Line Chart", "Bar Chart", "Scatter Plot", "Pie Chart", "Heatmap"]
    )
    
    col1, col2 = st.columns([3, 1])
    
    with col2:
        st.markdown(f"""
        <div class="{theme_class} custom-card">
            <h3 style="color: {"#0066cc" if st.session_state.theme == "light" else "#4da6ff"};">
                Chart Settings
            </h3>
        </div>
        """, unsafe_allow_html=True)
        
        if viz_type != "Pie Chart" and viz_type != "Heatmap":
            x_axis = st.selectbox("X-axis", ["date", "region", "category"])
            y_axis = st.selectbox("Y-axis", ["sales", "customers"], index=0)
            color_by = st.selectbox("Color by", ["None", "region", "category"], index=0)
        
        if viz_type == "Pie Chart":
            pie_metric = st.selectbox("Metric", ["sales", "customers"], index=0)
            group_by = st.selectbox("Group by", ["region", "category"], index=0)
        
        if viz_type == "Heatmap":
            heatmap_x = st.selectbox("X-axis", ["region", "category"], index=0)
            heatmap_y = st.selectbox("Y-axis", ["category", "region"], index=1)
            agg_func = st.selectbox("Aggregate function", ["mean", "sum", "count"], index=1)
            heatmap_value = st.selectbox("Value", ["sales", "customers"], index=0)
    
    with col1:
        st.markdown(f"""
        <div class="{theme_class} custom-card">
            <h3 style="color: {"#0066cc" if st.session_state.theme == "light" else "#4da6ff"};">
                {viz_type}
            </h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Create visualization based on selection
        if viz_type == "Line Chart":
            color_param = None if color_by == "None" else color_by
            fig = px.line(
                data, 
                x=x_axis, 
                y=y_axis,
                color=color_param,
                template='plotly_white' if st.session_state.theme == "light" else 'plotly_dark'
            )
            st.plotly_chart(fig, use_container_width=True)
            
        elif viz_type == "Bar Chart":
            color_param = None if color_by == "None" else color_by
            fig = px.bar(
                data, 
                x=x_axis, 
                y=y_axis,
                color=color_param,
                template='plotly_white' if st.session_state.theme == "light" else 'plotly_dark'
            )
            st.plotly_chart(fig, use_container_width=True)
            
        elif viz_type == "Scatter Plot":
            color_param = None if color_by == "None" else color_by
            fig = px.scatter(
                data, 
                x=x_axis, 
                y=y_axis,
                color=color_param,
                size_max=15,
                opacity=0.7,
                template='plotly_white' if st.session_state.theme == "light" else 'plotly_dark'
            )
            st.plotly_chart(fig, use_container_width=True)
            
        elif viz_type == "Pie Chart":
            grouped_data = data.groupby(group_by)[pie_metric].sum().reset_index()
            fig = px.pie(
                grouped_data, 
                values=pie_metric, 
                names=group_by,
                hole=0.4,
                template='plotly_white' if st.session_state.theme == "light" else 'plotly_dark'
            )
            st.plotly_chart(fig, use_container_width=True)
            
        elif viz_type == "Heatmap":
            pivot_data = pd.pivot_table(
                data, 
                values=heatmap_value, 
                index=heatmap_y, 
                columns=heatmap_x,
                aggfunc=agg_func
            )
            
            fig = px.imshow(
                pivot_data,
                text_auto=True,
                aspect="auto",
                color_continuous_scale='Blues' if st.session_state.theme == "light" else 'Viridis',
                template='plotly_white' if st.session_state.theme == "light" else 'plotly_dark'
            )
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)
    
    # Additional interactive elements
    st.markdown(f"""
    <div class="{theme_class} custom-card">
        <h3 style="color: {"#0066cc" if st.session_state.theme == "light" else "#4da6ff"};">
            Sales Distribution
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig = px.histogram(
            data, 
            x='sales',
            nbins=20,
            opacity=0.7,
            template='plotly_white' if st.session_state.theme == "light" else 'plotly_dark'
        )
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fig = px.box(
            data, 
            x='region', 
            y='sales',
            color='region',
            template='plotly_white' if st.session_state.theme == "light" else 'plotly_dark'
        )
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)

elif selected == "About":
    st.markdown(f"""
    <div class="page-transition {theme_class} custom-card">
        <h2 style="color: {"#0066cc" if st.session_state.theme == "light" else "#4da6ff"};">
            About This Dashboard
        </h2>
        <p>This interactive dashboard demonstrates various animations and UI features in Streamlit.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"""
        <div class="{theme_class} custom-card">
            <h3 style="color: {"#0066cc" if st.session_state.theme == "light" else "#4da6ff"};">
                Features Demonstrated
            </h3>
            <ul>
                <li><strong>Theme Switching:</strong> Toggle between light and dark modes</li>
                <li><strong>Page Transitions:</strong> Smooth animations between pages</li>
                <li><strong>Interactive Elements:</strong> Animated buttons, cards, and controls</li>
                <li><strong>Responsive Layout:</strong> Adapts to different screen sizes</li>
                <li><strong>Data Visualization:</strong> Multiple chart types with interactive controls</li>
                <li><strong>Custom Styling:</strong> CSS animations and hover effects</li>
                <li><strong>Lottie Animations:</strong> Engaging vector animations</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="{theme_class} custom-card">
            <h3 style="color: {"#0066cc" if st.session_state.theme == "light" else "#4da6ff"};">
                How to Use
            </h3>
            <p>Navigate through the dashboard using the sidebar menu. Each section demonstrates different interactive features:</p>
            <ul>
                <li><strong>Home:</strong> Overview and key metrics</li>
                <li><strong>Data Explorer:</strong> Filter and examine the dataset</li>
                <li><strong>Visualizations:</strong> Interactive charts and graphs</li>
                <li><strong>About:</strong> Information about the dashboard</li>
            </ul>
            <p>Toggle between light and dark themes using the button in the sidebar.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        try:
            st_lottie(lottie_data, height=200, key="about_animation")
        except Exception as e:
            st.warning("Could not load animation. Using fallback.")
            st.image("https://via.placeholder.com/200x150?text=Animation", use_column_width=True)
        
        st.markdown(f"""
        <div class="{theme_class} custom-card">
            <h3 style="color: {"#0066cc" if st.session_state.theme == "light" else "#4da6ff"};">
                Libraries Used
            </h3>
            <ul>
                <li>Streamlit</li>
                <li>Pandas & NumPy</li>
                <li>Plotly Express</li>
                <li>Streamlit Lottie</li>
                <li>Streamlit Option Menu</li>
                <li>Custom CSS</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="{theme_class} custom-card">
            <h3 style="color: {"#0066cc" if st.session_state.theme == "light" else "#4da6ff"};">
                Try It Out!
            </h3>
            <p>Click the button below to see a random animation effect:</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🎬 Show Random Animation"):
            animated_progress()

# Add scrolling animation script
