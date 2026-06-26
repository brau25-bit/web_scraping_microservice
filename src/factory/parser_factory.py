from src.parsers.manhwa18_parser import Manhwa18Parser
from src.exception.error import CustomError

class ParserFactory:

    @staticmethod
    def create_parser(source: str, html: str):
        if source == "manhwa18":
            return Manhwa18Parser(html)
        
        raise CustomError("no source provided", 400, "no_source")