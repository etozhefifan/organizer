def logger_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception as ex:
            print('Error occured during transfer: ', str(ex))
            raise
        return result
    return wrapper
