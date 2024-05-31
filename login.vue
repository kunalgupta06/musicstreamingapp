<template>
    <div class="taskbar">
        <img class="logo" src="../assets/Music Studio (3).png" />
        <h1 class="appname">MUSICOHOLIC</h1>
    </div>
    <div class="login">
        <input type="text" v-model="usernameOrEmail" placeholder="Enter Your Username or Email" />
        <input type="password" v-model="password" placeholder="Enter Password" />

        

        <button @click="login()">Login</button>
    </div>
</template>

<script>
export default {
    name: 'loginPage',
    data() {
        return {
            usernameOrEmail: '',
            password: '',
            loginOption: 'email' // Default login option is email
        };
    },
    methods: {
        login() {
            // Check if username or email and password match with the signup data
            const userFound = this.checkCredentials();

            if (userFound) {
                alert(`Login successful as ${this.usernameOrEmail}`);
                // Perform additional actions for successful login
            } else {
                alert('Invalid credentials. Please check and try again');
            }
        },
        checkCredentials() {
            // Simulate checking credentials against signup data
            // Replace this with your actual logic to check against your signup data
            const signupData = [
                { username: 'exampleuser', email: 'user@example.com', password: 'password123' },
                // Add more signup data as needed
            ];

            return signupData.some(user => {
                if (this.loginOption === 'email') {
                    return user.email === this.usernameOrEmail && user.password === this.password;
                } else {
                    return user.username === this.usernameOrEmail && user.password === this.password;
                }
            });
        },
        setLoginOption(option) {
            this.loginOption = option;
        }
    }
};
</script>
