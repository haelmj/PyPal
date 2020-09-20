from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
import filetype


def fileExplorer():
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    file_path= askopenfilename() # show an "Open" dialog box and return the path to the selected file
    return file_path
    
# test function to call fileexplorer:
# def main():
#     file_path = fileExplorer()
#     kind = filetype.guess(file_path)
#     if kind is None:
#         print('Cannot guess file type!')
#         return

#     print('File extension: %s' % kind.extension)
#     print('File MIME type: %s' % kind.mime)

# if __name__ == '__main__':
#     main()