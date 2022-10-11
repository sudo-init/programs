import glob
from sklearn.model_selection import train_test_split

data_path = 'C:/Users/user/projects/delta_robot/dataset'


img_list = sorted(glob.glob(data_path + '/images/*.jpg'))

train_list, val_list = train_test_split(img_list, test_size=0.25, random_state=2022)

with open(data_path + "/train.txt", "w") as f:
    f.write("\n".join(train_list) + "\n")

with open(data_path + "/val.txt", "w") as f:
    f.write("\n".join(val_list) + "\n")
    
    

# C:/Users/user/projects/delta_robot/dataset