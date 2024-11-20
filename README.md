```python
from stories import story_client

await story_client.start()
```

```python
from stories import get_story

peer = message.media.peer
story_id = message.media.id

story = await get_story(peer, story_id)
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
