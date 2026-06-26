from src.sources.manhwa18_source import Manhwa18Source
from src.exception.error import CustomError

class SourceFactory:

    @staticmethod
    def create_source(source_name: str):

        if source_name == "manhwa18":
            return Manhwa18Source() 
        
        raise CustomError("no source provided", 400, "no_source")