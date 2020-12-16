<template>
  <v-app>
    <v-app-bar
      app
      dark
    >   
        <v-btn id= "home" href="/Home"> <v-icon left> mdi-home </v-icon>
          home </v-btn>
          
        <v-btn id= "explore" href="/Explore"> <v-icon left> mdi-earth </v-icon>
          explore </v-btn>

         <v-btn id= "help" href="/Test"> <v-icon left> mdi-shape-plus </v-icon>
          test </v-btn>

         <v-btn id= "help" href="/Help"> <v-icon left> mdi-help-circle </v-icon>
          help </v-btn>

        <v-spacer> </v-spacer>

        <v-btn id= "signUp" href="/SignUp"> <v-icon left> mdi-account-plus </v-icon>
          sign up </v-btn>

    </v-app-bar>


    <v-main>
     <router-view/>
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
