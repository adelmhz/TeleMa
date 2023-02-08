import os

class Settings:
    API_ID = '4699123'
    API_HASH = '281f234f99f9f0cb72b5f2c39c33549e'
    session_string = 'BQAJEtgAt64UpXk6fu6sRYnA98M19QuI1l2l32x9kI_CrixwvaNcnfIcmKZQ-ZIfQHnyNIQylS0dj2G_N8NecbAHPQ9dX9577Ks42qZCOZyVsz7-dKh0pYdpVLWJcY4G3YJitcvAtFQQzmr0AahASOtNWSbcbdHSv_fGbUQ-d6TL7gGagtQp1tl0aeAzT_Ljp4Jkgat5PQ39PhAh4zAF2I0J1jhzCG5hpdCvpYkXR7WTkE_T-_JWrPSB4KEHO6nVSUKjpkXt_XwopH3-PqfSMRuT4FvUwimPqJU1RzokwzUCzxwA_5lyFc830P83wX0tY1uimS_-cM2idXcOTvRmX6pv4eDNCgAAAAB_VUjMAA'
    phone = '+8801969895867'
    TELEGRAM_CHAT_ID = 777000
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    UPLOAD_PATH = os.path.join(BASE_DIR, 'uploads')
    PROXY = {
     "scheme": "socks5",  # "socks4", "socks5" and "http" are supported
     "hostname": "pr.roxlabs.cn",
     "port": 4600,
     "username": "user-rox1548187-region-id",
     "password": "123456qq"
 }

settings = Settings()