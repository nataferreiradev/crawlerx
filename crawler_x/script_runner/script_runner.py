class PythonScriptRunner:
    def __init__(self, path: str):
        self.path = path

    def run(self, globals_dict=None, locals_dict=None):
        with open(self.path, 'r', encoding='utf-8') as file:
            script_code = file.read()
            exec(script_code, globals_dict, locals_dict)
