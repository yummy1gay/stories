```python
from stories import story_client
import asyncio

async def main():
    await story_client.start()
    await story_client.run_until_disconnected()

asyncio.run(main())
```

```python
from stories import get_story

story = await get_story(event)
```

```python
from stories import (
    get_story_text,
    get_story_entities,
    get_story_media,
    get_story_views,
    get_story_date
)

text = await get_story_text(story)
entities = await get_story_entities(story)
media = await get_story_media(story)
views = await get_story_views(story)
date = await get_story_date(story)

```
