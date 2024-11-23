import os,sys
class CustomException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)