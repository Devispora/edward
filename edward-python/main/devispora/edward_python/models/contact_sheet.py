from enum import Enum


class RepType(str, Enum):
    OutfitRep = 'Outfit Rep'
    CommunityRep = 'Community Rep'
    ScrimTeam = 'Scrim Team'
    ObserverUser = 'Observer User'


class Contact:
    def __init__(self, groups: [str], char_name: str, email: str, discord_handle: str, discord_id: int,
                 rep_type: RepType, account_limit: int):
        self.groups = groups
        self.char_name = char_name
        self.email = email
        self.discord_handle = discord_handle
        self.discord_id = discord_id
        self.rep_type = rep_type
        self.account_limit = account_limit
