from crawler_x.modules.data_recover.service.dataRecover import DataRecover

class PegarDiretorioZippado:
    def __init__(self):
        self.data_recover = DataRecover()
        
    def execute(self,directory_name):
        self.data_recover.delete_zip_files()
        return self.data_recover.zip_directory_by_name(directory_name)