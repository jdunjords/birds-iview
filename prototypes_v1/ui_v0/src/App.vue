<template>
  <v-app>
    <v-app-bar
      app
      dark
    >   
        <v-btn id = "home" href="/Home"> <v-icon left> mdi-home </v-icon>
          home </v-btn>
     
        <v-btn id = "login" href="/Explore">  <v-icon left> mdi-earth </v-icon>
        Explore </v-btn>

        <v-btn id = "demo" href="/Demo">  <v-icon left> mdi-shape-plus </v-icon>
        Demo </v-btn>

           <v-spacer></v-spacer>
   
        <v-btn id = "signup" href= "/Signup"> <v-icon left> mdi-account-plus </v-icon>
          Sign Up </v-btn>
    </v-app-bar>


    <v-main>
     <router-view> </router-view>
    </v-main>
    
  </v-app>
</template>

<script>


export default {
  name: 'App',

  components: {
      
  },

  data: () => ({
    
  }),
};
</script>