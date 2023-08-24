import logging
import sys 

def error_message_detail(error, error_details):
    _, _, exc_tb = error_details
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "error occurred in python script name {}, line number {}, error message: {}".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class Custom_Exception(Exception):
    def __init__(self, error_message, error_details):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_details)
        
    def __str__(self):
        return self.error_message

