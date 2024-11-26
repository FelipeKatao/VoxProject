import traceback

class VoxConsole:
    def __init__(self) -> None:
        pass

    def VoxValidate(self,FunctionValue,Rule):
        try:
            self.VoxRules(FunctionValue(),Rule)
            return "Projeto executado com sucesso."
        except Exception as e:
            tb_original = ''.join(traceback.format_tb(e.__traceback__))
            tb = traceback.extract_tb(e.__traceback__)
            eA = f"{tb_original}  {tb[len(tb)-1]}"
            return eA
        
    def VoxRules(self,Rule,values):
        ...
            