import motor.motor_asyncio
from pymongo import MongoClient

# Create a MongoDB client
client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
database = client.school_blog

# Access the posts collection
posts_collection = database.posts
