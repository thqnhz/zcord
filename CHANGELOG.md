# Changelog for Zcord

This project uses mixed Calendar versioning: YYYY.feature.patch(.tag)

## 2026.0.2.dev - [Unreleased]

### Added:
  - `Guild`, `Embed`, `Attachment` classes
  - `ConnectionState` for high level API calls
    - `send_message` to send a message with channel ID
    - `fetch_guild` to get guild info

### Changed:
  - Moved API interaction to `REST` class
  - Renamed `types` module to `models`
  - Moved all enums into a separate `enums` module

## 2026.0.1.dev - 2026/06/23

The start of the project

### Added:
  - `Message`, `Channel`, `Role`, `User` classes
  - `HTTPClient`, `Bot` classes
  - `HTTPClient/Bot.send_message` (content only)
  - Documentation page at https://zcord.readthedocs.io
