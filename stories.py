from telethon import TelegramClient
from telethon.tl.functions.stories import GetStoriesByIDRequest
from telethon.tl.types import StoryItem

api_id = ""
api_hash = ""
story_client = TelegramClient("story_client", api_id, api_hash)

async def get_story(event):
    try:
        await story_client.get_messages(event.chat_id, event.message.id)
        response = await story_client(GetStoriesByIDRequest(peer=event.media.peer, id=[event.media.id]))
        if response.stories:
            return response.stories[0]
        else:
            raise ValueError("Story not found.")
    except Exception as e:
        raise RuntimeError(f"Failed to fetch the story: {e}")

async def get_story_text(story):
    if not isinstance(story, StoryItem):
        raise ValueError("Invalid story object.")
    return story.caption if story.caption else "No caption"

async def get_story_entities(story):
    if not isinstance(story, StoryItem):
        raise ValueError("Invalid story object.")
    return story.entities if story.entities else []

async def get_story_media(story):
    if not isinstance(story, StoryItem):
        raise ValueError("Invalid story object.")
    return story.media

async def get_story_views(story):
    if not isinstance(story, StoryItem):
        raise ValueError("Invalid story object.")
    return story.views if story.views is not None else 0

async def get_story_date(story):
    if not isinstance(story, StoryItem):
        raise ValueError("Invalid story object.")
    return story.date