# This is a simple Python program.
# it is to demonstrate my understanding of OOSD, use of ML and GUI elements and basic python skills
# I threw this together quickly as a demonstration, it is not particularly impressive, but appears to work fine
# it assess whether a given phrase is positive or negative using NLTK VADER
import tkinter as tk

from sentiment_analysis import Sentiment_analyser


class GUI:

    def __init__(self):
        self.sentiment_analyser = Sentiment_analyser()

        self.window = tk.Tk()
        self.sentiment_label = tk.Label(text='Sentiment')
        self.window.title("Sentiment Tester")
        self.instruction = tk.Label(text="Enter a sentence in the field, then press Submit")
        self.instruction.pack()
        self.field = tk.Entry()
        self.field.pack()
        self.submit = tk.Button(text="Submit",
                                command=self.submit,
                                )
        self.submit.pack()
        self.sentiment_label.pack()


    def run_GUI(self):
        self.window.mainloop()


    def submit(self):
        text = self.field.get()
        # manages empty field submission,
        if text == "":
            return
        self.field.delete(0, 'end')
        self.sentiment_analyser.process(text)
        sentiment = self.sentiment_analyser.get_sentiment()
        self.draw_result(sentiment)

    def draw_result(self, sentiment):
        pass
        # is a negative phrase
        if sentiment == 0:
            self.sentiment_label.config(
                text="Negative phrase",
                bg="red",
                fg="black"
            )

        # is a positive phrase
        else:
            self.sentiment_label.config(
                text='Positive phrase',
                bg='green',
                fg='white'
            )
        

if __name__ == "__main__":
    interface = GUI()

    interface.run_GUI()
