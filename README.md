Music Streaming App
This is a music streaming app just like Spotify(ONGOING PROJECT), Here the one can register as Creator or Music Listener.
This multi-user application serves as a dynamic platform for streaming music and reading lyrics, catering to both general users and content creators. Admins oversee the system, ensuring smooth operation and content management, while users can immerse themselves in a rich musical experience. They can play songs, read lyrics, rate their favorites, and create personalized playlists. Content creators have the capability to add new songs, albums, and lyrics, enriching the app's library. Each album in the system is detailed with an ID, name, artist, and other relevant information, while individual songs include an ID, name, lyrics, genre, duration, and creation date. The system is designed to automatically highlight the latest additions, keeping users updated with the newest music and lyrics available. This seamless integration of functionalities fosters an engaging and interactive musical community.
This multi-user application for music streaming and lyric reading is designed with a robust architecture that accommodates different user roles, ensuring a seamless and secure experience for both general users and content creators. The base requirements are as follows:

Admin’s Dashboard

A comprehensive dashboard that allows admins to oversee and manage the entire platform. Admins can monitor user activity, manage content, and ensure the system's smooth operation.
User and Creator Signup/Login (RBAC)

Role-Based Access Control (RBAC) ensures secure and appropriate access for different user types. General users and creators can sign up and log in with credentials that grant them access to specific functionalities based on their roles.
Mandatory admin login with RBAC ensures only authorized personnel can access the administrative features.
General User Profile

Each general user has a profile where they can view and manage their activity, including played songs, rated songs, created playlists, and personal preferences.
Creator Profile

Users registered as creators have dedicated profiles where they can manage their content. This includes adding new songs, albums, and lyrics, as well as tracking their content’s performance.
Song Management

A robust system for managing songs, including adding, editing, and deleting song entries. Each song has detailed metadata such as ID, name, lyrics, genre, duration, and creation date.
Album management features allow creators to associate multiple songs with an album, each album having its ID, name, artist, and other relevant information.
Playlist Management

Users can create, edit, and delete playlists. They can add their favorite songs to playlists, making it easy to access their preferred music.
Search Functionality

A powerful search feature that enables users to find songs, albums, and playlists quickly. The search functionality supports various filters and sorting options to enhance user experience.
Backend Jobs

Export Jobs: Enable the export of data such as user activity reports, playlist contents, and song metadata for analysis or backup purposes.
Reporting Jobs: Generate regular reports on platform usage, song ratings, user engagement, and other key metrics to help administrators and creators understand performance.
Alert Jobs: Automated alerts for critical system events such as low storage, high traffic, or errors in song uploads to ensure timely action and maintain system integrity.
Backend Performance: Optimize backend processes to ensure fast response times, handle high traffic loads, and provide a seamless user experience. This includes database indexing, caching strategies, and load balancing.
## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
