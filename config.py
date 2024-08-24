import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "22039620"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "8a7dabe0dccfbac57618a63b924d3240")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://yadavjitendray218:br7rDRVXTZf8sMPM@cluster0.u8pjo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
