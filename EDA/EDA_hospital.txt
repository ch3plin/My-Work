# 🏨 Hospitality Domain — Exploratory Data Analysis

A data analysis project exploring hotel booking patterns, occupancy rates, and revenue trends across multiple cities and room categories.

## 📁 Dataset

The project uses five CSV files:

| File | Description |
|------|-------------|
| `fact_bookings.csv` | Individual booking records (guests, revenue, platform, room) |
| `fact_aggregated_bookings.csv` | Aggregated bookings with capacity per property and room |
| `dim_date.csv` | Date dimension with day type (weekday/weekend) |
| `dim_hotels.csv` | Hotel metadata (property ID, city, category) |
| `dim_rooms.csv` | Room type mapping (room ID to room class) |
| `new_data_august.csv` | Incremental August data for updated analysis |

## 🔍 Analysis Performed

### Data Cleaning
- Removed bookings with zero or negative guest counts
- Filtered revenue outliers using the **3-sigma rule** (mean ± 3×std)
- Imputed missing capacity values with **median**
- Removed anomalous rows where `successful_bookings > capacity`

### Feature Engineering
- Computed **occupancy percentage** per property and room:  
  `oc_per = (successful_bookings / capacity) × 100`

### Exploratory Analysis
- Booking platform distribution (bar chart)
- Occupancy % by **room class** (Standard, Elite, Premium, Presidential)
- Occupancy % by **city**
- Occupancy % by **day type** (weekday vs. weekend)
- City-wise occupancy for **June 2022**
- City-wise **revenue realized** (sorted descending)

### Data Integration
- Merged all dimension tables with fact tables on `property_id`, `room_category`, and `check_in_date`
- Appended August 2022 data to extend the time range

## 🛠️ Tech Stack

- **Python 3**
- **pandas** — data manipulation and merging
- **matplotlib** (via pandas `.plot()`) — visualizations

## 🚀 Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/hospitality-eda.git
   cd hospitality-eda
   ```

2. Install dependencies:
   ```bash
   pip install pandas matplotlib
   ```

3. Place the dataset CSVs in a `datasets/` folder at the project root.

4. Update the file paths in the notebook to point to your local `datasets/` directory.

5. Open and run the notebook:
   ```bash
   jupyter notebook EDA.ipynb
   ```

## 📊 Key Insights

- Occupancy rates vary significantly across room classes and cities.
- Weekend vs. weekday occupancy shows differing demand patterns.
- Revenue concentration differs from occupancy concentration by city — high occupancy does not always mean highest revenue.

## 📂 Project Structure

```
hospitality-eda/
├── datasets/
│   ├── fact_bookings.csv
│   ├── fact_aggregated_bookings.csv
│   ├── dim_date.csv
│   ├── dim_hotels.csv
│   ├── dim_rooms.csv
│   └── new_data_august.csv
├── EDA.ipynb
└── README.md
```