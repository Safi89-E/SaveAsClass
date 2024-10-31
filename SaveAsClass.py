
import sys  
from PyQt6.QtWidgets import (QApplication,
                              QWidget,
                                QVBoxLayout,
                                  QLabel,
                                    QTextEdit,
                                      QPushButton
)

def read_file_content(filename):  
    try:  
        with open(filename, 'r') as file:  
            content = file.read()  
        return content  
    except FileNotFoundError:  
        return f"The file {filename} does not exist."  
    except Exception as e:  
        return str(e)  

# نام فایل را مشخص کنید  
filename = 'empty.py'  

# خواندن محتویات فایل  
content = read_file_content(filename)  
print("Content of the file:")  
print(content)  
class SaveAsWindow(QWidget):  
    def __init__(self):  
        super().__init__()  

        # تنظیمات اولیه پنجره  
        self.setWindowTitle("Save As")  
        self.setGeometry(100, 100, 300, 200)  
        
        # ایجاد یک layout عمودی  
        layout = QVBoxLayout()  

        # برچسب "Save As:"  
        self.label = QLabel("Save As:")  
        layout.addWidget(self.label)  

        # ایجاد QTextEdit  
        self.text_edit = QTextEdit()  
        layout.addWidget(self.text_edit)  

        # دکمه برای ذخیره  
        self.save_button = QPushButton("Save")  
        self.save_button.clicked.connect(self.save_file01)  
        layout.addWidget(self.save_button)  

        self.setLayout(layout)  

    def save_file01(self):  
        # متن وارد شده در QTextEdit را به عنوان نام فایل دریافت می‌کنیم  
          
       
        file_name = self.text_edit.toPlainText()
        # بررسی اینکه آیا نام فایل خالی باشد  
        if not file_name:  
            print("Filename cannot be empty.")  
            return  

        # ایجاد فایل با نام مشخص شده  
        with open(file_name + '.txt', 'w') as file:  
            file.write(content)  # محتوایی که می‌خواهید ذخیره کنید  

        print(f"File saved as '{file_name}.txt'") 
        self.save_button.clicked.connect(self.close) 

# اجرای برنامه  
if __name__ == "__main__":  
    app = QApplication(sys.argv)  
    window = SaveAsWindow()  
    window.show()  
    sys.exit(app.exec())  