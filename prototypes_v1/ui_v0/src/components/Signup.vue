<template>
    <v-container>
<v-row class="text-center">

  <v-col id = "col-1">  
  </v-col>

  <v-col id = "col-2">  
    <v-card
      height= "550"
      width = "500"
      elevation="4"
      > 
    

     <v-form  ref= "form "
     v-model = "valid"> 

      <div id = "signUp">
        <h1 class = "text-center" > Become a pEEp </h1> 
        <v-text-field
            v-model="firstname"
            :counter="20"
            :rules = "FnameRules"
            label = "First Name"
            required >
        </v-text-field>
        
         <v-text-field
            v-model="lastname"
            :counter="20"
            :rules = "LnameRules"
            label = "Last Name"
            required >
        </v-text-field>

        <v-text-field
            v-model="email"
            :rules = "emailRules"
            label = "Email"
            required >
        </v-text-field>

         <v-text-field
            v-model="password"
            :rules = "passRules"
            label = "Password"
            required >
        </v-text-field>

         <v-text-field
            v-model="lastname"
            :rules = "confirmPassRules"
            label = "Confirm Password"
            required >
        </v-text-field>
         
         <p> accept terms and conditions </p>

          <v-btn id = "signupButton" > sign up </v-btn>
           
      </div>
     </v-form>
    </v-card>
  </v-col>

  <v-col id = "col-3"> 

      
  </v-col>
</v-row>
</v-container>
</template>

<script>
export default {
    name: "Signup",

    data: () => ({
      
    })
}
</script>

<style scoped>
#signUp {
    margin: 20px;
    padding-top: 20px;;
}

#signUpButton {
    width: 150px;
    height: 60px;
    font-size: 25px;
}
</style>