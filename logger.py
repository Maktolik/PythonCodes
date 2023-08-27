def log_errors(func):
    def logger(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError as z_error:
            file_content1 = ('<{}>  <{}>  <{}>  <{}>\n'.format(func.__name__, kwargs, Exception, z_error))
            with open('function_errors.log', 'a', encoding='utf8') as file:
                file.write(file_content1)
            raise ZeroDivisionError

        except ValueError as v_error:
            file_content2 = ('<{}>  <{}>  <{}>  <{}>\n'.format(func.__name__, args, Exception, v_error))
            with open('function_errors.log', 'a', encoding='utf8') as file:
                file.write(file_content2)
            raise ValueError

    return logger
