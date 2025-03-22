from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout,
                             QVBoxLayout, QTextEdit,
                             QPushButton, QLabel, QListWidget, 
                             QLineEdit)
import json

'''Notes in json'''
notes_data = {
    "Algorithmics" : {
        "text" : "This is top school in Cambodia.",
        "tags" : ["learn", "study", "programming"]
    }
}

with open('notes_data_file.json', 'w') as file:
        # to create a json file with above dictionary data 
        json.dump(notes_data, file) 

app = QApplication([])

window = QWidget()
window.setWindowTitle('Smart Note Application')
window.resize(900, 600)

# tow vertical layouts
col1 = QVBoxLayout()
col2 = QVBoxLayout()
full_layout = QHBoxLayout()

# objects
text_editer = QTextEdit()
list_of_notes = QLabel('List of Notes')
list_widget = QListWidget()
delete_btn = QPushButton('delete note')
create_btn = QPushButton('create note')
save_btn = QPushButton('save note')

list_of_tag = QLabel('List of Tags')
tages_list_widget = QListWidget()
add_tage_btn = QPushButton('Add tag')
untage_btn = QPushButton('Untage')
search_by_tage = QPushButton('Search note by tags')
line_edit = QLineEdit('Enter tage...')

row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()
row4 = QHBoxLayout()

# add_widget
col1.addWidget(text_editer)
col2.addWidget(list_of_notes)
col2.addWidget(list_widget)
row1.addWidget(create_btn)
row1.addWidget(delete_btn)
row2.addWidget(save_btn)

col2.addLayout(row1)
col2.addLayout(row2)


col2.addWidget(list_of_tag)
col2.addWidget(tages_list_widget)
col2.addWidget(line_edit)
row3.addWidget(add_tage_btn)
row3.addWidget(untage_btn)
row4.addWidget(search_by_tage)

col2.addLayout(row3)
col2.addLayout(row4)

# add layout
full_layout.addLayout(col1)
full_layout.addLayout(col2)

# set layout to winsdow
window.setLayout(full_layout)


def display_notes():
    # this is function is used to display info from notes_data 
    # into application interface.
    key = list_widget.selectedItems()[0].text()
    text_editer.setText(notes_data[key]['text'])
    tages_list_widget.clear()
    tages_list_widget.addItems(notes_data[key]['tags'])

# connecting to the events
list_widget.itemClicked.connect(display_notes)


# by default, display items from json to list of notes
with open('notes_data_file.json', 'r') as file:
      data = json.load(file)
list_widget.addItems(data)

window.show()

app.exec_()