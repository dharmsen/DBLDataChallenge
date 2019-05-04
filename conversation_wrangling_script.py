# Dependencies
import time
import sqlite3
import pandas as pd

class ConversationWrangler:
    '''Performs filtering and feature
    engineering steps on airline conversation data.
    '''
    def __init__(self, file_name):
        '''
            Takes a conversation csv file with the columns 'conversation_id' and 'raw_tweets_info'
        '''
        self.file_name = file_name
        # Read in files to DataFrames
        print('Reading in datasets')
        self.df = pd.read_csv(self.file_name, names=['conversation_id', 'raw_tweets_info'])
        self.conn = sqlite3.connect('full_conversation_database.db')
        self.conv_df = pd.read_sql('SELECT * from tweets', self.conn)
        print('Loaded both dataframes. Continuing with wrangling operations')

    def conversation_length(self):
        '''
        Extracts conversation length for each conversation and adds them
        to a new column
        '''
        print('Starting with conversation_length feature')
        self.df['conversation_length'] = [len(eval(tweet)) for tweet in list(self.df['raw_tweets_info'])]
        print('conversation_length added')

    def filter_conversations(self, min_length=2):
        '''
        Keeps only conversation which have a certain length
        Take an argument 'min_length' which the denotes
        the minimum length of conversations you want to keep
        Requires conversation length to be computed
        '''
        print('Starting with filter_conversations')
        self.df = self.df[self.df['conversation_length'] >= min_length]
        print('filter_conversations added')

    def tweet_ids(self):
        '''
        Extracts a list of tweet ids from each conversation
        and adds them to a new column.
        '''
        print('Starting with tweet_ids feature')
        tweet_ids = []
        # Collect list of lists with tweet ids from every conversation
        for conv in list(self.df['raw_tweets_info']):
            ids = []
            for tweet in eval(conv):
                ids.append(tweet[0])
            # Append flipped version
            tweet_ids.append(ids[::-1])

        # Add tweet_ids feature to DataFrame
        self.df['tweet_ids'] = tweet_ids
        print('tweets_ids added')

    def user_ids(self):
        '''.
        Extracts a list of user ids from each conversation
        and adds them to a new column.
        '''
        print('Starting with user_ids feature')
        user_ids = []
        # Collect list of lists with user ids from every conversation
        for conv in list(self.df['raw_tweets_info']):
            ids = []
            for tweet in eval(conv):
                ids.append(str(tweet[1]))
            # Append flipped version
            user_ids.append(ids[::-1])

        # Add user_ids feature to DataFrame
        self.df['user_ids'] = user_ids
        print('user_ids added')

    def airlines_involved(self):
        '''
        Checks which airlines are involved in a conversation
        and adds those airlines to a new column.
        Required user_ids to be added.
        '''
        print('Starting with airlines_involved feature')
        # Map airline ids and names
        keys = ["56377143", "106062176", "18332190", "22536055", "124476322", "26223583", "2182373406", "38676903",
                  "1542862735", "253340062", "218730857", "45621423", "20626359"]
        values = ["KLM", "AirFrance", "British_Airways", "AmericanAir", "Lufthansa", "AirBerlin", "AirBerlin assist",
                "easyJet", "RyanAir", "SingaporeAir", "Qantas", "EtihadAirways", "VirginAtlantic"]
        keys = [int(key) for key in keys]
        airline_dict = dict(zip(keys, values))

        # Collect contents of airlines_involved feature
        airlines = []
        for row in list(self.df['user_ids']):
            # Check if there are airlines involved in the conversation
            if bool(set(list(row)).intersection(keys)):
                # Collect the ids of the airlines
                airline_ids = set((list(row))).intersection(keys)
                # Extract airline names from these ids
                extracted_airlines = [airline_dict[airline_id] for airline_id in airline_ids]
                airlines.append(extracted_airlines)
            else:
                # Add placeholder
                airlines.append('No airlines involved')

        # Append feature to the DataFrame
        self.df['airlines_involved'] = airlines
        print('airlines_involved added')

    def add_conversations(self):
        '''
        Adds conversations for every row.
        Requires two datasets to be loaded
        Requires tweet_ids to be added
        '''
        print('Starting add_conversations')
        self.df = self.df[self.df['airlines_involved'] != 'No airlines involved']
        print(f'Extracting: {len(self.df)} conversations')
        all_conversations = []
        n_row = 1
        for row in list(self.df['tweet_ids']):
            conversation = list(self.conv_df[self.conv_df['id_str'].isin(row)]['text'])
            all_conversations.append(conversation)
            if n_row % 1000 == 0:
                to_go = len(self.df) - n_row
                print(f'{n_row} rows done. {to_go} more rows to go.')
            n_row += 1
        print('conversation feature added')
        return all_conversations

    def to_csv(self, file_name=None):
        '''
        Saves the DataFrame to a csv file
        '''
        print('Saving to csv')
        if file_name == None:
            # Standard file_name
            file_name = f'wrangled_{self.file_name}'
        self.df.to_csv(file_name, index=False)
        print('Saved to csv')

    def to_sql_table(self):
        '''
        Adds the DataFrame to an SQL table
        '''
        # TODO Make function that adds DataFrame to an SQL table
        pass

    def full_standard_wrangle(self, min_length=2, file_name=None):
        '''
        Performs all steps in the class
        Takes an argument 'min_length' for filtering conversations
        '''
        print('Starting with full_standard_wrangle')
        self.conversation_length()
        self.filter_conversations(min_length=min_length)
        self.tweet_ids()
        self.user_ids()
        self.airlines_involved()
        #self.add_conversations()
        self.to_csv(file_name=file_name)
        print('Done with full_standard_wrangle!')

    def extract_conversations(self, min_length=2):
        self.conversation_length()
        self.filter_conversations(min_length=min_length)
        self.user_ids()
        self.tweet_ids()
        self.airlines_involved()
        conversations = self.add_conversations()
        new_df = pd.DataFrame({'Conversations' : conversations})
        new_df.to_csv('Conversations.csv', index=False)

if __name__ == '__main__':
    # Keep time
    t_start = time.time()
    # Do the wrangling
    wrangler = ConversationWrangler('full_db_conversations_final.csv')
    #wrangler.full_standard_wrangle(min_length=2, file_name='wrangled_conversations_db_with_full_conversations.csv')
    wrangler.extract_conversations(min_length=2)
    # Check and print how many seconds it took
    t_finish = time.time()
    total_time = round((t_finish - t_start), 2)
    print('Runtime = {} seconds'.format(total_time))
    wrangler.conn.close()



