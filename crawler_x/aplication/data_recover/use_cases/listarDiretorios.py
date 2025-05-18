from crawler_x.modules.data_recover.service.dataRecover import DataRecover

class ListarDiretorios:
    def __init__(self):
        self.data_recover = DataRecover()
        
    def execute(self):
        return self.data_recover.recover_directories()