import sys


class CustomException(Exception):

    def __init__(self, error_message, error_detail=None):
        super().__init__(error_message)

        self.error_message = error_message
        self.error_detail = error_detail

    def __str__(self):

        try:

            if self.error_detail is not None:

                _, _, exc_tb = self.error_detail.exc_info()

                if exc_tb is not None:

                    file_name = exc_tb.tb_frame.f_code.co_filename
                    line_number = exc_tb.tb_lineno

                    return (
                        f"Error occurred in Python script "
                        f"[{file_name}] "
                        f"line number [{line_number}] "
                        f"error message [{self.error_message}]"
                    )

            return f"Error message [{self.error_message}]"

        except Exception:

            return f"Error message [{self.error_message}]"