<template>
  <v-container>
    <div class = "loginCard">
         <v-card
      height= "370"
      width = "350"
      elevation="4"
      > 
     <v-card-title > Welcome Back Peeps!</v-card-title>

     <v-form  ref= "form "
     v-model = "valid"> 

      <div id = "login">
        <v-text-field
            v-model="username"
            :rules = "username"
            label = "Username"
            required >
        </v-text-field>
        
         <v-text-field
            v-model="password"
            :rules = "password"
            label = "Password"
            required >
        </v-text-field>

        <v-btn id = "loginButton" > login </v-btn>


        <p> <br> dont have an account? <br> <a href= "/SignUp" > 
       sign up here! </a> </p>
        </div>
     </v-form>
    </v-card>
  </div>


  </v-container>
</template>

<script>


  export default {
    name: 'Login-Box',
    components: {
     
    },

    data: () => ({
      
    }),
  }
</script>

<style scoped>
#login{
  margin: 20px;
}
#loginButton {
    width: 100px;
    height: 40px;
    font-size: 15px;
}
.loginCard {
  margin-top: 70px;
  padding-left: 50px;
}

</style>

