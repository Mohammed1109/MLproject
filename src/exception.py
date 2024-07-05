import sys
from logger import logging

def error_msg_detail(error , error_details:sys):
    _,_,exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename # this will help me to get the file name in which error is there
    error_msg = 'Error occured in python script name [{0}] line number [{1}] and error message [{2}]'.format(
        file_name , exc_tb.tb_lineno,str(error)
    )

    return error_msg

class CustomException(Exception):
    def __init__(self , error_msg , error_details:sys):
        super().__init__(error_msg)
        self.error_msg = error_msg_detail(error_msg , error_details=error_details)

    def __str__(self):
        return self.error_msg


# if __name__ == '__main__':
#     try:
#         a = 1/0
#     except Exception as e:
#         logging.info('Divide By Zero error')
#         raise CustomException(e , sys)