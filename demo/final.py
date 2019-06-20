# Import Stuff
# import pandas as pd


class Demo:
    def __init__(self, directory):
        self.dir = directory
        self.unzipper = ''
        self.data_extractor = ''
        self.sentiment_extractor = ''
        self.date_extractor = ''
        self.incoming_outcoming_extractor = ''
        self.plotter = ''

    def demo(self):
        pass
        # self.unzipper.unzip_all()
        # self.data_extractor.make_csv()
        # self.sentiment_extractor.add_sentiment()
        # self.date_extractor.extract_date()
        # self.incoming_outcoming_extractor.extract()
        # self.plotter.plot()


if __name__ == ' __main__':
    demo = Demo('demo')
    demo.demo()
