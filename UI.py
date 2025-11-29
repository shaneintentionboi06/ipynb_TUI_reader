from textual.app import App, ComposeResult
from textual.widgets import Header,Footer,Static,TextArea


class editor(App):
    
    BINDINGS = [('q','quit','Quit Program')]
    
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Static(content="Hello World")
        yield Footer()
        
        
if __name__ == "__main__":
    App = editor()
    App.run()