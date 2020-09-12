from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from apikey import apikey
from googleapiclient.http import MediaFileUpload
CLIENT_SECRET_FILE = 'client_secret.json'
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
credentials = flow.run_console()
youtube = build('youtube', 'v3', credentials=credentials)

request = youtube.channelBanners().insert(
        channelId="UCiBfuUreTbKvBKtQbb6SIWQ",
        body={},
        
        media_body=MediaFileUpload("2.jpg")
    )
response = request.execute()

print(response)

