import os
import sys


class CustomException(Exception):
    def __init__(self, error_message: Exception, error_details: sys):
        # Set the error message using the detailed message method
        self.error_message = CustomException.get_detailed_error_message(
            error_message=error_message, error_details=error_details
        )

    @staticmethod
    def get_detailed_error_message(error_message: Exception, error_details: sys):
        """
        Constructs a detailed error message.
        """
        _, _, exc_tb = error_details.exc_info()
        exception_block_line_number = exc_tb.tb_frame.f_lineno
        try_block_line_number = exc_tb.tb_lineno
        file_name = exc_tb.tb_frame.f_code.co_filename

        # Create the detailed error message
        detailed_message = (
            f"*** Error occurred during execution ***\n"
            f"File: [{file_name}] \n"
            f"Try block line number: [{try_block_line_number}] \n"
            f"Exception block line number: [{exception_block_line_number}] \n"
            f"Error message: [{error_message}]"
        )
        return detailed_message

    def __str__(self) -> str:
        return self.error_message

    def __repr__(self) -> str:
        return f"{CustomException.__name__}({self.error_message})"
