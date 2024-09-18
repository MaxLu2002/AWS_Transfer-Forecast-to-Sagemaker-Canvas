<!-- English Version -->
# FAKE_toy_sales.csv Dataset Description
1. The data records the sales performance of various toys over the past five years.
2. This dataset includes fields such as date, toy ID, toy name, category, sales quantity, and price.
3. Toys are categorized into different types, such as Building, Art, and Stress Relief.
4. The sales data covers daily records from January 1, 2018, to December 31, 2023.
5. There is a wide range of toy sales and prices, from low-priced art toys to high-priced building toys.

# Toy Sales Forecast and Analysis Workshop

In this workshop, you will practically operate two AWS services: **Amazon Forecast** and **Amazon Canvas**, to understand their differences in data analysis and forecasting. This workshop aims to guide you through data preparation, uploading, analysis, and forecasting, helping you compare these two services in terms of user experience and results.

## Workshop Objectives

- Learn how to use Amazon Forecast for demand forecasting.
- Experience Amazon Canvas for visual analysis and What-If Analysis.
- Through hands-on practice, gain a deep understanding of the differences between these two services in terms of model configuration, flexibility of use, and result presentation.

## Steps to Use

### 1. Forecast Analysis

The purpose of **Forecast.py** is to convert the data into a format suitable for use with AWS Forecast for demand forecasting. It splits the data into three main parts: Target Data, Meta Data, and Related Data.

#### Steps:

1. Run `Forecast.py` to generate the necessary datasets:
    ```bash
    python Forecast.py
    ```
    This will generate three datasets: `toy_TD.csv`, `toy_MD.csv`, and `toy_RD.csv`, and store them in the `./Forecast_dataset/` folder.
   
2. Upload these three datasets to AWS S3, which will serve as input for training the model in Amazon Forecast.

3. Go to Amazon Forecast in the AWS Management Console, and follow the standard procedure to configure and train the model. Ensure that the corresponding datasets are selected for Target Data, Meta Data, and Related Data.

4. Once the model training is complete, use the Predictor to perform demand forecasting and download the results for analysis.

#### Key Points:

- Amazon Forecast is suitable for time-series forecasting, providing accurate demand predictions based on historical data and related variables (e.g., price changes).
- The model configuration process in Forecast requires more data handling and preparation, making it ideal for large-scale and complex data structures.

---

### 2. Canvas Visual Analysis

The purpose of **Canvas.py** is to prepare a cleaned dataset for AWS Canvas and automatically generate empty sales data for the next seven days, enabling the What-If Analysis feature in Canvas.

#### Steps:

1. Run `Canvas.py`:
    ```bash
    python Canvas.py
    ```
    This will generate `cleaned_data.csv`, which includes the original data and empty sales data for the next seven days. The file will be stored in the `./canvas_dataset/` folder.

2. In the AWS Management Console, go to SageMaker Canvas, and create or enable a SageMaker Domain.

3. Upload the `cleaned_data.csv` file to Canvas for data configuration.

4. Use Canvas's visual interface for analysis, and leverage the What-If Analysis feature to simulate various future scenarios and observe the impact of different variables (e.g., price changes) on future sales.

#### Key Points:

- Amazon Canvas offers a simple and easy-to-use visual interface, ideal for non-technical users to quickly get started with data exploration and analysis.
- With What-If Analysis, you can simulate various potential sales scenarios, especially useful when no complete future data is available.
- Compared to Forecast, Canvas is more intuitive for data preparation and operation, but its analysis depth is relatively limited, making it suitable for smaller-scale or simpler analysis tasks.

---

### 3. Comparing Analysis Results

After completing the operations, compare the analysis results of Forecast and Canvas through the following aspects:

- **Flexibility**: Forecast is better suited for large-scale, complex demand forecasting, with high accuracy based on multiple variables, while Canvas focuses on easy-to-use operations and visual analysis.
- **Accuracy of Results**: Forecast typically provides more accurate predictions based on more variables and time-series analysis, whereas Canvas emphasizes flexibility in visualizing and simulating future scenarios.
- **Ease of Use**: Forecast requires more complex data preparation and model configuration, making it ideal for users with a technical background. Canvas provides a simple interface for non-technical users to explore and analyze data.

Through these comparisons, you will gain a clearer understanding of the advantages and application scenarios of both AWS services.

---

## Related Resources

- [Amazon Forecast](https://aws.amazon.com/forecast/)
- [Amazon SageMaker Canvas](https://aws.amazon.com/sagemaker/canvas/)
- [pandas Documentation](https://pandas.pydata.org/)
