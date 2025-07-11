# Gene Tracker App

This project analyzes and visualizes weight and body fat percentage data to help users understand trends and baseline norms using personal health data. Built with Python, it includes visual tools for:

- 📊 Weight distribution analysis
- 📈 Relationship between weight and body fat %
- 🚻 Body fat comparison by sex

## 🚀 Features

- Cleaned and structured data from wearable/device exports
- Visual analytics using `pandas`, `seaborn`, and `matplotlib`
- Ready to integrate with genetic and fasting data sources

> ⚠️ **Note:** The core predictive model (`fat_loss_model.py`) is proprietary and excluded from this repository.

## 🛡 License

This project is licensed under the **Business Source License 1.1 (BSL)**.  
Non-commercial use is permitted under the terms of the license.  
Commercial use (e.g., in a paid product, platform, or service) **requires a commercial license**.

See [`LICENSE.md`](LICENSE.md) for full terms.

If you're interested in using the fat loss model commercially, please contact:
📬 **callummelrose@gmail.com**

## 🛠 Getting Started

```bash
git clone https://github.com/Callummelrose93/gene-tracking.git
cd gene-tracking
pip install -r requirements.txt
python scripts/analysis.py

