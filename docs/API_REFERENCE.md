# API Reference for aiodiscourse

## Admin Namespace

- `anonymize_user(user_id: int)`  
  Anonymize a user account by replacing identifying information.

- `approve_user(user_id: int)`  
  Approve a user who is pending moderation.

- `create_backup()`  
  Trigger creation of a new site backup.

- `download_backup(filename: str)`  
  Download an existing backup file by filename.

- `get_user(user_id: int)`  
  Retrieve detailed admin-level user info.

- `grant_trust(user_id: int, level: int)`  
  Set a user's trust level.

- `list_backups()`  
  List all existing site backups.

- `list_badges()`  
  List all configured badges on the site.

- `list_user_actions(user_id: int)`  
  Retrieve a user’s action logs (e.g. posts, likes, flags).

- `list_users(**kwargs)`  
  List users with admin-level filtering (e.g. `active`, `suspended`, etc.).

## Categories Namespace

- `create(name: str, color: str, text_color: str, parent_category_id: Optional[int] = None, **kwargs)`  
  Create a new category. Requires `name`, `color`, and `text_color`. Optionally nest under a parent category.

- `get(category_id: int)`  
  Retrieve details for a specific category by ID.

- `list()`  
  List all visible categories.

## Groups Namespace

- `add_user(group_id: int, username: str)`  
  Add a user to a group.

- `create(name: str, **kwargs)`  
  Create a new group with the specified name and optional settings.

- `get(group_id: int)`  
  Get group details by ID.

- `list()`  
  List all groups.

- `remove_user(group_id: int, username: str)`  
  Remove a user from a group.

## Notifications Namespace

- `list()`  
  List the current user's notifications.

- `mark_read(notification_id: int)`  
  Mark a single notification as read.

- `mute(notification_level: str)`  
  Mute a specific level of notifications (e.g., `"watching_first_post"`).

## Posts Namespace

- `bookmark(post_id: int)`  
  Bookmark a post.

- `create(topic_id: int, raw: str, reply_to_post_number: Optional[int] = None, **kwargs)`  
  Create a new post in a topic. You can reply to a specific post using `reply_to_post_number`.

- `delete(post_id: int)`  
  Delete a post by its ID.

- `get(post_id: int)`  
  Retrieve the details of a post by its ID.

- `like(post_id: int)`  
  Like a post.

- `update(post_id: int, raw: str)`  
  Edit the contents of a post.

## Search Namespace

- `advanced(**kwargs)`  
  Perform an advanced search with filters like `tags`, `in:title`, `status`, etc.

- `iter_results(query: str, **kwargs)`  
  Iterate through paginated search results.

- `query(query: str, **kwargs)`  
  Perform a standard search with the given query string.

## Tags Namespace

- `create_group(name: str, tag_names: list[str])`  
  Create a tag group containing the given tags.

- `get(tag_name: str)`  
  Get information about a single tag.

- `list()`  
  List all tags available on the site.

- `update_group(group_id: int, **kwargs)`  
  Update the properties or membership of a tag group.

## Topics Namespace

- `archive(topic_id: int, **kwargs)`  
  Archive a topic (makes it read-only).

- `bump(topic_id: int)`  
  Bump a topic to the top of the latest list.

- `close(topic_id: int, message: Optional[str] = None)`  
  Close a topic and optionally leave a moderator message.

- `create(...)`  
  Create a new topic. (See full signature in `PostsNamespace`.)

- `get(topic_id: int)`  
  Retrieve full details for a topic by ID.

- `hide(topic_id: int, **kwargs)`  
  Hide a topic (sets `visible = false`).

- `iter_latest()`  
  Return an async iterator over the latest topics.

- `list_latest()`  
  Return a list of the latest topics.

- `pin(topic_id: int, until: Optional[str] = None, globally: bool = False, message: Optional[str] = None)`  
  Pin a topic locally or globally. Optionally provide an `until` date (`YYYY-MM-DD`) to auto-unpin.

- `reopen(topic_id: int, message: Optional[str] = None)`  
  Reopen a previously closed topic.

- `unarchive(topic_id: int, **kwargs)`  
  Unarchive a topic.

- `unhide(topic_id: int, **kwargs)`  
  Unhide a topic (sets `visible = true`).

- `unpin(topic_id: int, globally: bool = False, message: Optional[str] = None)`  
  Unpin a topic locally or globally.

- `update_status(topic_id: int, status: str, enabled: bool | str, **kwargs)`  
  Core method to update any topic status.  
  `status` must be one of `"closed"`, `"pinned"`, `"pinned_globally"`, `"archived"`, or `"visible"`.  
  `enabled` must be a string: `"true"` or `"false"`.  
  Only `pinned` and `pinned_globally` support the optional `until` parameter.

## Uploads Namespace

- `upload(filename: str, file: BinaryIO)`  
  Upload a generic file (attachment) to Discourse.

- `upload_avatar(filename: str, file: BinaryIO)`  
  Upload an avatar image for the current user.

## Users Namespace

- `create(username: str, email: str, password: str, name: Optional[str] = None, **kwargs)`  
  Create a new user account. Additional fields like `active`, `approved`, or `title` can be passed via `kwargs`.

- `deactivate(username: str)`  
  Deactivate a user account. The user will no longer be able to log in.

- `get(username: str)`  
  Retrieve full user details by username.

- `iter_directory(**kwargs)`  
  Return an iterator over users in the public directory. Supports filtering options like `order`, `period`, or `group`.

- `suspend(username: str, duration_days: int, reason: Optional[str] = None)`  
  Suspend a user for a specified number of days with an optional reason.
