class ApiObject():
    def __init__(self,name,url,query_params,headers):
        self.url = url
        self.name = name
        self.query_params = query_params
        self.headers = headers