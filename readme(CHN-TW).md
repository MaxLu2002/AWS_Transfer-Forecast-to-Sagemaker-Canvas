# FAKE_toy_sales.csv 資料集說明
1. 資料記錄了不同玩具過去五年在銷售中的表現
2. 這份資料包含日期、玩具ID、玩具名稱、類別、銷售數量與價格等欄位。
3. 玩具被分為不同的類別，例如建築類、藝術類、壓力舒緩類。
4. 銷售數據範圍涵蓋自2018年1月1日開始到2023年12月31日的每日記錄。
5. 資料中每個玩具的銷量和價格差異很大，從低價的藝術玩具到高價的建築玩具都有。 ​

# 玩具銷售預測與分析 Workshop
在這個 workshop 中，你將透過實際操作兩種 AWS 服務：**Amazon Forecast** 和 **Amazon Canvas**，以了解它們在資料分析與預測上的不同。本 workshop 目的在引導你從資料準備、上傳到分析與預測，並幫助你比較這兩個服務在使用體驗和結果上的差異。

## Workshop 目標
- 學習如何使用 Amazon Forecast 對資料進行需求預測。
- 體驗 Amazon Canvas 的視覺化分析與假設情境分析（What-If Analysis）。
- 透過操作，深入理解這兩種服務在模型配置、使用靈活性以及結果展示上的異同。

## 使用步驟
### 1. Forecast 預測分析
**Forecast.py** 的目的是將資料轉換為適合 AWS Forecast 進行需求預測的格式，並將資料拆分為三個主要部分：目標數據（Target Data）、元數據（Meta Data）和關聯數據（Related Data）。
#### 操作流程：
1. 執行 `Forecast.py`，生成所需的資料集：
    ```bash
    python Forecast.py
    ```
    這將生成 `toy_TD.csv`、`toy_MD.csv` 和 `toy_RD.csv` 三個資料集，並存放於 `./Forecast_dataset/` 資料夾中。
2. 將這三個資料集上傳至 AWS S3，作為 Amazon Forecast 訓練模型的輸入。
3. 在 AWS Management Console 中進入 Amazon Forecast，依照預設流程進行配置並訓練模型。確保為 Target Data、Meta Data、Related Data 選擇對應的資料集。
4. 模型訓練完成後，使用預測器（Predictor）進行需求預測，並下載結果進行分析。
#### 重點：
- Amazon Forecast 適合進行時間序列預測，並能根據歷史數據和相關變數（例如價格變動）進行準確的需求預測。
- 它的預測模型配置過程需要較多的數據處理與結構化資料的準備，適合處理大量、結構複雜的資料集。

---

### 2. Canvas 視覺化分析
**Canvas.py** 的目的是為 AWS Canvas 準備清理過的資料集，並且自動生成未來七天的空白銷售數據，以便啟用 Canvas 的「假設情境分析」（What-If Analysis）功能。
#### 操作流程：
1. 執行 `Canvas.py`：
    ```bash
    python Canvas.py
    ```
    這會生成 `cleaned_data.csv`，該檔案包含了原始資料與未來七天的空白銷售數據，儲存在 `./canvas_dataset/` 資料夾中。
2. 在 AWS Management Console 中，進入 SageMaker Canvas，並建立或啟用 SageMaker Domain。
3. 上傳 `cleaned_data.csv` 至 Canvas，進行資料配置。
4. 利用 Canvas 提供的可視化介面進行分析，並使用其「假設情境分析」功能，模擬未來的各種可能情境，觀察不同變數（例如價格變動）對未來銷售的影響。
#### 重點：
- Amazon Canvas 提供簡單易用的可視化操作介面，適合非技術用戶快速上手，並進行初步的資料探索和假設分析。
- 透過 What-If Analysis，你可以模擬未來各種可能的銷售場景，尤其是當沒有完整的未來數據時，這種功能非常實用。
- 相較於 Forecast，Canvas 在資料準備和操作上更為直觀，但分析的細緻度相對較低，適合較小規模或需求簡單的分析場景。

---

### 3. 比較分析結果
操作完成後，透過以下幾個角度比較 Forecast 與 Canvas 的分析結果：
- **使用靈活性**：Forecast 更適合大型、結構複雜的需求預測，並能根據多變數進行高準確度的預測；Canvas 則側重於簡易操作與視覺化分析。
- **結果準確性**：Forecast 的預測結果基於更多變量和時間序列分析，通常更具準確性；Canvas 更強調視覺化呈現和模擬未來情境的靈活性。
- **操作難易度**：Forecast 的數據準備和模型配置較為複雜，適合有技術背景的使用者；Canvas 提供簡單的界面，方便非技術使用者進行資料探索與分析。

希望透過這些比較，你將對兩種 AWS 服務的優勢與應用場景有更清晰的理解。

---

## 相關資源
- [Amazon Forecast](https://aws.amazon.com/forecast/)
- [Amazon SageMaker Canvas](https://aws.amazon.com/sagemaker/canvas/)
- [pandas Documentation](https://pandas.pydata.org/)