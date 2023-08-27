from datetime import datetime
import webbrowser


def story_logger(func):
    def logger(*args, **kwargs):
        file_content1 = ('<{}>  <{}>  <{}>  <{}> \n'.format('START', func.__name__, kwargs, datetime.now()))
        with open('storyLog.log', 'a', encoding='utf8') as file:
            file.write(file_content1)
        func(*args, **kwargs)
        file_content2 = ('<{}>  <{}>  <{}>  <{}> \n'.format('FINISH', func.__name__, kwargs, datetime.now()))
        with open('storyLog.log', 'a', encoding='utf8') as file:
            file.write(file_content2)
    return logger


@story_logger
def open_url(url):
    webbrowser.open(url)


open_url('https://github.com')

