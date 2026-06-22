# GÖK-SUSA: Autonomous Satellite-Driven Drought and Forest Health Early Warning System

GÖK-SUSA is an advanced, autonomous geographic information and decision-support system designed to monitor, analyze, and predict environmental degradation, climate change impacts, and water scarcity. Focused on the vital water reservoirs and surrounding forest ecosystems of Izmir, Turkey (specifically the Tahtalı Dam basin), this platform merges multi-spectral remote sensing data with real-time meteorological observations to build a machine-learning-powered environmental forecast.

---

## Core Architecture and Capabilities

The system functions as an automated production pipeline that ingests raw planetary data and converts it into actionable ecological indicators through three distinct frameworks:

### 1. Remote Sensing and Multi-Spectral Indices

By processing Sentinel-2 satellite data tracks, GÖK-SUSA computes highly precise matrix calculations across distinct light wavelengths:

* **Forest Degradation Analysis (NDVI):** Utilizing Near-Infrared (Band 8) and Visible Red (Band 4) frequencies, the system monitors photosynthetic activity to capture subtle shifts in canopy health.

* **Surface Water Hydrology (NDWI):** Utilizing Green (Band 3) and Near-Infrared (Band 8) frequencies to delineate water bodies and measure structural water stress within the dam site.

### 2. Meteorological Contextualization

The platform interfaces directly with localized weather sensors via the Meteostat engine, extracting relative humidity (rhum) and exact surface temperature grids (temp) to map environmental stress dynamics.

### 3. Predictive Machine Learning Engine

At its backend, a mathematical regression model maps the structural correlation between historic precipitation trends and active reservoir volume fluctuations. Built on top of scikit-learn, this predictive system runs linear extrapolation models to generate a 3-month rolling horizon forecast of water capacity risk levels.

---

## Software Stack and System Dependencies

The backend engine and frontend delivery dashboard are engineered completely using open-source Python frameworks:

| Component / Library | Functional Role within GÖK-SUSA |
| :--- | :--- |
| **Streamlit** | Core reactive UI engine, dashboard state management, and geospatial rendering. |
| **Rasterio** | Geospatial raster data ingestion, coordinate reference system (CRS) transformations, and GeoTIFF pixel matrix conversion. |
| **Scikit-Learn** | Predictive analytical layer running specialized LinearRegression pipelines for time-series forecasting. |
| **Seaborn & Matplotlib** | Generation of micro-pixel heatmaps mapping spatial vegetation loss, and multi-axis temporal trend lines. |
| **Plotly Graph Objects** | Dynamic gauge visualization rendering real-time capacity and stress margins. |
| **Pandas** | High-performance data-frame manipulation for tracking and filtering incoming meteorological arrays. |

---

## Operational Panel Breakdown

When executed, the analytical instrument segregates tasks into localized screen modules:

### The Command Center (Sidebar)

* **Status Tracking:** Features a dynamic progress indicator reflecting runtime stability and pipeline operational readiness.

* **Geospatial Coordinates:** Dynamic decimal inputs (Latitude and Longitude) targeting specific measurement zones within the Izmir ecosystem.

* **Temporal Anchors:** Target date inputs driving historical dataset alignments.

### Primary Analytical Canvas

* **Real-Time Statistical Cards:** Instantly delivers comparative metrics showcasing January vs. July reservoir volumes, annual localized temperature deviations, and mean canopy health indices.

* **Geospatial Mapping Matrix:** Generates an interactive geographic visualizer centered natively over the exact coordinates of the dam infrastructure.

* **Dual Multi-Spectral Heatmaps:** Renders side-by-side comparative matrices plotting vegetation loss grids (gist_earth_r) alongside immediate surface water changes.

* **Temporal Trend Alignment:** A multi-variable chart tracking the cross-sectional correlation between historical forest health indexes and hydrological depletion timelines across a 12-month sequence.

* **AI Early Warning Banner:** An automated, high-visibility classification alert detailing the projected dam capacity percentage if climatic boundaries persist unaltered over the subsequent quarter.

---

## How to Run the System Locally

To initiate the pipeline and host the visualization dashboard on your local machine, follow the environment configuration steps outlined below:

1. Clone this repository to your local system.

2. Ensure you have your localized dataset directories structured as uydu_goruntuleri/ (containing your multi-spectral GeoTIFF files) and veriler/ (containing localized climate CSV files).

3. Open your system terminal within the root project directory.

4. Execute the application layer by running the following command:
```bash
   streamlit run app.py
