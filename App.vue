<template>
  <!-- <div>
  <LandingPage />
  <SignUp />

  </div> -->
  <router-view/>

</template>

<script>
// import Vue from 'vue';
// import VueRouter from 'vue-router';
// import SignUp from './components/SignUp.vue'
// import LandingPage from './components/LandingPage.vue'

// Vue.use(VueRouter);

// const routes = [
//   { path: '/', component: LandingPage },
//   { path: '/signup', component: SignUp },
// ];

// const router = new VueRouter({
//   routes,
// });

export default {
  name: 'App',
  
}
//  components: {
//    SignUp,
//    LandingPage
//  }

</script>

<style>
#app {
  font-family: Avenir, Arial, Helvetica, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: -5px;
  background-color: rgb(255, 255, 255);
  
}
</style>
