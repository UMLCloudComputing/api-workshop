# All information for the API can be found in the link below
# https://gist.github.com/StephenBlackWasAlreadyTaken/adb0525344bedade1e25

# Application ID foud by a previous reverse engineering of the share app done by the user
# who wrote the above docs
APPLICATION_ID = 'd8665ade-9673-4e27-9ff6-92db4ce13d13'

# API Endpoints
BASE_URL_US = 'https://share2.dexcom.com/ShareWebServices/Services'
LOGIN_ENDPOINT = '/General/LoginPublisherAccountByName'
AUTH_ENDPOINT = '/General/AuthenticatePublisherAccount'
CURRENT_EGV_ENDPOINT = '/Publisher/ReadPublisherLatestGlucoseValues'

# TrendArrow Mappinf for symbols
TTREND_ARROW_MAP = {
	'None':           '', 
	'Flat':           '→',
	'SingleUp':       '↑',
	'DoubleUp':       '↑↑',
	'FortyFiveUp':    '↗',
	'SingleDown':     '↓',
	'DoubleDown':     '↓↓',
	'FortyFiveDown':  '↘',
	'NotComputable':  '?',
	'RateOutOfRange': '-',
}

# Default Values
DEFAULT_MINUTES = 1440