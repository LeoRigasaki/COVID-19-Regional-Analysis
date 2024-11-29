# COVID-19 Regional Analysis: South Asia vs Middle East

## 📖 Overview
This project examines the impact of COVID-19 across South Asia and the Middle East. The analysis focuses on:
- **COVID-19 Trends**: Total cases, positivity rates, and ICU patient trends.
- **Vaccination Progress**: How GDP and population density relate to vaccination rates.
- **Statistical Testing**: Hypothesis testing (t-test) to compare vaccination progress across regions.
- **Predictive Modeling**: Linear regression to identify key predictors of total cases.

The project uses interactive and static visualizations, along with Python-based data analysis techniques.

---

## ✨ Key Features
- 📈 **Time-Series Trends**: Interactive visualizations for total cases, vaccination progress, and positivity rates.
- 📊 **Correlation Analysis**: Explore relationships between GDP, vaccination progress, and population density.
- 📉 **Predictive Modeling**: Use linear regression to predict total cases based on demographic and health-related factors.
- 🔬 **Hypothesis Testing**: Perform a t-test to compare vaccination progress between South Asia and the Middle East.
- 📂 **Interactive Visualizations**: Dropdown selectors for country-specific analysis.

---

## 📊 Dataset
- **Source**: [Our World in Data](https://ourworldindata.org/coronavirus)
- **File**: `data/owid-covid-data.csv`
- **Description**: Contains global COVID-19 statistics, including:
  - Total cases and deaths
  - Vaccination data
  - GDP per capita
  - Population density

---

## 🛠️ How to Set Up and Run

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/COVID-19-Regional-Analysis.git
cd COVID-19-Regional-Analysis
```

### 2️⃣ Set Up a Virtual Environment
It’s recommended to use a virtual environment for dependency isolation:
```bash
python -m venv venv
```

Activate the virtual environment:
- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Jupyter Notebook
Navigate to the `notebook` directory and start the Jupyter Notebook:
```bash
cd notebook
jupyter notebook
```

Open `covid-analysis.ipynb` in your browser.

### 5️⃣ Deactivate the Virtual Environment (Optional)
After finishing your work:
```bash
deactivate
```

---

## 📂 Project Structure
```
COVID-19-Regional-Analysis/
├── data/                    # Dataset directory
│   └── owid-covid-data.csv  # Source data file
├── notebook/                # Jupyter notebooks for analysis
│   └── covid-analysis.ipynb # Main notebook
├── requirements.txt         # Required dependencies
└── README.md                # Project documentation
```

---

## 📈 Example Visualizations
### Total Cases Trend (Interactive)
![Total Cases Trend](https://user-images.githubusercontent.com/example.png)

### Vaccination Progress
![Vaccination Progress](https://user-images.githubusercontent.com/example2.png)

### GDP Per Capita vs Total Cases
![GDP Scatter](https://user-images.githubusercontent.com/example3.png)

---

## ⚡ Results and Insights
1. **Vaccination Progress**:
   - Middle Eastern countries show stronger correlation with GDP compared to South Asia.
   - South Asia demonstrates lower vaccination progress due to socio-economic constraints.

2. **Positivity Rates**:
   - South Asia shows spikes in positivity rates due to late detection and testing issues.
   - Middle East maintains a consistent positivity rate trend.

3. **Regression Findings**:
   - GDP per capita and vaccination progress significantly predict total cases.
   - Population density shows weaker correlation.

4. **Hypothesis Testing**:
   - Statistically significant differences in vaccination progress between the two regions (p-value < 0.05).

---

## 🚀 Future Improvements
- Include additional features like government stringency index and healthcare capacity.
- Apply advanced predictive models (e.g., Random Forest).
- Extend analysis to other continents or global comparisons.

---

## 🤝 Contributions
Feel free to fork this repository, submit pull requests, or report issues.

---
