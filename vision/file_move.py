from logger import Logger
import os
import shutil


class FileMove():

    def __init__(self):
        self.logger = Logger()
        
        
    def get_file_list(self, file_path):
        
        try:
            if os.path.exists(file_path):
                return os.listdir(file_path)[1:]
                
        except Exception as e:
            self.logger.exception(e)
            
    def move_mapping_file(self, files, image_source_path, image_target_path, label_source_path, label_target_path):
        for file in files:
            image_file = file.split('.')[0] + '.' + 'jpg'    # image file name
            shutil.copy(image_source_path + '/' + image_file, image_target_path + '/' + image_file)  # copy image file
            shutil.copy(label_source_path + '/' + file, label_target_path + '/' + file)              # copy label file
            
    def run(self, image_source_path, image_target_path, label_source_path, label_target_path):
        files = self.get_file_list(label_source_path)
        train_valid_ratio = 0.25
        threshold = int(len(files) * train_valid_ratio) 
        
        valid_image_target_path = image_target_path + '/' + 'valid'
        train_image_target_path = image_target_path + '/' + 'train'
        valid_label_target_path = label_target_path + '/' + 'valid'
        train_label_target_path = label_target_path + '/' + 'train'
        
        try:
            self.move_mapping_file(files[:threshold], image_source_path, valid_image_target_path, 
                                label_source_path, valid_label_target_path)
            self.move_mapping_file(files[threshold:], image_source_path, train_image_target_path, 
                                label_source_path, train_label_target_path)
        
        except Exception as e:
            self.logger.exception(e)
            
    
def test():
    image_source_path = 'C:/Users/user/projects/delta_robot/data/captured_images'
    image_target_path = 'C:/Users/user/projects/delta_robot/data/images'
    label_source_path = 'C:/Users/user/projects/delta_robot/data/labeled_data'
    label_target_path = 'C:/Users/user/projects/delta_robot/data/labels'
    
    FileMove().run(image_source_path, image_target_path, label_source_path, label_target_path)
    
    

if __name__ == '__main__':
    test()
    