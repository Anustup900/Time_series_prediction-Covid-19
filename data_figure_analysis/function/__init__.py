import os

parent_path = os.path.abspath(os.pardir)

TRAIN_FILE = parent_path + '/data/time_series_covid19_confirmed_US.csv'
TRAIN_FILE_CONVERT = parent_path + '/data/daily_cases.txt'
TWEETS_FILE_CSV = parent_path + '/data/tweets/tweets-ids-%s.csv'
TWEETS_FILE_CSV_MERGE = parent_path + '/data/tweets-ids-merge-filter.csv'

states_full = ['Alabama','Alaska','American Samoa','Arizona','Arkansas','California',
 'Colorado','Connecticut','Delaware','Diamond Princess','District of Columbia','Florida','Georgia',
 'Grand Princess','Guam','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana',
 'Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri',
 'Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York',
 'North Carolina','North Dakota','Northern Mariana Islands','Ohio','Oklahoma','Oregon','Pennsylvania','Puerto Rico',
 'Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont',
 'Virgin Islands','Virginia','Washington','West Virginia','Wisconsin','Wyoming']