from breezypythongui import EasyFrame

class TestGUI(EasyFrame):

    def __init__(self):
        EasyFrame.__init__(self, title="Test GUI", width=300, height=100, background="gray", resizable=False)

        self.guessLabel = self.addLabel(text="Guess: ", row=0, column=0)
        self.guessField = self.addIntegerField(value=0, row=0, column=1, sticky="W")

        self.addButton(text="Guess!", row=2, column=0, columnspan=2)

TestGUI().mainloop()