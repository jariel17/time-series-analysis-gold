import opendatasets as od
import os
import shutil

def download_dataset():
    dataset_url = "https://www.kaggle.com/datasets/nisargchodavadiya/daily-gold-price-20152021-time-series"
    
    if os.path.exists("data/Gold Price.csv"):
        print("Dataset already downloaded!")
        return
    
    try:
        od.download(dataset_url, data_dir="data")
        print("Dataset downloaded successfully!")
    except Exception as e:
        print(f"Download failed: {e}")
        print("Please download manually from Kaggle")
        return
    
    shutil.move("daily-gold-price-20152021-time-series/Gold Price.csv", "data/Gold Price.csv")

if __name__ == "__main__":
    download_dataset()