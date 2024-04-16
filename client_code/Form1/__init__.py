from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run before the form opens.

  def run_code_click(self, **event_args):
    """This method is called when the button is clicked"""
    result = anvil.server.call('func', self.input_data.file.name, self.input_data.file)

    csv_file = anvil.BlobMedia('text/plain', result.encode('utf-8'), name='Your Keywords Clustered.csv')
    anvil.media.download(csv_file)
    
    pass
