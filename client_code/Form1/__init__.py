from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run before the form opens.

  def run_code_click(self, **event_args):
    """This method is called when the button is clicked"""
    contents = self.input_data.file
    print("contents", contents)
    print("self.input_data.file.name", self.input_data.file.name)
    anvil.server.call('func', self.input_data.file.name, contents)
    pass
