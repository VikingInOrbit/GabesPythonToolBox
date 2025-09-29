from ..DataProsesing.DataRW import *
# from ..Utility.Debug import * ## sircular imports

#TODO logger cant have debug statments

class Logger:

    file_encoding = None

    @classmethod
    def start_loger(cls, file_path:str = "debug/In_relative_dir",caracter_encoding:str='utf-8',file_encoding:str='csv'):
        if not file_path:
            NotImplementedError
        #set cls.file_path
        NotImplementedError

    @classmethod
    def save_to_file(cls, data): #can i also apend data?
        """save log objects to a file"""
        write_data(data)#only writes full file
        NotImplementedError

    def log(cls, message: str, message_type: str = "-", group: str = None, verbosity: int = 1):


        #TODO fast read data to file as data comes inn



        NotImplementedError
    

