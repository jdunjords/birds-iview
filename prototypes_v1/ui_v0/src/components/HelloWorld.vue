<template>
<v-container>
<v-row class="text-center">

  <v-col id = "col-1">  
  </v-col>

  <v-col id = "col-2">  
     <h1 > What is pEEp? </h1>
  </v-col>

    <v-col id = "col-3">  
  </v-col>

  <v-col id = "col-4"> 
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
  </v-col>
</v-row>
</v-container>
</template>

<script>
  export default {
    name: 'HelloWorld',

    data: () => ({
      
    })
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
  margin-top: 50px;
  padding-left: 50px;
}

</style>