<template>
<header>
        <h1>Discover Music with Our Platform</h1>
        <p>Stream your favorite songs anytime, anywhere.</p>
        <router-link to="/signup">
        <button>Get Started</button>
    </router-link>
    </header>

    <section>
        <!-- Content for the main section of the landing page -->
    </section>

    <footer>
        <p>&copy; 2024 Your Company. All rights reserved.</p>
    </footer>

</template>

<script>
export default {
  name: 'LandingPage',
  // Add any logic or data specific to the LandingPage component
};
</script>

<style>
body {
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
            background-color: #1e1e1e;
            color: #fff;
        }

        header {
            padding: 20px;
            text-align: center;
        }

        section {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 80vh;
            background-color: #282828;
            color: #fff;
        }

        h1 {
            font-size: 3em;
            margin-bottom: 20px;
        }

        p {
            font-size: 1.5em;
            margin-bottom: 30px;
        }

        button {
            padding: 15px 30px;
            font-size: 1.5em;
            background-color: #1db954;
            color: #fff;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        button:hover {
            background-color: #1ed760;
        }

        footer {
            text-align: center;
            padding: 20px;
            background-color: #282828;
            color: #fff;
        }
</style>