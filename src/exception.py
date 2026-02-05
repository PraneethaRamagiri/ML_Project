import sys
import src.logger
import logging



# This function creates a detailed error message
# including file name, line number, and error description
def error_message_detail(error,error_detail:sys):

    # exc_info() returns:
    # (exception_type, exception_value, traceback)
    # We only need traceback, so we ignore first two

   
    _,_,exc_tb = error_detail.exc_info()    # exc_info()  gives 3 parameters,,3rd parameter gives info about in which file error has occured and in which line and also error message
   
   # Get the file name where the error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script named [{0}] line number [{1}] and error message is [{2}]".format(
        file_name,
        exc_tb.tb_lineno,str(error)
    )
    return error_message


# Custom exception class for better error handling

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):

        # Call the parent Exception class constructor

        super().__init__(error_message)

        # Generate and store detailed error message

        self.error_message = error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
    

if __name__=='__main__':
    try:
        a = 1/0
    except Exception as e:
        logging.info("Logging has started")
        raise CustomException(e,sys)