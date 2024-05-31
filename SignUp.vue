<template>
    <div class="taskbar">
        <img class="logo" src="../assets/Music Studio (3).png" />
        <h1 class="appname">MUSICOHOLIC</h1>
    </div>
    <div class="register">

        <input type="user_name" v-model="user_name" placeholder="Enter Your User Name" />


        <input type="email" v-model="email" placeholder="Enter E-Mail" />
        <input type="password" v-model="password" placeholder="Enter Password" />
        <input type="password" v-model="confirmPassword" placeholder="Enter Confirm Password" />
        <div class="toggle-switch">
            <span :class="{ 'active': isCreator }" @click="toggleRole('creator')">Creator</span>
            <span :class="{ 'active': !isCreator }" @click="toggleRole('user')">User</span>
        </div>
        <button @click="signUp()">Sign Up</button>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'SignUp',
    data() {
        return {
            user_name: '',
            email: '',
            password: '',
            confirmPassword: '',
            isCreator: true, // Default role is Creator
            role: ''
        };
    },
    methods: {
        async signUp() {


            if (this.password === this.confirmPassword) {
                this.role = this.isCreator ? 'Creator' : 'User';
                const result = await axios.post("http://127.0.0.1:5000/user/signup", {
                    user_name: this.user_name,
                    email: this.email,
                    password: this.password,
                    role: this.role
                })
                console.log("result=", result)
                console.log("result=", result.data)
                console.log("result=", result.data.message)
                alert(`Signing up as ${this.role}`);
                this.$router.push('/login')
            } else {
                alert('Passwords do not match. Please check and try again');
            }
        },
        toggleRole(role) {
            this.isCreator = role === 'creator';
        }
    }
}

</script>

<style>
.logo {
    width: 140px;

}

.taskbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px;
    /* Adjust the padding according to your design */
    background-color: rgba(107, 1, 177, 0.752);
    /* Set the background color of the taskbar */
    margin-top: none;
    border-radius: 50px;
}

.appname {
    margin-left: auto;
    margin-right: auto;
    color: rgb(251, 251, 251);
}

.register input {
    width: 300px;
    height: 40px;
    padding-left: 20px;
    display: block;
    margin-bottom: 20px;
    margin-left: auto;
    margin-right: auto;
    border: 1px solid skyblue;
    margin-top: 40px;

}

.register button {
    width: 300px;
    height: 40px;
    border: 1px solid skyblue;
    color: white;
    background-color: rgb(112, 112, 255);
    cursor: pointer;
}

.toggle-switch {
    display: flex;
    justify-content: space-between;
    margin-top: 20px;
    cursor: pointer;
    width: 200px;
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 10px;
}

.toggle-switch span {
    padding: 10px;
    border: 1px solid skyblue;
    flex-grow: 1;
    text-align: center;
}

.toggle-switch span.active {
    background-color: rgb(112, 112, 255);
    color: white;
}
</style>