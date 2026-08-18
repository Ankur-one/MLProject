import sys


def error_message_detail(error, error_detail):
    _, _, exc_tb = error_detail

    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno

    error_message = (
        f"Error occurred in python script name "
        f"[{file_name}] line number [{line_number}] "
        f"error message [{str(error)}]"
    )

    return error_message


class CustomerException(Exception):

    def __init__(self, error_message, error_detail):
        super().__init__(error_message)
        self.error_message = error_message
        self.error_detail = error_detail

    def __str__(self):
        return error_message_detail(
            self.error_message,
            self.error_detail
        )


if __name__ == "__main__":

    try:
        a = 1 / 0

    except Exception as e:
        print(CustomerException(e, sys.exc_info()))