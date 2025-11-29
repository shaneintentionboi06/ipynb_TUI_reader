from textual.app import App,ComposeResult
from textual.widgets import Header,Footer,TextArea,Static, Welcome
from textual import events

class backo(App):
    BINDINGS = [('q','quit','Quit Test'), ('d','Toggle Dark Mode',"Switch Modes")]
    
    COLORS = ["white","black","blue",]
    
    # def Texas(Static):
    
    
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Welcome()
        yield Footer()    
    def on_button_pressed(self) -> None:
        self.exit()
        
    def on_mount(self) -> None:
        self.screen.styles.background = "darkblue" 
        
    def on_key(self, event) -> None:
        if  event.key.isdecimal() and int(event.key) < len(self.COLORS):
            self.screen.styles.background = self.COLORS[int(event.key)]
            
            
my_app = backo()
my_app.run()