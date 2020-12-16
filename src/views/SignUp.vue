<template>
  <v-container>
    <v-row class= "text-center">
       <v-col id = "col-1">  </v-col>
       <v-col id = "col-2">  
       <SignUpBox/> 
       </v-col>

      <v-col id = "col-3">  </v-col>
    </v-row>
  </v-container>
</template>

<script>
  import SignUpBox from '../components/SignUp-Box';

  export default {
    name: 'SignUp',
    components: {
     SignUpBox,
    },

    data: () => ({
      
    }),
  }
</script>

<style scoped>

</style>

