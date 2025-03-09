#import
from datasets import load_dataset
from datasets import DownloadConfig
import os
logo = '''
       ###
       ###
       ###
    #########
    #########
     #######
      #####
       ###
        #
  __________________
 /                  \\
|   ______________   |
|  |              |  |
|  |    [####]    |  |
|  |    [####]    |  |
|  |    [####]    |  |
|  |______________|  |
 \\__________________/
   Dataset downloader
'''
#logo printing
print(logo)

#dataset and branch select
dataset_name = input("Enter dataset")
dataset_revision = input("Enter revision (main on defoult)") or "main"

#data splitting
data = {"train": "train.csv", "test": "test.csv"}
data_split = input("Enter data split (train/test, leave empty for all): ").strip
if not data_split:
    data_split = None

#download folder
download_folder = os.path.join(os.path.dirname(__file__), "datasets")
os.makedirs(download_folder, exist_ok=True)

download_config = DownloadConfig(cache_dir=download_folder)


#settings confirmation
#print("dataset: " , dataset_name)
#print("revision: " , dataset_revision)
#print("split: " , data_split)
confirmation = input("is all correct ? [y/n]")

if confirmation == "y":
    dataset = load_dataset(
        dataset_name,
        #split=data_split,
        revision=dataset_revision,
         cache_dir=download_folder



    )