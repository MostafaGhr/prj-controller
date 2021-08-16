import decouple

config = decouple.AutoConfig()

BROKER_URL = config('BROKER_URL')
TASHCAN_ID = config('TASHCAN_ID', cast=int)