# django-site

TODO:
- Thread Controller

# Api Examples

Return Example:
{"code": "OK", "message": {"count": 2, "next": null, "previous": null, "results": [ ... ]}}

"CODE" will always be ERROR when any errors occur, and OK if the request was successful

# Get all titles
http://{HOST}:{PORT}/api/titles?page=1&page_size=1

# Get volumes by TITLE_ID
http://{HOST}:{PORT}/api/getvol?title_id=1

# Get detailed information about the Title
http://{HOST}:{PORT}/api/info?id=1

### Get chapters by VOLUME_ID. Supports pagination
http://{HOST}:{PORT}/api/chapter?volume_id=1&page=1&page_size=1

### Set like to chapter by CHAPTER_ID
http://{HOST}:{PORT}/api/like?chapter_id=1
