import os
import sys


class CustomException(Exception):
    """
    Custom exception class to capture and display detailed error messages.
    """

    def __init__(self, error_message: Exception, error_details: sys):
        """
        Initialize the custom exception with a detailed error message.
        :param error_message: The original exception message.
        :param error_details: The sys module to extract traceback details.
        """
        self.error_message = CustomException.get_detailed_error_message(
            error_message=error_message, error_details=error_details
        )

    @staticmethod
    def get_detailed_error_message(error_message: Exception, error_details: sys):
        """
        Constructs a detailed error message.
        :param error_message: The original exception message.
        :param error_details: The sys module to extract traceback details.
        :return: A string containing the detailed error message.
        """
        try:
            _, _, exc_tb = error_details.exc_info()
            if exc_tb is None:
                return f"Error message: [{error_message}] (No traceback available)"

            # Extract traceback details
            exception_block_line_number = exc_tb.tb_frame.f_lineno
            try_block_line_number = exc_tb.tb_lineno
            file_name = exc_tb.tb_frame.f_code.co_filename

            # Construct the detailed message
            detailed_message = (
                f"*** Error occurred during execution ***\n"
                f"File: [{file_name}] \n"
                f"Try block line number: [{try_block_line_number}] \n"
                f"Exception block line number: [{exception_block_line_number}] \n"
                f"Error message: [{error_message}]"
            )
            return detailed_message
        except Exception as e:
            # Handle any errors during traceback extraction
            return f"Error constructing detailed message: [{str(e)}]. Original error: [{error_message}]"

    def __str__(self) -> str:
        """
        Return the detailed error message as a string representation.
        """
        return self.error_message

    def __repr__(self) -> str:
        """
        Return a string representation for debugging purposes.
        """
        return f"{CustomException.__name__}({self.error_message})"
