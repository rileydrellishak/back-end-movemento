# Movemento Back End
Movemento, a mobile application for users to mindfully log their exercise. Lots of exercise logging apps like Strava and Apple Fitness are focused on the quantitative aspects of exercising. Movemento is intended to be a mindful exercise tracker where users can reflect on their exercise experiences from a mindfulness and wellness approach, focusing more on the qualitative benefits like improved mood, better sleep, and improved quality of life.
## Models
|Model|Description|Attributes and Relationships|
|-|-|-|
|User|Represents a persona in the app|`id`, `name`;<br>has many `JournalEntry`'s
|JournalEntry|A journal post made by a user| `id`, `movements`, `moods_before`, `moods_after`, `reflection`, `user_id`,`img_path`, `created_at`;<br>belongs to a `User`
|Movement|Tracks type of physical movement in an entry|`id`, `name`, `slug` (normalized lowercase and underscored version, used for consistent identification by name), `category` (cardio, sports, mobility, etc.), `is_outdoor` (boolean to describe where movement usually takes place);<br> can belong to many different `JournalEntry`'s
|Mood|Tracks mood before/after a period of movement|`id`, `name`, `slug` (normalized lowercase and underscored version, used for consistent identification by name), `valence` (positive, neutral, or negative feeling), `energy` (high, medium, low energy feeling);<br> can belong to many different `JournalEntry`'s

>Mood categorizations of valence and energy are based upon the [Circumplex Model of Affect](https://pmc.ncbi.nlm.nih.gov/articles/PMC2367156/) and are included as future features involving tracking mood over time and how it responds to different types of movements and activities.

## Routes
|Route|Method|Description|Notes|
|-|-|-|-|
`/users/<id>/entries`|GET|Returns all entries for a user|Only entries belonging to that user
`/users/<id>/entries`|POST|Creates a new journal entry for a user|`user_id` is taken from the URL
`/users/<id>/entries/<entry_id>`|PATCH|Updates a journal entry|Only allowed for entries belonging to the user
`/users/<id>/entries/<entry_id>`|DELETE|Deletes a journal entry|Only allowed for entries belonging to the user
`/entries/<id>/photo`|PUT|Uploads an object to OCI Object Storage|Requires pre-authenticated request
`/entries/<id>/photo`|DELETE|Deletes an object from OCI Object Storage|Used with updating an entry's photo

>Some routes are for Demo only, such as `/users/<id>` to get a specific user persona and `/users` to create one or get all personas.
## Tech Stack
- [Frontend](https://github.com/rileydrellishak/front-end-movemento): React Native, Expo
- Backend: Python, Flask (Custom REST API)
- Database: PostgreSQL
- Cloud Storage: Oracle Cloud Infrastructure (OCI) Object Storage
- ORM: SQLAlchemy
- Deployment: Render (back end), Supabase (database)

## Setup Instructions
### Running your own local Flask server
1. Clone the repository.
```
git clone https://github.com/rileydrellishak/back-end-movemento
cd back-end-movemento
```
2. Create and activate a virtual environment.
```
python3 -m venv venv
source venv/bin/activate
```
3. Install dependencies.
```
pip install -r requirements.txt
```
4. Create your own instance of a Supabase PostgreSQL database.
5. Create your own Oracle Cloud Infrastructure Object Storage instance with appropriate read-write policies and pre-authenticated requests.
6. Create a .env file in the root directory and add required environment variables.
  - SUPABASE_URL
  - DATABASE_URL
  - SUPABASE_PUBLISHABLE_KEY
  - SUPABASE_SERVICE_ROLE_KEY
  - OCI_USER
  - OCI_TENANCY
  - OCI_FINGERPRINT
  - OCI_REGION
  - OCI_NAMESPACE
  - OCI_BUCKET_NAME
  - OCI_IMAGE_MAX_SIZE
  - OCI_JPEG_QUALITY
  - OCI_COMPARTMENT_ID
  - OCI_READ_PAR_URL
  - OCI_WRITE_PAR_URL
  - OCI_PRIVATE_KEY
7. Start your server!
```
flask run --debug
```
### Using the deployed backend and endpoints
[Backend URL](https://back-end-movemento.onrender.com)

## Potential Features
- Increased usage of movement and mood categories to conduct data analysis of movements, moods, and how they impact each other over time.
- User authentication and accounts with Supabase authentication.
